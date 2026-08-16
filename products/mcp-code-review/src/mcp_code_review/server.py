"""
MCP Code Review Server — MCP protocol implementation.

Exposes tools:
  - review_code: Review source code snippet
  - review_diff: Review a git diff
  - review_file: Review a local file
"""
from pathlib import Path

from mcp import types
from mcp.server import Server
from mcp.server.stdio import stdio_server

from mcp_code_review.config import discover_config_path, load_config
from mcp_code_review.reviewer import CodeReviewer

app = Server("code-review")


def _reviewer_for(start_dir: Path | None = None) -> CodeReviewer:
    """Create a reviewer with config discovered from start_dir (or server cwd)."""
    config_path = discover_config_path(start_dir)
    return CodeReviewer(load_config(config_path))


@app.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="review_code",
            description="Review source code for bugs, security, performance, and quality issues.",
            inputSchema={
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "The source code to review"},
                    "language": {"type": "string", "description": "Programming language (python, typescript, go, rust, etc.)"},
                },
                "required": ["code"],
            },
        ),
        types.Tool(
            name="review_diff",
            description="Review a git diff for potential issues before merging.",
            inputSchema={
                "type": "object",
                "properties": {
                    "diff": {"type": "string", "description": "The git diff output to review"},
                },
                "required": ["diff"],
            },
        ),
        types.Tool(
            name="review_file",
            description="Review a local file for code quality and security issues.",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Absolute path to the file"},
                    "language": {"type": "string", "description": "Programming language (auto-detect if not provided)"},
                },
                "required": ["path"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    match name:
        case "review_code":
            code = arguments["code"]
            language = arguments.get("language", "auto")
            result = _reviewer_for().review_code(code, language)

        case "review_diff":
            diff = arguments["diff"]
            result = _reviewer_for().review_diff(diff)

        case "review_file":
            path = Path(arguments["path"])
            if not path.exists():
                return [types.TextContent(type="text", text=f"Error: File not found: {path}")]
            language = arguments.get("language", _detect_language(path))
            code = path.read_text(encoding="utf-8")
            result = _reviewer_for(path.parent).review_code(code, language)

        case _:
            return [types.TextContent(type="text", text=f"Unknown tool: {name}")]

    return [types.TextContent(type="text", text=result)]


def _detect_language(path: Path) -> str:
    """Detect programming language from file extension."""
    ext_map = {
        ".py": "python",
        ".js": "javascript",
        ".jsx": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".go": "go",
        ".rs": "rust",
        ".java": "java",
        ".kt": "kotlin",
        ".swift": "swift",
        ".rb": "ruby",
        ".php": "php",
        ".c": "c",
        ".cpp": "cpp",
        ".h": "c",
        ".hpp": "cpp",
        ".cs": "csharp",
        ".scala": "scala",
        ".vue": "vue",
        ".svelte": "svelte",
    }
    return ext_map.get(path.suffix, "unknown")


async def main() -> None:
    """Run the MCP server over STDIO transport."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())
