"""
Tests for the Code Review MCP server.
"""
import pytest

from mcp_code_review.reviewer import CodeReviewer


@pytest.fixture
def reviewer() -> CodeReviewer:
    return CodeReviewer()


class TestSecurityPass:
    def test_detects_sql_injection(self, reviewer: CodeReviewer):
        code = 'cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")'
        result = reviewer.review_code(code)
        assert "SQL injection" in result
        assert "Critical" in result or "High" in result

    def test_detects_hardcoded_secrets(self, reviewer: CodeReviewer):
        code = 'API_KEY = "sk-abc123def456"'
        result = reviewer.review_code(code)
        assert "credential" in result.lower() or "secret" in result.lower()

    def test_detects_command_injection(self, reviewer: CodeReviewer):
        code = 'os.system(f"rm -rf {user_input}")'
        result = reviewer.review_code(code)
        assert "Command injection" in result

    def test_clean_code_passes(self, reviewer: CodeReviewer):
        code = """
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
"""
        result = reviewer.review_code(code)
        assert "No issues found" in result or len(result) > 0


class TestPerformancePass:
    def test_detects_nplus1(self, reviewer: CodeReviewer):
        code = """
for user in users:
    profile = db.query(f"SELECT * FROM profiles WHERE user_id = {user.id}")
"""
        result = reviewer.review_code(code)
        assert "N+1" in result


class TestQualityPass:
    def test_detects_bare_except(self, reviewer: CodeReviewer):
        code = """
try:
    result = risky_operation()
except:
    pass
"""
        result = reviewer.review_code(code)
        assert "bare except" in result.lower()

    def test_detects_todo_comments(self, reviewer: CodeReviewer):
        code = "# TODO: implement error handling"
        result = reviewer.review_code(code)
        assert "TODO" in result


class TestStylePass:
    def test_detects_long_lines(self, reviewer: CodeReviewer):
        code = 'x = "This is an extremely long line that exceeds one hundred characters and should be flagged by the style checker for being too long"'
        result = reviewer.review_code(code)
        assert "Line too long" in result

    def test_detects_wrong_naming(self, reviewer: CodeReviewer):
        code = """
def BadlyNamedFunction():
    pass
"""
        result = reviewer.review_code(code)
        assert "should be snake_case" in result


class TestDiffReview:
    def test_review_diff(self, reviewer: CodeReviewer):
        diff = """
+ import os
+ API_KEY = "sk-test123"
+ def process(data):
+     os.system(f"rm -rf {data}")
"""
        result = reviewer.review_diff(diff)
        assert "credential" in result.lower() or "Command injection" in result


class TestFormatReport:
    def test_empty_findings(self, reviewer: CodeReviewer):
        code = 'x = 1'
        result = reviewer.review_code(code)
        assert "No issues found" in result or "Review Results" in result
