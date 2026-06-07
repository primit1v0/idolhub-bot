# Contributing

Read [Current Baseline](BASELINE.md) before changing behavior.

## Repository Rules

- `config.example.json` is the only tracked configuration template.
- Never commit `config.json`, secrets, databases, logs, or workspace output.
- Do not reintroduce global phase numbering into active docs.
- Historical specs and plans must retain their status banners.
- Use existing PocketFlow, loader, and registry patterns.
- Avoid new dependencies when stdlib or an existing dependency is sufficient.

## Setup

```bash
cp config.example.json config.json
uv sync --extra vector
```

Export only variables referenced by local `config.json`.

## Quality Gates

```bash
uv run pytest
uv run ruff check . --select F,I
```

The repository currently has full-repo Ruff formatting debt; `ruff format
--check .` reports the existing files that need a dedicated formatting-only
change. Do not mix that mechanical rewrite into feature or documentation work.

Security tools are installed under `.audit-tools/bin/` in the maintained local
environment:

```bash
.audit-tools/bin/bandit -r core memory tools api mcp_server
.audit-tools/bin/semgrep --config auto core memory tools api mcp_server
.audit-tools/bin/pip-audit -r requirements.txt
```

## Dependencies

Before adding a dependency:

1. Check stdlib and existing dependencies.
2. Document the reason in `docs/DEPENDENCIES.md`.
3. Put optional capabilities behind an extra.
4. Update `uv.lock`.
5. Run tests and dependency audit.

Use `uv add`, not direct `pip install`, for project dependencies.

## Extension Changes

| Type | Required changes |
|---|---|
| Skill | Add Markdown file with valid YAML frontmatter and tests |
| Plugin | Add plugin class under configured directory and tests |
| Tool | Add function, `TOOLS_SCHEMA`, `TOOLS_MAPPING`, and tests |
| Provider layout | Update `core/llm.py`, config docs/template, and tests |

Tools are not auto-discovered from `tools.dir`.

## Commits And Publishing

Use concise conventional prefixes: `feat`, `fix`, `refactor`, `docs`, `chore`,
or `test`.

The maintained workflow is:

1. verify;
2. commit scoped files;
3. authenticate Git operations with `gh auth setup-git`;
4. push without force unless an explicitly approved history rewrite requires
   `--force-with-lease`.
