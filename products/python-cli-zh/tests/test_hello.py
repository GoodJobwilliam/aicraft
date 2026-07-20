"""
hello 命令的测试用例。
"""
from typer.testing import CliRunner

from cli.main import app

runner = CliRunner()


def test_hello_basic() -> None:
    """测试基本问候。"""
    result = runner.invoke(app, ["hello", "张三"])
    assert result.exit_code == 0
    assert "你好" in result.stdout
    assert "张三" in result.stdout


def test_hello_formal() -> None:
    """测试正式问候。"""
    result = runner.invoke(app, ["hello", "李四", "--formal"])
    assert result.exit_code == 0
    assert "您好" in result.stdout
    assert "李四" in result.stdout


def test_hello_multiple() -> None:
    """测试多次重复。"""
    result = runner.invoke(app, ["hello", "王五", "--count", "3"])
    assert result.exit_code == 0
    assert "次数" in result.stdout


def test_hello_missing_name() -> None:
    """测试缺少必要参数时显示错误。"""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code != 0


def test_version_flag() -> None:
    """测试 --version 参数。"""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "CLI 中文模板" in result.stdout or "v0" in result.stdout


def test_help_flag() -> None:
    """测试 --help 参数。"""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.stdout
