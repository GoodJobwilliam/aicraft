# AICraft — AI-Powered Developer Tools

Production-ready developer tools, code templates, and AI prompt packs. Built by engineers, for engineers.

## Products

### Prompt Packs

| Product | Price | Description |
|---------|-------|-------------|
| [100 Developer AI Prompts](./products/100-ai-prompts/) | $19 | 100 battle-tested prompts covering code review, testing, DevOps, security, and APIs. Copy, paste, ship. |
| [AI + Trading Prompt Pack](./products/ai-trading-prompts/) | $29 | 30 prompts for AI-powered stock analysis. Level 2 order book, technical patterns, fund flow, sentiment, backtesting. |
| [AI Agent Prompts Pack](./products/ai-agent-prompts/) | $29 | 50 production-tested prompts for building AI agents with Claude Code, LangChain, n8n. Architecture to deployment. |
| [API Development Prompts](./products/api-dev-prompts/) | $19 | 35 prompts for the full API lifecycle: design, implementation, testing, docs, and production ops. |

### Code Templates

| Product | Price | Description |
|---------|-------|-------------|
| [Python CLI Generator](./products/python-cli-generator/) | $49 | Build beautiful CLI apps in minutes. Modern Python scaffold with Typer, Rich, Pydantic v2, structlog, httpx, CI/CD. |
| [Python CLI 中文模板](./products/python-cli-zh/) | $19 | 专为中国开发者打造的 Python CLI 脚手架。全中文文档和注释，5 分钟搭建专业级命令行工具。 |
| [FastAPI Starter Kit](./products/fastapi-starter/) | $59 | Launch your FastAPI backend in 5 minutes. Async SQLAlchemy 2.0, JWT auth, Docker Compose, full test suite. |

### MCP Tools

| Product | Price | Description |
|---------|-------|-------------|
| [MCP Code Review Server](./products/mcp-code-review/) | Free (MIT) | AI code review in your editor. Local security-pattern checks, N+1 detection, team rules, and severity ratings. Install in 10 seconds. |

Custom rules & team profiles: commit a `.mcp-code-review.yaml` to your repo for shared regex rules, disabled checks, severity overrides, and per-repo thresholds.

Start with the [free 10-minute trial](https://aicraft.vip/trial.html) or [download the versioned trial bundle](https://github.com/GoodJobwilliam/aicraft/releases/tag/mcp-code-review-0.1.2). It uses an intentionally unsafe sample, not your repository, and produces a structured local report.

If that workflow proves useful for a shared team baseline, the optional [Team Rules Pack](https://www.creem.io/payment/prod_6Z3S3jGNPsCyRSqNi397ZY) is a one-time **$49** purchase. It includes 63 ready-made rules for Python, JavaScript/TypeScript, Go, and Java; GitHub Actions and GitLab CI merge-gate templates; and 20 review prompts. For a real pull-request check, copy the [secretless GitHub Actions starter](./products/mcp-code-review/examples/github-actions/mcp-code-review.yml). It uses the pinned PyPI `0.1.2` release; no API key or paid service is required.

[Share structured trial feedback](https://github.com/GoodJobwilliam/aicraft/issues/new?template=trial-feedback.yml&title=Trial%20feedback) or [request a free team trial](https://github.com/GoodJobwilliam/aicraft/issues/new?template=team-trial.yml&title=Team%20trial%20request). Do not include source code or credentials.

Marketplaces: [Official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.GoodJobwilliam%2Faicraft-code-review) · [LightNow](https://lightnow.ai/servers/io.github.GoodJobwilliam/aicraft-code-review) · [mcpservers.org](https://mcpservers.org/servers/goodjobwilliam/aicraft) · [cursor.directory](https://cursor.directory/plugins/mcp-code-review-server) · [PyPI](https://pypi.org/project/aicraft-code-review/)

For a repeatable, read-only distribution audit, run `python3 scripts/distribution_report.py`. It reports PyPI and GitHub Release downloads separately; downloads are distribution signals, not contacts, customers, or revenue.

### AgentPowers Skills (Free)

| Skill | Description |
|-------|-------------|
| Code Review Agent | 4-pass code review with local security-pattern checks, performance analysis, and quality checks |
| Git Commit Assistant | Conventional Commits from git diff. Auto-detects type, scope, breaking changes |
| PR Description Generator | Auto-generates PR descriptions from git history and diff |

## Pricing Philosophy

All products are priced based on market research and the value they deliver:

- **Prompt packs** at $19-$29 solve specific, high-value problems for developers
- **Code templates** at $49-$59 save 10-40 hours of setup time — priced at a fraction of the time they save
- **MCP Code Review Server** is free and MIT-licensed; the optional Team Rules Pack is $49 for shared rules, CI gates, and prompts

Most products are one-time purchases with lifetime updates. MCP Code Review has a free, MIT-licensed local workflow and an optional one-time Team Rules Pack for teams that want a versioned shared baseline.

## Roadmap

- [x] Initial product lineup (9 products)
- [x] GitHub Pages storefront with custom domain
- [x] Creem merchant setup (stable Team Rules Pack payment link active)
- [x] Official MCP Registry listing (0.1.2 active)
- [ ] Next.js SaaS Starter Kit

## Tech Stack

- Storefront: GitHub Pages (`aicraft.vip`)
- Payment processing: Creem (Merchant of Record)
- Distribution: Digital download

## License

Each product is licensed individually. See product READMEs for details.

---

Built by [GoodJobWilliam](https://github.com/GoodJobwilliam)
