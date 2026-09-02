"""
Core review logic — 4-pass analysis: Security → Performance → Quality → Style.

Every finding carries a stable `check` id so that a ReviewConfig can
disable it, override its severity, or filter by minimum severity.
"""
import re
from typing import NamedTuple

from mcp_code_review.config import SEVERITY_ORDER, ReviewConfig, load_config


class Finding(NamedTuple):
    severity: str  # critical, high, medium, info
    line: int
    issue: str
    category: str  # security, performance, quality, style
    fix: str
    check: str = ""  # stable check id for config filtering/overrides


class CodeReviewer:
    """
    Multi-pass code reviewer.
    Runs Security, Performance, Quality, and Style passes, then applies
    the active ReviewConfig (custom rules, disabled checks, thresholds).
    """

    def __init__(self, config: ReviewConfig | None = None) -> None:
        self.config = config if config is not None else load_config()

    def review_code(self, code: str, language: str = "auto") -> str:
        """Review source code snippet."""
        return self._format_report(self.review_code_findings(code, language))

    def review_code_findings(self, code: str, language: str = "auto") -> list[Finding]:
        """Return structured findings for a source code snippet."""
        lines = code.split("\n")
        findings: list[Finding] = []

        findings.extend(self._security_pass(code, lines))
        findings.extend(self._performance_pass(code, lines))
        findings.extend(self._quality_pass(code, lines))
        findings.extend(self._style_pass(code, lines, language))

        return self._apply_config(findings, code)

    def review_diff(self, diff: str) -> str:
        """Review a git diff."""
        return self._format_report(self.review_diff_findings(diff))

    def review_diff_findings(self, diff: str) -> list[Finding]:
        """Return structured findings for a git diff."""
        # Extract added/modified lines from diff
        added_lines = []
        for line in diff.split("\n"):
            if line.startswith("+") and not line.startswith("+++"):
                added_lines.append(line[1:])

        code = "\n".join(added_lines)
        return self.review_code_findings(code, "auto")

    # ── Config application ────────────────────────────────────────

    def _apply_config(self, findings: list[Finding], code: str) -> list[Finding]:
        """Apply ReviewConfig: custom rules, disabled checks, overrides, thresholds."""
        config = self.config

        # Custom rules first so they participate in filtering/overrides too.
        for rule in config.custom_rules:
            try:
                regex = re.compile(rule.pattern)
            except re.error as exc:
                findings.append(Finding(
                    "info", 1,
                    f"Invalid regex in custom rule '{rule.name}': {exc}",
                    "quality",
                    "Fix the rule pattern in your config",
                    rule.name,
                ))
                continue
            for match in regex.finditer(code):
                line_num = code[:match.start()].count("\n") + 1
                findings.append(Finding(
                    rule.severity, line_num, rule.issue,
                    rule.category, rule.fix, rule.name,
                ))

        disabled = set(config.disabled_checks)
        applied: list[Finding] = []
        for finding in findings:
            if finding.check and finding.check in disabled:
                continue
            severity = finding.severity
            if finding.check and finding.check in config.severity_overrides:
                severity = config.severity_overrides[finding.check]
            if severity != finding.severity:
                finding = finding._replace(severity=severity)
            applied.append(finding)

        if config.min_severity is not None:
            cutoff = SEVERITY_ORDER[config.min_severity]
            applied = [f for f in applied if SEVERITY_ORDER.get(f.severity, 99) <= cutoff]

        return applied

    # ── Pass 1: Security ──────────────────────────────────────────

    def _security_pass(self, code: str, lines: list[str]) -> list[Finding]:
        findings = []

        patterns = [
            (r"(?i)exec\(|eval\(|compile\(|__import__\(", "Use of dynamic code execution",
             "Replace with safer alternatives (ast.literal_eval, subprocess with args)", "dynamic_exec"),
            (r"(?i)(cursor\.execute|connection\.execute|session\.execute)\s*\(\s*f['\"]",
             "SQL injection via f-string", "Use parameterized queries: cursor.execute(sql, params)", "sql_injection"),
            (r"(?i)pickle\.loads?\(|yaml\.load\s*\(|marshal\.loads?\(",
             "Insecure deserialization", "Use safe alternatives (json, or yaml.safe_load)", "deserialization"),
            (r"(?i)os\.system\(|subprocess\.Popen\(|subprocess\.call\(|child_process\.exec\b",
             "Command injection risk", "Use subprocess.run with args list, not shell=True", "command_injection"),
            (r"(?i)input\s*\(\s*\)", "Bare input() in Python 2", "Use raw_input() or validate input", "input_py2"),
            (r"(?i)\.innerHTML\s*=|\.outerHTML\s*=|dangerouslySetInnerHTML",
             "XSS via innerHTML", "Use textContent or DOMPurify for sanitization", "xss_innerhtml"),
            (r"(?i)\b(?:secret|passwd|password|api[_-]?key|token)\b\s*(?:=|:)\s*['\"][^'\"]+['\"]",
             "Hardcoded credential/secret", "Move to environment variable or secret manager", "hardcoded_secret"),
        ]

        for pattern, issue, fix, check in patterns:
            for match in re.finditer(pattern, code):
                line_num = code[:match.start()].count("\n") + 1
                findings.append(Finding("high", line_num, issue, "security", fix, check))

        return findings

    # ── Pass 2: Performance ───────────────────────────────────────

    def _performance_pass(self, code: str, lines: list[str]) -> list[Finding]:
        findings = []

        # N+1 query patterns (loop with DB query)
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            # Detect loops with DB queries inside
            if any(kw in stripped for kw in ["for ", "while "]):
                # Check next few lines for DB queries
                for j in range(i, min(i + 5, len(lines) + 1)):
                    next_line = lines[j - 1].strip()
                    if any(db in next_line for db in [".query(", ".execute(", ".find(", ".filter("]):
                        findings.append(Finding(
                            "high", i, "N+1 query: DB query inside loop",
                            "performance", "Use batch query or eager loading (select_related / includes)",
                            "nplus1",
                        ))
                        break

        # Unbounded list growth
        list_patterns = re.finditer(r"(\w+)\s*=\s*\[\s*\]", code)
        for match in list_patterns:
            var_name = match.group(1)
            append_pattern = re.search(rf"{re.escape(var_name)}\.append\(", code)
            if append_pattern:
                line_num = code[:append_pattern.start()].count("\n") + 1
                # Check if there's any limiting logic
                if "break" not in code[append_pattern.start():append_pattern.start() + 200] and "limit" not in code.lower():
                    findings.append(Finding(
                        "medium", line_num, f"Unbounded list '{var_name}' growth",
                        "performance", "Add size limit or use pagination/yield",
                        "unbounded_list",
                    ))

        return findings

    # ── Pass 3: Quality ───────────────────────────────────────────

    def _quality_pass(self, code: str, lines: list[str]) -> list[Finding]:
        findings = []

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Bare except clauses
            if re.match(r"except\s*:", stripped):
                findings.append(Finding(
                    "high", i, "Bare except clause catches all exceptions",
                    "quality", "Use specific exception types (except ValueError:)",
                    "bare_except",
                ))

            # Pass in except block
            if re.match(r"except\s+\w+\s*:", stripped):
                # Check if next non-empty line is just "pass"
                for j in range(i, min(i + 3, len(lines) + 1)):
                    if lines[j - 1].strip() == "pass":
                        findings.append(Finding(
                            "medium", i, "Empty except block swallows errors",
                            "quality", "At minimum log the exception: logger.exception()",
                            "empty_except",
                        ))
                        break

            # TODO/FIXME comments
            if re.match(r"\s*#\s*(TODO|FIXME|HACK|XXX)", stripped):
                findings.append(Finding(
                    "info", i, f"Unresolved comment: {stripped.strip()}",
                    "quality", "Address before merging or create a tracking issue",
                    "todo_comment",
                ))

        # Missing return type annotation (Python)
        for match in re.finditer(r"def \w+\(.*\):", code):
            line_num = code[:match.start()].count("\n") + 1
            func_def = match.group()
            if "->" not in func_def:
                findings.append(Finding(
                    "info", line_num, "Missing return type annotation",
                    "quality", "Add -> ReturnType to function signature",
                    "missing_return_type",
                ))

        return findings

    # ── Pass 4: Style ─────────────────────────────────────────────

    def _style_pass(self, code: str, lines: list[str], language: str) -> list[Finding]:
        findings = []

        # Long lines
        for i, line in enumerate(lines, 1):
            if len(line.rstrip("\n")) > 100 and not line.strip().startswith("#"):
                findings.append(Finding(
                    "info", i, f"Line too long ({len(line.rstrip())} chars)",
                    "style", "Break into multiple lines (<100 chars recommended)",
                    "long_lines",
                ))

        # Check naming conventions for Python
        if language in ("python", "auto"):
            for i, line in enumerate(lines, 1):
                stripped = line.strip()
                # Function names should be snake_case in Python
                func_match = re.match(r"def\s+([A-Z][a-zA-Z0-9_]*)\(", stripped)
                if func_match:
                    findings.append(Finding(
                        "info", i, f"Function '{func_match.group(1)}' should be snake_case",
                        "style", f"Rename to {func_match.group(1).lower()}",
                        "snake_case",
                    ))

                # Class names should be PascalCase
                class_match = re.match(r"class\s+([a-z][a-zA-Z0-9_]*)", stripped)
                if class_match:
                    findings.append(Finding(
                        "info", i, f"Class '{class_match.group(1)}' should be PascalCase",
                        "style", "Capitalize first letter of class name",
                        "pascal_case",
                    ))

        return findings

    # ── Report Formatting ─────────────────────────────────────────

    def _format_report(self, findings: list[Finding]) -> str:
        if not findings:
            return "## Review Results\n\nNo issues found. Code looks clean! ✅"

        findings.sort(key=lambda f: (SEVERITY_ORDER.get(f.severity, 99), f.line))

        sections = {
            "critical": [],
            "high": [],
            "medium": [],
            "info": [],
        }
        for f in findings:
            sections[f.severity].append(f)

        sev_icons = {"critical": "🔴", "high": "🟠", "medium": "🟡", "info": "🟢"}
        sev_labels = {"critical": "Critical", "high": "High", "medium": "Medium", "info": "Info"}

        output = ["## Review Results\n"]

        for severity in ["critical", "high", "medium", "info"]:
            items = sections[severity]
            if not items:
                continue
            icon = sev_icons[severity]
            label = sev_labels[severity]
            output.append(f"### {icon} {label} ({len(items)})")
            output.append("| Line | Issue | Category | Fix |")
            output.append("|------|-------|----------|-----|")
            for f in items:
                output.append(f"| {f.line} | {f.issue} | {f.category} | {f.fix} |")
            output.append("")

        # Summary
        output.append("### Summary")
        for severity in ["critical", "high", "medium", "info"]:
            count = len(sections[severity])
            output.append(f"- **{sev_labels[severity]}**: {count}")

        total = len(findings)
        if total > 0:
            has_critical = len(sections["critical"]) > 0
            verdict = "**Block** — critical issues must be fixed" if has_critical else "**Conditional Pass** — address high/medium issues"
            output.append(f"\n**Overall verdict**: {verdict}")

        return "\n".join(output)
