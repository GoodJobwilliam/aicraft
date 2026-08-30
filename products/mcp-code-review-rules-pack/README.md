# MCP Code Review — Team Rules Pack & CI Playbook

The paid companion pack for the free open-source [`aicraft-code-review`](https://github.com/GoodJobwilliam/aicraft) MCP server.

You get in **minutes** what normally takes teams weeks: production-grade rule profiles for 4 languages, CI wiring that gates merges, and 20 LLM review prompts.

## What's inside

| File | What it does |
|------|--------------|
| `rules/python.yaml` | 21 security/correctness/quality rules for Python |
| `rules/javascript.yaml` | 16 rules for JavaScript & TypeScript (React, Vue, Node) |
| `rules/go.yaml` | 13 rules for Go |
| `rules/java.yaml` | 13 rules for Java |
| `ci/github-actions.yml` | GitHub Actions workflow: review every PR, comment the report, **block merge on critical findings** |
| `ci/gitlab-ci.yml` | GitLab CI MR gate with the same behavior; keeps `review-report.txt` as an artifact |
| `llm-prompts.md` | 20 prompts for deep semantic review with Claude/GPT/Gemini |

Every rule uses the stable `custom_rules` schema (name / pattern / severity / category / issue / fix) plus tuned `severity_overrides` for the built-in checks — validated against MCP Code Review v0.1.2.

## Install (2 minutes)

```bash
pip install "aicraft-code-review==0.1.2" "mcp<2"

# Copy the profile for your language to your repo root
cp rules/python.yaml .mcp-code-review.yaml

# Or keep profiles shared and point the whole team at one file:
export MCP_CODE_REVIEW_CONFIG=/path/to/rules/python.yaml
```

Now every teammate's Claude Code / Cursor / Windsurf session reviews diffs with the **same rules** — no config drift.

## Wire up CI (5 minutes)

```bash
cp ci/github-actions.yml .github/workflows/code-review.yml
```

What you get:

- Exit code `0` — clean, nothing happens.
- Exit code `1` — high/medium findings → a report comment is posted on the PR, merge stays open.
- Exit code `2` — critical findings → **the workflow fails and blocks the merge.**
- GitLab CI keeps `review-report.txt` as an artifact even when the review job fails, so reviewers can inspect the findings.
- Both templates keep the text report as a downloadable artifact. The GitHub Actions template requests `contents: read`, `issues: write`, and `pull-requests: read`; PR comments are enabled only for same-repository PRs because fork tokens are read-only.

## How to customize

Rules are plain YAML. Example:

```yaml
custom_rules:
  - name: no-internal-export
    pattern: 'export .*[Ii]nternal'
    severity: medium
    category: team-convention
    issue: "Internal API exported by accident"
    fix: "Move behind the internal package boundary"
```

Tune built-in checks without writing regex:

```yaml
severity_overrides:
  long_lines: info      # relax
  hardcoded_secret: critical   # tighten

disabled_checks:
  - snake_case          # skip naming style
```

Full docs: <https://github.com/GoodJobwilliam/aicraft>

## Purchase

The Team Rules Pack is a one-time **$49** purchase with lifetime updates. [Open secure checkout via Creem](https://creem.io/checkout/prod_6Z3S3jGNPsCyRSqNi397ZY/ch_6wLlsvodjjvKq73eBpZCP0).

## License

You may use these rule files and workflows in any number of projects, including commercial ones, within your team. Redistribution/resale of the pack itself is not permitted.
