"""
CLI 主入口 — 使用 Typer 框架构建命令行应用。

用法：
    python -m cli hello 张三
    python -m cli show-config
    python -m cli --version
"""
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

from cli.commands import hello, config

# 创建 Typer 应用实例
app = typer.Typer(
    name="cli-zh",
    help="Python CLI 项目模板（中文版）",
    add_completion=False,
    pretty_exceptions_enable=False,
)

# 注册子命令
app.command()(hello.hello)
app.command()(config.show_config)

console = Console()


def _version_callback(value: bool) -> None:
    """显示版本号并退出。"""
    if value:
        from src import __version__
        console.print(f"[bold]CLI 中文模板[/bold] v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False, "--version", "-V", help="显示版本号并退出",
        callback=_version_callback,
    ),
    config_file: Optional[Path] = typer.Option(
        None, "--config", "-c",
        help="配置文件路径",
        exists=True, file_okay=True, dir_okay=False,
    ),
    json_output: bool = typer.Option(
        False, "--json", help="以 JSON 格式输出"
    ),
) -> None:
    """
    Python CLI 项目模板（中文版）
    
    一个生产级的命令行应用脚手架，包含配置管理、日志、HTTP 客户端等常用功能。
    """
    # 在 context 中存储全局选项
    ctx.obj = {
        "config_file": config_file,
        "json_output": json_output,
    }


if __name__ == "__main__":
    app()
