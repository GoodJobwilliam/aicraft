"""
Tests for the hello command.
"""
from typer.testing import CliRunner

from cli.main import app

runner = CliRunner()


def test_hello_basic() -> None:
    """Test basic hello command."""
    result = runner.invoke(app, ["hello", "World"])
    assert result.exit_code == 0
    assert "Hello" in result.stdout
    assert "World" in result.stdout


def test_hello_formal() -> None:
    """Test formal greeting."""
    result = runner.invoke(app, ["hello", "Dr. Smith", "--formal"])
    assert result.exit_code == 0
    assert "Good day" in result.stdout
    assert "Dr. Smith" in result.stdout


def test_hello_multiple() -> None:
    """Test greeting repeated N times."""
    result = runner.invoke(app, ["hello", "World", "--count", "3"])
    assert result.exit_code == 0
    # Should have 3 rows in the output
    assert "Iteration" in result.stdout


def test_hello_no_name_shows_error() -> None:
    """Test that missing required argument shows error."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code != 0
    assert "Missing argument" in result.stdout or "Error" in result.stdout
