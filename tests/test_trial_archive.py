from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
TRIAL = ROOT / "products/mcp-code-review/trial"
ARCHIVE = ROOT / "products/mcp-code-review-trial.zip"
EXPECTED = (
    "README.md",
    "README.zh.md",
    "sample.py",
    ".mcp-code-review.json",
    "trial-config.json",
    "run-trial.sh",
)


def test_standalone_trial_archive_matches_trial_files():
    with ZipFile(ARCHIVE) as archive:
        assert set(archive.namelist()) == set(EXPECTED)
        for name in EXPECTED:
            assert archive.read(name) == (TRIAL / name).read_bytes()


def test_trial_pages_link_to_standalone_archive():
    for name in ("trial.html", "trial.zh.html"):
        content = (ROOT / name).read_text(encoding="utf-8")
        assert "/products/mcp-code-review-trial.zip" in content


def test_trial_launcher_is_a_transparent_uvx_wrapper():
    launcher = (TRIAL / "run-trial.sh").read_text(encoding="utf-8")
    assert "uvx --from aicraft-code-review --with 'mcp<2' mcp-code-review review-file sample.py" in launcher
    assert "exit 2" in launcher
