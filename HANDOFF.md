HANDOFF CONTEXT (updated 2026-07-29)
===============

CURRENT STATE
-------------
- Website: https://aicraft.vip — live, has Smithery + Creem links
- Creem: 9 products live, payout active (Alipay → China bank)
- GitHub: GoodJobwilliam/aicraft — all changes pushed
- Email for accounts: yaohuixue1@gmail.com

LAUNCH STATUS (2026-07-29)
---------------------------

| Platform | Status | Notes |
|----------|--------|-------|
| **Smithery.ai** | ✅ Live | [yaohuixue1/mcp-code-review](https://smithery.ai/servers/yaohuixue1/mcp-code-review) — published via MCPB bundle, quality score 52/100 |
| **Product Hunt** | ✅ Launching | Scheduled for July 29 at 12:01 AM PDT. Images uploaded, comments active. [Edit page](https://www.producthunt.com/posts/mcp-code-review-server/edit) |
| **Hacker News** | ✅ Posted | [Item #49058442](https://news.ycombinator.com/item?id=49058442) — Show HN blocked (new account), posted as regular link |
| **Reddit r/mcp** | ⚠️ Removed | [Post](https://www.reddit.com/r/mcp/comments/1v76tt5/) caught by spam filter. Needs account aging or modmail appeal |
| **Reddit r/ClaudeAI** | ❌ Blocked | New account post button disabled. Draft in SOCIAL_MEDIA.md |
| **PitchHut** | ⏳ Pending | Signup link sent to yaohuixue1@gmail.com. Click in inbox to claim [preview page](https://pitchhut.com/project/aicraft-ai-tools-templates) |
| **PyPI** | ✅ Done | `pip install mcp-code-review` works |
| **awesome-mcp-servers** | ✅ PR submitted | [#10918](https://github.com/punkpeye/awesome-mcp-servers/pull/10918) |
| **Cline MCP Marketplace** | ✅ Submitted | [Issue #2106](https://github.com/cline/mcp-marketplace/issues/2106) |

CODE FIXES PUSHED (2026-07-26/29)
----------------------------------
- `pyproject.toml` — Added `build-system`, `tool.uv.package = true`, entry point fix
- `__init__.py` — Added `asyncio.run()` wrapper for async main
- `__main__.py` — New file for `python -m mcp_code_review`
- `smithery.yaml` — Updated config schema with llmApiKey
- `.well-known/mcp/server-card.json` — Static server metadata
- `index.html` — Added Smithery marketplace link
- `README.md` — Added Smithery badge + Product Hunt launch badge
- `mcp-code-review.mcpb` — MCPB bundle for Smithery deployment

NEXT STEPS (new conversation)
------------------------------
1. **PitchHut** — Check yaohuixue1@gmail.com for login link, claim project page
2. **Product Hunt** — Check live launch stats, reply to user comments
3. **Reddit r/mcp** — Account aged (2 days), could try reposting or modmail appeal
4. **Reddit r/ClaudeAI** — Same account restriction, draft ready in SOCIAL_MEDIA.md
5. **Smithery quality** — 52/100, improvements: TXT record on aicraft.vip, link from website to Smithery (done), paid plan

CONSTRAINTS
-----------
- $0 budget
- Creem (Alipay → China bank) for payouts
- User in China
- Browser interactions via Playwright CDP (ws://127.0.0.1:9229)
- Smithery API key: smry_EtMB... (in CLI config)
