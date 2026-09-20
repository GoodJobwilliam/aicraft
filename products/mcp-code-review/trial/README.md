# MCP Code Review: 10-minute team trial

This free, local trial lets a small team test shared review rules before discussing the paid Team Rules Pack or Team Updates. No source code leaves the machine, and no payment is created by running these commands.

After the review, a locally built package can print the machine-readable contract with `mcp-code-review schema`. This becomes part of the public installed package after the next PyPI release; the current public `0.1.2` release does not include it yet.

## 1. Install

```bash
uvx --from aicraft-code-review --with "mcp<2" mcp-code-review review-file sample.py
```

If you already use an environment with the package installed, run the same review command directly:

```bash
pip install "aicraft-code-review==0.1.2" "mcp<2"
mcp-code-review review-file sample.py
```

## 2. Run the sample

From this directory, run the bundled launcher (it uses the same isolated path and falls back to a temporary Python install):

```bash
./run-trial.sh
```

The launcher uses uvx when available; otherwise it installs the pinned public package into a temporary directory and removes that directory on exit.
After the result, it prints the three feedback questions and a copyable GitHub feedback link. The launcher's exit code remains the review exit code (`1` for this sample).

The adjacent `.mcp-code-review.json` is discovered automatically. You should see a high-severity command-injection finding and a medium-severity team-convention finding. The non-zero exit code is suitable for a merge gate.

## 3. Try your own file

Copy `.mcp-code-review.json` to a test repository, adjust the `custom_rules` pattern and message, then run:

```bash
mcp-code-review review-file path/to/file.py
```

For a shared path that every teammate uses, set `MCP_CODE_REVIEW_CONFIG` to the committed JSON file. The same profile works from Claude Code, Cursor, Cline, or the CLI.

## 4. Decide whether there is a team problem

After one review, ask:

- Did the team catch a real issue before merge?
- Which rule should be shared across repositories?
- Which finding was noisy or missing?
- Would monthly rule drops, CI workflow refreshes, or rollout help save review time?

If the answer points to an ongoing team need, share the outcome in the [structured trial feedback form](https://github.com/GoodJobwilliam/aicraft/issues/new?template=trial-feedback.yml&title=Trial%20feedback), or use the [free team trial request form](https://github.com/GoodJobwilliam/aicraft/issues/new?template=team-trial.yml&title=Team%20trial%20request) for a guided team test. Include the team size, languages, workflow, and pain. Do not include source code or secrets.

The optional **Team Rules Pack** is a one-time `$49` add-on with [secure checkout via Creem](mailto:731685147@qq.com?subject=AICraft%20Team%20Rules%20Pack%20checkout%20request&body=Team%20size%3A%20%5B%5D%0AMain%20languages%3A%20%5B%5D%0ACurrent%20review%20workflow%3A%20%5B%5D%0AWhat%20you%20need%20from%20the%20pack%3A%20%5B%5D). **Team Updates Starter** is `$19/month` or `$190/year` for up to 3 engineers; **Team Pilot** is `$99/month` or `$990/year` for up to 10 engineers with CI and tuning support. Scope and launch date are confirmed before charging.