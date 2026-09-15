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


def test_public_mcp_copy_does_not_overstate_owasp_coverage():
    for path in [
        ROOT / "index.html",
        ROOT / "SOCIAL_MEDIA.md",
        ROOT / "README.md",
        ROOT / "blog/index.html",
        ROOT / "blog/distribution-playbook.html",
    ]:
        content = path.read_text(encoding="utf-8").casefold()
        assert "owasp security scanning" not in content
        assert "owasp top 10" not in content
    assert "deterministic security-pattern checks" in (ROOT / "index.html").read_text(encoding="utf-8").casefold()
    assert "deterministic local security-pattern checks" in (ROOT / "SOCIAL_MEDIA.md").read_text(encoding="utf-8").casefold()


def test_creem_status_does_not_confuse_checkout_setup_with_revenue():
    content = (ROOT / "CREEM_PRODUCTS.md").read_text(encoding="utf-8").casefold()
    assert "尚未建立自动订阅" in content
    assert "确认付款" in content
    assert "mrr" in content


def test_chinese_product_offer_matches_team_rules_pack_scope():
    content = (ROOT / "products/mcp-code-review/README.zh.md").read_text(encoding="utf-8")
    assert "一次性 $49 的 Team Rules Pack" in content
    assert "终身授权" not in content
    assert "邮件支持" not in content
    assert "免费服务器仍按 MIT 协议提供" in content


def test_root_readme_exposes_trial_and_team_feedback_paths():
    content = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "https://aicraft.vip/trial.html" in content
    assert "template=trial-feedback.yml" in content
    assert "template=team-trial.yml" in content
    assert "examples/mcp-code-review" in content or "examples/github-actions/mcp-code-review.yml" in content
    assert "TEAM_PILOT_BRIEF.md" in content
    assert "releases/tag/mcp-code-review-0.1.2" in content
    assert "scripts/distribution_report.py" in content


def test_team_trial_forms_capture_an_explicit_offer_tier():
    for path in [
        ROOT / ".github/ISSUE_TEMPLATE/team-trial.yml",
        ROOT / ".github/ISSUE_TEMPLATE/team-trial-zh.yml",
    ]:
        content = path.read_text(encoding="utf-8")
        assert "id: offer-tier" in content
        assert "Scope not clear yet" in content or "还不清楚具体范围" in content
        assert "This records interest only" in content or "这里只记录意向" in content


def test_trial_feedback_forms_capture_decision_role():
    for path in [
        ROOT / ".github/ISSUE_TEMPLATE/trial-feedback.yml",
        ROOT / ".github/ISSUE_TEMPLATE/trial-feedback-zh.yml",
    ]:
        content = path.read_text(encoding="utf-8")
        assert "id: decision-role" in content
        assert "decision maker" in content or "决策者" in content


def test_trial_forms_capture_target_start_month():
    for path in [ROOT / ".github/ISSUE_TEMPLATE/team-trial.yml", ROOT / ".github/ISSUE_TEMPLATE/team-trial-zh.yml"]:
        content = path.read_text(encoding="utf-8")
        assert "id: target-start-month" in content
        assert "YYYY-MM" in content
        marker = content.index("id: target-start-month")
        assert "required: true" in content[marker : marker + 500]


def test_trial_feedback_keeps_core_observations_required_but_qualification_optional():
    for path in [ROOT / ".github/ISSUE_TEMPLATE/trial-feedback.yml", ROOT / ".github/ISSUE_TEMPLATE/trial-feedback-zh.yml"]:
        content = path.read_text(encoding="utf-8")
        for marker in ["id: caught", "id: shared-rule", "id: noisy"]:
            start = content.index(marker)
            assert "required: true" in content[start : start + 500]
        for marker in ["id: offer-tier", "id: decision-window", "id: decision-role", "id: target-start-month", "id: precommitment"]:
            start = content.index(marker)
            next_field = content.find("\n  - type:", start)
            section = content[start : next_field if next_field != -1 else len(content)]
            assert "可选" in section or "Optional" in section
            assert "required: true" not in section


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


def test_release_workflow_is_tagged_trusted_and_validates_artifacts():
    workflow = (ROOT / ".github/workflows/mcp-code-review-release.yml").read_text(encoding="utf-8")
    releasing = (ROOT / "products/mcp-code-review/RELEASING.md").read_text(encoding="utf-8")
    assert '"aicraft-code-review-v*"' in workflow
    assert "id-token: write" in workflow
    assert "uv build --clear --out-dir dist-release" in workflow
    assert "uv publish dist-release/* --trusted-publishing always" in workflow
    assert "schema/review-result.schema.json" in workflow
    assert 'if path.suffix in {".whl", ".gz"}' in workflow
    assert "uv sync --extra dev --extra yaml" in workflow
    assert "uv sync --extra dev --extra yaml" in releasing
    assert "long-lived PyPI" in releasing
    assert "0.1.2" in releasing


def test_published_package_contains_the_json_schema():
    import zipfile
    import subprocess
    import tempfile

    product = ROOT / "products/mcp-code-review"
    with tempfile.TemporaryDirectory() as temp_dir:
        output = Path(temp_dir)
        subprocess.run(["uv", "build", "--clear", "--wheel", "--out-dir", str(output)], cwd=product, check=True, capture_output=True, text=True)
        wheel = next(output.glob("*.whl"))
        with zipfile.ZipFile(wheel) as archive:
            packaged = archive.read("mcp_code_review/schema/review-result.schema.json")
    assert packaged == (product / "schema/review-result.schema.json").read_bytes()


def test_schema_command_is_documented_for_installed_consumers():
    english = (ROOT / "products/mcp-code-review/README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "products/mcp-code-review/README.zh.md").read_text(encoding="utf-8")
    assert "next PyPI release" in english
    assert "下一版 PyPI 发布后" in chinese
    assert "当前公开的 `0.1.2` 尚未包含它" in (ROOT / "products/mcp-code-review/trial/README.zh.md").read_text(encoding="utf-8")


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
    assert "team%20trial%20qualification" in english
    assert "%E5%9B%A2%E9%98%9F%E8%AF%95%E7%94%A8%E8%B5%84%E6%A0%BC" in chinese
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
    release = "releases/tag/mcp-code-review-0.1.2"
    assert release in content
    assert release in zh


def test_team_updates_email_path_captures_qualification_fields():
    english = (ROOT / "team-updates.html").read_text(encoding="utf-8")
    chinese = (ROOT / "team-updates.zh.html").read_text(encoding="utf-8")
    for field in ("Offer%20tier%20to%20validate", "Decision%20role", "Decision%20timing", "Target%20start%20month", "Conditional%20start%20commitment"):
        assert field in english
    for field in ("%E8%A6%81%E9%AA%8C%E8%AF%81%E7%9A%84%E5%A2%9E%E5%80%BC%E6%A1%A3%E4%BD%8D", "%E5%86%B3%E7%AD%96%E8%A7%92%E8%89%B2", "%E5%86%B3%E7%AD%96%E6%97%B6%E9%97%B4", "%E7%9B%AE%E6%A0%87%E5%BC%80%E5%A7%8B%E6%9C%88%E4%BB%BD", "%E6%9C%89%E6%9D%A1%E4%BB%B6%E7%9A%84%E5%BC%80%E5%A7%8B%E6%89%BF%E8%AF%BA"):
        assert field in chinese


def test_trial_email_paths_capture_offer_and_decision_fields():
    english = (ROOT / "trial.html").read_text(encoding="utf-8")
    chinese = (ROOT / "trial.zh.html").read_text(encoding="utf-8")
    for field in ("Offer%20tier%20to%20validate", "Decision%20role", "Decision%20timing", "Target%20start%20month", "Conditional%20start%20commitment"):
        assert field in english
    for field in ("%E8%A6%81%E9%AA%8C%E8%AF%81%E7%9A%84%E5%A2%9E%E5%80%BC%E6%A1%A3%E4%BD%8D", "%E5%86%B3%E7%AD%96%E8%A7%92%E8%89%B2", "%E5%86%B3%E7%AD%96%E6%97%B6%E9%97%B4", "%E7%9B%AE%E6%A0%87%E5%BC%80%E5%A7%8B%E6%9C%88%E4%BB%BD", "%E6%9C%89%E6%9D%A1%E4%BB%B6%E7%9A%84%E5%BC%80%E5%A7%8B%E6%89%BF%E8%AF%BA"):
        assert field in chinese
    release = "https://github.com/GoodJobwilliam/aicraft/releases/tag/mcp-code-review-0.1.2"
    assert release in english
    assert release in chinese
