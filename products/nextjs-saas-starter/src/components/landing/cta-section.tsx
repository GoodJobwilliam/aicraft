import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";

export function CTASection() {
  return (
    <section className="border-t py-24">
      <div className="container">
        <div className="relative mx-auto max-w-3xl overflow-hidden rounded-2xl border bg-gradient-to-br from-primary/5 via-primary/10 to-primary/5 p-12 text-center">
          <div className="absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_center,_hsl(var(--primary))_0%,_transparent_60%)] opacity-5" />

          <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">
            Ready to Build Your SaaS?
          </h2>
          <p className="mx-auto mt-4 max-w-xl text-lg text-muted-foreground">
            Join hundreds of developers who launched their SaaS with this
            starter kit. Get everything you need in one download.
          </p>

          <div className="mt-10 flex items-center justify-center gap-4">
            <Button asChild size="xl">
              <Link href="/register">
                Get Started Now
                <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
            </Button>
            <Button asChild variant="outline" size="xl">
              <Link href="#features">View Features</Link>
            </Button>
          </div>
        </div>
      </div>
    </section>
  );
}
