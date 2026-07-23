HANDOFF CONTEXT
===============

USER REQUESTS (AS-IS)
---------------------
- "查看一下HANDOFF.md，creem回复了邮件Hi,

Thanks for submitting your onboarding details for AICraft. After reviewing your application, our compliance team requires a few changes to your product and account information before we can approve your store for live payments.

Please review our Account review checklist. Your product likely doesn't comply with one or more items. Ensure your submission fully meets every requirement.

⚠️ Please pay special attention to:

Overall Product Readiness
Clear Pricing Display
Pricing defined but not yet available for purchase
What to do next

1. Go through the checklist and make the required updates to your product and website.

2. Verify that your business information in Store settings is accurate and up to date.

3. Once you've made the required changes, go to your Payout Accounts page and click Request re-review to submit your store for re-review.

Once submitted, our team will promptly re-review your account so we can continue supporting your business. This typically takes 24-48 hours.

Have questions? support@creem.io is here to help.

Best regards,
The Creem team"
- "提交，还有现在不能先把对应zip上传上去吗？"
- "可以"

GOAL
----
Creem re-review submitted and approved so all 9 products can start selling. Next: upload ZIP files to each Creem product, click Request re-review, then after approval begin active sales and promotion.

WORK COMPLETED
--------------
- Installed Creem CLI (npm global @creem_io/cli v0.2.2) and authenticated with live API key
- Created all 9 products on Creem via CLI with correct pricing ($19-$99), tax mode (exclusive, digital-goods-service), and billing type (onetime)
- Generated individual checkout links for each product pointing success URL to https://aicraft.vip/success
- Redesigned index.html from scratch: added Buy on Creem buttons with actual checkout URLs, separated 3 free AgentPowers skills into their own Free section, added refund policy in footer, added payment info section (Visa/Mastercard/Amex/PayPal/Apple Pay/Google Pay), improved overall visual design
- Updated CREEM_PRODUCTS.md with all Creem product IDs and checkout URLs
- Updated HANDOFF.md with current session state
- Committed all changes (commit 61b3e76)

CURRENT STATE
-------------
- Project: /Users/william/work/AIcompany/aicraft/ (git: GoodJobwilliam/aicraft, branch: main)
- Creem store: registered, KYC approved, live mode active, 9 products created with checkout links
- Website: https://aicraft.vip (HTTPS working, Let's Encrypt cert valid until 2026-10-20)
- Website has Buy on Creem buttons for all 9 products, separate free skills section, refund policy
- 9 Creem product IDs generated (prod_395F1NjE24OJPGOy6PH5m through prod_dzmFVoiZqNFRR8f4wujQD)
- Checkout links generated (https://creem.io/checkout/prod_.../ch_...)
- ZIP files ready at products/*.zip for all products
- 3 free AgentPowers skills on separate section (not priced)
- MCP Marketplace: live at free tier (needs Stripe for paid)
- No uncommitted changes in working tree

PENDING TASKS
-------------
- [user-action] Upload each product's ZIP file via Creem Dashboard (Products > select product > File Downloads > upload ZIP)
  - Products ZIP file mapping: 100-ai-prompts.zip ($19), ai-trading-prompts.zip ($29), python-cli-generator.zip ($49), python-cli-zh.zip ($19), mcp-code-review.zip ($49), fastapi-starter.zip ($59), ai-agent-prompts.zip ($29), api-dev-prompts.zip ($19), nextjs-saas-starter.zip ($99)
- [user-action] After uploading ZIPs, go to Creem Dashboard > Balance > Payout Account > Request re-review
- [pending] Creem approval (24-48 hours) - after which products can be sold
- [pending] After Stripe availability: switch MCP Marketplace from free to paid ($49)
- [pending] Submit to MCPFind (guide in submissions/mcpfind-submission.yml)
- [pending] Monitor mcp.directory listing status
- [pending] Consider subscription/prompt membership for recurring revenue

KEY FILES
---------
- index.html - Storefront with Creem checkout links, free skills section, refund policy
- CREEM_PRODUCTS.md - Product manifest with Creem IDs and checkout URLs
- products/*.zip - All 9 product ZIP files ready for upload
- HANDOFF.md - This handoff file
- PROGRESS.md - Progress tracking
- LAUNCHGUIDE.md - MCP marketplace auto-fill metadata
- submissions/ - MCP directory submission guides
- README.md - GitHub repo product catalog

IMPORTANT DECISIONS
-------------------
- Creem API/CLI cannot upload digital files - file uploads must be done through Creem Dashboard web UI (Products > enable File Downloads > upload ZIP)
- All products are one-time purchases (not subscriptions), digital downloads
- Tax mode: exclusive, category: digital-goods-service
- Prices based on prior market research: $19-$99 range, no $10-19 death zone
- Free AgentPowers skills shown separately from paid products to avoid Creem compliance issues
- User provides minimal one-time setup (accounts, API keys); agent handles everything else
- User is in China, Alipay-to-bank payout via Creem is the only payout channel

EXPLICIT CONSTRAINTS
--------------------
- User cannot spend money from their wallet; all costs must be $0
- No Stripe/PayPal/crypto available for payouts; Creem (Alipay to China bank) is the primary payout channel
- User is in China; platforms requiring Stripe/PayPal/crypto are blocked
- User wants AI to work autonomously; they only provide minimal one-time setup (accounts, domain)

CONTEXT FOR CONTINUATION
------------------------
- Creem CLI is installed globally (npm -g @creem_io/cli v0.2.2) and logged in to live environment
- Creem API key used was creem_6ie97AMxyyfX2xROw9WLTj (live)
- The checkout links use per-product checkout sessions (ch_ IDs) - these are permanent but may need recreation if products get updated
- Creem's account review checklist requires: live product, visible pricing, purchase flow, privacy policy + ToS, support email, no false info - all now addressed
- Re-review is requested from Creem Dashboard > Balance > Payout Account
- Typical re-review turnaround: 24-48 hours
- All git operations use path: /Users/william/work/AIcompany/aicraft
- The original stuck session (ses_08517d416ffeJLknfecIWNinRV) is corrupted and should not be revisited
