#!/usr/bin/env sh
set -eu

if ! command -v uvx >/dev/null 2>&1; then
  printf '%s\n' 'uvx is required. Install uv from https://docs.astral.sh/uv/ or use the pip command in README.md.' >&2
  exit 2
fi

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$script_dir"

printf '%s\n' 'Running the local MCP Code Review trial...'
printf '%s\n' 'A non-zero exit code is expected because sample.py contains deliberate findings.'
exec uvx --from aicraft-code-review --with 'mcp<2' mcp-code-review review-file sample.py
