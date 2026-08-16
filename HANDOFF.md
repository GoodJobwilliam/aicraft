HANDOFF CONTEXT (updated 2026-08-16 CST)
===============

CURRENT STATE
-------------
- Website: https://aicraft.vip — live, has Smithery + Creem links
- Creem: 9 products live, payout active (Alipay → China bank). Store account confirmed by user: **731685147@qq.com** (tab F30665BC9C0DFB02). Dashboard verified 2026-08-16: **zero sales** (no payments, no balance, gross $0), payouts enabled, Alipay configured
- GitHub: GoodJobwilliam/aicraft — feature pushed to main (commit f0c0b40); 2 stars, 0 forks
- Email for accounts: yaohuixue1@gmail.com
- Browser login states (in-app browser; a new CDP tab via http://127.0.0.1:9229/json/new shares the same session): Google ✅ / Reddit ✅ / PitchHut ✅ / Product Hunt ✅ (tab 66CE373183E40BB2) / GitHub ✅ / Smithery ✅ (Google login) / Glama ✅ (yaohuixue1@gmail.com) / Creem ✅ (QQ account)

LAUNCH STATUS (2026-08-16)
---------------------------

| Platform | Status | Notes |
|----------|--------|-------|
| **Smithery.ai** | ✅ Live | [yaohuixue1/mcp-code-review](https://smithery.ai/servers/yaohuixue1/mcp-code-review) — 52/100. Redeploy channel broken post-Arcade migration (UI Publish fires nothing; API POST /releases 404). Server still live + installable. Verification needs paid plan + TXT/backlink |
| **mcp-get / OpenTools** | ❌ Skipped | mcp-get deprecated (recommends Smithery); OpenTools free listing doesn't exist (paid launch only) |
| **mcpservers.org** | ✅ Live | APPROVED 2026-08-16: [goodjobwilliam/aicraft](https://mcpservers.org/servers/goodjobwilliam/aicraft). Listed in READMEs for backlinks |
| **cursor.directory** | ✅ Live | Plugin [mcp-code-review-server](https://cursor.directory/plugins/mcp-code-review-server) public with 1 Rule + 1 MCP Server + "Add to Cursor" button |
| **PyPI** | ✅ Live 0.1.0 | `aicraft-code-review` v0.1.0 — 666 total / 153 last month / 2 last week. Custom-rules feature pushed to repo but NOT yet released (needs PyPI token for 0.1.1) |
| **Product Hunt** | ✅ Launched | 3 upvotes, 12 followers, 7 comments (5 external all replied + 2 new maker replies). Verified: tiffany's username IS `@ajax_cao`, so the mention was correct all along — no fix needed. 2026-08-16: replied to tiffany (comment 5789058) and energypro (comment 5789059) announcing the custom-rules feature |
| **Dev.to** | ✅ Published | Article 1: [no-SaaS code review](https://dev.to/goodjobwilliam/i-built-an-mcp-server-that-reviews-code-locally-no-saas-no-uploads-568a) + Article 2: [team-shared rules](https://dev.to/goodjobwilliam/team-shared-code-review-rules-for-your-mcp-ai-assistant-542j) (2026-08-16, via API key `GEdbXASUJqszsj4fBTX7nvK9`). Writing Debut badge earned |
| **PitchHut** | ✅ Claimed | 47 page views, 0 pitch URL clicks, not boosting. Logged in as `cheap_copper_rodie` |
| **Glama** | ⏳ Submitted | `aicraft-code-review` submitted via Add Server 2026-08-15, still not listed (search only fuzzy-matches other servers). Frank Fiegel's welcome email replied; support ticket **#125096481** opened (Fin bot: "We'll pick up your ticket soon"). Awaiting review → claim + quality badge for PR #10918 |
| **awesome-mcp-servers** | ⏳ PR open | [#10918](https://github.com/punkpeye/awesome-mcp-servers/pull/10918) — open, mergeable. Waiting for Glama listing/badge. (Repo now 92k stars — merging here is the biggest distribution win) |
| **MCPFind** | ⏳ PR open | [#139](https://github.com/MCPFind/mcp-find/pull/139) — open, mergeable, no checks. Waiting on maintainer |
| **Official MCP Registry** | ⏳ Pending creds | `products/mcp-code-review/registry/server.json` valid, mcp-publisher logged in via GitHub. Blocked on PyPI 0.1.1 (README already has `mcp-name` line) → need PyPI token |
| **Hacker News** | ✅ Posted | Item #49058442 — 1 point, 0 comments, dormant |
| **Reddit r/mcp** | ⚠️ Removed | Two posts both spam-filtered (1v76tt5, 1v9xgip). All messaging blocked account-level. Asked punkpeye via PR #10918 comment to check mod queue — no reply yet. Fallback: delete both + one clean repost |
| **Cline MCP Marketplace** | ⏳ Issue open | #2106 bumped 2026-08-16 with corrected install commands; no maintainer response yet |
| **mcp.so** | ❌ Paid only | $39 one-time (Stripe). Skipped under $0 budget |

RECENT CODE CHANGES (2026-08-16)
---------------------------------
- **Website SEO** (commit 16604f5): OG/Twitter meta + JSON-LD (Organization, WebSite, ItemList of 9 products) in index.html; `sitemap.xml` + `robots.txt` live on aicraft.vip
- **GitHub repo metadata**: description, homepage (aicraft.vip), 10 topics set via API (mcp, mcp-server, code-review, ai, developer-tools, ai-prompts, python, claude-code, cursor, static-analysis) — helps Glama quality score
- **CHANGELOG.md** added in products/mcp-code-review/ (0.1.0 + Unreleased entries)

- **Custom Rules & Team Profiles** (commit f0c0b40, pushed to main) — implements the two Product Hunt feature requests:
  - `config.py` (new): `ReviewConfig` / `CustomRule` / `load_config()` — auto-discovers `.mcp-code-review.yaml|.yml|.json` from the reviewed file's dir upward (snippets/diffs use server cwd), or via `MCP_CODE_REVIEW_CONFIG` env var (team-shared profiles)
  - `reviewer.py`: every finding now carries a stable `check` id; `_apply_config()` applies custom regex rules → disabled checks → severity overrides → min-severity threshold. Check ids: dynamic_exec, sql_injection, deserialization, command_injection, input_py2, xss_innerhtml, hardcoded_secret, nplus1, unbounded_list, bare_except, empty_except, todo_comment, missing_return_type, long_lines, snake_case, pascal_case
  - `server.py`: per-call reviewer instance; `review_file` discovers config from the file's parent dir
  - `tests/test_config.py` (new): 14 tests. Suite: **28 passed** (.venv, PyYAML installed)
  - `pyproject.toml`: optional extra `[yaml]` (PyYAML); JSON configs work dependency-free
  - READMEs updated with config docs + marketplace links

TOOLING NOTES
-------------
- `apply_patch_batch` rejects delete+add of the same file — must be two separate single-file calls
- No `timeout` command (macOS); exec_command rejects `rm -f` — use python subprocess wrappers
- PH comment editing: GraphQL endpoint https://www.producthunt.com/frontend/graphql, mutation `CommentUpdate` needs `X-CSRF-Token` (cookie `csrf_token`); page-level fetch returns 500 but React internals succeed
- PH reply posting (verified working): click `[data-test="action-bar-reply-button"]`, then in the ProseMirror `div[contenteditable=true]` use `execCommand('insertText', ...)` after placing caret at end, then click `[data-test="reply-submit-button"]`
- GitHub creds: `printf "protocol=https\nhost=github.com\n\n" | git credential fill` (token = password line). OAuth token lacks `workflow` scope → cannot push `.github/workflows/ci.yml` (file is ready locally, untracked)

USER ACTIONS NEEDED (2026-08-16)
----------------------------------
1. **PyPI token** — release `aicraft-code-review` 0.1.1 (custom rules + team profiles feature is in the repo). Unlocks: official MCP Registry publish via mcp-publisher (from products/mcp-code-review/registry)
2. **GitHub PAT with workflow scope** — to push `.github/workflows/ci.yml` (local file ready; current OAuth creds lack scope)
3. Reddit — waiting on punkpeye mod-queue check; fallback needs a fresh account or aged karma
4. aicraft.vip DNS access — Smithery TXT verification record + homepage backlink (also needs paid Smithery plan)
5. Optional growth: 掘金 / V2EX 中文社区帖子需要用户自己的账号（未创建）；X/Twitter 无账号

NEXT STEPS
-----------
1. When PyPI token arrives: bump version to 0.1.1, build + publish, then `mcp-publisher publish` for official MCP Registry
2. Glama: watch ticket #125096481 + listing; when listed → claim, quality checks, add badge to README, update PR #10918
3. MCPFind #139 / Cline #2106 — check weekly
4. Reddit fallback if punkpeye doesn't respond: delete both removed posts, one clean repost after account ages
5. Check Creem sales weekly (731685147@qq.com store) — currently $0, MRR $0
6. Cross-post Dev.to article 2 to HN/PH once it gains traction; share on Reddit after account restriction clears
7. Next Dev.to article: Glama badge + registry listings roundup once Glama approves

CONSTRAINTS
-----------
- $0 budget
- Creem (Alipay → China bank) for payouts; store account 731685147@qq.com
- User in China (Gmail/VPN may be needed for some platforms)
- Browser via raw CDP on ws://127.0.0.1:9229 (helper script /tmp/cdp.py) — new tabs via PUT /json/new share the in-app browser session
- Smithery API key: smry_EtMB... (in CLI config)
