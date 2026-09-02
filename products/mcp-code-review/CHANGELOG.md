# Changelog

All notable changes to the MCP Code Review Server are documented here.

## Unreleased

### Fixed

- Clarified `review-diff --git` as the unstaged working-tree review and added `review-diff --staged` for index changes.
- CLI file and Git errors now return a concise error with CI exit code `2` instead of a traceback or silent empty review.
- MCP tool calls now validate required arguments and return actionable errors for invalid paths, unreadable files, or malformed input.
- Invalid JSON/YAML team configs now return actionable errors in both CLI and MCP modes instead of raw parser tracebacks.
- Tightened the built-in hardcoded-secret check to require a literal assignment, reducing false positives on comments, function names, and environment lookups.
- Corrected the documented `uvx` invocation to use the PyPI package as the source and the exposed `mcp-code-review` console script.
- Aligned public capability wording with the implemented deterministic checks; documentation no longer claims race-condition detection or complete OWASP Top 10 coverage.

### Added

- Added an opt-in CLI `--format json` output with a versioned schema, stable check ids, severity counts, verdict, and CI exit code. The feature is source-only until a new PyPI release is published.

## 0.1.2 — 2026-08-17

### Added

- Publish `README.md` in PyPI metadata (official MCP Registry `mcp-name` ownership validation).

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
