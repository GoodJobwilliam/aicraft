# Issue-Specific Outreach Drafts

These drafts are prepared for manual review and sending. They are not sent automatically. Before posting, read the current issue thread, check whether the project welcomes external suggestions, and remove any sentence that is no longer accurate.

## Verified send order (2026-09-03)

1. **A3** has the freshest active discussion (updated 2026-08-31) and asks a concrete workflow-design question. Use the revised reply below; do not introduce the product unless a maintainer asks for an example.
2. **A2** has no comments and a well-defined MCP acceptance checklist. Use it as a concise architecture suggestion, not a promotion.
3. **A4** is an active design proposal and is suitable only if the maintainer is inviting implementation discussion.
4. **A1** remains open, but its maintainer has already identified both the nested Cursor payload and missing `uvx` prerequisite. The earlier generic question is obsolete; use the updated test-oriented reply below only if it adds something to the website-side fix.
5. **A5** and **A6** already contain promotional replies from unrelated tools. Do not add another unsolicited tool pitch. Keep them as research references unless someone explicitly asks for alternatives.

## A1 — code-review-graph #703

Issue: https://github.com/tirth8205/code-review-graph/issues/703

> The latest maintainer note already narrows this to the website's Add-to-Cursor payload, rather than the repository CLI installer. A regression test that decodes the generated payload would make the boundary explicit: assert that `mcpServers.code-review-graph` itself has `command`/`args`, rather than a second nested `code-review-graph` key.
>
> ~~~json
> {
>   "command": "uvx",
>   "args": ["code-review-graph", "serve"]
> }
> ~~~
>
> For an `uvx`-based server, the install page should also either state the `uv` prerequisite or emit a fallback executable. That lets the test distinguish malformed configuration from a missing local binary.

## A2 — agentic-review-tool #5

Issue: https://github.com/sdempsay/agentic-review-tool/issues/5

> The MCP stdio boundary looks well scoped. I would make the tool result contract explicit before the host integrations: include stable finding IDs, severity values, a summary, and a machine-readable decision field, while retaining the human-readable report for chat. That gives the CLI, MCP host, and later CI integration one shared result model.
>
> For the blocking decision, it may be useful to keep transport/model failures distinct from review findings: return a structured unavailable/error result for the former, and let the CI wrapper decide whether that is advisory. This prevents a transient local-model failure from being mistaken for a code-policy failure.

## A3 — Uno #24305

Issue: https://github.com/unoplatform/uno/issues/24305

> The provider-authentication detail in the latest investigation reinforces the split proposed here: an agent-review job can remain advisory and emit a warning/summary when its credential path fails, while a separate deterministic policy job is the only review-related check allowed to block a merge.
>
> That policy job can consume a versioned JSON result with stable rule IDs and severities, so it is auditable and reproducible without treating rate limits, timeouts, or credential failures as defects in the pull request. This also makes it possible to tighten a small set of local rules over time without coupling merge safety to the hosted agent.

## A4 — asterinas #4

Issue: https://github.com/androidAppGuard/asterinas/issues/4

> The domain-knowledge MCP idea could pair well with a deterministic local pre-check. One useful contract boundary may be stable rule IDs, severity values, and a machine-readable result, so known security and policy patterns remain testable even when retrieval misses context. Would you want that pre-check to run before the domain-specific review, or only as a merge-gate companion?

## A5 — rpguide #47

Issue: https://github.com/Gabriel-GM5/rpguide/issues/47

> For a Claude code-review Action, I would separate the report from the blocking decision: run the review with read-only permissions, publish the report as an artifact, and let a small policy step decide whether Critical findings should fail the check. That keeps fork PRs safe while allowing repository-owned TDD/SDD conventions to become explicit rules. Does that fit the workflow you are designing?

## A6 — Sourcery #477

Issue: https://github.com/sourcery-ai/sourcery/issues/477

> A CLI review path becomes much easier to compose when the output contract is stable: deterministic check IDs, severity counts, and exit codes for clean/high/critical results, alongside a human-readable report. A committed local rules file could then make the same command useful in CI without sending source to a hosted scanner. Which part of the CLI workflow is the highest priority for your users?

## A7 — agent-co-op-mcp #40

Issue: https://github.com/lwgerhardt/agent-co-op-mcp/issues/40

> The three items in this issue reinforce each other: a single package-version source prevents the CLI and MCP server from drifting, while a structured return type gives integrations a stable boundary to test. I would keep the human-readable rendering at the CLI or host layer and return a typed object from MCP, with an explicit schema/version when the result is persisted or sent to CI.
>
> For the CI additions, a format check alongside lint catches a different class of drift than tests, so it seems useful to keep both. Would you prefer the shared result model to live in a small domain module, or remain close to the MCP tool definitions until another consumer needs it?

## A8 — caroline #79

Issue: https://github.com/SociableSteve/caroline/issues/79

> The decision to keep one standing scanner in both the local hook and CI seems like the right boundary: the repository should own the rule configuration, while the hook gives fast feedback and CI remains the merge gate. For the unresolved non-provider toggle, I would start with explicit blocking patterns for private keys, connection strings, and the project's own token shapes, and keep broad generic matches warning-level until fixtures show they are useful. That keeps a false positive reviewable without weakening the required check. How are you planning to represent a deliberate suppression so the local and CI paths cannot drift?

Manual note: the maintainer has already chosen secretlint and documented its rationale. Do not pitch AICraft unless they ask for a comparison or an example of a separate local deterministic checker.

## Manual send checklist

- Confirm the issue is still open and the question is still relevant.
- Reply in the issue's normal technical context; do not create a new issue for promotion.
- Do not paste source code, credentials, or private project details.
- Do not claim endorsement, partnership, trial, or customer status.
- If the maintainer asks for a tool comparison, then share the free trial URL: https://aicraft.vip/trial.html
- Record a contact in OUTREACH_LOG.csv only after the reply is actually posted, with the issue URL and discovery_source=GitHub issue search.

The drafts are opportunities for human outreach, not funnel evidence. A posted reply is a contact; only a real trial, explicit conditional commitment, or confirmed Creem payment advances the corresponding funnel field.
