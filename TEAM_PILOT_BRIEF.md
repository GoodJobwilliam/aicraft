# Team Pilot Brief

This is the scope sheet for the AICraft Team Updates founding pilot. It is designed to be shared with a small engineering team before any payment is requested. The free MCP Code Review Server remains local and MIT-licensed; this pilot adds human-maintained rules and rollout help.

## Who it fits

- Up to 10 engineers
- A team already using pull requests, CI, or an MCP-compatible editor
- A concrete recurring problem with inconsistent review rules, merge gates, or false positives
- A decision maker who can confirm scope and a target start date

## First 30 days

1. **Kickoff and baseline**: confirm the team's language mix, repositories in scope, current review workflow, and one measurable pain.
2. **Shared profile**: deliver one versioned rules profile for the agreed languages and document how teammates load it locally.
3. **CI setup review**: review one GitHub Actions or GitLab CI integration and provide a corrected merge-gate template.
4. **Tuning review**: review one batch of false-positive or missing-rule examples described without private source code, then propose severity or rule changes.
5. **Handoff note**: provide the final profile, setup notes, open limitations, and a recommendation for the next month.

## Acceptance checklist

The pilot is considered useful when the team can answer yes to these questions:

- Can every participating engineer run the same profile locally?
- Does the CI job produce a readable report and a predictable exit code?
- Is at least one named review pain addressed or made measurable?
- Does the team know which findings should block a merge and which should remain advisory?

## Price and payment trigger

- **Team Pilot**: $99/month or $990/year, up to 10 engineers.
- Payment is requested only after the team confirms this scope, the start date, and the billing cadence in writing.
- A trial request, issue comment, or conditional statement is not a charge and is not recorded as revenue.
- After payment, the non-secret Creem order or subscription reference is recorded internally for reconciliation.

## Boundaries

This pilot does not include hosted code scanning, access to private repositories, 24/7 support, emergency response, unlimited custom rules, or a guarantee that every finding is correct. Source code stays with the team; examples for tuning should be summarized or redacted.

## Start conversation

Reply with four facts:

1. Team size and languages
2. Current review path (editor, pull request, CI, or a mix)
3. The one recurring pain to validate
4. The earliest month you could start if the acceptance checklist is met

For smaller teams, the Starter option is $19/month or $190/year for up to 3 engineers, with monthly rule drops and lightweight rollout questions. The same scope-confirmation rule applies.
