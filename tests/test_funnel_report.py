import csv
from pathlib import Path

import pytest
from scripts.funnel_report import report

HEADER = [
    "date",
    "channel",
    "contact_or_audience",
    "github_issue",
    "team_size",
    "main_languages",
    "discovery_source",
    "current_workflow",
    "decision_role",
    "decision_window",
    "offer_tier",
    "qualified_reply",
    "team_test",
    "paid_signal",
    "precommitment",
    "rules_pack_sales",
    "team_updates_subscribers",
    "one_time_revenue_usd",
    "mrr_usd",
    "payment_reference",
    "next_follow_up",
    "next_action",
]


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(rows)


def row(**overrides: str) -> dict[str, str]:
    values = {key: "" for key in HEADER}
    values.update({"date": "2026-08-30", "channel": "test", "contact_or_audience": "sample"})
    values.update(overrides)
    return values


def test_empty_log_reports_zero(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(path, [])
    output = report(path)
    assert "contacts: 0" in output
    assert "MRR (USD): 0.00" in output


def test_revenue_and_mrr_are_separate(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(
        path,
        [
            row(qualified_reply="yes", team_test="yes", paid_signal="yes", offer_tier="Team Rules Pack", rules_pack_sales="1", one_time_revenue_usd="49", payment_reference="creem:order-1"),
            row(precommitment="yes", offer_tier="Team Updates Starter", team_updates_subscribers="1", mrr_usd="19", payment_reference="creem:subscription-1"),
        ],
    )
    output = report(path)
    assert "pre-commitments: 1" in output
    assert "One-time revenue (USD): 49.00" in output
    assert "MRR (USD): 19.00" in output


def test_yes_accepts_chinese_values(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(path, [row(qualified_reply="是", team_test="有")])
    output = report(path)
    assert "qualified replies: 1" in output
    assert "team tests: 1" in output


def test_missing_column_is_rejected(tmp_path: Path):
    path = tmp_path / "log.csv"
    path.write_text("date,channel\n2026-08-30,test\n", encoding="utf-8")
    with pytest.raises(ValueError, match="missing required columns"):
        report(path)


def test_offer_tier_column_is_required(tmp_path: Path):
    path = tmp_path / "log.csv"
    path.write_text(
        "date,channel,contact_or_audience,qualified_reply,team_test,paid_signal,precommitment,"
        "rules_pack_sales,team_updates_subscribers,one_time_revenue_usd,mrr_usd,payment_reference,next_follow_up\n"
        "2026-08-30,test,sample,,,,,,,,,\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="offer_tier"):
        report(path)


def test_offer_tier_signals_keep_unconfirmed_revenue_at_zero(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(
        path,
        [
            row(offer_tier="Team Pilot", team_test="yes", paid_signal="yes"),
            row(offer_tier="Starter", precommitment="yes"),
            row(
                offer_tier="Team Pilot",
                team_updates_subscribers="1",
                mrr_usd="99",
                payment_reference="creem:subscription-99",
            ),
        ],
    )

    output = report(path)

    assert "Offer tier signals" in output
    assert "Starter: 1 contacts, 0 tests, 0 paid signals, 1 pre-commitments, 0 subscribers, $0.00 MRR" in output
    assert "Team Pilot: 2 contacts, 1 tests, 1 paid signals, 0 pre-commitments, 1 subscribers, $99.00 MRR" in output
    assert "MRR (USD): 99.00" in output


def test_discovery_source_signals_are_grouped(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(
        path,
        [
            row(discovery_source="Official MCP Registry", team_test="yes"),
            row(discovery_source="Official MCP Registry", paid_signal="yes"),
            row(discovery_source="Product Hunt", precommitment="yes"),
        ],
    )

    output = report(path)

    assert "Discovery source signals" in output
    assert "Official MCP Registry: 2 contacts, 1 tests, 1 paid signals, 0 pre-commitments, 0 subscribers, $0.00 MRR" in output
    assert "Product Hunt: 1 contacts, 0 tests, 0 paid signals, 1 pre-commitments, 0 subscribers, $0.00 MRR" in output
    assert "Conversion: tests 1/2 (50.0%), paid signals 1/2 (50.0%), pre-commitments 0/2 (0.0%)" in output


def test_offer_tier_conversion_rates_are_reported(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(
        path,
        [
            row(offer_tier="Team Pilot", team_test="yes", paid_signal="yes", precommitment="yes"),
            row(offer_tier="Team Pilot", team_test="yes"),
        ],
    )

    output = report(path)

    assert "Conversion: tests 2/2 (100.0%), paid signals 1/2 (50.0%), pre-commitments 1/2 (50.0%)" in output


def test_negative_revenue_is_rejected(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(path, [row(one_time_revenue_usd="-1")])
    with pytest.raises(ValueError, match="cannot be negative"):
        report(path)


def test_revenue_requires_payment_reference(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(path, [row(offer_tier="Team Rules Pack", one_time_revenue_usd="49")])
    with pytest.raises(ValueError, match="payment_reference"):
        report(path)


def test_revenue_requires_offer_tier(tmp_path: Path):
    path = tmp_path / "log.csv"
    write_rows(path, [row(one_time_revenue_usd="49", payment_reference="creem:order-1")])
    with pytest.raises(ValueError, match="offer_tier"):
        report(path)
