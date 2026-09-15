#!/usr/bin/env sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$script_dir"

printf '%s\n' 'Running the local MCP Code Review trial...'
printf '%s\n' 'A non-zero exit code is expected because sample.py contains deliberate findings.'
if command -v uvx >/dev/null 2>&1; then
  set +e
  uvx --from aicraft-code-review --with 'mcp<2' mcp-code-review review-file sample.py
  review_exit=$?
  set -e
else
  # Keep the bundle usable on machines that have Python but not uv. The temporary
  # package directory is removed on exit so the trial does not modify the user's Python install.
  if ! command -v python3 >/dev/null 2>&1; then
    printf '%s\n' 'uvx or python3 is required. Install uv or Python, then run this script again.' >&2
    exit 2
  fi
  tmp_dir=$(mktemp -d "${TMPDIR:-/tmp}/aicraft-trial.XXXXXX")
  cleanup() { rm -rf "$tmp_dir"; }
  trap cleanup EXIT INT TERM
  python3 -m pip install --disable-pip-version-check --quiet --target "$tmp_dir/site" \
    "aicraft-code-review==0.1.2" "mcp<2"
  set +e
  PYTHONPATH="$tmp_dir/site${PYTHONPATH:+:$PYTHONPATH}" python3 -m mcp_code_review review-file sample.py
  review_exit=$?
  set -e
fi

printf '%s\n' ''
printf '%s\n' 'Trial complete. Share three non-confidential observations:'
printf '%s\n' '1) What did it catch? 2) Which rule should be shared? 3) What was noisy or missing?'
printf '%s\n' 'Feedback form: https://github.com/GoodJobwilliam/aicraft/issues/new?template=trial-feedback.yml&title=Trial%20feedback'
printf '%s\n' 'Email: 731685147@qq.com (no source code or secrets needed)'
exit "$review_exit"
