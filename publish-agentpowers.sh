#!/usr/bin/env bash
# AICraft — one-shot publish script for AgentPowers
# Usage: bash publish-agentpowers.sh
# Requires: npx, a GitHub account (for login)

set -e

echo "=== AICraft AgentPowers Publisher ==="
echo ""

# 1. Login
echo "[1/3] Logging in to AgentPowers..."
npx @agentpowers/cli login

# 2. Publish Code Review Agent (free — for reputation/lead gen)
echo "[2/3] Publishing Code Review Agent..."
npx @agentpowers/cli publish ./products/code-review-agent --price 0 \
  --description "Comprehensive code review with security, performance, and style analysis for Python, TypeScript, and Go."

# 3. Publish Git Commit Assistant (free — for reputation/lead gen)
echo "[3/3] Publishing Git Commit Assistant..."
npx @agentpowers/cli publish ./products/git-commit-assistant --price 0 \
  --description "Writes structured Conventional Commits from git diff output."

echo ""
echo "=== Done! ==="
echo "Next steps:"
echo "  - Check listing at https://agentpowers.ai/dashboard"
echo "  - Link your AICraft store (goodjobwilliam.github.io/aicraft) in your seller profile"
echo "  - Monitor downloads: https://agentpowers.ai/dashboard/earnings"
