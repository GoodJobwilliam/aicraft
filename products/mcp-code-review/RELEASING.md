# Releasing MCP Code Review

The public PyPI package is currently '0.1.2'. The repository may contain a
source change that is not in that release; do not describe it as available on
PyPI until the release workflow has completed and the public package metadata
has been checked.

## No-cost release path

1. Run 'uv sync --extra dev', 'uv run ruff check src/ tests/', and
   'uv run pytest tests/ -q' from this directory.
2. Update 'version' in 'pyproject.toml', 'uv.lock', the changelog, and public
   install examples in one reviewed change. Keep the JSON schema version
   compatible unless the output contract itself changes.
3. Create and push a tag named 'aicraft-code-review-vX.Y.Z' after the commit
   is reviewed. A tag is the explicit release approval; ordinary pushes do not
   publish anything.
4. The 'Release MCP Code Review' workflow rebuilds the wheel and source
   distribution, checks that the CLI and JSON schema are included, reruns the
   tests, and publishes through PyPI Trusted Publishing. No long-lived PyPI
   token is stored in the repository or workflow.
5. Verify the public PyPI JSON endpoint, the install command in a clean
   environment, and the Official MCP Registry version before updating website
   copy. A successful GitHub run alone is not evidence that a package is
   publicly installable.

The workflow is intentionally manual at the final approval boundary. It does
not create a release, change a tag, or publish a package on its own.
