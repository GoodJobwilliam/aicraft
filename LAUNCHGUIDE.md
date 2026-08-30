# MCP Code Review Server — Launch Guide

## One-liner
Code review as an MCP server — structured reviews with OWASP security scanning for Claude Code, Cursor, and any MCP client.

## Description
MCP Code Review Server brings professional-grade code review to your AI assistant. Connect it to Claude Code, Cursor, or any MCP-compatible client and get structured code reviews with bug detection, security scanning (OWASP Top 10), performance analysis, and style checks — all with severity ratings and actionable fix suggestions.

## Category
Developer Tools

## Tags
code-review, security, owasp, static-analysis, developer-tools, python

## Use Cases
- Review code before committing
- Scan pull requests for security issues
- Audit existing codebases for bugs and anti-patterns
- Get structured, severity-rated feedback on any code snippet

## Features
| Tool | Description |
|------|-------------|
| `review_code` | Review any source code snippet for bugs, security, performance, and style |
| `review_diff` | Review a git diff for potential issues before merging |
| `review_file` | Review a local file by path |

## Pricing and offer structure
- **Free server**: the MCP Code Review Server is MIT-licensed and runs locally.
- **Team Rules Pack**: one-time **$49** purchase with 63 validated rules, CI merge-gate workflows, and 20 LLM review prompts; lifetime updates for the pack.
- **Team Updates**: early-access recurring offer at **$19/month or $190/year** for monthly rule drops, workflow refreshes, and rollout support. Scope and launch date are confirmed before charging; this is not yet an automated subscription.

## Tech
- Python 3.11+
- MCP Python SDK
- pip/uvx installable
- Local server (no cloud dependency)

## Setup Requirements
- Python 3.11 or later
- An MCP-compatible client (Claude Code, Cursor, Claude Desktop, etc.)
- No API keys required — runs entirely locally

## Install Commands
```bash
# Via uvx (recommended, no install)
uvx --with "mcp<2" aicraft-code-review

# Via pip
pip install "aicraft-code-review==0.1.2" "mcp<2"
python -m mcp_code_review
```

The `mcp<2` constraint keeps the server compatible with the current MCP Python SDK API.

## Repository
https://github.com/GoodJobwilliam/aicraft
