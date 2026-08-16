# Changelog

All notable changes to the MCP Code Review Server are documented here.

## 0.1.1 — 2026-08-16

### Added

- CLI mode: `mcp-code-review review-file PATH` / `review-diff` / `review-code` run reviews directly from the terminal (no MCP client needed), with CI-friendly exit codes (0/1/2).

- Custom rules & team profiles: commit a `.mcp-code-review.yaml` (or `.yml` / `.json`) to your repo to define custom regex rules, disable checks, override severities, and set a minimum severity threshold.
- Team-shared configs via the `MCP_CODE_REVIEW_CONFIG` environment variable.
- Per-repo config discovery: `review_file` looks for a config file from the reviewed file's directory upward.
- Stable check ids for every built-in finding: `dynamic_exec`, `sql_injection`, `deserialization`, `command_injection`, `input_py2`, `xss_innerhtml`, `hardcoded_secret`, `nplus1`, `unbounded_list`, `bare_except`, `empty_except`, `todo_comment`, `missing_return_type`, `long_lines`, `snake_case`, `pascal_case`.
- Optional `[yaml]` extra for PyYAML support (JSON configs need no extra dependencies).

### Fixed

- Pinned `mcp` to `>=1.6,<2` so fresh installs don't pull the incompatible `mcp` 2.x API (which removed `Server.list_tools`).

## 0.1.0 — 2026-07-29

### Added

- Initial release: `review_code`, `review_diff`, and `review_file` tools over MCP stdio.
- Four review passes: security (OWASP patterns), performance (N+1 queries, unbounded growth), quality (exception handling, TODO comments, type annotations), and style (line length, naming).
- Structured Markdown report with severity sections and summary.

### Fixed

- Style pass f-string that rendered `{func_match.group(1).lower()}` literally instead of the suggested name.
