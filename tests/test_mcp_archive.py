from pathlib import Path
from zipfile import ZipFile
import json

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
        "trial/run-trial.sh",
    }
    with ZipFile(ARCHIVE) as archive:
        assert set(archive.namelist()) == expected
        for name in expected:
            assert archive.read(name) == (PRODUCT / name).read_bytes()


def test_container_and_mcpb_distribution_metadata_use_current_runtime():
    dockerfile = (PRODUCT / "Dockerfile").read_text(encoding="utf-8")
    assert "pip install --no-cache-dir ." in dockerfile
    assert "aicraft-code-review==0.1.2" not in dockerfile
    assert "a79a6fb" not in dockerfile

    with ZipFile(PRODUCT / "mcp-code-review.mcpb") as archive:
        manifest = json.loads(archive.read("manifest.json"))
        server = archive.read("server/index.js").decode("utf-8")

    assert manifest["version"] == "0.1.2"
    args = manifest["server"]["mcp_config"]["args"]
    assert args == ["--from", "aicraft-code-review", "--with", "mcp<2", "mcp-code-review"]
    assert "--from" in server and "aicraft-code-review" in server
