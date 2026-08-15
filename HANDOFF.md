HANDOFF CONTEXT (updated 2026-08-15 CST)
===============

CURRENT STATE
-------------
- Website: https://aicraft.vip — live, has Smithery + Creem links
- Creem: 9 products live, payout active (Alipay → China bank); all 9 checkout links verified 200 this round
- GitHub: GoodJobwilliam/aicraft — all changes pushed; 2 stars, 0 forks
- Email for accounts: yaohuixue1@gmail.com
- Browser login states (in-app browser; a new CDP tab via http://127.0.0.1:9229/json/new shares the same session): Google ✅ / Reddit ✅ / PitchHut ✅ / Product Hunt ❌ logged out / GitHub ✅ (GoodJobwilliam, tab B97CF33D7CE0A9A76CC72D29B953D4DE)

LAUNCH STATUS (2026-08-15)
---------------------------

| Platform | Status | Notes |
|----------|--------|-------|
| **Smithery.ai** | ✅ Live | [yaohuixue1/mcp-code-review](https://smithery.ai/servers/yaohuixue1/mcp-code-review) — quality score 52/100 unchanged, "No capabilities found" (stdio not introspected), deployed ~20 days ago |
| **Glama** | ⏳ Submitted | Submitted `aicraft-code-review` via Add Server 2026-08-15 (logged in as yaohuixue1@gmail.com). Repo pushed with `glama.json`, `products/mcp-code-review/Dockerfile`, MIT LICENSE. Awaiting Glama review/checks → then claim + quality badge for PR #10918 |
| **Official MCP Registry** | ⏳ Pending creds | `products/mcp-code-review/registry/server.json` valid (name `io.github.GoodJobwilliam/aicraft-code-review`). Publish blocked: PyPI README must contain `mcp-name: io.github.GoodJobwilliam/aicraft-code-review` (added to repo README) → need PyPI token to release 0.1.1. mcp-publisher installed at /tmp/mcp-publisher, already logged in via GitHub |
| **Product Hunt** | ✅ Launched | 3 upvotes, 12 followers. Still no new comments (5 total, all replied). Minor: reply to `tiffany` still starts with `@ajax_cao` — fixing requires PH login, session is logged out |
| **Hacker News** | ✅ Posted | [Item #49058442](https://news.ycombinator.com/item?id=49058442) — 1 point, 0 comments, dormant |
| **Reddit r/mcp** | ⚠️ Removed | TWO posts both caught by spam filter: [1v76tt5](https://www.reddit.com/r/mcp/comments/1v76tt5/) and [1v9xgip](https://www.reddit.com/r/mcp/comments/1v9xgip/). All Reddit messaging blocked server-side (verified 2026-08-15): modmail + PMs to punkpeye/lucgagan all return `You can't message that user.` — account-level restriction (20d old, 1 link karma). Posts still `removed_by_category: reddit`. ✅ 2026-08-15: asked punkpeye via PR comment [issuecomment-5302901572](https://github.com/punkpeye/awesome-mcp-servers/pull/10918#issuecomment-5302901572) to check the mod queue |
| **Reddit r/ClaudeAI** | ⏳ Never posted | Account has only the 2 r/mcp posts — r/ClaudeAI draft in SOCIAL_MEDIA.md (now uses correct package name) |
| **PitchHut** | ✅ Claimed | [aicraft-ai-tools-templates](https://www.pitchhut.com/project/aicraft-ai-tools-templates) — published, 47 page views, 0 pitch URL clicks, not boosting. Logged in as `cheap_copper_rodie` |
| **PyPI** | ✅ Name consistent | `aicraft-code-review` v0.1.0 — 666 total / 153 last month / 2 last week. All repo copy now uses `aicraft-code-review` (fixed 2026-08-15) |
| **awesome-mcp-servers** | ⏳ PR open | [#10918](https://github.com/punkpeye/awesome-mcp-servers/pull/10918) — Glama submitted 2026-08-15 + repo prepared (glama.json/Dockerfile/LICENSE); comments on PR: Reddit mod-queue ask [5302901572](https://github.com/punkpeye/awesome-mcp-servers/pull/10918#issuecomment-5302901572), Glama progress [5302967022](https://github.com/punkpeye/awesome-mcp-servers/pull/10918#issuecomment-5302967022). Waiting for Glama review → claim → badge |
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
5. 🟢 **Cline MCP Marketplace** — No activity since Jul 24, could follow up on #2106
6. 🟢 **Smithery quality (52/100)** — Still "No capabilities found" (stdio-only servers aren't introspected). Options unchanged: TXT domain verification on aicraft.vip, or paid remote hosting

CONSTRAINTS
-----------
- $0 budget
- Creem (Alipay → China bank) for payouts
- User in China (Gmail/VPN may be needed for some platforms)
- Browser via raw CDP on ws://127.0.0.1:9229 (helper script /tmp/cdp.py) — new tabs via PUT /json/new share the in-app browser session
- Smithery API key: smry_EtMB... (in CLI config)
