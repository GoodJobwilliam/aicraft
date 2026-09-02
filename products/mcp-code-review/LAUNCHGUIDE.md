# MCP Code Review Server — Launch Guide

## One-liner
Code review as an MCP server — structured local security-pattern reviews for Claude Code, Cursor, and any MCP client.

## Description
MCP Code Review Server brings local, structured code review to your AI assistant. Connect it to Claude Code, Cursor, or any MCP-compatible client and get deterministic checks for common injection, deserialization, credential, performance, quality, and style patterns, with severity ratings and actionable fix suggestions.

## Category
Developer Tools

## Tags
code-review, security, static-analysis, developer-tools, python

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
- **Team Updates Starter**: early-access recurring offer at **$19/month or $190/year** for up to 3 engineers, with monthly rule drops and lightweight rollout support.
- **Team Updates Team Pilot**: early-access recurring offer at **$99/month or $990/year** for up to 10 engineers, including a shared profile, CI setup review, false-positive tuning review, and first-30-day rollout support. Scope and launch date are confirmed before charging; this is not yet an automated subscription.

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
uvx --from aicraft-code-review --with "mcp<2" mcp-code-review

# Via pip
pip install "aicraft-code-review==0.1.2" "mcp<2"
python -m mcp_code_review
```

The `mcp<2` constraint keeps the server compatible with the current MCP Python SDK API.

For the optional paid upgrade, use the [Team Rules Pack checkout](https://creem.io/checkout/prod_6Z3S3jGNPsCyRSqNi397ZY/ch_6wLlsvodjjvKq73eBpZCP0). It is a one-time $49 purchase; the server itself remains free and MIT-licensed.

## Repository
https://github.com/GoodJobwilliam/aicraft
