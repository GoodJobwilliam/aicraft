"""Tests for MCP tool input validation and file errors."""

import pytest

from mcp_code_review.server import call_tool


def text(result):
    return result[0].text


@pytest.mark.asyncio
async def test_review_code_requires_non_empty_string():
    assert text(await call_tool("review_code", [])) == "Error: 'arguments' must be an object"
    assert text(await call_tool("review_code", {})) == "Error: 'code' must be a non-empty string"
    assert text(await call_tool("review_code", {"code": "   "})) == "Error: 'code' must be a non-empty string"


@pytest.mark.asyncio
async def test_review_diff_requires_non_empty_string():
    assert text(await call_tool("review_diff", {"diff": ""})) == "Error: 'diff' must be a non-empty string"


@pytest.mark.asyncio
async def test_review_file_validates_path(tmp_path):
    assert text(await call_tool("review_file", {})) == "Error: 'path' must be a non-empty string"
    assert text(await call_tool("review_file", {"path": str(tmp_path / "missing.py")})).startswith("Error: File not found:")
    assert text(await call_tool("review_file", {"path": str(tmp_path)})) == f"Error: Path is not a file: {tmp_path}"


@pytest.mark.asyncio
async def test_review_file_reads_utf8_and_reviews(tmp_path):
    target = tmp_path / "sample.py"
    target.write_text("os.system('ls')\n", encoding="utf-8")
    result = await call_tool("review_file", {"path": str(target)})
    assert "Command injection" in text(result)


@pytest.mark.asyncio
async def test_unknown_tool_returns_error():
    assert text(await call_tool("no_such_tool", {})) == "Error: Unknown tool: no_such_tool"
