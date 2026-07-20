"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import { Check } from "lucide-react";
import Link from "next/link";

const plans = [
  {
    name: "Free",
    description: "Perfect for getting started",
    price: { monthly: 0, yearly: 0 },
    features: [
      "Basic dashboard",
      "Up to 3 projects",
      "Community support",
      "Standard analytics",
    ],
    cta: "Get Started",
    href: "/register",
  },
  {
    name: "Pro Monthly",
    description: "For growing teams",
    price: { monthly: 29, yearly: 290 },
    features: [
      "Everything in Free",
      "Unlimited projects",
      "Priority support",
      "Advanced analytics",
      "Team members (5)",
      "API access",
    ],
    highlighted: true,
    cta: "Subscribe",
    href: "/register",
  },
  {
    name: "Pro Yearly",
    description: "Best value for businesses",
    price: { monthly: 24, yearly: 240 },
    features: [
      "Everything in Pro Monthly",
      "Unlimited team members",
      "Dedicated support",
      "Custom integrations",
      "SLA guarantee",
      "Early access features",
    ],
    cta: "Subscribe",
    href: "/register",
    popular: true,
  },
];

export function PricingSection() {
  const [annual, setAnnual] = useState(false);

  return (
    <section id="pricing" className="border-t py-24">
      <div className="container">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">
            Simple, Transparent Pricing
          </h2>
          <p className="mt-4 text-lg text-muted-foreground">
            Choose the plan that fits your needs. No hidden fees.
          </p>
        </div>

        {/* Toggle */}
        <div className="mt-10 flex items-center justify-center gap-3">
          <span
            className={cn(
              "text-sm font-medium",
              !annual ? "text-foreground" : "text-muted-foreground"
            )}
          >
            Monthly
          </span>
          <button
            onClick={() => setAnnual(!annual)}
            className={cn(
              "relative inline-flex h-6 w-11 items-center rounded-full transition-colors",
              annual ? "bg-primary" : "bg-input"
            )}
          >
            <span
              className={cn(
                "inline-block h-5 w-5 transform rounded-full bg-white shadow transition-transform",
                annual ? "translate-x-6" : "translate-x-0.5"
              )}
            />
          </button>
          <span
            className={cn(
              "text-sm font-medium",
              annual ? "text-foreground" : "text-muted-foreground"
            )}
          >
            Annual
            <span className="ml-1.5 rounded-full bg-emerald-500/10 px-2 py-0.5 text-xs text-emerald-600 dark:text-emerald-400">
              Save 17%
            </span>
          </span>
        </div>

        {/* Plans */}
        <div className="mx-auto mt-12 grid max-w-5xl gap-8 lg:grid-cols-3">
          {plans.map((plan) => (
            <div
              key={plan.name}
              className={cn(
                "relative flex flex-col rounded-2xl border p-8",
                plan.popular &&
                  "border-primary shadow-lg ring-1 ring-primary",
                plan.highlighted && "lg:scale-105"
              )}
            >
              {plan.popular && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                  <span className="inline-flex items-center rounded-full bg-primary px-3 py-1 text-xs font-semibold text-primary-foreground">
                    Popular
                  </span>
                </div>
              )}

              <div>
                <h3 className="text-lg font-semibold">{plan.name}</h3>
                <p className="mt-1 text-sm text-muted-foreground">
                  {plan.description}
                </p>

                <div className="mt-6">
                  <span className="text-4xl font-bold">
                    ${annual ? plan.price.yearly : plan.price.monthly}
                  </span>
                  <span className="ml-1 text-sm text-muted-foreground">
                    /{annual ? "year" : "month"}
                  </span>
                </div>
              </div>

              <ul className="mt-8 flex-1 space-y-3">
                {plan.features.map((feature) => (
                  <li key={feature} className="flex items-start gap-3">
                    <Check className="mt-0.5 h-4 w-4 shrink-0 text-emerald-500" />
                    <span className="text-sm">{feature}</span>
                  </li>
                ))}
              </ul>

              <Button
                asChild
                className="mt-8 w-full"
                variant={plan.popular ? "default" : "outline"}
              >
                <Link href={plan.href}>{plan.cta}</Link>
              </Button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
