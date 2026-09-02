# AICraft GTM Next Steps

## Focus
- Free open-source MCP Code Review Server
- Paid Team Rules Pack
- New recurring offer: Team Updates

## Current offer shape
- One-time purchase: Team Rules Pack
- Recurring add-on: Team Updates
  - monthly rule drops
  - CI workflow refreshes
  - rollout/help email support
- Starter founding price to test: $19/month or $190/year (up to 3 engineers)
- Team Pilot founding price to test: $99/month or $990/year (up to 10 engineers)
- Team Pilot scope: first 30 days = one shared profile, one CI setup review, one rule/false-positive review, and rollout email support
- Team Pilot scope sheet: `TEAM_PILOT_BRIEF.md` (share before discussing payment; includes acceptance checklist and boundaries)
- Pre-sale flow: collect interest by email first; charge only after delivery scope and launch date are confirmed

## What is already done
- homepage and Chinese landing page focus on the MCP Code Review funnel
- dedicated Team Updates pages are live, with a structured GitHub team-trial form
- outreach copy and qualification questions are in `OUTREACH_PACK.md`; the dated public-evidence queue is in `OUTREACH_QUEUE.md`
- manual follow-up and conversion criteria are in `TRIAL_FOLLOWUP_PLAYBOOK.md`
- weekly funnel reporting uses `OUTREACH_LOG.csv` and `scripts/funnel_report.py`
- public launch guides and product READMEs use the current PyPI 0.1.2 install path

## Next zero-budget execution loop
1. Send 20 targeted messages using `OUTREACH_PACK.md`, starting with the highest-priority entries in `OUTREACH_QUEUE.md`.
2. Use public project channels only; invite qualified replies to the GitHub team-trial form, follow `TRIAL_FOLLOWUP_PLAYBOOK.md`, and record every contact in `OUTREACH_LOG.md`.
3. Offer the free server first; invite qualified teams to test the Team Rules Pack.
4. Record decision role and paid-decision timing in `OUTREACH_LOG.md`; prioritize teams that can decide this month or next.
5. Ask testers which tier they would explicitly pre-commit to before any recurring checkout is created; target Team Pilot when CI and tuning work is requested.
6. Record `offer_tier` as `Starter`, `Team Pilot`, or `Team Rules Pack` for each qualified conversation. Run `python3 scripts/funnel_report.py` weekly; review the tier breakdown after 20 contacts and adjust the offer around repeated pain, not vanity metrics.
7. When a team asks for recurring support, send `TEAM_PILOT_BRIEF.md`, ask them to confirm the four start facts, and only then discuss a written scope/start-date confirmation.

## External blockers
- PyPI, V2EX, 掘金, Product Hunt, or Indie Hackers login/OTP/CAPTCHA may require an in-browser action.
- VPN-dependent channels remain unavailable while the existing connection is off.
- No paid tools, ads, subscriptions, or infrastructure are required for this validation loop.

## First outreach questions
- How many engineers are on your team?
- Which languages do you review most?
- Do you want just rules, or rules plus CI and rollout help?
