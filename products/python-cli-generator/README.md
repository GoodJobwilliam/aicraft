# Python CLI Starter Template

A production-ready Python CLI project scaffold with modern tooling.

## Features

- **Typer** (modern Click) for CLI argument parsing with auto-generated help
- **Rich** for beautiful terminal output (tables, progress bars, panels, markdown)
- **Pydantic v2** for configuration management
- **structlog** for structured logging with JSON output
- **httpx** for async HTTP requests
- **pytest** with coverage, mocking, and fixtures
- **Ruff** for linting and formatting
- **GitHub Actions** CI/CD pipeline
- **Makefile** for common development tasks

## Quick Start

```bash
# Create project from template
cookiecutter https://github.com/GoodJobwilliam/python-cli-starter
# Or copy and rename the template manually

# Install dependencies
make install

# Run the CLI
python -m cli hello --name World

# Run tests
make test
```

## Project Structure

```
src/
├── cli/
│   ├── __init__.py
│   ├── main.py          # CLI entry point
│   └── commands/
│       ├── hello.py      # Example command
│       ├── config.py     # Config management command
│       └── serve.py      # Long-running process example
├── core/
│   ├── __init__.py
│   ├── config.py         # Pydantic settings
│   ├── logger.py         # Structured logging setup
│   └── client.py         # HTTP client wrapper
tests/
├── conftest.py           # Fixtures
├── test_hello.py
└── test_config.py
config/
├── default.yaml          # Default configuration
└── schema.yaml           # Config validation schema
```

## Usage

```bash
# Show help
cli --help
cli hello --help

# Run with options
cli hello --name Alice --count 3 --formal

# Use configuration file
cli --config config/prod.yaml hello

# Output as JSON
cli --json hello

# Run development server
cli serve --port 8080

# Show version
cli --version
```

## Development

```bash
make install      # Install dependencies
make dev          # Install with dev dependencies
make test         # Run tests
make lint         # Run linter
make format       # Format code
make clean        # Clean build artifacts
```

## Tech Stack

- Python 3.11+
- [Typer](https://typer.tiangolo.com/)
- [Rich](https://rich.readthedocs.io/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [structlog](https://www.structlog.org/)
- [httpx](https://www.python-httpx.org/)
- [pytest](https://docs.pytest.org/)
- [Ruff](https://docs.astral.sh/ruff/)
