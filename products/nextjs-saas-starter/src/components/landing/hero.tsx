import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

export function Hero() {
  return (
    <section className="relative overflow-hidden py-24 sm:py-32">
      {/* Background gradient */}
      <div className="absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_top_right,_hsl(var(--primary))_0%,_transparent_50%)] opacity-10" />

      <div className="container">
        <div className="mx-auto max-w-3xl text-center">
          <div className="mb-6 inline-flex items-center rounded-full border px-4 py-1.5 text-sm font-medium">
            🚀 Production-Ready SaaS Starter
          </div>

          <h1 className="text-4xl font-bold tracking-tight sm:text-5xl md:text-6xl">
            Launch Your SaaS in
            <span className="text-primary"> Days</span>, Not Months
          </h1>

          <p className="mt-6 text-lg leading-8 text-muted-foreground">
            A complete, production-grade Next.js boilerplate with authentication,
            Stripe subscriptions, PostgreSQL database, email, and a beautiful
            dashboard. Save 40+ hours of repetitive setup.
          </p>

          <div className="mt-10 flex items-center justify-center gap-4">
            <Button asChild size="xl">
              <Link href="/register">
                Get Started
                <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
            </Button>
            <Button asChild variant="outline" size="xl">
              <Link href="#features">Learn More</Link>
            </Button>
          </div>

          <div className="mt-12 flex items-center justify-center gap-8 text-sm text-muted-foreground">
            <span className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-emerald-500" />
              Next.js 14
            </span>
            <span className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-emerald-500" />
              TypeScript
            </span>
            <span className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-emerald-500" />
              Stripe
            </span>
            <span className="flex items-center gap-2">
              <div className="h-2 w-2 rounded-full bg-emerald-500" />
              Prisma
            </span>
          </div>
        </div>
      </div>
    </section>
  );
}
