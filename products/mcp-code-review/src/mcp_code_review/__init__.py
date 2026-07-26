"""
MCP Code Review Server — expose code review as MCP tools.

Usage:
    mcp-code-review            # Start STDIO server (for MCP clients)
    python -m mcp_code_review  # Same
"""
import asyncio
from mcp_code_review.server import main


def run() -> None:
    """Entry point: run the async main() with asyncio."""
    asyncio.run(main())


if __name__ == "__main__":
    run()
