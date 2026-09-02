from scripts.github_trial_report import (
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
