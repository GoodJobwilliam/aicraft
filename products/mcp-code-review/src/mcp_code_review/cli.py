"""CLI mode: run reviews directly from the terminal (no MCP client required).

Usage:
    mcp-code-review review-file PATH
    mcp-code-review review-diff [DIFF]
    mcp-code-review review-diff --git
    mcp-code-review review-code CODE
"""
import argparse
import subprocess
import sys
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mcp-code-review", description="Review code locally from the terminal.")
    sub = parser.add_subparsers(dest="command")

    p_file = sub.add_parser("review-file", help="Review a local file by path")
    p_file.add_argument("path", help="Path to the file to review")

    p_diff = sub.add_parser("review-diff", help="Review a git diff (arg, stdin, or --git for staged changes)")
    p_diff.add_argument("diff", nargs="?", help="Diff text (otherwise read from stdin)")
    p_diff.add_argument("--git", action="store_true", help="Use `git diff` output from the current repo")

    p_code = sub.add_parser("review-code", help="Review a code snippet")
    p_code.add_argument("code", help="Source code to review")
    p_code.add_argument("--language", default="auto", help="Programming language hint")

    args = parser.parse_args(argv)

    if args.command == "review-file":
        path = Path(args.path).resolve()
        reviewer = _reviewer_for(path.parent)
        report = reviewer.review_code(path.read_text(encoding="utf-8", errors="replace"))
    elif args.command == "review-diff":
        if args.git:
            diff = subprocess.run(["git", "diff"], capture_output=True, text=True).stdout
        elif args.diff is not None:
            diff = args.diff
        else:
            diff = sys.stdin.read()
        reviewer = _reviewer_for()
        report = reviewer.review_diff(diff)
    elif args.command == "review-code":
        reviewer = _reviewer_for()
        report = reviewer.review_code(args.code, args.language)
    else:
        parser.print_help()
        return 0

    print(report)
    return _exit_code(report)
