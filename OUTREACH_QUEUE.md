# Outreach Queue (public evidence)

Generated 2026-09-03 from the public GitHub repository API. Every row is a prospect, not a customer or endorsement. This file records public metadata and suggested technical questions only; it does not send messages or create issues.

Read each repository README, contribution guide, and recent issues before contacting a maintainer. Record any real contact or reply in `OUTREACH_LOG.csv`.

| Priority | Public repository | Evidence checked | Issue link | Suggested opener |
|---:|---|---|---|---|
| 1 | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | Issues enabled; 137 open issues; last push 2026-08-27; Python | [Issues](https://github.com/tirth8205/code-review-graph/issues) | How do you measure false positives when a code graph feeds review context, and would a committed local rule profile help? |
| 2 | [subvertnormality/paranoia](https://github.com/subvertnormality/paranoia) | Issues enabled; 11 open issues; last push 2026-08-29; Python | [Issues](https://github.com/subvertnormality/paranoia/issues) | How do you combine adversarial review with repeatable policy checks that can block a merge? |
| 3 | [sourceant/sourceant](https://github.com/sourceant/sourceant) | Issues enabled; 26 open issues; last push 2026-08-30; Python | [Issues](https://github.com/sourceant/sourceant/issues) | Could a repository-committed rules file complement persistent engineering context without adding cloud scanning? |
| 4 | [n24q02m/better-code-review-graph](https://github.com/n24q02m/better-code-review-graph) | Issues enabled; 1 open issue; last push 2026-09-02; Python | [Issues](https://github.com/n24q02m/better-code-review-graph/issues) | Are shared review rules or CI gates part of your target workflow across repositories? |
| 5 | [waybarrios/opencode-power-pack](https://github.com/waybarrios/opencode-power-pack) | Issues enabled; 1 open issue; last push 2026-09-02; Python | [Issues](https://github.com/waybarrios/opencode-power-pack/issues) | Which review checks do users request most often but still lack in agent workflows? |
| 6 | [oliver-kriska/claude-elixir-phoenix](https://github.com/oliver-kriska/claude-elixir-phoenix) | Issues enabled; 18 open issues; last push 2026-08-27; Python | [Issues](https://github.com/oliver-kriska/claude-elixir-phoenix/issues) | Would a shared local policy profile help keep specialist-agent reviews consistent for Phoenix teams? |
| 7 | [PyModel/pythinker-cli](https://github.com/PyModel/pythinker-cli) | Issues enabled; 34 open issues; last push 2026-08-27; Python | [Issues](https://github.com/PyModel/pythinker-cli/issues) | Would machine-readable severity and CI exit codes fit your review-first shell loop? |
| 8 | [HeJiguang/codescan](https://github.com/HeJiguang/codescan) | Issues enabled; 9 open issues; last push 2026-04-02; Python | [Issues](https://github.com/HeJiguang/codescan/issues) | Which security checks need team-specific severity overrides when the scanner runs through MCP? |

## Fresh candidates (API rechecked 2026-08-30)

These candidates were added after a second public-API search. The evidence is intentionally limited to repository metadata and README claims; inspect contribution rules and recent issues before any contact.

| Priority | Public repository | Evidence checked | Issue link | Suggested opener |
|---:|---|---|---|---|
| 9 | [varungor365/mcp-audit-scanner](https://github.com/varungor365/mcp-audit-scanner) | Issues enabled; 7 open issues; last push 2026-08-30; Python AST scanner for MCP servers | [Issues](https://github.com/varungor365/mcp-audit-scanner/issues) | How do you want teams to turn read-only MCP audit findings into a shared local policy and CI gate without uploading server source? |
| 10 | [MichaelFu1998-create/pr-review-assistant](https://github.com/MichaelFu1998-create/pr-review-assistant) | Issues enabled; 0 open issues; last push 2026-08-30; MIT agentic GitHub PR reviewer | [Issues](https://github.com/MichaelFu1998-create/pr-review-assistant/issues) | Could deterministic local checks with stable severity and exit codes complement the agentic PR investigation before a fix is proposed? |
| 11 | [lgtm-hq/py-lintro](https://github.com/lgtm-hq/py-lintro) | Issues enabled; 164 open issues; last push 2026-08-30; Python CLI, GitHub Action, and MCP server | [Issues](https://github.com/lgtm-hq/py-lintro/issues) | Where do users need a committed cross-repository policy profile or false-positive control beyond the existing linter orchestration? |
| 12 | [msaad00/agent-bom](https://github.com/msaad00/agent-bom) | Issues enabled; 4 open issues; last push 2026-08-30; Apache-2.0 AI/MCP/cloud security scanner | [Issues](https://github.com/msaad00/agent-bom/issues) | Would a small local rule profile and merge-gate template help teams enforce MCP-specific checks alongside your broader evidence model? |
| 13 | [navapbc/rebar](https://github.com/navapbc/rebar) | Issues enabled; 1 open issue; last push 2026-08-30; Python CLI and MCP server; GitHub mirror is read-only | [Issues](https://github.com/navapbc/rebar/issues) | Since this mirror is read-only and review runs in Gerrit, which local policy or CI signal would be useful to validate agent-generated changes before merge? |
| 14 | [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) | Issues enabled; 4 open issues; last push 2026-08-31; JavaScript MCP server for GitLab merge requests | [Issues](https://github.com/kopfrechner/gitlab-mr-mcp/issues) | Issue #41 reports IDE diff review gaps; would a local deterministic review step and shared severity policy help before a GitLab merge request? |
| 15 | [mattzcarey/shippie](https://github.com/mattzcarey/shippie) | Issues enabled; 22 open issues; last push 2026-08-12; TypeScript code-review tooling | [Issues](https://github.com/mattzcarey/shippie/issues) | Which review findings need a stable local policy or CI gate alongside your current workflow? |

## Issue-backed signals (API checked 2026-09-03)

These rows have a concrete public issue related to the product problem. They are still prospects, not contacts. Read the full thread and contribution rules before deciding whether a technical reply is appropriate; do not turn a bug report into a sales pitch.

| Priority | Public issue | Evidence | Suggested technical opener |
|---:|---|---|---|
| A1 | [tirth8205/code-review-graph#703](https://github.com/tirth8205/code-review-graph/issues/703) | Maintainer's project; open issue reports Cursor install failure and uncertainty about `uvx` command configuration on macOS | Could a documented stdio command plus a copy-paste config example make the Cursor install path deterministic? I maintain a separate local MCP reviewer and can compare the setup assumptions if useful. |
| A2 | [sdempsay/agentic-review-tool#5](https://github.com/sdempsay/agentic-review-tool/issues/5) | Open task explicitly proposes an MCP stdio server for code review across Grok, Claude Desktop, Cursor, and OpenCode | For the stdio entry point, are stable severity IDs and CI exit codes part of the contract? That makes it easier to keep editor feedback and merge gates consistent. |
| A3 | [unoplatform/uno#24305](https://github.com/unoplatform/uno/issues/24305) | Open issue says a failed or flaky Claude review agent should remain advisory instead of failing the whole PR check rollup | Would separating the advisory review report from the blocking build status solve the false-red signal, while keeping a deterministic local gate available for security findings? |

## Contact Protocol

1. Ask the opener question in the project public channel; do not paste a sales pitch into an unrelated issue.
2. If the maintainer describes a recurring shared-rules or CI problem, offer the [free 10-minute trial](https://aicraft.vip/trial.html).
3. Discuss the `$49` Team Rules Pack only after the problem is confirmed; discuss Team Updates only when ongoing maintenance is requested.
4. Log the date, URL, response, and next follow-up. A public reply is a contact, not revenue; only a confirmed payment belongs in revenue fields.

These are public prospects, not customers. Do not infer interest from stars, downloads, or open-issue counts. The candidate metadata is an audit snapshot checked 2026-09-03, not evidence of contact, trial, pre-commitment, or payment.
