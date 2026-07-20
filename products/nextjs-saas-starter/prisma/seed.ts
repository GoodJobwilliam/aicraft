import { PrismaClient } from "@prisma/client";
import bcrypt from "bcryptjs";

const prisma = new PrismaClient();

async function main() {
  console.log("🌱 Seeding database...");

  // Clean existing data
  await prisma.subscription.deleteMany();
  await prisma.session.deleteMany();
  await prisma.account.deleteMany();
  await prisma.user.deleteMany();

  // Create admin user
  const adminPassword = await bcrypt.hash("admin123", 12);
  const admin = await prisma.user.create({
    data: {
      name: "Admin User",
      email: "admin@example.com",
      passwordHash: adminPassword,
      role: "ADMIN",
    },
  });

  await prisma.subscription.create({
    data: {
      userId: admin.id,
      plan: "PRO_MONTHLY",
      status: "ACTIVE",
    },
  });

  // Create demo user
  const userPassword = await bcrypt.hash("demo123", 12);
  const demo = await prisma.user.create({
    data: {
      name: "Demo User",
      email: "demo@example.com",
      passwordHash: userPassword,
      role: "USER",
    },
  });

  await prisma.subscription.create({
    data: {
      userId: demo.id,
      plan: "FREE",
      status: "ACTIVE",
    },
  });

  console.log("✅ Seed complete!");
  console.log("   Admin: admin@example.com / admin123");
  console.log("   Demo:  demo@example.com / demo123");
}

main()
  .catch((e) => {
    console.error("❌ Seed failed:", e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
