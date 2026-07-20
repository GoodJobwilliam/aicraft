import type { User as PrismaUser, Subscription } from "@prisma/client";

// ─── Auth Types ────────────────────────────────────────────────

export type UserRole = "USER" | "ADMIN";

export type SafeUser = Omit<
  PrismaUser,
  "passwordHash" | "createdAt" | "updatedAt"
> & {
  subscription: Subscription | null;
};

// ─── Subscription Types ────────────────────────────────────────

export type PlanType = "FREE" | "PRO_MONTHLY" | "PRO_YEARLY";

export type SubscriptionStatus =
  | "ACTIVE"
  | "CANCELED"
  | "INCOMPLETE"
  | "INCOMPLETE_EXPIRED"
  | "PAST_DUE"
  | "TRIALING"
  | "UNPAID";

export interface PricingPlan {
  id: PlanType;
  name: string;
  description: string;
  price: number;
  interval: "month" | "year";
  features: string[];
  highlighted?: boolean;
  priceId: string;
}

// ─── Navigation Types ──────────────────────────────────────────

export interface NavItem {
  label: string;
  href: string;
  icon: React.ReactNode;
  requiresSubscription?: boolean;
}

// ─── API Response Types ────────────────────────────────────────

export interface ApiResponse<T = unknown> {
  success: boolean;
  data?: T;
  error?: string;
}

// ─── Form Types ────────────────────────────────────────────────

export interface RegisterFormData {
  name: string;
  email: string;
  password: string;
  confirmPassword: string;
}

export interface LoginFormData {
  email: string;
  password: string;
}

// ─── Stripe Types ──────────────────────────────────────────────

export interface StripeProduct {
  id: string;
  name: string;
  description: string | null;
  features: string[];
  prices: {
    monthly: StripePrice | null;
    yearly: StripePrice | null;
  };
}

export interface StripePrice {
  id: string;
  unitAmount: number;
  interval: "month" | "year";
}
