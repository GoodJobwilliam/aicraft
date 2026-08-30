"""Keep the paid ZIP deliverable synchronized with its source files."""

from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "mcp-code-review-rules-pack.zip"
EXPECTED_FILES = (
    "README.md",
    "llm-prompts.md",
    "ci/github-actions.yml",
    "ci/gitlab-ci.yml",
    "rules/python.yaml",
    "rules/javascript.yaml",
    "rules/go.yaml",
    "rules/java.yaml",
)


def test_archive_contains_current_pack_files():
    with ZipFile(ARCHIVE) as archive:
        names = set(archive.namelist())
        assert names == set(EXPECTED_FILES)
        for name in EXPECTED_FILES:
            assert archive.read(name) == (ROOT / name).read_bytes()


def test_gitlab_template_persists_report_and_propagates_exit_code():
    template = (ROOT / "ci/gitlab-ci.yml").read_text(encoding="utf-8")
    assert " > review-report.txt" in template
    assert "cat review-report.txt" in template
    assert 'exit "$EXIT"' in template
    assert "when: always" in template
