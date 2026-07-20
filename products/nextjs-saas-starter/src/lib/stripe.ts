import type Stripe from "stripe";
import { db } from "./db";

/**
 * Lazy Stripe server-side client — only created when STRIPE_SECRET_KEY is present.
 * Prevents build errors when env vars are not set.
 */
let _stripe: Stripe | null = null;

export function getStripe(): Stripe {
  if (_stripe) return _stripe;
  if (!process.env.STRIPE_SECRET_KEY) {
    throw new Error("Stripe is not configured — set STRIPE_SECRET_KEY");
  }

  // Dynamic import avoids module-level instantiation breaking builds
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const StripeLib = require("stripe");
  _stripe = new StripeLib(process.env.STRIPE_SECRET_KEY, {
    apiVersion: "2025-02-24.acacia",
    typescript: true,
  }) as Stripe;
  return _stripe;
}

/**
 * Stripe price IDs from environment
 */
export const STRIPE_PRICES = {
  monthly: process.env.STRIPE_PRICE_MONTHLY ?? "",
  yearly: process.env.STRIPE_PRICE_YEARLY ?? "",
} as const;

/**
 * Check if Stripe is configured
 */
export function isStripeConfigured(): boolean {
  return !!process.env.STRIPE_SECRET_KEY;
}

/**
 * Create a Stripe Checkout Session for subscription
 */
export async function createCheckoutSession({
  priceId,
  successUrl,
  cancelUrl,
}: {
  priceId: string;
  successUrl: string;
  cancelUrl: string;
}) {
  const stripe = getStripe();
  if (!stripe) throw new Error("Stripe is not configured");

  const session = await stripe.checkout.sessions.create({
    mode: "subscription",
    payment_method_types: ["card"],
    line_items: [{ price: priceId, quantity: 1 }],
    success_url: successUrl,
    cancel_url: cancelUrl,
    subscription_data: { metadata: {} },
  });

  return session;
}

/**
 * Create a Stripe Customer Portal session
 */
export async function createPortalSession({
  customerId,
  returnUrl,
}: {
  customerId: string;
  returnUrl: string;
}) {
  const stripe = getStripe();
  if (!stripe) throw new Error("Stripe is not configured");

  const session = await stripe.billingPortal.sessions.create({
    customer: customerId,
    return_url: returnUrl,
  });

  return session;
}

/**
 * Get or create a Stripe Customer ID for a user
 */
export async function getOrCreateCustomerId({
  userId,
  email,
  name,
}: {
  userId: string;
  email: string;
  name?: string | null;
}) {
  const stripe = getStripe();
  if (!stripe) throw new Error("Stripe is not configured");

  const subscription = await db.subscription.findUnique({
    where: { userId },
  });

  if (subscription?.stripeCustomerId) {
    return subscription.stripeCustomerId;
  }

  const customer = await stripe.customers.create({
    email,
    name: name ?? undefined,
    metadata: { userId },
  });

  await db.subscription.upsert({
    where: { userId },
    update: { stripeCustomerId: customer.id },
    create: {
      userId,
      stripeCustomerId: customer.id,
      plan: "FREE",
      status: "ACTIVE",
    },
  });

  return customer.id;
}
