"""
Tests for configuration management.
"""
from typer.testing import CliRunner

from cli.main import app

runner = CliRunner()


def test_show_config() -> None:
    """Test config display command."""
    result = runner.invoke(app, ["show-config"])
    assert result.exit_code == 0
    assert "Current Configuration" in result.stdout
    assert "app_name" in result.stdout


def test_version_flag() -> None:
    """Test --version flag."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "CLI Starter" in result.stdout or "v0" in result.stdout


def test_help_flag() -> None:
    """Test --help flag."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.stdout
