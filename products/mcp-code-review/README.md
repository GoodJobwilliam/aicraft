# MCP Code Review Server

mcp-name: io.github.GoodJobwilliam/aicraft-code-review

[![smithery badge](https://smithery.ai/badge/yaohuixue1/mcp-code-review)](https://smithery.ai/servers/yaohuixue1/mcp-code-review)
[![Product Hunt](https://img.shields.io/badge/Launch-July%2029%2C%202026-orange?style=flat-square&logo=product-hunt)](https://www.producthunt.com/products/mcp-code-review-server?launch=mcp-code-review-server)


Code review as an MCP server. Connect it to Claude Code, Cursor, or any MCP-compatible AI assistant.

## Features

- **`review_code`** — Review any source code snippet for bugs, security, performance, and style
- **`review_diff`** — Review a git diff for potential issues before merging
- **`review_file`** — Review a local file by path

Powered by the same methodology as our Code Review Agent: OWASP Top 10 scanning, N+1 query detection, race condition analysis, and structured output with severity ratings.

## Quick Start

### Via `uvx` (no install)

```bash
# Add to your Claude Code MCP config:
claude mcp add code-review -- uvx aicraft-code-review
```

Or add to your `~/.cursor/mcp.json` or `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "code-review": {
      "command": "uvx",
      "args": ["aicraft-code-review"]
    }
  }
}
```

### Via pip

```bash
pip install aicraft-code-review
python -m mcp_code_review
```

## Usage Examples

Once connected, ask your AI assistant:

> "Review this Python code for security issues: [paste code]"
> "Review this diff before I commit: [paste diff]"
> "Review this file: /path/to/file.py"

The AI will call the MCP server and return structured results.

### Sample Output

```
## Review Results

### 🔴 Critical (1)
| Line | Issue | Category | Fix |
|------|-------|----------|-----|
| 42 | SQL injection via f-string | Security | Use parameterized queries |

### 🟠 High (2)
| Line | Issue | Category | Fix |
|------|-------|----------|-----|
| 15 | Unvalidated user input | Security | Add input validation |
| 78 | N+1 query in loop | Performance | Add select_related |

### Summary
- **Critical**: 1 — must fix
- **High**: 2 — should fix
- **Medium**: 0
- **Info**: 0
```

## Development

```bash
git clone https://github.com/GoodJobwilliam/aicraft
cd aicraft
pip install -e ".[dev]"
python -m mcp_code_review  # Start server
```

## Requirements

- Python 3.11+
- An MCP-compatible client (Claude Code, Cursor, etc.)

## License

MIT
