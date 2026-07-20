import { NextResponse } from "next/server";
import { getStripe } from "@/lib/stripe";
import { db } from "@/lib/db";
import { sendSubscriptionConfirmationEmail } from "@/lib/email";
import type Stripe from "stripe";

/**
 * Stripe Webhook Handler
 *
 * Handles subscription lifecycle events:
 * - checkout.session.completed → activate subscription
 * - invoice.paid → renew subscription
 * - customer.subscription.updated → update plan/status
 * - customer.subscription.deleted → cancel subscription
 */
export async function POST(req: Request) {
  try {
    const body = await req.text();
    const signature = req.headers.get("stripe-signature");

    if (!signature) {
      return NextResponse.json(
        { error: "Missing stripe-signature header" },
        { status: 400 }
      );
    }

    const webhookSecret = process.env.STRIPE_WEBHOOK_SECRET;
    if (!webhookSecret) {
      console.error("Missing STRIPE_WEBHOOK_SECRET");
      return NextResponse.json(
        { error: "Webhook not configured" },
        { status: 500 }
      );
    }

    const stripe = getStripe();
    let event: Stripe.Event;

    try {
      event = stripe.webhooks.constructEvent(body, signature, webhookSecret);
    } catch (err) {
      console.error("Webhook signature verification failed:", err);
      return NextResponse.json(
        { error: "Invalid signature" },
        { status: 400 }
      );
    }

    switch (event.type) {
      case "checkout.session.completed": {
        const session = event.data.object as Stripe.Checkout.Session;

        if (session.mode === "subscription" && session.subscription) {
          const subscriptionId = session.subscription as string;
          const customerId = session.customer as string;
          const userId = session.metadata?.userId;

          if (userId) {
            // Retrieve full subscription details
            const subscription =
              await stripe.subscriptions.retrieve(subscriptionId);

            const priceId = subscription.items.data[0]?.price.id;
            const plan = getPlanFromPriceId(priceId);

            await db.subscription.upsert({
              where: { userId },
              update: {
                stripeCustomerId: customerId,
                stripeSubscriptionId: subscriptionId,
                stripePriceId: priceId,
                stripeCurrentPeriodEnd: new Date(
                  subscription.current_period_end * 1000
                ),
                plan,
                status: "ACTIVE",
              },
              create: {
                userId,
                stripeCustomerId: customerId,
                stripeSubscriptionId: subscriptionId,
                stripePriceId: priceId,
                stripeCurrentPeriodEnd: new Date(
                  subscription.current_period_end * 1000
                ),
                plan,
                status: "ACTIVE",
              },
            });

            // Send confirmation email
            const user = await db.user.findUnique({ where: { id: userId } });
            if (user) {
              sendSubscriptionConfirmationEmail({
                email: user.email!,
                name: user.name,
                plan: plan.replace("_", " "),
              }).catch(console.error);
            }
          }
        }
        break;
      }

      case "invoice.paid": {
        const invoice = event.data.object as Stripe.Invoice;

        if (invoice.subscription) {
          const subscriptionId = invoice.subscription as string;
          const subscription =
            await stripe.subscriptions.retrieve(subscriptionId);

          const priceId = subscription.items.data[0]?.price.id;
          const plan = getPlanFromPriceId(priceId);

          await db.subscription.updateMany({
            where: { stripeSubscriptionId: subscriptionId },
            data: {
              stripePriceId: priceId,
              stripeCurrentPeriodEnd: new Date(
                subscription.current_period_end * 1000
              ),
              plan,
              status: "ACTIVE",
            },
          });
        }
        break;
      }

      case "customer.subscription.updated": {
        const subscription = event.data.object as Stripe.Subscription;
        const priceId = subscription.items.data[0]?.price.id;
        const plan = getPlanFromPriceId(priceId);

        await db.subscription.updateMany({
          where: { stripeSubscriptionId: subscription.id },
          data: {
            stripePriceId: priceId,
            stripeCurrentPeriodEnd: new Date(
              subscription.current_period_end * 1000
            ),
            stripeCancelAtPeriodEnd: subscription.cancel_at_period_end,
            plan,
            status: mapStripeStatus(subscription.status),
          },
        });
        break;
      }

      case "customer.subscription.deleted": {
        const subscription = event.data.object as Stripe.Subscription;

        await db.subscription.updateMany({
          where: { stripeSubscriptionId: subscription.id },
          data: {
            plan: "FREE",
            status: "CANCELED",
            stripeSubscriptionId: null,
            stripePriceId: null,
            stripeCurrentPeriodEnd: null,
          },
        });
        break;
      }
    }

    return NextResponse.json({ received: true });
  } catch (error) {
    console.error("Webhook error:", error);
    return NextResponse.json(
      { error: "Webhook handler failed" },
      { status: 500 }
    );
  }
}

/**
 * Map Stripe subscription status to our enum
 */
function mapStripeStatus(
  status: Stripe.Subscription.Status
): "ACTIVE" | "CANCELED" | "INCOMPLETE" | "INCOMPLETE_EXPIRED" | "PAST_DUE" | "UNPAID" | "TRIALING" {
  switch (status) {
    case "active":
      return "ACTIVE";
    case "canceled":
      return "CANCELED";
    case "incomplete":
      return "INCOMPLETE";
    case "incomplete_expired":
      return "INCOMPLETE_EXPIRED";
    case "past_due":
      return "PAST_DUE";
    case "trialing":
      return "TRIALING";
    case "unpaid":
      return "UNPAID";
    default:
      return "ACTIVE";
  }
}

/**
 * Determine plan from Stripe price ID
 */
function getPlanFromPriceId(priceId: string | undefined): "FREE" | "PRO_MONTHLY" | "PRO_YEARLY" {
  if (!priceId) return "FREE";

  if (priceId === process.env.STRIPE_PRICE_MONTHLY) {
    return "PRO_MONTHLY";
  }

  if (priceId === process.env.STRIPE_PRICE_YEARLY) {
    return "PRO_YEARLY";
  }

  return "FREE";
}
