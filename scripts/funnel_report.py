#!/usr/bin/env python3
"""Print a factual customer-funnel report from OUTREACH_LOG.csv."""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from datetime import date
from pathlib import Path

TARGET_MRR = 2000.0
TARGET_OFFERS = (("Starter", 19.0), ("Team Pilot", 99.0))

REQUIRED_COLUMNS = {
    "date",
    "channel",
    "contact_or_audience",
    "github_issue",
    "qualified_reply",
    "team_test",
    "paid_signal",
    "precommitment",
    "offer_tier",
    "rules_pack_sales",
    "team_updates_subscribers",
    "one_time_revenue_usd",
    "mrr_usd",
    "payment_reference",
    "next_follow_up",
}


def _yes(row: dict[str, str], key: str) -> bool:
    return row.get(key, "").strip().lower() in {"yes", "y", "true", "1", "是", "有"}


def _money(row: dict[str, str], key: str) -> float:
    value = row.get(key, "").strip().replace(",", "")
    if not value:
        return 0.0
    try:
        amount = float(value)
    except ValueError as exc:
        raise ValueError(f"{key} must be numeric, got {value!r}") from exc
    if amount < 0:
        raise ValueError(f"{key} cannot be negative")
    return amount


def _validate_payment_evidence(row: dict[str, str], row_number: int) -> None:
    """Require a traceable reference whenever confirmed revenue is recorded."""
    one_time = _money(row, "one_time_revenue_usd")
    mrr = _money(row, "mrr_usd")
    if one_time > 0 or mrr > 0:
        if not row.get("offer_tier", "").strip():
            raise ValueError(f"row {row_number} needs offer_tier when revenue is greater than zero")
        if not row.get("payment_reference", "").strip():
            raise ValueError(f"row {row_number} needs payment_reference when revenue is greater than zero")


def _rate(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "n/a"
    return f"{numerator / denominator * 100:.1f}%"


def _conversion_line(rows: list[dict[str, str]]) -> str:
    contacts = len(rows)
    tests = sum(_yes(row, "team_test") for row in rows)
    signals = sum(_yes(row, "paid_signal") for row in rows)
    commitments = sum(_yes(row, "precommitment") for row in rows)
    return (
        f"  Conversion: tests {tests}/{contacts} ({_rate(tests, contacts)}), "
        f"paid signals {signals}/{contacts} ({_rate(signals, contacts)}), "
        f"pre-commitments {commitments}/{contacts} ({_rate(commitments, contacts)})"
    )


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - columns
        if missing:
            names = ", ".join(sorted(missing))
            raise ValueError(f"{path} is missing required columns: {names}")
        rows = [row for row in reader if any((value or "").strip() for value in row.values())]
        for row_number, row in enumerate(rows, start=2):
            _validate_payment_evidence(row, row_number)
        return rows


def _tier_summary(rows: list[dict[str, str]]) -> list[str]:
    """Return factual conversion counts grouped by the selected offer tier."""
    tiers: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        tier = row.get("offer_tier", "").strip()
        if tier:
            tiers[tier].append(row)

    if not tiers:
        return []

    lines = ["", "Offer tier signals"]
    for tier in sorted(tiers, key=str.casefold):
        tier_rows = tiers[tier]
        contacts = len(tier_rows)
        tests = sum(_yes(row, "team_test") for row in tier_rows)
        signals = sum(_yes(row, "paid_signal") for row in tier_rows)
        commitments = sum(_yes(row, "precommitment") for row in tier_rows)
        subscribers = sum(_money(row, "team_updates_subscribers") for row in tier_rows)
        mrr = sum(_money(row, "mrr_usd") for row in tier_rows)
        lines.append(
            f"- {tier}: {contacts} contacts, {tests} tests, {signals} paid signals, "
            f"{commitments} pre-commitments, {subscribers:g} subscribers, ${mrr:.2f} MRR"
        )
        lines.append(_conversion_line(tier_rows))
    return lines


def _source_summary(rows: list[dict[str, str]]) -> list[str]:
    """Return factual conversion counts grouped by discovery source."""
    sources: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        source = row.get("discovery_source", "").strip()
        if source:
            sources[source].append(row)

    if not sources:
        return []

    lines = ["", "Discovery source signals"]
    for source in sorted(sources, key=str.casefold):
        source_rows = sources[source]
        contacts = len(source_rows)
        tests = sum(_yes(row, "team_test") for row in source_rows)
        signals = sum(_yes(row, "paid_signal") for row in source_rows)
        commitments = sum(_yes(row, "precommitment") for row in source_rows)
        subscribers = sum(_money(row, "team_updates_subscribers") for row in source_rows)
        mrr = sum(_money(row, "mrr_usd") for row in source_rows)
        lines.append(
            f"- {source}: {contacts} contacts, {tests} tests, {signals} paid signals, "
            f"{commitments} pre-commitments, {subscribers:g} subscribers, ${mrr:.2f} MRR"
        )
        lines.append(_conversion_line(source_rows))
    return lines


def _target_gap(mrr: float) -> list[str]:
    """Show the remaining MRR gap and the customer count at each recurring tier."""
    gap = max(0.0, TARGET_MRR - mrr)
    lines = ["", "MRR target gap", f"- Target: ${TARGET_MRR:.2f} MRR", f"- Remaining: ${gap:.2f} MRR"]
    if gap == 0:
        lines.append("- Target status: reached")
        return lines

    lines.append("- Target status: not reached")
    for label, monthly_price in TARGET_OFFERS:
        customers = math.ceil(gap / monthly_price)
        lines.append(
            f"- At ${monthly_price:.0f}/month {label}: {customers} additional customers"
        )
    lines.append("- Next action: convert qualified trial feedback into a paid-scope confirmation before recording revenue.")
    return lines


def _follow_up_summary(rows: list[dict[str, str]], as_of: date | None = None) -> list[str]:
    """List due and upcoming follow-ups without changing funnel counts."""
    today = as_of or date.today()
    scheduled: list[tuple[date, dict[str, str]]] = []
    for row in rows:
        raw = row.get("next_follow_up", "").strip()
        if not raw:
            continue
        try:
            scheduled.append((date.fromisoformat(raw), row))
        except ValueError as exc:
            raise ValueError(f"next_follow_up must be YYYY-MM-DD, got {raw!r}") from exc

    if not scheduled:
        return []

    lines = ["", f"Follow-up queue (as of {today.isoformat()})"]
    for due, row in sorted(scheduled, key=lambda item: item[0]):
        status = "due" if due <= today else "upcoming"
        contact = row.get("contact_or_audience", "unknown contact").strip() or "unknown contact"
        action = row.get("next_action", "").strip() or "review the conversation and choose one next step"
        lines.append(f"- {status}: {due.isoformat()} — {contact} — {action}")
    return lines


def report(path: Path, as_of: date | None = None) -> str:
    rows = read_rows(path)
    counts = {
        "contacts": len(rows),
        "qualified replies": sum(_yes(row, "qualified_reply") for row in rows),
        "team tests": sum(_yes(row, "team_test") for row in rows),
        "paid signals": sum(_yes(row, "paid_signal") for row in rows),
        "pre-commitments": sum(_yes(row, "precommitment") for row in rows),
        "Team Rules Pack sales": sum(_money(row, "rules_pack_sales") for row in rows),
        "Team Updates subscribers": sum(_money(row, "team_updates_subscribers") for row in rows),
    }
    one_time = sum(_money(row, "one_time_revenue_usd") for row in rows)
    mrr = sum(_money(row, "mrr_usd") for row in rows)

    lines = [f"Source: {path}", "", "Funnel"]
    lines.extend(f"- {label}: {value:g}" for label, value in counts.items())
    lines.extend(
        [
            f"- One-time revenue (USD): {one_time:.2f}",
            f"- MRR (USD): {mrr:.2f}",
            f"- MRR target progress: {mrr / TARGET_MRR * 100:.2f}%",
            "",
            "Only confirmed payments belong in revenue fields. A paid signal or pre-commitment is not revenue.",
        ]
    )
    lines.extend(_target_gap(mrr))
    lines.extend(_follow_up_summary(rows, as_of))
    lines.extend(_tier_summary(rows))
    lines.extend(_source_summary(rows))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Report AICraft customer-funnel evidence.")
    parser.add_argument("csv_path", nargs="?", type=Path, default=Path("OUTREACH_LOG.csv"))
    parser.add_argument("--as-of", type=date.fromisoformat, help="Evaluate follow-ups as of YYYY-MM-DD")
    args = parser.parse_args()
    try:
        print(report(args.csv_path, args.as_of))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
