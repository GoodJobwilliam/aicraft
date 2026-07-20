import {
  Shield,
  CreditCard,
  Mail,
  LayoutDashboard,
  Users,
  Zap,
} from "lucide-react";

const features = [
  {
    title: "Authentication",
    description:
      "Email/password and OAuth via Google and GitHub. Session management, password reset, and account security built-in.",
    icon: Shield,
  },
  {
    title: "Subscription Billing",
    description:
      "Full Stripe integration with monthly/yearly plans, secure checkout, webhook handling, and customer portal.",
    icon: CreditCard,
  },
  {
    title: "Transactional Email",
    description:
      "Automated welcome emails, subscription confirmations, and password resets via Resend with beautiful templates.",
    icon: Mail,
  },
  {
    title: "Admin Dashboard",
    description:
      "Professional dashboard with sidebar navigation, stats overview, settings, and billing management pages.",
    icon: LayoutDashboard,
  },
  {
    title: "Team Ready",
    description:
      "Role-based access control (RBAC) with user and admin roles. Ready for team features and multi-tenant setups.",
    icon: Users,
  },
  {
    title: "Modern Stack",
    description:
      "Next.js 14 App Router, TypeScript, Tailwind CSS, Prisma, PostgreSQL, and full test suite with Vitest.",
    icon: Zap,
  },
];

export function FeaturesSection() {
  return (
    <section id="features" className="border-t py-24">
      <div className="container">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">
            Everything You Need to Launch
          </h2>
          <p className="mt-4 text-lg text-muted-foreground">
            A complete SaaS foundation that saves you 40+ hours of boilerplate
            setup. Focus on building your product, not auth flows.
          </p>
        </div>

        <div className="mx-auto mt-16 grid max-w-5xl gap-8 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((feature) => {
            const Icon = feature.icon;
            return (
              <div
                key={feature.title}
                className="group relative rounded-xl border p-6 transition-shadow hover:shadow-md"
              >
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10 text-primary">
                  <Icon className="h-6 w-6" />
                </div>
                <h3 className="mt-4 font-semibold">{feature.title}</h3>
                <p className="mt-2 text-sm text-muted-foreground">
                  {feature.description}
                </p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
