import io
import json

from scripts.github_trial_report import (
    fetch_issues,
    issue_record,
    parse_form_body,
    report,
)

BODY = """### Team size
4

### Main languages
Python, TypeScript

### Offer tier discussed
Team Updates Team Pilot

### Decision timing
This month

### Conditional start commitment
Yes, subject to confirming scope and start date
"""


def test_parse_form_body_supports_english_fields():
    fields = parse_form_body(BODY)
    assert fields["team_size"] == "4"
    assert fields["languages"] == "Python, TypeScript"
    assert fields["precommitment"].startswith("Yes")


def test_issue_record_normalizes_pilot_without_counting_revenue():
    record = issue_record(
        {
            "title": "[Team trial] shared rules",
            "html_url": "https://github.com/GoodJobwilliam/aicraft/issues/1",
            "created_at": "2026-09-03T01:02:03Z",
            "user": {"login": "example"},
            "body": BODY,
        }
    )
    assert record["offer_tier"] == "Team Pilot"
    assert record["date"] == "2026-09-03"
    assert "revenue" not in record


def test_chinese_fields_are_supported():
    fields = parse_form_body("### 团队规模\n3\n\n### 讨论的增值档位\nTeam Updates Starter\n")
    assert fields == {"team_size": "3", "offer_tier": "Team Updates Starter"}


def test_report_is_explicitly_manual_and_zero_revenue():
    output = report(
        [
            {
                "title": "[Trial feedback] result",
                "html_url": "https://github.com/GoodJobwilliam/aicraft/issues/2",
                "created_at": "2026-09-03T01:02:03Z",
                "user": {"login": "example"},
                "body": BODY,
            }
        ]
    )
    assert "Trial/feedback issues: 1" in output
    assert "manually verify scope, price, start date, and payment" in output
    assert "Only confirmed Creem payments belong in revenue fields" in output


def test_report_empty_issues_is_truthful():
    output = report([])
    assert "Trial/feedback issues: 0" in output
    assert "No trial or feedback issues found" in output


class _Response:
    def __init__(self, payload):
        self._stream = io.StringIO(json.dumps(payload))

    def __enter__(self):
        return self._stream

    def __exit__(self, *_args):
        self._stream.close()


def test_fetch_issues_reads_all_pages_and_excludes_pull_requests():
    calls = []

    def opener(request, timeout):
        calls.append((request.full_url, timeout))
        page = 1 if "page=1&" in request.full_url or request.full_url.endswith("page=1") else 2
        if page == 1:
            payload = [{"number": n} for n in range(100)]
            payload.append({"number": 999, "pull_request": {"url": "https://example.test/pr/999"}})
        else:
            payload = [{"number": 1000}]
        return _Response(payload)

    issues = fetch_issues(api_base="https://api.example.test", opener=opener)

    assert len(issues) == 101
    assert issues[-1]["number"] == 1000
    assert all("pull_request" not in issue for issue in issues)
    assert len(calls) == 2
