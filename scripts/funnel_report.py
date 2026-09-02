#!/usr/bin/env python3
"""Print a factual customer-funnel report from OUTREACH_LOG.csv."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path

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
    if (one_time > 0 or mrr > 0) and not row.get("payment_reference", "").strip():
        raise ValueError(
            f"row {row_number} needs payment_reference when revenue is greater than zero"
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
    return lines


def report(path: Path) -> str:
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
            f"- MRR target progress: {mrr / 2000 * 100:.2f}%",
            "",
            "Only confirmed payments belong in revenue fields. A paid signal or pre-commitment is not revenue.",
        ]
    )
    lines.extend(_tier_summary(rows))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Report AICraft customer-funnel evidence.")
    parser.add_argument("csv_path", nargs="?", type=Path, default=Path("OUTREACH_LOG.csv"))
    args = parser.parse_args()
    try:
        print(report(args.csv_path))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
