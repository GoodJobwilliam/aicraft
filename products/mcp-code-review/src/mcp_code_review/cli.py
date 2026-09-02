"""CLI mode: run reviews directly from the terminal (no MCP client required).

Usage:
    mcp-code-review review-file PATH
    mcp-code-review review-diff [DIFF]
    mcp-code-review review-diff --git
    mcp-code-review review-diff --staged
    mcp-code-review review-code CODE
"""
import argparse
import json
import subprocess
import sys
from importlib.resources import files
from pathlib import Path

from mcp_code_review.config import discover_config_path, load_config
from mcp_code_review.reviewer import CodeReviewer


def _reviewer_for(start_dir: Path | None = None) -> CodeReviewer:
    config_path = discover_config_path(start_dir)
    return CodeReviewer(load_config(config_path))


def _exit_code(report: str) -> int:
    """Return a CI-friendly exit code based on the worst severity found.
    
    0 = clean / only info-level findings, 1 = high or medium issues,
    2 = critical issues.
    """
    markers = [("### 🔴 Critical", 2), ("### 🟠 High", 1), ("### 🟡 Medium", 1)]
    for marker, code in markers:
        if marker in report:
            return code
    return 0


def _findings_exit_code(findings: list) -> int:
    """Return the same CI status used by the Markdown output."""
    severities = {getattr(finding, "severity", "") for finding in findings}
    if "critical" in severities:
        return 2
    if severities.intersection({"high", "medium"}):
        return 1
    return 0


def _json_report(findings: list) -> str:
    """Serialize findings without requiring consumers to parse Markdown."""
    counts = {severity: sum(f.severity == severity for f in findings) for severity in ("critical", "high", "medium", "info")}
    exit_code = _findings_exit_code(findings)
    verdict = "block" if exit_code == 2 else "conditional_pass" if exit_code == 1 else "clean"
    payload = {
        "schema_version": 1,
        "findings": [
            {"severity": f.severity, "line": f.line, "issue": f.issue, "category": f.category, "fix": f.fix, "check": f.check}
            for f in findings
        ],
        "summary": counts,
        "verdict": verdict,
        "exit_code": exit_code,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def _schema_json() -> str:
    """Return the bundled result schema so CI consumers need no repository checkout."""
    schema = files("mcp_code_review").joinpath("schema/review-result.schema.json")
    return schema.read_text(encoding="utf-8")


def _git_diff(*, staged: bool = False) -> str:
    """Read a working-tree or staged diff and fail clearly outside a Git repo."""
    command = ["git", "diff"]
    if staged:
        command.append("--cached")
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        detail = result.stderr.strip() or "git diff failed"
        raise RuntimeError(detail)
    return result.stdout


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mcp-code-review", description="Review code locally from the terminal.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("schema", help="Print the machine-readable review result schema")

    p_file = sub.add_parser("review-file", help="Review a local file by path")
    p_file.add_argument("path", help="Path to the file to review")
    p_file.add_argument("--format", choices=("markdown", "json"), default="markdown", dest="output_format", help="Output format")

    p_diff = sub.add_parser("review-diff", help="Review a git diff (argument, stdin, working tree, or index)")
    p_diff.add_argument("diff", nargs="?", help="Diff text (otherwise read from stdin)")
    git_group = p_diff.add_mutually_exclusive_group()
    git_group.add_argument("--git", action="store_true", help="Review unstaged working-tree changes")
    git_group.add_argument("--staged", action="store_true", help="Review staged changes in the index")
    p_diff.add_argument("--format", choices=("markdown", "json"), default="markdown", dest="output_format", help="Output format")

    p_code = sub.add_parser("review-code", help="Review a code snippet")
    p_code.add_argument("code", help="Source code to review")
    p_code.add_argument("--language", default="auto", help="Programming language hint")
    p_code.add_argument("--format", choices=("markdown", "json"), default="markdown", dest="output_format", help="Output format")

    args = parser.parse_args(argv)

    if args.command == "schema":
        print(_schema_json())
        return 0

    try:
        if args.command == "review-file":
            path = Path(args.path).resolve()
            reviewer = _reviewer_for(path.parent)
            findings = reviewer.review_code_findings(path.read_text(encoding="utf-8", errors="replace"))
        elif args.command == "review-diff":
            if args.git or args.staged:
                if args.diff is not None:
                    parser.error("review-diff accepts a diff argument or --git/--staged, not both")
                diff = _git_diff(staged=args.staged)
            elif args.diff is not None:
                diff = args.diff
            else:
                diff = sys.stdin.read()
            reviewer = _reviewer_for()
            findings = reviewer.review_diff_findings(diff)
        elif args.command == "review-code":
            reviewer = _reviewer_for()
            findings = reviewer.review_code_findings(args.code, args.language)
        else:
            parser.print_help()
            return 0
    except (OSError, UnicodeError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.output_format == "json":
        print(_json_report(findings))
        return _findings_exit_code(findings)
    report = reviewer._format_report(findings)
    print(report)
    return _findings_exit_code(findings)
