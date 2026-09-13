#!/usr/bin/env sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$script_dir"

printf '%s\n' 'Running the local MCP Code Review trial...'
printf '%s\n' 'A non-zero exit code is expected because sample.py contains deliberate findings.'
if command -v uvx >/dev/null 2>&1; then
  exec uvx --from aicraft-code-review --with 'mcp<2' mcp-code-review review-file sample.py
fi

# Keep the bundle usable on machines that have Python but not uv. The temporary
# environment is removed on exit so the trial does not modify the user's Python install.
if ! command -v python3 >/dev/null 2>&1; then
  printf '%s\n' 'uvx or python3 is required. Install uv or Python, then run this script again.' >&2
  exit 2
fi
tmp_dir=$(mktemp -d "${TMPDIR:-/tmp}/aicraft-trial.XXXXXX")
cleanup() { rm -rf "$tmp_dir"; }
trap cleanup EXIT INT TERM
python3 -m venv "$tmp_dir/venv"
"$tmp_dir/venv/bin/python" -m pip install --disable-pip-version-check --quiet \
  "aicraft-code-review==0.1.2" "mcp<2"
exec "$tmp_dir/venv/bin/mcp-code-review" review-file sample.py
