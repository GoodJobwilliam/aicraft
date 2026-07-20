# Next.js SaaS Starter Kit

> **Production-ready SaaS boilerplate. Auth, subscriptions, dashboard, email — all built and ready to deploy.**

Save **40+ hours** of repetitive setup with a complete, professional-grade Next.js 14+ foundation. Built with TypeScript, Auth.js, Stripe, Prisma, and Tailwind CSS.

![Version](https://img.shields.io/badge/version-1.0.0-black)
![Next.js](https://img.shields.io/badge/Next.js-14-black)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue)
![Stripe](https://img.shields.io/badge/Stripe-integrated-purple)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

### 🔐 Authentication
- Email/password registration & login with bcrypt hashing
- Google OAuth & GitHub OAuth integration
- Forgot password flow with email reset
- Session management via Auth.js v5 (NextAuth.js)
- JWT-based sessions with TypeScript types

### 💳 Subscription Billing
- Full Stripe integration (Checkout + Webhooks + Customer Portal)
- Monthly and annual pricing with toggle
- Stripe webhook handling for subscription lifecycle
- Automatic subscription status sync
- Customer Portal for managing payment methods & invoices

### 📊 Dashboard
- Professional sidebar navigation (desktop + mobile)
- Overview with stats cards
- Settings page (profile + password change)
- Billing page with plan comparison
- Responsive design (mobile-first)

### 📧 Transactional Emails
- Welcome email on registration
- Subscription confirmation email
- Password reset email
- Beautiful HTML templates (customizable)
- Powered by Resend

### 🎨 UI Components
- 15+ production-ready components (Button, Card, Input, Dialog, Toast, Badge, Avatar, Dropdown, Tabs, Switch, etc.)
- Dark mode support via `next-themes`
- Framer Motion animations
- Responsive throughout

### 🧪 Testing
- Vitest + React Testing Library
- Component tests for UI library
- Utility function tests
- Ready-to-extend test setup

---

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- PostgreSQL (local or Docker)
- Stripe account (for subscriptions)
- Resend account (for email)

### 1. Clone & Install

```bash
git clone <your-repo-url> my-saas
cd my-saas
cp .env.example .env
npm install
```

### 2. Start PostgreSQL

```bash
# Using Docker (recommended)
docker compose up -d postgres

# Or use make
make db-up
```

### 3. Configure Environment

Edit `.env` with your credentials:

```env
# Required
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/saas_starter"
AUTH_SECRET="your-secret-here"  # npx auth secret

# Optional (for OAuth)
AUTH_GOOGLE_ID=
AUTH_GOOGLE_SECRET=
AUTH_GITHUB_ID=
AUTH_GITHUB_SECRET=

# Stripe (required for billing)
STRIPE_SECRET_KEY=
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
STRIPE_WEBHOOK_SECRET=
STRIPE_PRICE_MONTHLY=
STRIPE_PRICE_YEARLY=

# Resend (required for email)
RESEND_API_KEY=
RESEND_FROM_EMAIL=noreply@yourdomain.com
```

### 4. Database Setup

```bash
npm run db:migrate
npm run db:seed
```

### 5. Start Development

```bash
npm run dev
# or
make dev
```

Open [http://localhost:3000](http://localhost:3000) 🎉

---

## 🏗️ Project Structure

```
nextjs-saas-starter/
├── prisma/
│   ├── schema.prisma          # Database schema (User, Subscription, Account, Session)
│   └── seed.ts                # Seed data (admin + demo users)
├── src/
│   ├── app/
│   │   ├── (auth)/            # Auth pages (login, register, forgot-password)
│   │   ├── (dashboard)/       # Dashboard pages (home, settings, billing)
│   │   ├── api/               # API routes (auth, stripe, user)
│   │   ├── layout.tsx         # Root layout with providers
│   │   └── page.tsx           # Landing page
│   ├── components/
│   │   ├── ui/                # Reusable UI components (shadcn-inspired)
│   │   ├── dashboard/         # Dashboard-specific (sidebar, header)
│   │   ├── landing/           # Landing page sections
│   │   └── providers.tsx      # Session + Theme providers
│   ├── hooks/                 # Custom hooks (use-toast)
│   ├── lib/
│   │   ├── auth.ts            # NextAuth.js configuration
│   │   ├── db.ts              # Prisma client singleton
│   │   ├── stripe.ts          # Stripe client + helpers
│   │   ├── email.ts           # Email sending (Resend)
│   │   └── utils.ts           # Utility functions
│   ├── styles/
│   │   └── globals.css        # Tailwind + CSS variables
│   └── types/
│       └── index.ts           # Shared TypeScript types
├── tests/
│   ├── setup.ts               # Test setup + mocks
│   └── example.test.ts        # Component + utility tests
├── docker-compose.yml         # PostgreSQL + App
├── Dockerfile                 # Production build
├── Makefile                   # Dev commands
└── .env.example               # Environment template
```

---

## 🛠️ Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Production build |
| `npm run test` | Run tests |
| `npm run lint` | Lint code |
| `npm run typecheck` | TypeScript check |
| `npm run db:migrate` | Run database migrations |
| `npm run db:seed` | Seed database |
| `npm run db:studio` | Open Prisma Studio |
| `npm run db:reset` | Reset database |
| `make dev` | Start dev server |
| `make db-up` | Start PostgreSQL |
| `make setup` | Full project setup |

---

## 📦 Tech Stack

| Category | Technology |
|----------|-----------|
| **Framework** | Next.js 14 (App Router) |
| **Language** | TypeScript 5 |
| **Styling** | Tailwind CSS 3 + CSS Variables |
| **Auth** | Auth.js v5 (NextAuth.js) |
| **Database** | PostgreSQL + Prisma ORM |
| **Payments** | Stripe (Checkout + Webhooks + Portal) |
| **Email** | Resend |
| **Forms** | React Hook Form + Zod |
| **UI** | Radix UI Primitives + shadcn-inspired |
| **Animation** | Framer Motion |
| **Testing** | Vitest + Testing Library |

---

## 🔒 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABASE_URL` | ✅ | PostgreSQL connection string |
| `AUTH_SECRET` | ✅ | NextAuth.js encryption secret |
| `AUTH_GOOGLE_ID` | ❌ | Google OAuth client ID |
| `AUTH_GOOGLE_SECRET` | ❌ | Google OAuth client secret |
| `AUTH_GITHUB_ID` | ❌ | GitHub OAuth client ID |
| `AUTH_GITHUB_SECRET` | ❌ | GitHub OAuth client secret |
| `STRIPE_SECRET_KEY` | ❌* | Stripe secret key |
| `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` | ❌* | Stripe publishable key |
| `STRIPE_WEBHOOK_SECRET` | ❌* | Stripe webhook signing secret |
| `STRIPE_PRICE_MONTHLY` | ❌* | Stripe monthly price ID |
| `STRIPE_PRICE_YEARLY` | ❌* | Stripe yearly price ID |
| `RESEND_API_KEY` | ❌* | Resend API key |

*Required for the corresponding feature (billing/email).

---

## 🐳 Docker Deployment

```bash
# Build and run with Docker Compose
docker compose up -d

# Or using make
make docker-up
```

The production Docker image:
1. Installs dependencies in a `deps` stage
2. Builds the app in a `builder` stage
3. Runs with a non-root `nextjs` user
4. Exposes port 3000

---

## 📝 License

MIT — use for personal and commercial projects.

---

## 🤝 Support

- Documentation: Read this README
- Issues: Open a GitHub issue
- Email: support@saasstarter.com

---

*Built with ❤️ for developers who want to ship faster.*
