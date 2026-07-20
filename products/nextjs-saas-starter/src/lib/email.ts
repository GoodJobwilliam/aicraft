import { absoluteUrl } from "./utils";

/**
 * Lazy Resend client — only created when RESEND_API_KEY is present.
 * Prevents build errors when the env var is not set.
 */
function getResend() {
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) return null;

  // Dynamic import to avoid module-level instantiation
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const { Resend } = require("resend");
  return new Resend(apiKey);
}

const FROM_EMAIL = process.env.RESEND_FROM_EMAIL ?? "noreply@example.com";

/**
 * Email sending helper — no-ops when Resend is not configured.
 */
function isEmailConfigured(): boolean {
  return !!process.env.RESEND_API_KEY;
}

/**
 * Send a welcome email after registration
 */
export async function sendWelcomeEmail({
  email,
  name,
}: {
  email: string;
  name: string | null;
}) {
  if (!isEmailConfigured()) {
    console.log(`[Email] Welcome email skipped — no RESEND_API_KEY`);
    return;
  }

  try {
    const resend = getResend();
    if (!resend) return;

    await resend.emails.send({
      from: FROM_EMAIL,
      to: email,
      subject: "Welcome to SaaS Starter!",
      html: `
        <div style="font-family: sans-serif; max-width: 480px; margin: 0 auto;">
          <h1 style="color: #18181b;">Welcome${name ? `, ${name}` : ""}!</h1>
          <p style="color: #52525b; line-height: 1.6;">
            Thank you for joining SaaS Starter. We're excited to have you on board.
          </p>
          <p style="color: #52525b; line-height: 1.6;">
            Get started by exploring your dashboard and setting up your subscription.
          </p>
          <a
            href="${absoluteUrl("/dashboard")}"
            style="
              display: inline-block;
              padding: 12px 24px;
              background-color: #18181b;
              color: #fafafa;
              text-decoration: none;
              border-radius: 8px;
              font-weight: 600;
            "
          >
            Go to Dashboard
          </a>
        </div>
      `,
    });
  } catch (error) {
    console.error("Failed to send welcome email:", error);
  }
}

/**
 * Send a subscription confirmation email
 */
export async function sendSubscriptionConfirmationEmail({
  email,
  name,
  plan,
}: {
  email: string;
  name: string | null;
  plan: string;
}) {
  if (!isEmailConfigured()) {
    console.log(`[Email] Subscription email skipped — no RESEND_API_KEY`);
    return;
  }

  try {
    const resend = getResend();
    if (!resend) return;

    await resend.emails.send({
      from: FROM_EMAIL,
      to: email,
      subject: `Subscription Confirmed — ${plan}`,
      html: `
        <div style="font-family: sans-serif; max-width: 480px; margin: 0 auto;">
          <h1 style="color: #18181b;">Subscription Confirmed</h1>
          <p style="color: #52525b; line-height: 1.6;">
            Hi${name ? ` ${name}` : ""},
          </p>
          <p style="color: #52525b; line-height: 1.6;">
            Your <strong>${plan}</strong> subscription is now active.
            You have access to all Pro features.
          </p>
          <p style="color: #52525b; line-height: 1.6;">
            You can manage your subscription anytime from your billing settings.
          </p>
          <a
            href="${absoluteUrl("/dashboard/billing")}"
            style="
              display: inline-block;
              padding: 12px 24px;
              background-color: #18181b;
              color: #fafafa;
              text-decoration: none;
              border-radius: 8px;
              font-weight: 600;
            "
          >
            Manage Billing
          </a>
        </div>
      `,
    });
  } catch (error) {
    console.error("Failed to send subscription email:", error);
  }
}

/**
 * Send a password reset email
 */
export async function sendPasswordResetEmail({
  email,
  resetUrl,
}: {
  email: string;
  resetUrl: string;
}) {
  if (!isEmailConfigured()) {
    console.log(`[Email] Password reset email skipped — no RESEND_API_KEY`);
    return;
  }

  try {
    const resend = getResend();
    if (!resend) return;

    await resend.emails.send({
      from: FROM_EMAIL,
      to: email,
      subject: "Reset your password",
      html: `
        <div style="font-family: sans-serif; max-width: 480px; margin: 0 auto;">
          <h1 style="color: #18181b;">Reset Your Password</h1>
          <p style="color: #52525b; line-height: 1.6;">
            Click the link below to reset your password. This link expires in 1 hour.
          </p>
          <a
            href="${resetUrl}"
            style="
              display: inline-block;
              padding: 12px 24px;
              background-color: #18181b;
              color: #fafafa;
              text-decoration: none;
              border-radius: 8px;
              font-weight: 600;
            "
          >
            Reset Password
          </a>
          <p style="color: #a1a1aa; font-size: 14px; margin-top: 24px;">
            If you didn't request this, you can safely ignore this email.
          </p>
        </div>
      `,
    });
  } catch (error) {
    console.error("Failed to send password reset email:", error);
  }
}
