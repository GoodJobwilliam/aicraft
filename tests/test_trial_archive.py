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
        assert "./run-trial.sh" in content


def test_trial_page_primary_actions_download_the_standalone_bundle():
    english = (ROOT / "trial.html").read_text(encoding="utf-8")
    chinese = (ROOT / "trial.zh.html").read_text(encoding="utf-8")
    assert '<a class="button primary" href="/products/mcp-code-review-trial.zip">Download the trial bundle</a>' in english
    assert '<a class="button primary" href="/products/mcp-code-review-trial.zip">下载试用包</a>' in chinese


def test_trial_pages_use_a_directly_executable_first_review_command():
    english = (ROOT / "trial.html").read_text(encoding="utf-8")
    chinese = (ROOT / "trial.zh.html").read_text(encoding="utf-8")
    command = "uvx --from aicraft-code-review --with \"mcp&lt;2\" mcp-code-review review-file sample.py"
    assert command in english
    assert command in chinese
    assert english.count("Try your own rule") == 1
    assert chinese.count("试试自己的规则") == 1
    assert "Complete that file download first" in english
    assert "先完成文件下载" in chinese
    assert "curl -fsSLO https://aicraft.vip/products/mcp-code-review-trial.zip" in english
    assert "curl -fsSLO https://aicraft.vip/products/mcp-code-review-trial.zip" in chinese


def test_trial_pages_put_file_setup_before_sample_execution():
    english = (ROOT / "trial.html").read_text(encoding="utf-8")
    chinese = (ROOT / "trial.zh.html").read_text(encoding="utf-8")
    assert english.index("Download the trial files") < english.index("Run the sample review")
    assert chinese.index("下载试用文件") < chinese.index("运行示例审查")


def test_trial_launcher_prefers_uvx_and_has_a_python_fallback():
    launcher = (TRIAL / "run-trial.sh").read_text(encoding="utf-8")
    assert "uvx --from aicraft-code-review --with 'mcp<2' mcp-code-review review-file sample.py" in launcher
    assert "script_dir=$(CDPATH= cd -- \"$(dirname -- \"$0\")\" && pwd)" in launcher
    assert "python3 -m pip install" in launcher
    assert "--target" in launcher
    assert '"aicraft-code-review==0.1.2" "mcp<2"' in launcher
    assert "PYTHONPATH=" in launcher
    assert "trap cleanup EXIT INT TERM" in launcher
    assert "exit 2" in launcher
