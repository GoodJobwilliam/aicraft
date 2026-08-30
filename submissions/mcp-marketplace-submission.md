# MCP Marketplace Submission — MCP Code Review Server

1. Register at https://mcp-marketplace.io/signup
2. Click "Submit a Tool"
3. Fill in:
   - Server name: MCP Code Review Server
   - GitHub repo: https://github.com/GoodJobwilliam/aicraft
   - Description: Local, open-source code review as an MCP server — structured reviews with OWASP security scanning, team-shared rules, and CI merge gates
   - Category: Developer Tools
   - Pricing: Free MIT-licensed server; optional $49 Team Rules Pack; Team Updates Starter at $19/month or $190/year (up to 3 engineers) and Team Pilot at $99/month or $990/year (up to 10 engineers), both manual validation and not yet automated
   - Tags: code-review, security, owasp, static-analysis, python
4. The LAUNCHGUIDE.md is already prepared in the repo for auto-fill. Install from PyPI with `uvx --with "mcp<2" aicraft-code-review` (current release: 0.1.2).
