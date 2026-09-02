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
      "args": ["--with", "mcp<2", "aicraft-code-review"]
    }
  }
}
```

### Option 2: pip
```bash
pip install "aicraft-code-review==0.1.2" "mcp<2"
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
- Python 3.11+
- `uvx` (for Option 1) or `pip` (for Option 2)
- No API keys required
- No environment variables needed

## Team upgrade
The server is free and MIT-licensed. Teams that need ready-made multi-language profiles, CI merge gates, and review prompts can [get the one-time $49 Team Rules Pack via Creem](https://creem.io/checkout/prod_6Z3S3jGNPsCyRSqNi397ZY/ch_6wLlsvodjjvKq73eBpZCP0).

## Verification
After installation, ask: "Review this Python code: \`\`\`python\nprint('hello')\n\`\`\`"
