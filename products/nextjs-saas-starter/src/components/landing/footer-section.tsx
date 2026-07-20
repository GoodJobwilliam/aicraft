import Link from "next/link";

export function FooterSection() {
  return (
    <footer className="border-t py-12">
      <div className="container">
        <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
          <div>
            <div className="flex items-center space-x-2">
              <div className="h-8 w-8 rounded-lg bg-primary flex items-center justify-center">
                <span className="text-sm font-bold text-primary-foreground">
                  S
                </span>
              </div>
              <span className="text-lg font-bold">SaaS Starter</span>
            </div>
            <p className="mt-4 text-sm text-muted-foreground">
              Production-ready Next.js boilerplate for your next SaaS product.
            </p>
          </div>

          <div>
            <h4 className="font-semibold">Product</h4>
            <ul className="mt-4 space-y-2">
              <li>
                <Link
                  href="#features"
                  className="text-sm text-muted-foreground transition-colors hover:text-foreground"
                >
                  Features
                </Link>
              </li>
              <li>
                <Link
                  href="#pricing"
                  className="text-sm text-muted-foreground transition-colors hover:text-foreground"
                >
                  Pricing
                </Link>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold">Company</h4>
            <ul className="mt-4 space-y-2">
              <li>
                <span className="text-sm text-muted-foreground">About</span>
              </li>
              <li>
                <span className="text-sm text-muted-foreground">Blog</span>
              </li>
              <li>
                <span className="text-sm text-muted-foreground">Contact</span>
              </li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold">Legal</h4>
            <ul className="mt-4 space-y-2">
              <li>
                <span className="text-sm text-muted-foreground">Privacy</span>
              </li>
              <li>
                <span className="text-sm text-muted-foreground">Terms</span>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-12 border-t pt-8 text-center text-sm text-muted-foreground">
          &copy; {new Date().getFullYear()} SaaS Starter. All rights reserved.
        </div>
      </div>
    </footer>
  );
}
