#!/usr/bin/env python3
"""Read public GitHub trial issues and print a manual-review queue.

This tool is intentionally read-only. Issue-form answers are lead evidence, not
payments or confirmed subscriptions, so it never writes OUTREACH_LOG.csv.
"""

from __future__ import annotations

import argparse
import json
import re
from collections.abc import Callable
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DEFAULT_REPO = "GoodJobwilliam/aicraft"
DEFAULT_API = "https://api.github.com"

_FIELD_ALIASES = {
    "team size": "team_size",
    "团队规模": "team_size",
    "main languages": "languages",
    "主要语言": "languages",
    "how did you find mcp code review?": "discovery_source",
    "你从哪里知道 mcp code review？": "discovery_source",
    "current review workflow": "workflow",
    "当前审查流程": "workflow",
    "biggest review pain": "pain",
    "最大的审查痛点": "pain",
    "trial timing": "trial_window",
    "试用时间": "trial_window",
    "ongoing updates interest": "updates_interest",
    "持续更新意向": "updates_interest",
    "role in the decision": "decision_role",
    "你在决策中的角色": "decision_role",
    "decision timing": "decision_window",
    "决策时间": "decision_window",
    "conditional start commitment": "precommitment",
    "有条件的开始承诺": "precommitment",
    "offer tier discussed": "offer_tier",
    "讨论的增值档位": "offer_tier",
    "next step": "next_step",
    "下一步": "next_step",
}

_HEADING = re.compile(r"^###\s+(.+?)\s*$")


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\r", "").strip())


def parse_form_body(body: str) -> dict[str, str]:
    """Extract issue-form answers by heading, supporting English and Chinese forms."""
    fields: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.splitlines():
        match = _HEADING.match(line)
        if match:
            current = _FIELD_ALIASES.get(_clean(match.group(1)).casefold())
            if current:
                fields[current] = []
            continue
        if current and _clean(line):
            fields[current].append(_clean(line))

    return {key: _clean(" ".join(values)) for key, values in fields.items()}


def normalize_offer_tier(value: str) -> str:
    lowered = value.casefold()
    if "pilot" in lowered or "试点" in value:
        return "Team Pilot"
    if "starter" in lowered:
        return "Starter"
    if "rules pack" in lowered or "规则包" in value:
        return "Team Rules Pack"
    if "free" in lowered or "免费" in value:
        return "Free server"
    return ""


def issue_record(issue: dict[str, object]) -> dict[str, str]:
    answers = parse_form_body(str(issue.get("body") or ""))
    title = _clean(str(issue.get("title") or "Untitled issue"))
    created = str(issue.get("created_at") or "")
    try:
        date = datetime.fromisoformat(created).date().isoformat()
    except ValueError:
        date = created[:10]
    user = issue.get("user")
    author = str(user.get("login") or "") if isinstance(user, dict) else ""
    return {
        "date": date,
        "title": title,
        "url": str(issue.get("html_url") or ""),
        "author": author,
        "team_size": answers.get("team_size", ""),
        "languages": answers.get("languages", ""),
        "discovery_source": answers.get("discovery_source", ""),
        "workflow": answers.get("workflow", ""),
        "pain": answers.get("pain", ""),
        "trial_window": answers.get("trial_window", ""),
        "offer_tier": normalize_offer_tier(answers.get("offer_tier", "") or answers.get("updates_interest", "")),
        "updates_interest": answers.get("updates_interest", ""),
        "decision_role": answers.get("decision_role", ""),
        "decision_window": answers.get("decision_window", ""),
        "precommitment": answers.get("precommitment", ""),
        "next_step": answers.get("next_step", ""),
    }


def fetch_issues(
    repo: str = DEFAULT_REPO,
    *,
    api_base: str = DEFAULT_API,
    opener: Callable[..., object] = urlopen,
) -> list[dict[str, object]]:
    """Fetch public issues; pull requests are excluded from the lead queue."""
    issues: list[dict[str, object]] = []
    page = 1
    while True:
        query = urlencode({"state": "all", "per_page": 100, "page": page})
        url = f"{api_base.rstrip('/')}/repos/{repo}/issues?{query}"
        request = Request(
            url,
            headers={"Accept": "application/vnd.github+json", "User-Agent": "aicraft-trial-report"},
        )
        with opener(request, timeout=20) as response:  # type: ignore[call-arg]
            payload = json.load(response)
        if not isinstance(payload, list):
            raise TypeError("GitHub API returned an unexpected payload")
        issues.extend(item for item in payload if isinstance(item, dict) and "pull_request" not in item)
        if len(payload) < 100:
            return issues
        page += 1


def report(issues: list[dict[str, object]], *, repo: str = DEFAULT_REPO) -> str:
    records = [issue_record(issue) for issue in issues]
    records = [
        record
        for record in records
        if record["offer_tier"]
        or record["next_step"]
        or "trial" in record["title"].casefold()
        or "试用" in record["title"]
    ]
    lines = [f"Source: public GitHub issues for {repo}", "", f"Trial/feedback issues: {len(records)}"]
    if not records:
        lines.append("No trial or feedback issues found.")
        lines.append("")
        lines.append("This report never infers revenue; all commercial fields require manual confirmation.")
        return "\n".join(lines)

    for index, record in enumerate(records, start=1):
        lines.extend(
            [
                "",
                f"{index}. {record['title']} ({record['date']})",
                f"   URL: {record['url']}",
                f"   Team/languages: {record['team_size'] or 'unknown'} / {record['languages'] or 'unknown'}",
                f"   Discovery source: {record['discovery_source'] or 'unknown'}",
                f"   Offer signal: {record['offer_tier'] or 'unselected'}",
                f"   Decision window: {record['decision_window'] or 'unknown'}",
                f"   Conditional commitment: {record['precommitment'] or 'not answered'}",
                "   Action: manually verify scope, price, start date, and payment before updating OUTREACH_LOG.csv.",
            ]
        )
    lines.extend(["", "No issue answer is revenue. Only confirmed Creem payments belong in revenue fields."])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only report of public AICraft trial issues.")
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--api-base", default=DEFAULT_API, help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        print(report(fetch_issues(args.repo, api_base=args.api_base), repo=args.repo))
    except (HTTPError, URLError, OSError, TypeError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
