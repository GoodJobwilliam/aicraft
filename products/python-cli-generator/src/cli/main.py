"""
CLI entry point and application definition.
"""
from pathlib import Path
from typing import Optional

import typer
from rich import print as rprint
from rich.console import Console

from cli.commands import hello, config, serve

app = typer.Typer(
    name="cli",
    help="Production-grade Python CLI application",
    add_completion=False,
    pretty_exceptions_enable=False,
)

# Register subcommands
app.command()(hello.hello)
app.command()(config.show_config)
app.command()(config.set_config)
app.command()(serve.serve)

console = Console()


def _version_callback(value: bool) -> None:
    if value:
        from src import __version__

        rprint(f"[bold]CLI Starter[/bold] v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False, "--version", "-V", help="Show version and exit", callback=_version_callback
    ),
    config_file: Optional[Path] = typer.Option(
        None, "--config", "-c", help="Path to config file", exists=True, file_okay=True, dir_okay=False
    ),
    json_output: bool = typer.Option(
        False, "--json", help="Output in JSON format"
    ),
) -> None:
    """
    Production-grade Python CLI application with modern tooling.
    """
    # Store global options in context
    ctx.obj = {
        "config_file": config_file,
        "json_output": json_output,
    }


if __name__ == "__main__":
    app()
