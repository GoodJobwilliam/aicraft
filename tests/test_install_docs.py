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
        ROOT / "products/mcp-code-review/llms-install.md",
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


def test_free_server_docs_do_not_claim_unimplemented_race_detection():
    paths = [
        ROOT / "README.md",
        ROOT / "index.html",
        ROOT / "products/mcp-code-review/README.md",
        ROOT / "products/mcp-code-review/README.zh.md",
    ]

    for path in paths:
        content = path.read_text(encoding="utf-8").casefold()
        assert "race condition analysis" not in content, path
        assert "race analysis" not in content, path
        assert "竞态分析" not in content, path


def test_mcp_metadata_describes_deterministic_local_checks():
    for path in [
        ROOT / "products/mcp-code-review/pyproject.toml",
        ROOT / "products/mcp-code-review/registry/server.json",
        ROOT / "products/mcp-code-review/.well-known/mcp/server-card.json",
    ]:
        content = path.read_text(encoding="utf-8").casefold()
        assert "deterministic" in content or "structured local security-pattern" in content, path
        assert "owasp top 10" not in content, path


def test_public_launch_metadata_matches_implemented_capabilities():
    paths = [ROOT / "LAUNCHGUIDE.md", ROOT / "glama.json", ROOT / "submissions/mcp-marketplace-submission.md", ROOT / "rules/mcp-code-review.mdc"]
    for path in paths:
        content = path.read_text(encoding="utf-8").casefold()
        assert "owasp top 10" not in content, path
        assert "owasp security scanning" not in content, path
    assert "deterministic" in (ROOT / "LAUNCHGUIDE.md").read_text(encoding="utf-8").casefold()


def test_creem_status_does_not_confuse_checkout_setup_with_revenue():
    content = (ROOT / "CREEM_PRODUCTS.md").read_text(encoding="utf-8").casefold()
    assert "尚未建立自动订阅" in content
    assert "确认付款" in content
    assert "mrr" in content


def test_root_readme_exposes_trial_and_team_feedback_paths():
    content = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "https://aicraft.vip/trial.html" in content
    assert "template=trial-feedback.yml" in content
    assert "template=team-trial.yml" in content
    assert "examples/mcp-code-review" in content or "examples/github-actions/mcp-code-review.yml" in content
    assert "TEAM_PILOT_BRIEF.md" in content


def test_ai_agent_install_guide_uses_the_real_console_script():
    content = (ROOT / "products/mcp-code-review/llms-install.md").read_text(encoding="utf-8")
    assert '"--from", "aicraft-code-review", "--with", "mcp<2", "mcp-code-review"' in content
    assert '"--with", "mcp<2", "aicraft-code-review"' not in content


def test_json_output_schema_is_present_and_versioned():
    import json

    schema = json.loads((ROOT / "products/mcp-code-review/schema/review-result.schema.json").read_text(encoding="utf-8"))
    assert schema["$schema"].endswith("draft/2020-12/schema")
    assert schema["properties"]["schema_version"] == {"const": 1}
    assert set(schema["properties"]["verdict"]["enum"]) == {"clean", "conditional_pass", "block"}
    assert schema["required"] == ["schema_version", "findings", "summary", "verdict", "exit_code"]


def test_free_github_actions_starter_is_documented_and_secretless():
    workflow = (ROOT / "products/mcp-code-review/examples/github-actions/mcp-code-review.yml").read_text(encoding="utf-8")
    readme = (ROOT / "products/mcp-code-review/README.md").read_text(encoding="utf-8")
    assert "uvx --from aicraft-code-review==0.1.2 --with \"mcp<2\" mcp-code-review review-diff" in workflow
    assert "actions/checkout@v4" in workflow
    assert "astral-sh/setup-uv@v6" in workflow
    assert "secrets." not in workflow
    assert "Free GitHub Actions starter" in readme


def test_cli_json_output_validates_against_published_schema():
    import json
    import subprocess
    import sys

    product = ROOT / "products/mcp-code-review"
    schema = json.loads((product / "schema/review-result.schema.json").read_text(encoding="utf-8"))
    python = product / ".venv/bin/python"
    result = subprocess.run(
        [str(python), "-m", "mcp_code_review", "review-code", "eval('x')", "--format", "json"],
        cwd=product,
        env={"PYTHONPATH": str(product / "src"), "PATH": str(product / ".venv/bin")},
        capture_output=True,
        text=True,
        check=False,
    )
    payload = json.loads(result.stdout)
    assert payload["schema_version"] == schema["properties"]["schema_version"]["const"]
    assert payload["verdict"] in schema["properties"]["verdict"]["enum"]
    assert payload["exit_code"] in schema["properties"]["exit_code"]["enum"]
    assert set(payload) == set(schema["properties"])
    assert set(payload["summary"]) == {"critical", "high", "medium", "info"}
    assert all(set(finding) == {"severity", "line", "issue", "category", "fix", "check"} for finding in payload["findings"])
    assert result.returncode == payload["exit_code"] == 1


def test_trial_pages_offer_a_low_friction_email_feedback_path():
    english = (ROOT / "trial.html").read_text(encoding="utf-8")
    chinese = (ROOT / "trial.zh.html").read_text(encoding="utf-8")
    assert "mailto:731685147@qq.com?subject=AICraft%20trial%20feedback" in english
    assert "mailto:731685147@qq.com?subject=AICraft%20%E8%AF%95%E7%94%A8%E5%8F%8D%E9%A6%88" in chinese
    assert "run-trial.sh" in (ROOT / "products/mcp-code-review/trial/README.md").read_text(encoding="utf-8")
    workflow_url = "products/mcp-code-review/examples/github-actions/mcp-code-review.yml"
    assert workflow_url in english
    assert workflow_url in chinese


def test_homepage_exposes_a_three_step_mcp_path():
    content = (ROOT / "index.html").read_text(encoding="utf-8")
    assert 'id="mcp-path"' in content
    assert "/trial.html" in content
    assert "/team-updates.html" in content
    zh = (ROOT / "zh.html").read_text(encoding="utf-8")
    assert 'id="mcp-path"' in zh
    assert "/trial.zh.html" in zh
    assert "/team-updates.zh.html" in zh
