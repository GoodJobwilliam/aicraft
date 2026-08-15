# MCP Code Review Server - Install Guide for AI Agents

## Overview
MCP server that provides AI-assisted code review capabilities. Analyzes source code for bugs, security vulnerabilities, performance issues, and code quality problems.

## Available Tools

### 1. review_code
- **Description**: Review any source code snippet
- **Input**: `code` (string) - The source code to review, `language` (string, optional) - Programming language
- **Output**: Structured review with severity ratings

### 2. review_diff
- **Description**: Review a git diff for potential issues
- **Input**: `diff` (string) - The git diff content
- **Output**: Structured review of changes

### 3. review_file
- **Description**: Review a local file by path
- **Input**: `path` (string) - Absolute path to the file
- **Output**: Structured file review

## Installation

### Option 1: uvx (recommended, no install)
```json
{
  "mcpServers": {
    "code-review": {
      "command": "uvx",
      "args": ["aicraft-code-review"]
    }
  }
}
```

### Option 2: pip
```bash
pip install aicraft-code-review
```
Then configure:
```json
{
  "mcpServers": {
    "code-review": {
      "command": "python",
      "args": ["-m", "mcp_code_review"]
    }
  }
}
```

## Requirements
- Python 3.10+
- `uvx` (for Option 1) or `pip` (for Option 2)
- No API keys required
- No environment variables needed

## Verification
After installation, ask: "Review this Python code: \`\`\`python\nprint('hello')\n\`\`\`"
