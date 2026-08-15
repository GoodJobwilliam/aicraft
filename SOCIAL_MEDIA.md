# 社交媒体推广帖（草稿）

## Reddit — r/MCP

> **Title:** I built an open-source MCP server for AI code review with OWASP scanning
>
> **Body:**
> Hey r/MCP,
>
> I've been using Claude Code + Cursor for a while and wanted automated code review without paying for yet another SaaS subscription. So I built an MCP server that does exactly that.
>
> **MCP Code Review Server** — 3 tools, zero SaaS fees:
> - `review_code` — paste any code, get structured feedback (bugs, security, performance)
> - `review_diff` — review git diffs before merging
> - `review_file` — review local files by path
>
> It integrates with Claude Code, Cursor, Cline — any MCP client. The review includes OWASP security pattern scanning out of the box.
>
> GitHub: https://github.com/GoodJobwilliam/aicraft/tree/main/products/mcp-code-review
> Install: `pip install aicraft-code-review`
>
> Would love feedback from the community!

---

## Reddit — r/ClaudeAI

> **Title:** PSA: You can add AI code review to Claude Code in 30 seconds for free
>
> **Body:**
> Just discovered this workflow and wanted to share:
>
> ```
> pip install aicraft-code-review
> claude mcp add code-review -- uvx aicraft-code-review
> ```
>
> Now you can just ask Claude to "review this code" and it runs structural analysis + OWASP checks before responding. No more pasting into ChatGPT.
>
> It's an open MCP server, works with Cursor/Cline too. The review output is way more detailed than what Claude gives you by default because it's running purpose-built analysis tools.

---

## Product Hunt

> **Tagline:** AI code review that works in your editor — no SaaS fees, no uploads
>
> **Description:**
> MCP Code Review Server brings production-grade code review to your AI coding assistant.
>
> **Key Features:**
> - 🔒 OWASP security scanning built-in
> - 🐛 Bug and vulnerability detection
> - 📊 Structured severity ratings
> - 🔌 Works with Claude Code, Cursor, Cline
> - 💰 One-time $49 payment, lifetime updates
>
> **How it works:**
> 1. `pip install aicraft-code-review`
> 2. Add to your MCP client config
> 3. Ask your AI to review any code

---

## Hacker News — Show HN

> **Title:** Show HN: MCP Code Review Server – AI code review in your editor, self-hosted
>
> **Body:**
> I built an MCP server that adds code review capabilities to any AI coding assistant.
>
> Three tools:
> - review_code(code, language) → structured feedback with severity
> - review_diff(diff) → review git changes before merging
> - review_file(path) → review any file by path
>
> Why I built it: all the AI code review tools I found were either SaaS (upload your code to someone's server) or required a paid Copilot subscription. This runs locally, uses your existing LLM, and costs $49 once.
>
> Tech stack: Python, MCP protocol, supports any LLM backend (OpenAI, Anthropic, Groq, local models).
>
> Install: pip install aicraft-code-review
> Repo: https://github.com/GoodJobwilliam/aicraft/tree/main/products/mcp-code-review
> Site: https://aicraft.vip

## Dev.to — Published 2026-08-16

> **URL:** https://dev.to/goodjobwilliam/i-built-an-mcp-server-that-reviews-code-locally-no-saas-no-uploads-568a
> **Title:** I Built an MCP Server That Reviews Code Locally — No SaaS, No Uploads
> **Tags:** #mcp #opensource #python
> **Account:** goodjobwilliam (GitHub OAuth)
