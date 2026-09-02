from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_public_install_docs_use_the_pypi_package_and_console_script_names():
    """Keep public onboarding aligned with the executable exposed by PyPI."""
    required_command = "uvx --from aicraft-code-review --with"
    stale_command = 'uvx --with "mcp<2" aicraft-code-review'
    paths = [
        ROOT / "products/mcp-code-review/README.md",
        ROOT / "products/mcp-code-review/README.zh.md",
        ROOT / "products/mcp-code-review/trial/README.md",
        ROOT / "products/mcp-code-review/trial/README.zh.md",
        ROOT / "trial.html",
        ROOT / "trial.zh.html",
        ROOT / "index.html",
        ROOT / "zh.html",
    ]

    for path in paths:
        content = path.read_text(encoding="utf-8")
        assert required_command in content, path
        assert "mcp-code-review" in content, path
        assert stale_command not in content, path
