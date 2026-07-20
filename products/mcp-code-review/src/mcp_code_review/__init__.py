"""
MCP Code Review Server — expose code review as MCP tools.

Usage:
    mcp-code-review            # Start STDIO server (for MCP clients)
    python -m mcp_code_review  # Same
"""
from mcp_code_review.server import main

if __name__ == "__main__":
    main()
