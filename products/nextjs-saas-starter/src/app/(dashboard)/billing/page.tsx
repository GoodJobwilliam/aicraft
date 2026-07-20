"use client";

import { useState } from "react";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Icons } from "@/components/ui/icons";
import { toast } from "@/hooks/use-toast";
import { Switch } from "@/components/ui/switch";

const plans = [
  {
    id: "FREE",
    name: "Free",
    price: { monthly: 0, yearly: 0 },
    features: ["Basic dashboard", "3 projects", "Community support"],
  },
  {
    id: "PRO_MONTHLY",
    name: "Pro Monthly",
    price: { monthly: 29, yearly: 290 },
    features: [
      "Unlimited projects",
      "Priority support",
      "Advanced analytics",
      "Team members (5)",
      "API access",
    ],
  },
  {
    id: "PRO_YEARLY",
    name: "Pro Yearly",
    price: { monthly: 24, yearly: 240 },
    features: [
      "Unlimited projects",
      "Dedicated support",
      "Custom integrations",
      "Unlimited team members",
      "SLA guarantee",
    ],
    popular: true,
  },
];

export default function BillingPage() {
  const { data: session } = useSession();
  const router = useRouter();
  const [annual, setAnnual] = useState(false);
  const [loading, setLoading] = useState<string | null>(null);

  async function handleCheckout(planId: string) {
    if (planId === "FREE") {
      toast({
        title: "Free Plan",
        description: "You are currently on the Free plan.",
      });
      return;
    }

    setLoading(planId);
    try {
      const response = await fetch("/api/stripe/create-checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          planId,
          interval: annual ? "year" : "month",
        }),
      });

      const result = await response.json();

      if (!response.ok) {
        toast({
          title: "Error",
          description: result.error || "Failed to create checkout session",
          variant: "destructive",
        });
        return;
      }

      // Redirect to Stripe Checkout
      if (result.url) {
        window.location.href = result.url;
      }
    } catch {
      toast({
        title: "Error",
        description: "An unexpected error occurred",
        variant: "destructive",
      });
    } finally {
      setLoading(null);
    }
  }

  async function handlePortal() {
    setLoading("portal");
    try {
      const response = await fetch("/api/stripe/portal", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
      });

      const result = await response.json();

      if (!response.ok) {
        toast({
          title: "Error",
          description: result.error || "Failed to open portal",
          variant: "destructive",
        });
        return;
      }

      if (result.url) {
        window.location.href = result.url;
      }
    } catch {
      toast({
        title: "Error",
        description: "An unexpected error occurred",
        variant: "destructive",
      });
    } finally {
      setLoading(null);
    }
  }

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold tracking-tight">Billing</h2>
        <p className="text-muted-foreground">
          Manage your subscription and billing information.
        </p>
      </div>

      {/* Current Plan */}
      <Card>
        <CardHeader>
          <CardTitle>Current Plan</CardTitle>
          <CardDescription>
            You are currently on the{" "}
            {session?.user?.name ? "Free" : "Free"} plan.
          </CardDescription>
        </CardHeader>
        <CardContent className="flex items-center justify-between">
          <div>
            <p className="font-medium">Free Plan</p>
            <p className="text-sm text-muted-foreground">
              Basic features, upgrade to unlock more.
            </p>
          </div>
          <Badge variant="secondary">Active</Badge>
        </CardContent>
      </Card>

      {/* Toggle */}
      <div className="flex items-center justify-center gap-3">
        <span className="text-sm font-medium">Monthly</span>
        <Switch checked={annual} onCheckedChange={setAnnual} />
        <span className="text-sm font-medium">
          Annual
          <span className="ml-1.5 rounded-full bg-emerald-500/10 px-2 py-0.5 text-xs text-emerald-600">
            Save ~17%
          </span>
        </span>
      </div>

      {/* Plans */}
      <div className="grid gap-6 lg:grid-cols-3">
        {plans.map((plan) => (
          <Card
            key={plan.id}
            className={`relative ${
              plan.popular ? "border-primary shadow-lg ring-1 ring-primary" : ""
            }`}
          >
            {plan.popular && (
              <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                <span className="inline-flex items-center rounded-full bg-primary px-3 py-1 text-xs font-semibold text-primary-foreground">
                  Popular
                </span>
              </div>
            )}
            <CardHeader>
              <CardTitle>{plan.name}</CardTitle>
              <CardDescription>
                <span className="text-3xl font-bold text-foreground">
                  ${annual ? plan.price.yearly : plan.price.monthly}
                </span>
                <span className="ml-1">/{annual ? "year" : "month"}</span>
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <ul className="space-y-2">
                {plan.features.map((feature) => (
                  <li
                    key={feature}
                    className="flex items-center gap-2 text-sm"
                  >
                    <span className="h-1.5 w-1.5 rounded-full bg-primary shrink-0" />
                    {feature}
                  </li>
                ))}
              </ul>

              <Button
                className="w-full"
                variant={plan.popular ? "default" : "outline"}
                onClick={() => handleCheckout(plan.id)}
                disabled={loading === plan.id}
              >
                {loading === plan.id ? (
                  <>
                    <Icons.spinner className="mr-2 h-4 w-4 animate-spin" />
                    Redirecting...
                  </>
                ) : plan.id === "FREE" ? (
                  "Current Plan"
                ) : (
                  "Subscribe"
                )}
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Customer Portal */}
      <Card>
        <CardHeader>
          <CardTitle>Manage Subscription</CardTitle>
          <CardDescription>
            Update payment method, view invoices, or cancel your subscription.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <Button
            variant="outline"
            onClick={handlePortal}
            disabled={loading === "portal"}
          >
            {loading === "portal" ? (
              <>
                <Icons.spinner className="mr-2 h-4 w-4 animate-spin" />
                Opening...
              </>
            ) : (
              "Open Customer Portal"
            )}
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
