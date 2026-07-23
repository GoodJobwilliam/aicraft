HANDOFF CONTEXT
===============

USER REQUESTS (AS-IS)
---------------------
- "有一个对话卡死了，叫Agents build busy,你帮我看看情况"
- "是的，我想问的是https://aicraft.vip这个地址我已经可以访问了，但是https还没好，是不是ssl证书还没签发"
- "可以调整一下"
- "我需要的是你自己赚钱，不是问我应该多少唉，我负责账号等，你负责生产、推广、销售等一系列工作，我只要看到账户进账就行，而且目标是$2000每月"
- "把这个项目整体迁移到/Users/william/work/AIcompany下"

GOAL
----
Get HTTPS working on aicraft.vip, then go to Creem to request re-review so all 9 products can be listed for sale.

WORK COMPLETED
-------------
- Diagnosed a stuck session (ses_08517d416ffeJLknfecIWNinRV) where compaction produced corrupted repeated output, causing Agents build busy state
- Analyzed market pricing for AI prompts, developer boilerplates, MCP tools; adjusted all prices based on real market data
- Built 4 new products: FastAPI Starter Kit ($59, 31 files), AI Agent Prompts Pack ($29, 50 prompts), API Development Prompts ($19, 35 prompts), Next.js SaaS Starter Kit ($99, 69 files, 15 tests)
- Updated website index.html with all 9 products and new pricing
- Created GitHub repo README with full product catalog
- Set GitHub Topics (mcp, code-review, security, python, model-context-protocol) for auto-discovery by Glama/PulseMCP
- Published MCP Code Review Server (free tier) on mcp-marketplace.io
- Submitted MCP server to mcp.directory (pending review)
- Created LAUNCHGUIDE.md at repo root for marketplace auto-fill
- Prepared submission guides in submissions/ directory
- Moved project from /Users/william/Desktop/aicraft to /Users/william/work/AIcompany/aicraft
- Fixed HTTPS: deleted and recreated GitHub Pages config via API, triggered Let's Encrypt cert issuance for aicraft.vip (Let's Encrypt YR1, expires 2026-10-20), enabled HTTPS enforcement

CURRENT STATE
-------------
- Project: /Users/william/work/AIcompany/aicraft/ (git: GoodJobwilliam/aicraft)
- 9 products ready: 100 Developer AI Prompts ($19), AI+Trading Prompt Pack ($29), AI Agent Prompts Pack ($29), API Development Prompts ($19), Python CLI Generator ($49), Python CLI Chinese Template ($19), FastAPI Starter Kit ($59), Next.js SaaS Starter Kit ($99), MCP Code Review Server ($49)
- 3 free AgentPowers skills: Code Review Agent, Git Commit Assistant, PR Description Generator
- Website: https://aicraft.vip (HTTPS working, Let's Encrypt cert issued, enforcement enabled)
- MCP Marketplace listing: live (free tier, needs Stripe for paid)
- Creem store: registered, KYC approved, waiting for HTTPS to re-review
- Revenue target: $2000/month (avg ~$35/sale, need ~57 sales/month)

PENDING TASKS
-------------
- [done] SSL 证书签发 (Let's Encrypt YR1, aicraft.vip, 有效期至 2026-10-20)
- [done] Creem 全部 9 个产品已创建 + checkout 链接已生成 (2026-07-23)
- [done] 网站改版: 加 Buy on Creem 按钮、分离免费产品、加退款政策
- [user-action] 去 Creem 点重新审核 (Creem > Payout Accounts > Request re-review)
- [pending] Creem 审核通过后产品即可开始销售
- After Stripe availability: switch MCP Marketplace from free to paid ($49)
- Submit to MCPFind (guide in submissions/mcpfind-submission.yml)
- Monitor mcp.directory listing status (24h review)
- Consider subscription/prompt membership for recurring revenue

KEY FILES
---------
- /Users/william/work/AIcompany/aicraft/index.html - Storefront with all 9 products
- /Users/william/work/AIcompany/aicraft/CREEM_PRODUCTS.md - Product manifest for Creem listing
- /Users/william/work/AIcompany/aicraft/PROGRESS.md - Progress tracking
- /Users/william/work/AIcompany/aicraft/LAUNCHGUIDE.md - MCP marketplace auto-fill metadata
- /Users/william/work/AIcompany/aicraft/products/ - All product ZIPs and source files
- /Users/william/work/AIcompany/aicraft/submissions/ - MCP directory submission guides
- /Users/william/work/AIcompany/aicraft/products/nextjs-saas-starter/ - Full SaaS scaffold
- /Users/william/work/AIcompany/aicraft/products/mcp-code-review/ - MCP server source
- /Users/william/work/AIcompany/aicraft/README.md - GitHub repo product catalog
- /Users/william/work/AIcompany/aicraft/HANDOFF.md - This handoff file

IMPORTANT DECISIONS
-------------------
- User handles accounts only; AI handles production, marketing, sales autonomously
- Chrome 显示"不安全"是缓存问题，忽略；微信 ICP 备案警告是 GitHub Pages 先天限制，暂不处理
- All products sold as one-time purchases via Creem (Alipay payout for China user)
- Pricing based on Gumroad 2026 market data: $10-19 is death zone, $30-49 converts 28% better
- MCP server published as free on marketplace because user has no Stripe
- Target $2000/month across 9 products

EXPLICIT CONSTRAINTS
--------------------
- User cannot spend money from their wallet; all costs must be $0
- No Stripe/PayPal/crypto available for payouts; Creem (Alipay to China bank) is the primary payout channel
- User is in China; platforms requiring Stripe/PayPal/crypto are blocked
- User wants AI to work autonomously; they only provide minimal one-time setup (accounts, domain)

CONTEXT FOR CONTINUATION
-----------------------
- ✅ HTTPS is working on aicraft.vip (Let's Encrypt cert issued, enforcement enabled)
- Next step: user needs to go to Creem > Payout Accounts > Request re-review
- After Creem approval: create all 9 products in Creem dashboard using ZIPs from products/
- MCP marketplace listing is live at free tier; switch to paid when user gets Stripe
- The original stuck session (ses_08517d416ffeJLknfecIWNinRV) is corrupted and should not be revisited
- All git operations use path: /Users/william/work/AIcompany/aicraft
