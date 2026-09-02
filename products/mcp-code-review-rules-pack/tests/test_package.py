"""Keep the paid ZIP deliverable synchronized with its source files."""

from pathlib import Path
from zipfile import ZipFile
import re

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


def test_pack_contains_the_advertised_63_rules():
    counts = {
        path.name: len(re.findall(r"^  - name:", path.read_text(encoding="utf-8"), re.MULTILINE))
        for path in (ROOT / "rules").glob("*.yaml")
    }
    assert counts == {
        "python.yaml": 21,
        "javascript.yaml": 16,
        "go.yaml": 13,
        "java.yaml": 13,
    }
    assert sum(counts.values()) == 63


def test_github_template_can_comment_on_pull_requests():
    template = (ROOT / "ci/github-actions.yml").read_text(encoding="utf-8")
    assert "contents: read" in template
    assert "issues: write" in template
    assert "pull-requests: read" in template
    assert "outputs:" in template
    assert "exit_code: ${{ steps.review.outputs.exit_code }}" in template
    assert "if: steps.review.outputs.exit_code == '2'" in template
    assert "issues.createComment" in template
    assert "github.event.pull_request.head.repo.full_name == github.repository" in template
    assert "actions/upload-artifact@v4" in template
    assert "name: mcp-code-review-report" in template
    review_job = template.split("  comment:", 1)[0]
    assert "issues: write" not in review_job
