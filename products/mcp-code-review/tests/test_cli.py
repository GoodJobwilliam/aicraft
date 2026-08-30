"""Tests for the CLI mode (no MCP client required)."""
import subprocess
import sys
from pathlib import Path

from mcp_code_review import cli

VENV_PY = Path(__file__).resolve().parents[1] / ".venv" / "bin" / "python"
SRC = str(Path(__file__).resolve().parents[1] / "src")


def run_cli(*args: str, stdin: str = "") -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "mcp_code_review", *args],
        capture_output=True,
        text=True,
        input=stdin,
        env={"PYTHONPATH": SRC, "PATH": "/usr/bin:/bin"},
        check=False,
    )


class TestCliReviewCode:
    def test_review_code_flags_security_finding(self):
        result = run_cli("review-code", 'import os\nos.system("ls")\n')
        assert "Command injection" in result.stdout
        assert result.returncode == 1

    def test_review_code_clean_returns_zero(self):
        result = run_cli("review-code", "def add(a: int, b: int) -> int:\n    return a + b\n")
        assert result.returncode == 0


class TestCliReviewFile:
    def test_review_file_uses_adjacent_config(self, tmp_path):
        config = tmp_path / ".mcp-code-review.yaml"
        config.write_text(
            "custom_rules:\n"
            "  - name: no-todo\n"
            "    pattern: 'TODO'\n"
            "    severity: critical\n"
            "    issue: Leftover TODO\n"
        )
        target = tmp_path / "sample.py"
        target.write_text("# TODO: fix this\nprint('hi')\n")
        result = run_cli("review-file", str(target))
        assert "Leftover TODO" in result.stdout
        assert result.returncode == 2


class TestCliReviewDiff:
    def test_review_diff_from_stdin(self):
        diff = "diff --git a/x.py b/x.py\n--- a/x.py\n+++ b/x.py\n@@ -0,0 +1 @@\n+eval('1')\n"
        result = run_cli("review-diff", stdin=diff)
        assert "dynamic code execution" in result.stdout
        assert result.returncode >= 1

    def test_no_args_shows_help(self):
        result = run_cli("--help")
        assert "review-file" in result.stdout
        assert result.returncode == 0

    def test_help_distinguishes_staged_changes(self):
        result = run_cli("review-diff", "--help")
        assert "--staged" in result.stdout
        assert "unstaged working-tree" in result.stdout

    def test_staged_diff_uses_cached_git_diff(self, monkeypatch):
        calls = []

        class Result:
            returncode = 0
            stdout = "+eval('1')"
            stderr = ""

        def fake_run(command, **kwargs):
            calls.append(command)
            return Result()

        monkeypatch.setattr(cli.subprocess, "run", fake_run)
        assert "eval" in cli._git_diff(staged=True)
        assert calls == [["git", "diff", "--cached"]]

    def test_missing_file_returns_error_without_traceback(self, tmp_path):
        result = run_cli("review-file", str(tmp_path / "missing.py"))
        assert result.returncode == 2
        assert "error:" in result.stderr
        assert "Traceback" not in result.stderr
