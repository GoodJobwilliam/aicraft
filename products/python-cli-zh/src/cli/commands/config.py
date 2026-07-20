"""
配置管理命令 — 查看和修改应用配置。
"""
from pathlib import Path
from typing import Optional

import typer
from rich import print as rprint
from rich.table import Table

from core.config import Settings


def show_config(
    ctx: typer.Context,
) -> None:
    """
    显示当前配置。
    
    读取环境变量和配置文件中的设置，以表格形式展示。
    """
    settings = Settings()

    table = Table(title="当前配置")
    table.add_column("配置项", style="cyan", no_wrap=True)
    table.add_column("值", style="green")
    table.add_column("来源", style="yellow")

    for field_name in settings.model_fields_set:
        value = getattr(settings, field_name)
        table.add_row(field_name, str(value), "环境变量/文件")

    rprint(table)
