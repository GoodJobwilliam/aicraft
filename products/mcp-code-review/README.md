# MCP Code Review Server

mcp-name: io.github.GoodJobwilliam/aicraft-code-review

[![smithery badge](https://smithery.ai/badge/yaohuixue1/mcp-code-review)](https://smithery.ai/servers/yaohuixue1/mcp-code-review)
[![Product Hunt](https://img.shields.io/badge/Launch-July%2029%2C%202026-orange?style=flat-square&logo=product-hunt)](https://www.producthunt.com/products/mcp-code-review-server?launch=mcp-code-review-server)

中文文档：[README.zh.md](./README.zh.md)

Listed on: [Official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.GoodJobwilliam%2Faicraft-code-review) · [Smithery](https://smithery.ai/servers/yaohuixue1/mcp-code-review) · [mcpservers.org](https://mcpservers.org/servers/goodjobwilliam/aicraft) · [cursor.directory](https://cursor.directory/plugins/mcp-code-review-server)


Code review as an MCP server. Connect it to Claude Code, Cursor, or any MCP-compatible AI assistant.

## Features

- **`review_code`** — Review any source code snippet for bugs, security, performance, and style
- **`review_diff`** — Review a git diff for potential issues before merging
- **`review_file`** — Review a local file by path

The free server runs deterministic checks for common injection, deserialization, credential, performance, quality, and style patterns, then returns structured findings with severity ratings.

## Quick Start

### Via `uvx` (no install)

```bash
# Add to your Claude Code MCP config:
claude mcp add code-review -- uvx --from aicraft-code-review --with "mcp<2" mcp-code-review
```

Or add to your `~/.cursor/mcp.json` or `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "code-review": {
      "command": "uvx",
      "args": ["--from", "aicraft-code-review", "--with", "mcp<2", "mcp-code-review"]
    }
  }
}
```

### Via pip

```bash
pip install "aicraft-code-review==0.1.2" "mcp<2"
python -m mcp_code_review
```

> Compatibility note: PyPI `0.1.2` pins `mcp<2`. If you install the older `0.1.0` release, add the `mcp<2` constraint manually because MCP 2.0 removes `Server.list_tools`.

### Team Rules Pack ($49, one-time)

The free MIT server is enough for local review. If your team needs ready-made profiles and merge gates, the optional [Team Rules Pack is available through Creem](https://creem.io/checkout/prod_6Z3S3jGNPsCyRSqNi397ZY/ch_6wLlsvodjjvKq73eBpZCP0): 63 validated Python/JS·TS/Go/Java rules, GitHub Actions and GitLab CI templates, and 20 LLM review prompts with lifetime updates.

### Team Updates (early access)

Teams that want ongoing rule drops, CI workflow refreshes, and rollout support can join the **Team Updates** early-access list: Starter is [$19/month or $190/year](https://aicraft.vip/team-updates.html) for up to 3 engineers, and Team Pilot is $99/month or $990/year for up to 10 engineers. Read the [Team Pilot scope and acceptance checklist](https://github.com/GoodJobwilliam/aicraft/blob/main/TEAM_PILOT_BRIEF.md) before applying. The service is being validated with a small number of teams; delivery scope and launch date are confirmed before charging.

For a structured, free team trial, [open the GitHub trial request form](https://github.com/GoodJobwilliam/aicraft/issues/new?template=team-trial.yml&title=Team%20trial%20request). Do not include source code, credentials, or other confidential information.

### CLI mode (no MCP client needed)

```bash
# Review a local file (discovers .mcp-code-review.yaml from the file's directory)
mcp-code-review review-file path/to/file.py

# Review an unstaged git diff
git diff | mcp-code-review review-diff
mcp-code-review review-diff --git

# Review staged changes before committing
mcp-code-review review-diff --staged

# Review a snippet
mcp-code-review review-code "import os; os.system('ls')"
```

Exit codes are CI-friendly: `0` clean, `1` high/medium issues, `2` critical issues.

### Free GitHub Actions starter

The repository includes a copy-paste [GitHub Actions starter workflow](./examples/github-actions/mcp-code-review.yml). It checks the pull-request diff with the current PyPI release, needs no API key, and keeps the existing exit-code policy. The starter runs the built-in checks only; the optional Team Rules Pack adds shared profiles, maintained CI templates, and team-specific policy.

For CI systems that consume structured data, add `--format json` to any CLI review command. The JSON response has a stable `schema_version`, finding records with check ids, severity counts, a `verdict`, and the same `exit_code` used by the default Markdown output. This mode is currently available from the repository source; the PyPI `0.1.2` install remains the documented stable release until the next package is published.

The output contract is documented in [`schema/review-result.schema.json`](./schema/review-result.schema.json).

```bash
mcp-code-review review-file path/to/file.py --format json > review.json
```

## Usage Examples

## 10-minute team trial

Run the [self-serve trial kit](https://aicraft.vip/trial.html) to test a shared JSON profile against a deliberately unsafe sample. It uses the free local server, creates no charge, and gives the team a concrete basis for evaluating the optional Team Rules Pack and Team Updates.

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

## Custom Rules & Team Profiles

Ship your team's code standards as a config file — no code changes needed.

- **`.mcp-code-review.yaml` / `.yml` / `.json`** — auto-discovered from the reviewed file's directory upward; for snippets and diffs it is looked up from the server's working directory
- **`MCP_CODE_REVIEW_CONFIG` env var** — point every teammate at a shared config committed to your repo (team-shared rule profiles)
- **Custom regex rules** with severity, message, and suggested fix
- **`disabled_checks`** — silence noisy checks
- **`severity_overrides`** — bump or lower any check (e.g. make hardcoded secrets blocking)
- **`min_severity`** — only report findings at or above a threshold (per-repo noise control)

### Example `.mcp-code-review.yaml`

```yaml
disabled_checks:
  - todo_comment

severity_overrides:
  hardcoded_secret: critical

min_severity: medium

custom_rules:
  - name: no-console-log
    pattern: 'console\.log\('
    severity: high
    category: quality
    issue: Console logging left in production code
    fix: Use a structured logger instead
```

### Team setup

Commit the file to a shared repo, then wire every teammate's MCP client to it:

```json
{
  "mcpServers": {
    "code-review": {
      "command": "uvx",
      "args": ["--from", "aicraft-code-review", "--with", "mcp<2", "mcp-code-review"],
      "env": {
        "MCP_CODE_REVIEW_CONFIG": "/path/to/team-repo/.mcp-code-review.yaml"
      }
    }
  }
}
```

Available check ids: `dynamic_exec`, `sql_injection`, `deserialization`, `command_injection`, `input_py2`, `xss_innerhtml`, `hardcoded_secret`, `nplus1`, `unbounded_list`, `bare_except`, `empty_except`, `todo_comment`, `missing_return_type`, `long_lines`, `snake_case`, `pascal_case`.

YAML configs need `pip install "aicraft-code-review[yaml]"`; JSON configs work with no extra dependencies.

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
