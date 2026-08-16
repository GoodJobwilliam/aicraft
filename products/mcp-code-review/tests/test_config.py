"""
Tests for review configuration: custom rules, disabled checks,
severity overrides, min severity, and config discovery.
"""
import json
from pathlib import Path

import pytest

from mcp_code_review.config import (
    ENV_VAR,
    ReviewConfig,
    load_config,
)
from mcp_code_review.reviewer import CodeReviewer

try:
    import yaml  # noqa: F401

    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def make_reviewer(data: dict) -> CodeReviewer:
    return CodeReviewer(ReviewConfig.from_dict(data))


class TestCustomRules:
    def test_custom_rule_matches(self):
        reviewer = make_reviewer({
            "custom_rules": [
                {
                    "name": "no-console-log",
                    "pattern": r"console\.log\(",
                    "severity": "high",
                    "issue": "Console logging left in production code",
                    "fix": "Use a proper logger",
                }
            ]
        })
        result = reviewer.review_code("function f() {\n  console.log('x')\n}")
        assert "Console logging left in production code" in result
        assert "High" in result

    def test_invalid_regex_reports_info(self):
        reviewer = make_reviewer({
            "custom_rules": [{"name": "broken", "pattern": "(unclosed"}]
        })
        result = reviewer.review_code("x = 1")
        assert "Invalid regex" in result


class TestDisabledChecks:
    def test_disabled_check_filtered_out(self):
        reviewer = make_reviewer({"disabled_checks": ["todo_comment"]})
        result = reviewer.review_code("# TODO: implement error handling\nx = 1")
        assert "TODO" not in result

    def test_disabled_check_keeps_others(self):
        reviewer = make_reviewer({"disabled_checks": ["todo_comment"]})
        result = reviewer.review_code("API_KEY = 'sk-abc123'")
        assert "credential" in result.lower() or "secret" in result.lower()


class TestSeverityOverrides:
    def test_override_raises_severity(self):
        reviewer = make_reviewer({"severity_overrides": {"hardcoded_secret": "critical"}})
        result = reviewer.review_code("API_KEY = 'sk-abc123'")
        assert "Critical" in result

    def test_override_lowers_severity(self):
        reviewer = make_reviewer({"severity_overrides": {"hardcoded_secret": "info"}})
        result = reviewer.review_code("API_KEY = 'sk-abc123'")
        assert "### 🔴 Critical" not in result
        assert "Info" in result


class TestMinSeverity:
    def test_min_severity_filters_low_findings(self):
        reviewer = make_reviewer({"min_severity": "high"})
        result = reviewer.review_code("# TODO: implement error handling\nx = 1")
        assert "TODO" not in result

    def test_min_severity_keeps_high(self):
        reviewer = make_reviewer({"min_severity": "high"})
        result = reviewer.review_code("API_KEY = 'sk-abc123'")
        assert "credential" in result.lower() or "secret" in result.lower()

    def test_custom_rule_respects_min_severity(self):
        reviewer = make_reviewer({
            "min_severity": "high",
            "custom_rules": [
                {"name": "no-print", "pattern": r"print\(", "severity": "info"}
            ],
        })
        result = reviewer.review_code("print('debug')")
        assert "Matches custom rule" not in result


class TestConfigValidation:
    def test_invalid_severity_raises(self):
        with pytest.raises(ValueError):
            ReviewConfig.from_dict({"severity_overrides": {"x": "ultra"}})

    def test_invalid_min_severity_raises(self):
        with pytest.raises(ValueError):
            ReviewConfig.from_dict({"min_severity": "urgent"})

    def test_custom_rule_requires_pattern(self):
        with pytest.raises(ValueError):
            ReviewConfig.from_dict({"custom_rules": [{"name": "no-pattern"}]})


class TestConfigLoading:
    def test_load_json_config(self, tmp_path: Path):
        cfg = tmp_path / "cfg.json"
        cfg.write_text(json.dumps({"disabled_checks": ["long_lines"]}))
        config = load_config(cfg)
        assert config.disabled_checks == ["long_lines"]

    def test_env_var_points_to_config(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        cfg = tmp_path / "cfg.json"
        cfg.write_text(json.dumps({"min_severity": "medium"}))
        monkeypatch.setenv(ENV_VAR, str(cfg))
        config = load_config()
        assert config.min_severity == "medium"

    def test_env_var_missing_file_raises(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv(ENV_VAR, str(tmp_path / "nope.json"))
        with pytest.raises(FileNotFoundError):
            load_config()

    def test_discovers_config_in_parent_dir(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        (tmp_path / ".mcp-code-review.json").write_text(
            json.dumps({"disabled_checks": ["todo_comment"]})
        )
        nested = tmp_path / "src" / "pkg"
        nested.mkdir(parents=True)
        monkeypatch.chdir(nested)
        reviewer = CodeReviewer()
        result = reviewer.review_code("# TODO: later")
        assert "TODO" not in result

    @pytest.mark.skipif(not HAS_YAML, reason="PyYAML not installed")
    def test_load_yaml_config(self, tmp_path: Path):
        cfg = tmp_path / "cfg.yaml"
        cfg.write_text("disabled_checks:\n  - todo_comment\n")
        config = load_config(cfg)
        assert config.disabled_checks == ["todo_comment"]
