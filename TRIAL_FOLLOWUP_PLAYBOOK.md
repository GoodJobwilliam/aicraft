# Team Trial Follow-up Playbook

Manual, zero-budget process for turning a public trial request into a real product decision. Use only information the applicant chooses to share in the issue; never ask for source code, secrets, or private credentials.

## Service level

- Reply in the issue thread within 24 hours when practical.
- Acknowledge the team's stated language, workflow, pain, role, and decision window.
- Give one concrete next step, not a product tour.
- Close the loop after seven days if there is no response.

## Reply sequence

### 1. First reply

Thank them, restate the problem in one sentence, and point to the 10-minute trial kit. Ask them to report three things: what it caught, which rule they would share, and what was noisy.

### 2. Trial review

If they report a real finding, ask whether the same rule should run in every repository and whether CI should block on it. If they report noise, ask for the rule intent and desired severity; do not ask for private code.

### 3. Offer selection

- **Rules only**: point to the free config workflow first; offer the `$49` Team Rules Pack when the team wants the validated multi-language profiles, CI templates, and prompts.
- **Ongoing maintenance**: explain Team Updates at `$19/month` or `$190/year`, including monthly rules, CI refreshes, and rollout email support.
- **No decision yet**: leave the free server and trial kit as the next step; do not push a checkout link.

## Evidence thresholds

Record these in `OUTREACH_LOG.md`:

- **Qualified reply**: describes a recurring review pain and answers the workflow questions.
- **Team test**: runs the sample or a real non-confidential test and reports an outcome.
- **Paid signal**: explicitly says they would buy the `$49` pack or consider Team Updates at the stated price.
- **Pre-commitment**: names a target start month and accepts the stated scope and price, subject to the final checkout link.
- **Customer**: payment is confirmed in Creem; a message or intent does not count as revenue.

## Revenue math

The `$2,000` MRR target requires 106 Team Updates customers at the current `$19/month` founding price. Annual plans are tracked as recurring revenue using their monthly equivalent (`$190/year` = `$15.83` MRR per customer). Team Rules Pack purchases add one-time revenue but do not count toward MRR.

Do not treat one-time `$49` purchases as MRR. Track one-time revenue and recurring revenue separately.

## Weekly review

Every seven days, count: contacts, qualified replies, team tests, paid signals, pre-commitments, Team Rules Pack sales, Team Updates subscribers, one-time revenue, and MRR. Update the offer only when several conversations show the same pain.
