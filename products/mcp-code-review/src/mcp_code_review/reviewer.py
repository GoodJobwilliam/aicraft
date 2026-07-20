"""
Core review logic — 4-pass analysis: Security → Performance → Quality → Style.
"""
import re
from typing import NamedTuple


class Finding(NamedTuple):
    severity: str  # critical, high, medium, info
    line: int
    issue: str
    category: str  # security, performance, quality, style
    fix: str


class CodeReviewer:
    """
    Multi-pass code reviewer.
    Runs Security, Performance, Quality, and Style passes.
    """

    def review_code(self, code: str, language: str = "auto") -> str:
        """Review source code snippet."""
        lines = code.split("\n")
        findings: list[Finding] = []

        findings.extend(self._security_pass(code, lines))
        findings.extend(self._performance_pass(code, lines))
        findings.extend(self._quality_pass(code, lines))
        findings.extend(self._style_pass(code, lines, language))

        return self._format_report(findings)

    def review_diff(self, diff: str) -> str:
        """Review a git diff."""
        # Extract added/modified lines from diff
        added_lines = []
        for line in diff.split("\n"):
            if line.startswith("+") and not line.startswith("+++"):
                added_lines.append(line[1:])

        code = "\n".join(added_lines)
        return self.review_code(code, "auto")

    # ── Pass 1: Security ──────────────────────────────────────────

    def _security_pass(self, code: str, lines: list[str]) -> list[Finding]:
        findings = []

        patterns = [
            (r"(?i)exec\(|eval\(|compile\(|__import__\(", "Use of dynamic code execution", 
             "Replace with safer alternatives (ast.literal_eval, subprocess with args)"),
            (r"(?i)(cursor\.execute|connection\.execute|session\.execute)\s*\(\s*f['\"]",
             "SQL injection via f-string", "Use parameterized queries: cursor.execute(sql, params)"),
            (r"(?i)pickle\.loads?\(|yaml\.load\s*\(|marshal\.loads?\(",
             "Insecure deserialization", "Use safe alternatives (json, or yaml.safe_load)"),
            (r"(?i)os\.system\(|subprocess\.Popen\(|subprocess\.call\(|child_process\.exec\b",
             "Command injection risk", "Use subprocess.run with args list, not shell=True"),
            (r"(?i)input\s*\(\s*\)", "Bare input() in Python 2", "Use raw_input() or validate input"),
            (r"(?i)\.innerHTML\s*=|\.outerHTML\s*=|dangerouslySetInnerHTML",
             "XSS via innerHTML", "Use textContent or DOMPurify for sanitization"),
            (r"(?i)secret|api[_-]?key|password|token\s*=\s*['\"][^'\"]+['\"]",
             "Hardcoded credential/secret", "Move to environment variable or secret manager"),
        ]

        for pattern, issue, fix in patterns:
            for match in re.finditer(pattern, code):
                line_num = code[:match.start()].count("\n") + 1
                findings.append(Finding("high", line_num, issue, "security", fix))

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
                            "performance", "Use batch query or eager loading (select_related / includes)"
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
                        "performance", "Add size limit or use pagination/yield"
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
                    "quality", "Use specific exception types (except ValueError:)"
                ))

            # Pass in except block
            if re.match(r"except\s+\w+\s*:", stripped):
                # Check if next non-empty line is just "pass"
                for j in range(i, min(i + 3, len(lines) + 1)):
                    if lines[j - 1].strip() == "pass":
                        findings.append(Finding(
                            "medium", i, "Empty except block swallows errors",
                            "quality", "At minimum log the exception: logger.exception()"
                        ))
                        break

            # TODO/FIXME comments
            if re.match(r"\s*#\s*(TODO|FIXME|HACK|XXX)", stripped):
                findings.append(Finding(
                    "info", i, f"Unresolved comment: {stripped.strip()}",
                    "quality", "Address before merging or create a tracking issue"
                ))

        # Missing return type annotation (Python)
        for match in re.finditer(r"def \w+\(.*\):", code):
            line_num = code[:match.start()].count("\n") + 1
            func_def = match.group()
            if "->" not in func_def:
                findings.append(Finding(
                    "info", line_num, "Missing return type annotation",
                    "quality", "Add -> ReturnType to function signature"
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
                    "style", "Break into multiple lines (<100 chars recommended)"
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
                        "style", "Rename to {func_match.group(1).lower()}"
                    ))

                # Class names should be PascalCase
                class_match = re.match(r"class\s+([a-z][a-zA-Z0-9_]*)", stripped)
                if class_match:
                    findings.append(Finding(
                        "info", i, f"Class '{class_match.group(1)}' should be PascalCase",
                        "style", "Capitalize first letter of class name"
                    ))

        return findings

    # ── Report Formatting ─────────────────────────────────────────

    def _format_report(self, findings: list[Finding]) -> str:
        if not findings:
            return "## Review Results\n\nNo issues found. Code looks clean! ✅"

        severity_order = {"critical": 0, "high": 1, "medium": 2, "info": 3}
        findings.sort(key=lambda f: (severity_order.get(f.severity, 99), f.line))

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
        has_any = False

        for severity in ["critical", "high", "medium", "info"]:
            items = sections[severity]
            if not items:
                continue
            has_any = True
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
            if count > 0:
                output.append(f"- **{sev_labels[severity]}**: {count}")
            else:
                output.append(f"- **{sev_labels[severity]}**: 0")

        total = len(findings)
        if total > 0:
            has_critical = len(sections["critical"]) > 0
            verdict = "**Block** — critical issues must be fixed" if has_critical else "**Conditional Pass** — address high/medium issues"
            output.append(f"\n**Overall verdict**: {verdict}")

        return "\n".join(output)
