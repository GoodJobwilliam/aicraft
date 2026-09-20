# MCP Code Review — Team Rules Pack

The free, MIT-licensed [`aicraft-code-review`](https://github.com/GoodJobwilliam/aicraft/tree/main/products/mcp-code-review) server lets every team create and commit its own local rule profile. This directory intentionally contains only a small, runnable preview.

## Try the preview

Copy [`preview/python.yaml`](./preview/python.yaml) to a test repository as `.mcp-code-review.yaml`, then run the free server:

```bash
pip install "aicraft-code-review==0.1.2" "mcp<2"
cp preview/python.yaml /path/to/repository/.mcp-code-review.yaml
mcp-code-review review-file /path/to/repository/example.py
```

The preview demonstrates the configuration shape and representative policy checks; it is not the full Team Rules Pack.

## Team Rules Pack — $49, one-time

The paid delivery contains the complete, versioned set of 63 security, correctness, and team-policy rules for Python, JavaScript/TypeScript, Go, and Java; GitHub Actions and GitLab CI merge-gate templates; and 20 prompts for semantic review. It also includes lifetime updates for that pack version.

First [request a current secure Creem checkout link](mailto:731685147@qq.com?subject=AICraft%20Team%20Rules%20Pack%20checkout%20request&body=Team%20size%3A%20%5B%5D%0AMain%20languages%3A%20%5B%5D%0ACurrent%20review%20workflow%3A%20%5B%5D%0AWhat%20you%20need%20from%20the%20pack%3A%20%5B%5D). After checkout, email the non-secret receipt or order reference to [731685147@qq.com](mailto:731685147@qq.com?subject=AICraft%20Team%20Rules%20Pack%20delivery) for manual delivery. Do not send source code, credentials, or secrets.

For a team that needs a shared profile, CI setup review, and ongoing tuning rather than a one-time package, start with a [free Team Trial request](https://github.com/GoodJobwilliam/aicraft/issues/new?template=team-trial.yml&title=Team%20trial%20request). Scope and start date are confirmed before any Team Updates charge.

## License

The preview is provided for evaluation with the free server. A purchased Team Rules Pack may be used by the purchasing team in any number of its projects, including commercial projects; redistribution or resale of the full pack is not permitted.
