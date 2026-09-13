#!/usr/bin/env python3
"""Report public free-distribution signals without inferring revenue."""

from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from dataclasses import dataclass


@dataclass(frozen=True)
class DistributionSnapshot:
    pypi_last_day: int
    pypi_last_week: int
    pypi_last_month: int
    release_downloads: dict[str, int]


def _get_json(url: str, opener=urllib.request.urlopen) -> dict:
    request = urllib.request.Request(
        url, headers={"Accept": "application/vnd.github+json", "User-Agent": "aicraft-distribution-report"}
    )
    with opener(request, timeout=20) as response:
        payload = json.load(response)
    if not isinstance(payload, dict):
        raise TypeError(f"expected an object from {url}")
    return payload


def fetch_snapshot(
    *,
    package: str = "aicraft-code-review",
    repository: str = "GoodJobwilliam/aicraft",
    release_tag: str = "mcp-code-review-0.1.2",
    opener=urllib.request.urlopen,
) -> DistributionSnapshot:
    stats = _get_json(f"https://pypistats.org/api/packages/{package}/recent", opener)
    data = stats.get("data", {})
    recent = {key: int(data.get(key, 0)) for key in ("last_day", "last_week", "last_month")}
    release = _get_json(
        f"https://api.github.com/repos/{repository}/releases/tags/{release_tag}", opener
    )
    assets = release.get("assets", [])
    downloads = {str(asset["name"]): int(asset.get("download_count", 0)) for asset in assets}
    return DistributionSnapshot(
        pypi_last_day=recent["last_day"],
        pypi_last_week=recent["last_week"],
        pypi_last_month=recent["last_month"],
        release_downloads=downloads,
    )


def report(snapshot: DistributionSnapshot) -> str:
    lines = [
        "Public distribution signals",
        f"- PyPI aicraft-code-review downloads (last day): {snapshot.pypi_last_day}",
        f"- PyPI aicraft-code-review downloads (last 7 days): {snapshot.pypi_last_week}",
        f"- PyPI aicraft-code-review downloads (last 30 days): {snapshot.pypi_last_month}",
        "- GitHub Release asset downloads:",
    ]
    if snapshot.release_downloads:
        lines.extend(f"  - {name}: {count}" for name, count in sorted(snapshot.release_downloads.items()))
    else:
        lines.append("  - none recorded")
    lines.extend(
        [
            "",
            "These are distribution signals only. Downloads, stars, and release views are not contacts, trials, customers, or revenue.",
            "Only a qualified reply, completed team test, explicit paid signal, or confirmed payment advances the sales funnel.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Report public AICraft distribution signals.")
    parser.add_argument("--package", default="aicraft-code-review")
    parser.add_argument("--repository", default="GoodJobwilliam/aicraft")
    parser.add_argument("--release-tag", default="mcp-code-review-0.1.2")
    args = parser.parse_args()
    try:
        snapshot = fetch_snapshot(
            package=args.package, repository=args.repository, release_tag=args.release_tag
        )
    except (OSError, TypeError, ValueError) as exc:
        parser.error(f"could not fetch distribution signals: {exc}")
    print(report(snapshot))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
