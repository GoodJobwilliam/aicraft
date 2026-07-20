import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "@/styles/globals.css";
import { Providers } from "@/components/providers";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: {
    default: "SaaS Starter - Launch Your SaaS Faster",
    template: "%s | SaaS Starter",
  },
  description:
    "A production-ready SaaS boilerplate with authentication, subscriptions, and more. Launch your SaaS in minutes.",
  keywords: ["saas", "starter", "boilerplate", "nextjs", "subscription"],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
