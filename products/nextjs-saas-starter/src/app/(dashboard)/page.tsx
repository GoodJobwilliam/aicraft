import { auth } from "@/lib/auth";
import { db } from "@/lib/db";
import { redirect } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { formatDate } from "@/lib/utils";
import {
  Activity,
  CreditCard,
  DollarSign,
  Users,
  TrendingUp,
  TrendingDown,
} from "lucide-react";

export default async function DashboardPage() {
  const session = await auth();

  if (!session?.user) {
    redirect("/login");
  }

  const subscription = await db.subscription.findUnique({
    where: { userId: session.user.id },
  });

  const stats = [
    {
      title: "Total Revenue",
      value: "$12,345",
      change: "+20.1%",
      trend: "up",
      icon: DollarSign,
    },
    {
      title: "Active Users",
      value: "2,350",
      change: "+12.5%",
      trend: "up",
      icon: Users,
    },
    {
      title: "Subscriptions",
      value: "1,234",
      change: "+8.2%",
      trend: "up",
      icon: CreditCard,
    },
    {
      title: "Conversion Rate",
      value: "3.2%",
      change: "-0.5%",
      trend: "down",
      icon: Activity,
    },
  ];

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold tracking-tight">
          Welcome back{session.user.name ? `, ${session.user.name}` : ""}!
        </h2>
        <p className="text-muted-foreground">
          Here&apos;s an overview of your account.
        </p>
      </div>

      {/* Stats Grid */}
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => {
          const Icon = stat.icon;
          const TrendIcon = stat.trend === "up" ? TrendingUp : TrendingDown;
          return (
            <Card key={stat.title}>
              <CardHeader className="flex flex-row items-center justify-between pb-2">
                <CardTitle className="text-sm font-medium">
                  {stat.title}
                </CardTitle>
                <Icon className="h-4 w-4 text-muted-foreground" />
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold">{stat.value}</div>
                <p className="flex items-center gap-1 text-xs text-muted-foreground">
                  <TrendIcon
                    className={`h-3 w-3 ${
                      stat.trend === "up"
                        ? "text-emerald-500"
                        : "text-destructive"
                    }`}
                  />
                  <span
                    className={
                      stat.trend === "up"
                        ? "text-emerald-500"
                        : "text-destructive"
                    }
                  >
                    {stat.change}
                  </span>{" "}
                  from last month
                </p>
              </CardContent>
            </Card>
          );
        })}
      </div>

      {/* Subscription Status */}
      <Card>
        <CardHeader>
          <CardTitle>Subscription</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <p className="font-medium">
                {subscription?.plan === "FREE"
                  ? "Free Plan"
                  : subscription?.plan === "PRO_MONTHLY"
                    ? "Pro Monthly"
                    : "Pro Yearly"}
              </p>
              <p className="text-sm text-muted-foreground">
                {subscription?.status.toLowerCase() === "active"
                  ? "Your subscription is active"
                  : `Status: ${subscription?.status?.toLowerCase() ?? "N/A"}`}
              </p>
            </div>
            <Badge
              variant={
                subscription?.status === "ACTIVE" ? "success" : "warning"
              }
            >
              {subscription?.status ?? "ACTIVE"}
            </Badge>
          </div>
          {subscription?.stripeCurrentPeriodEnd && (
            <p className="text-sm text-muted-foreground">
              Current period ends{" "}
              {formatDate(subscription.stripeCurrentPeriodEnd)}
            </p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
