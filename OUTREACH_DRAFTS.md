# Issue-Specific Outreach Drafts

These drafts are prepared for manual review and sending. They are not sent automatically. Before posting, read the current issue thread, check whether the project welcomes external suggestions, and remove any sentence that is no longer accurate.

## A1 — code-review-graph #703

Issue: https://github.com/tirth8205/code-review-graph/issues/703

> I hit the same class of install ambiguity while testing a local MCP reviewer. One detail that may help the Cursor path: the PyPI distribution name and console-script name do not have to match. A deterministic stdio entry can make the executable explicit, for example:
>
> ~~~json
> {
>   "command": "uvx",
>   "args": ["--from", "aicraft-code-review", "--with", "mcp<2", "mcp-code-review"]
> }
> ~~~
>
> The important part is documenting whether Cursor expects a command, a URL, or an imported server definition. I would also show the equivalent uvx --from ... command next to the install button so a missing local uvx binary is a separate, obvious prerequisite. Does that match the failure mode you are seeing on macOS?

## A2 — agentic-review-tool #5

Issue: https://github.com/sdempsay/agentic-review-tool/issues/5

> The MCP stdio direction makes sense for editor-hosted follow-up. One contract detail worth pinning down early is deterministic finding metadata: stable rule IDs, severity values, and process exit codes for CI, while keeping the chat response human-readable. That lets the same review run be advisory in an editor but blocking in a merge gate when a team chooses it. A small JSON example in the MCP tool docs could make integrations easier to test across Grok, Claude Desktop, Cursor, and OpenCode.

## A3 — Uno #24305

Issue: https://github.com/unoplatform/uno/issues/24305

> The distinction between an advisory agent report and a blocking build signal seems important here. One practical split is to let the review job always publish its report and use a separate, deterministic policy job for findings that should block a merge. Then API failures, rate limits, and timeouts can stay neutral while a locally reproducible security or policy check still fails when the repository opts into it. Would that separation fit the workflow you are trying to preserve?

## Manual send checklist

- Confirm the issue is still open and the question is still relevant.
- Reply in the issue's normal technical context; do not create a new issue for promotion.
- Do not paste source code, credentials, or private project details.
- Do not claim endorsement, partnership, trial, or customer status.
- If the maintainer asks for a tool comparison, then share the free trial URL: https://aicraft.vip/trial.html
- Record a contact in OUTREACH_LOG.csv only after the reply is actually posted, with the issue URL and discovery_source=GitHub issue search.

The drafts are opportunities for human outreach, not funnel evidence. A posted reply is a contact; only a real trial, explicit conditional commitment, or confirmed Creem payment advances the corresponding funnel field.
