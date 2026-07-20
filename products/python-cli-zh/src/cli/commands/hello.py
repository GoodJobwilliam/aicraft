"""
打招呼命令 — 使用 Rich 库输出美观的终端内容。

演示功能：
    - 位置参数
    - 可选参数
    - Rich 表格输出
    - Rich 面板输出
"""
from typing import Optional

import typer
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

console = Console()


def hello(
    name: str = typer.Argument(..., help="你的名字"),
    count: int = typer.Option(1, "--count", "-n", help="重复次数"),
    formal: bool = typer.Option(False, "--formal", "-f", help="使用正式问候"),
) -> None:
    """
    向某人打招呼。
    
    支持普通和正式两种模式，可指定重复次数。
    """
    greeting = "您好" if formal else "你好"

    # 使用 Rich 表格展示
    table = Table(title=f"{greeting}，{name}！")
    table.add_column("次数", style="cyan", no_wrap=True)
    table.add_column("问候语", style="green")

    for i in range(1, count + 1):
        msg = f"{greeting}，{name}！" if not formal else f"{greeting}，尊敬的 {name}。很高兴认识您。"
        table.add_row(str(i), msg)

    rprint(table)

    # 输出汇总面板
    rprint(
        Panel(
            f"向 [bold]{name}[/bold] {greeting}了 [cyan]{count}[/cyan] 次",
            title="完成",
            border_style="green",
        )
    )
