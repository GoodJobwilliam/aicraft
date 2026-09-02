"""
MCP Code Review Server — expose code review as MCP tools.

Usage:
    mcp-code-review                  # Start STDIO server (for MCP clients)
    mcp-code-review review-file PATH # Run a review directly from the terminal
    mcp-code-review review-diff ...  # Review a git diff
    mcp-code-review review-code ...  # Review a code snippet
    mcp-code-review schema             # Print the JSON result schema
    python -m mcp_code_review        # Same as mcp-code-review
"""
import asyncio
import sys

from mcp_code_review.server import main


def run() -> None:
    """Entry point: CLI mode when arguments are given, MCP stdio server otherwise."""
    if len(sys.argv) > 1:
        from mcp_code_review.cli import main as cli_main

        raise SystemExit(cli_main(sys.argv[1:]))
    asyncio.run(main())


if __name__ == "__main__":
    run()
