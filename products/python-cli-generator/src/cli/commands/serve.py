"""
Development server command — demonstrates long-running process with Rich live display.
"""
import time
import random
from typing import Optional

import typer
from rich.live import Live
from rich.table import Table
from rich.panel import Panel


def serve(
    host: str = typer.Option("127.0.0.1", "--host", "-h", help="Bind address"),
    port: int = typer.Option(8080, "--port", "-p", help="Listen port"),
    workers: int = typer.Option(1, "--workers", "-w", help="Number of workers"),
) -> None:
    """
    Start a development server (simulated).
    """
    typer.echo(f"Starting server on {host}:{port} with {workers} worker(s)...")
    typer.echo("Press Ctrl+C to stop.")

    try:
        with Live(refresh_per_second=4, screen=True) as live:
            start = time.time()
            while True:
                elapsed = int(time.time() - start)
                req_count = random.randint(100, 500)
                avg_latency = round(random.uniform(12, 45), 1)

                table = Table(title=f"Server Status — {host}:{port}")
                table.add_column("Metric", style="cyan")
                table.add_column("Value", style="green")

                table.add_row("Uptime", f"{elapsed // 60}m {elapsed % 60}s")
                table.add_row("Workers", str(workers))
                table.add_row("Requests (sim)", f"{req_count}")
                table.add_row("Avg Latency", f"{avg_latency}ms")

                live.update(table)
                time.sleep(0.25)
    except KeyboardInterrupt:
        typer.echo("\nServer stopped.")
