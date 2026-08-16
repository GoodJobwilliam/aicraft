"""
Review configuration — custom rules, disabled checks, severity thresholds.

A config file can be placed:
  - next to the code being reviewed: `.mcp-code-review.yaml` (or `.json`)
  - anywhere, and pointed to via the `MCP_CODE_REVIEW_CONFIG` env var

Team-shared profiles work by committing the file to a shared repo and
pointing every teammate's client at it via `MCP_CODE_REVIEW_CONFIG`.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path

CONFIG_FILENAMES = (".mcp-code-review.yaml", ".mcp-code-review.yml", ".mcp-code-review.json")
ENV_VAR = "MCP_CODE_REVIEW_CONFIG"

VALID_SEVERITIES = {"critical", "high", "medium", "info"}
SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "info": 3}


@dataclass
class CustomRule:
    name: str
    pattern: str
    severity: str = "medium"
    category: str = "quality"
    issue: str = ""
    fix: str = ""

    def __post_init__(self) -> None:
        if self.severity not in VALID_SEVERITIES:
            raise ValueError(f"Invalid severity '{self.severity}' in rule '{self.name}'")
        if not self.issue:
            self.issue = f"Matches custom rule '{self.name}'"


@dataclass
class ReviewConfig:
    disabled_checks: list[str] = field(default_factory=list)
    severity_overrides: dict[str, str] = field(default_factory=dict)
    min_severity: str | None = None
    custom_rules: list[CustomRule] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> ReviewConfig:
        if not isinstance(data, dict):
            raise TypeError("Config root must be a mapping")

        disabled = data.get("disabled_checks", [])
        overrides = data.get("severity_overrides", {})
        min_severity = data.get("min_severity")
        custom_rules = data.get("custom_rules", [])

        if not isinstance(disabled, list) or not all(isinstance(x, str) for x in disabled):
            raise ValueError("'disabled_checks' must be a list of check ids")
        if not isinstance(overrides, dict):
            raise TypeError("'severity_overrides' must be a mapping of check id -> severity")
        for check_id, severity in overrides.items():
            if severity not in VALID_SEVERITIES:
                raise ValueError(f"Invalid severity '{severity}' for check '{check_id}'")
        if min_severity is not None and min_severity not in VALID_SEVERITIES:
            raise ValueError(f"Invalid min_severity '{min_severity}'")
        if not isinstance(custom_rules, list):
            raise TypeError("'custom_rules' must be a list")

        rules = []
        for raw in custom_rules:
            if not isinstance(raw, dict) or "pattern" not in raw:
                raise ValueError("Each custom rule needs a 'pattern' key")
            rules.append(
                CustomRule(
                    name=str(raw.get("name", raw["pattern"])),
                    pattern=str(raw["pattern"]),
                    severity=str(raw.get("severity", "medium")),
                    category=str(raw.get("category", "quality")),
                    issue=str(raw.get("issue", "")),
                    fix=str(raw.get("fix", "")),
                )
            )

        return cls(
            disabled_checks=list(disabled),
            severity_overrides=dict(overrides),
            min_severity=min_severity,
            custom_rules=rules,
        )


def _parse_text(text: str, path: Path) -> dict:
    if path.suffix in (".yaml", ".yml"):
        try:
            import yaml  # type: ignore

            data = yaml.safe_load(text)
        except ImportError:
            raise ValueError("YAML config requires PyYAML; use a .json config instead") from None
    else:
        data = json.loads(text)
    return data if isinstance(data, dict) else {}


def discover_config_path(start_dir: Path | None = None) -> Path | None:
    """Find a config file: env var first, then walk from start_dir up to home."""
    env_path = os.environ.get(ENV_VAR)
    if env_path:
        p = Path(env_path).expanduser()
        if p.exists():
            return p
        raise FileNotFoundError(f"Config from {ENV_VAR} not found: {p}")

    current = (start_dir or Path.cwd()).resolve()
    home = Path.home().resolve()
    while True:
        for name in CONFIG_FILENAMES:
            candidate = current / name
            if candidate.is_file():
                return candidate
        if current == home or current.parent == current:
            return None
        current = current.parent


def load_config(path: Path | None = None) -> ReviewConfig:
    """Load ReviewConfig from an explicit path, or auto-discover."""
    resolved = path or discover_config_path()
    if resolved is None:
        return ReviewConfig()
    text = resolved.read_text(encoding="utf-8")
    return ReviewConfig.from_dict(_parse_text(text, resolved))
