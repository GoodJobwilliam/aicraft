HANDOFF CONTEXT (updated 2026-08-15 CST)
===============

CURRENT STATE
-------------
- Website: https://aicraft.vip — live, has Smithery + Creem links
- Creem: 9 products live, payout active (Alipay → China bank); all 9 checkout links verified 200 this round
- GitHub: GoodJobwilliam/aicraft — all changes pushed; 2 stars, 0 forks
- Email for accounts: yaohuixue1@gmail.com
- Browser login states (in-app browser; a new CDP tab via http://127.0.0.1:9229/json/new shares the same session): Google ✅ / Reddit ✅ / PitchHut ✅ / Product Hunt ❌ logged out / GitHub ✅ (tab B97CF33D7CE0A9A76CC72D29B953D4DE) / Smithery ✅ (Google login, tab EB2A5316171BDBA656A7BF5FE7845F73) / Glama ✅ (yaohuixue1@gmail.com, tab 534F2F4A63022AC533A0DE84C48F4BB2)

LAUNCH STATUS (2026-08-15)
---------------------------

| Platform | Status | Notes |
|----------|--------|-------|
| **Smithery.ai** | ✅ Live | [yaohuixue1/mcp-code-review](https://smithery.ai/servers/yaohuixue1/mcp-code-review) — 52/100, "No capabilities found". History shows many FAILURE releases ("Build — No values to set") from empty configSchema. 2026-08-16: simplified smithery.yaml pushed, but redeploy channel broken post-Arcade migration (UI Publish fires nothing; API POST /releases 404). Server still live + installable. Verification needs paid plan + TXT/backlink (user DNS) |
| **Glama** | ⏳ Submitted | Submitted `aicraft-code-review` via Add Server 2026-08-15 (logged in as yaohuixue1@gmail.com). Repo pushed with `glama.json`, `products/mcp-code-review/Dockerfile`, MIT LICENSE. 2026-08-16: replied to Frank Fiegel's welcome email from Gmail (sent) explaining MCP use case + asking review status. Still not listed in directory search. Awaiting review → claim + quality badge for PR #10918 |
| **Official MCP Registry** | ⏳ Pending creds | `products/mcp-code-review/registry/server.json` valid (name `io.github.GoodJobwilliam/aicraft-code-review`). Publish blocked: PyPI README must contain `mcp-name: io.github.GoodJobwilliam/aicraft-code-review` (added to repo README) → need PyPI token to release 0.1.1. mcp-publisher installed at /tmp/mcp-publisher, already logged in via GitHub |
| **Product Hunt** | ✅ Launched | 3 upvotes, 12 followers. Still no new comments (5 total, all replied). Minor: reply to `tiffany` still starts with `@ajax_cao` — fixing requires PH login, session is logged out |
| **Hacker News** | ✅ Posted | [Item #49058442](https://news.ycombinator.com/item?id=49058442) — 1 point, 0 comments, dormant |
| **Reddit r/mcp** | ⚠️ Removed | TWO posts both caught by spam filter: [1v76tt5](https://www.reddit.com/r/mcp/comments/1v76tt5/) and [1v9xgip](https://www.reddit.com/r/mcp/comments/1v9xgip/). All Reddit messaging blocked server-side (verified 2026-08-15): modmail + PMs to punkpeye/lucgagan all return `You can't message that user.` — account-level restriction (20d old, 1 link karma). Posts still `removed_by_category: reddit`. ✅ 2026-08-15: asked punkpeye via PR comment [issuecomment-5302901572](https://github.com/punkpeye/awesome-mcp-servers/pull/10918#issuecomment-5302901572) to check the mod queue |
| **Reddit r/ClaudeAI** | ⏳ Never posted | Account has only the 2 r/mcp posts — r/ClaudeAI draft in SOCIAL_MEDIA.md (now uses correct package name) |
| **PitchHut** | ✅ Claimed | [aicraft-ai-tools-templates](https://www.pitchhut.com/project/aicraft-ai-tools-templates) — published, 47 page views, 0 pitch URL clicks, not boosting. Logged in as `cheap_copper_rodie` |
| **PyPI** | ✅ Name consistent | `aicraft-code-review` v0.1.0 — 666 total / 153 last month / 2 last week. All repo copy now uses `aicraft-code-review` (fixed 2026-08-15) |
| **awesome-mcp-servers** | ⏳ PR open | [#10918](https://github.com/punkpeye/awesome-mcp-servers/pull/10918) — Glama submitted 2026-08-15 + repo prepared (glama.json/Dockerfile/LICENSE); comments on PR: Reddit mod-queue ask [5302901572](https://github.com/punkpeye/awesome-mcp-servers/pull/10918#issuecomment-5302901572), Glama progress [5302967022](https://github.com/punkpeye/awesome-mcp-servers/pull/10918#issuecomment-5302967022). Waiting for Glama review → claim → badge |
| **MCPFind** | ⏳ PR open | [#139](https://github.com/MCPFind/mcp-find/pull/139) — opened 2026-08-16 (fork GoodJobwilliam/mcp-find, `community-servers.yml` entry, pypi/devtools). Mergeable, no checks configured, awaiting maintainer merge |
| **mcpservers.org** | ⏳ Submitted | Free submission 2026-08-16 (category Development). Review promised within 12h; email notification to yaohuixue1@gmail.com |
| **cursor.directory** | ⏳ Scanning | Plugin [mcp-code-review-server](https://cursor.directory/plugins/mcp-code-review-server) submitted 2026-08-16 — repo `.mcp.json` + `rules/mcp-code-review.mdc` (Open Plugins standard). Awaiting security agent scan → public |
| **Dev.to** | ✅ Published | [Article](https://dev.to/goodjobwilliam/i-built-an-mcp-server-that-reviews-code-locally-no-saas-no-uploads-568a) 2026-08-16 (tags #mcp #opensource #python). Account goodjobwilliam via GitHub OAuth |
| **mcp.so** | ❌ Paid only | Submission is $39 one-time (Stripe). Skipped under $0 budget |
| **Cline MCP Marketplace** | ⏳ Issue open | [#2106](https://github.com/cline/mcp-marketplace/issues/2106) — no comments since Jul 24 |

RECENT CODE CHANGES (2026-07-29)
---------------------------------
- `products/mcp-code-review/src/mcp_code_review/reviewer.py` — **Bug fix**: f-string in style pass was showing `{func_match.group(1).lower()}` literally instead of evaluating it. Added missing `f` prefix. All 11 tests pass.

DOC FIXES (2026-08-15)
----------------------
- PyPI naming consistency: `LAUNCHGUIDE.md`, `products/mcp-code-review/LAUNCHGUIDE.md`, `products/mcp-code-review/llms-install.md`, `products/mcp-code-review/README.md`, `SOCIAL_MEDIA.md` — all install commands now use `aicraft-code-review` (incl. uvx args)

PREVIOUS CODE FIXES (2026-07-26/29)
------------------------------------
- `pyproject.toml` — Added `build-system`, `tool.uv.package = true`, entry point fix
- `__init__.py` — Added `asyncio.run()` wrapper for async main
- `__main__.py` — New file for `python -m mcp_code_review`
- `smithery.yaml` — Updated config schema with llmApiKey
- `.well-known/mcp/server-card.json` — Static server metadata
- `index.html` — Added Smithery marketplace link
- `README.md` — Added Smithery badge + Product Hunt launch badge
- `mcp-code-review.mcpb` — MCPB bundle for Smithery deployment

NEXT STEPS
-----------
1. 🟡 **Glama** — ✅ submitted 2026-08-15 (pending review). When listed: claim it, wait for quality checks, add Glama score badge to README, and update PR #10918. Check Gmail (yaohuixue1@gmail.com) for review emails
2. 🟡 **Reddit r/mcp** — Modmail/PM all rejected by Reddit servers. ✅ PR comment sent 2026-08-15 asking punkpeye (r/mcp mod) to check mod queue; waiting for reply. Fallback if no response: delete both posts + one clean repost (no "test body")
3. 🟡 **Official MCP Registry** — server.json ready + CLI authenticated. Needs PyPI 0.1.1 release with `mcp-name` line in README (token required from user), then `mcp-publisher publish` from products/mcp-code-review/registry
4. 🟢 **Product Hunt** — Fix the `@ajax_cao` mis-mention in the reply to `tiffany`. Needs PH login first (session logged out; user can sign in with Google in the in-app browser tab)
4. ✅ **PyPI naming** — DONE 2026-08-15, all repo copy uses `aicraft-code-review`
5. 🟡 **Cline MCP Marketplace** — ✅ bumped #2106 on 2026-08-16 with corrected install commands (`aicraft-code-review`); waiting for review
6. 🟡 **Smithery quality (52/100)** — Config fixed & pushed (smithery.yaml). Republish via Releases page → watch for SUCCESS + capabilities. Verification itself needs paid plan. TXT DNS + homepage backlink would help score; needs user DNS access

USER ACTIONS NEEDED (2026-08-16)
----------------------------------
1. PyPI token — to publish `aicraft-code-review` 0.1.1 (README now has `mcp-name` line) so official MCP Registry publish passes ownership validation
2. Product Hunt login (Google) — still logged out; PH Google OAuth is blocked in the in-app browser ("browser insecure"), needs the user to sign in manually (in-app browser or their own Chrome)
5. Creem store ownership — logging in with yaohuixue1@gmail.com (magic link AND Google) lands on an empty "create store" account. The 9-product store must be under a different account (possibly yaohuixue2@gmail.com). User should confirm which account owns the Creem store so we can track sales
3. aicraft.vip DNS access — Smithery TXT verification record + homepage backlink (verification also needs paid plan)
4. GitHub PAT with workflow scope — to push `.github/workflows/ci.yml` (local file ready; current OAuth creds lack scope)

CONSTRAINTS
-----------
- $0 budget
- Creem (Alipay → China bank) for payouts
- User in China (Gmail/VPN may be needed for some platforms)
- Browser via raw CDP on ws://127.0.0.1:9229 (helper script /tmp/cdp.py) — new tabs via PUT /json/new share the in-app browser session
- Smithery API key: smry_EtMB... (in CLI config)
