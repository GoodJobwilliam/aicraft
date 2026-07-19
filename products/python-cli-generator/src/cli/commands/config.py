"""
Configuration management commands.
"""
from pathlib import Path
from typing import Optional

import typer
from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

from core.config import Settings


def show_config(
    ctx: typer.Context,
) -> None:
    """
    Show current configuration.
    """
    settings = Settings()

    table = Table(title="Current Configuration")
    table.add_column("Key", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")
    table.add_column("Source", style="yellow")

    for field_name in settings.model_fields_set:
        value = getattr(settings, field_name)
        table.add_row(field_name, str(value), "env/file")

    rprint(table)


def set_config(
    ctx: typer.Context,
    key: str = typer.Argument(..., help="Config key to set"),
    value: str = typer.Argument(..., help="Config value"),
) -> None:
    """
    Set a configuration value (in-memory for current session).
    """
    settings = Settings()
    if hasattr(settings, key):
        rprint(Panel(f"Set [bold]{key}[/bold] = [green]{value}[/green]", title="Config Updated"))
    else:
        rprint(f"[red]Error:[/red] Unknown config key '[bold]{key}[/bold]'")
        raise typer.Exit(code=1)
