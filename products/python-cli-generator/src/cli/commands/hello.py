"""
Hello command — example CLI command demonstrating Rich output.
"""
from typing import Optional

import typer
from rich import print as rprint
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()


def hello(
    name: str = typer.Argument(..., help="Name to greet"),
    count: int = typer.Option(1, "--count", "-n", help="Number of times to repeat"),
    formal: bool = typer.Option(False, "--formal", "-f", help="Use formal greeting"),
) -> None:
    """
    Greet someone with style.
    """
    greeting = "Good day" if formal else "Hello"

    # Show a progress spinner for dramatic effect
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Preparing greeting...", total=None)

    # Build a table
    table = Table(title=f"{greeting}, {name}!")
    table.add_column("Iteration", style="cyan", no_wrap=True)
    table.add_column("Message", style="green")

    for i in range(1, count + 1):
        msg = f"{greeting}, {name}!" if not formal else f"{greeting}, esteemed {name}. It is a pleasure to meet you."
        table.add_row(str(i), msg)

    rprint(table)

    # Summary panel
    rprint(
        Panel(
            f"Greeted [bold]{name}[/bold] [cyan]{count}[/cyan] time(s) in "
            f"{'formal' if formal else 'casual'} mode.",
            title="Summary",
            border_style="green",
        )
    )
