from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
PRODUCT = ROOT / "products/mcp-code-review"
ARCHIVE = ROOT / "products/mcp-code-review.zip"


def test_free_server_archive_contains_current_tracked_runtime_files():
    expected = {
        "README.md",
        "README.zh.md",
        "CHANGELOG.md",
        "LICENSE",
        "Dockerfile",
        "LAUNCHGUIDE.md",
        "llms-install.md",
        "pyproject.toml",
        "smithery.yaml",
        "registry/server.json",
        ".well-known/mcp/server-card.json",
        "uv.lock",
        "src/mcp_code_review/__init__.py",
        "src/mcp_code_review/__main__.py",
        "src/mcp_code_review/cli.py",
        "src/mcp_code_review/config.py",
        "src/mcp_code_review/reviewer.py",
        "src/mcp_code_review/server.py",
        "tests/test_cli.py",
        "tests/test_config.py",
        "tests/test_reviewer.py",
        "tests/test_server.py",
        "trial/.mcp-code-review.json",
        "trial/README.md",
        "trial/README.zh.md",
        "trial/sample.py",
        "trial/trial-config.json",
    }
    with ZipFile(ARCHIVE) as archive:
        assert set(archive.namelist()) == expected
        for name in expected:
            assert archive.read(name) == (PRODUCT / name).read_bytes()
