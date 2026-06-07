# Configuration Reference

`config.example.json` is the tracked template. Runtime reads local
`config.json`, which is ignored by Git.

```bash
cp config.example.json config.json
```

## Resolution Rules

1. JSON keys beginning with `_` are documentation metadata and are removed.
2. Every `$VARIABLE` in the remaining JSON is resolved from `os.environ`.
3. Missing variables fail startup with `KeyError`.
4. The resolved document is validated by `AppConfig`.

Resolution is recursive and does not skip inactive providers. Keep only
configured provider blocks in local `config.json`, or define every referenced
variable.

## Secrets

No dotenv loader is used. Export variables in the shell or inject them with a
service manager:

```bash
export TELEGRAM_BOT_TOKEN="..."
export GEMINI_API_KEY="..."
```

Environment files must remain outside the repository.

## Schema

### `app`

| Key | Default | Runtime status |
|---|---:|---|
| `name` | `idolhub` | Used for MCP server name |
| `mode` | `bot` | Used when CLI mode is omitted |
| `debug` | `false` | Accepted, not currently enforced |
| `timezone` | `Asia/Jakarta` | Accepted, not currently enforced |

### `agent`

| Key | Default | Runtime status |
|---|---:|---|
| `system_prompt` | required | Injected into every LLM request |
| `max_iterations` | `10` | Enforced |
| `tools_enabled` | `true` | Enforced |
| `memory_enabled` | `true` | Accepted, not currently enforced |
| `filter_enabled` | `true` | Enforced |
| `gating_enabled` | `true` | Enforced |

### `telegram`

| Key | Default | Runtime status |
|---|---:|---|
| `token` | required | Enforced |
| `allowed_users` | `[]` | Enforced; empty allows all users |
| `parse_mode` | `Markdown` | Enforced |

### `llm`

| Key | Default | Runtime status |
|---|---:|---|
| `provider` | `openai` | Selects `providers[provider]` |
| `model` | `gpt-4o` | Enforced |
| `temperature` | `0.7` | Enforced |
| `max_tokens` | `4096` | Enforced |
| `timeout` | `30` | Enforced |

Supported credential layouts:

| Provider | Credential field |
|---|---|
| `gemini` or other generic OpenAI-compatible provider | `api_key` |
| `openai` | `api_key` |
| `openai_codex` | `oauth_token` |
| `github_copilot` | `cli_token` |

Each provider requires `base_url`.

### `memory.short_term`

| Key | Default | Runtime status |
|---|---:|---|
| `backend` | `sqlite` | Only supported value |
| `path` | `./data/memory.db` | Enforced |
| `max_messages` | `50` | Active context limit |
| `fts_context_window` | `2` | Adjacent messages around FTS matches |
| `auto_prune_enabled` | `true` | Enforced |
| `auto_prune_limit` | `1000` | Per-user stored-message limit |

### `memory.long_term`

| Key | Default | Runtime status |
|---|---:|---|
| `backend` | `none` | `none` or `sqlite_vec` |
| `path` | `./data/vectors.db` | Enforced for sqlite-vec |
| `embedding_model` | `text-embedding-3-small` | Enforced |

For sqlite-vec:

```bash
uv sync --extra vector
```

If the extra is missing, startup fails before opening database connections.
Embedding failures do not interrupt short-term message storage and are logged.

### Extension Systems

| Section | Active keys | Accepted but not enforced |
|---|---|---|
| `skills` | `dir`, `enabled` | none |
| `tools` | `enabled` | `dir` |
| `plugins` | `dir` | `enabled` |

An empty `skills.enabled` or `tools.enabled` list enables all registered
entries.

### `api`

| Key | Runtime status |
|---|---|
| `host`, `port`, `cors_origins` | Enforced |
| `enabled` | Accepted, not currently enforced |

### `mcp`

`enabled` and `port` are accepted but not currently enforced. MCP starts only
when mode `mcp` is selected and uses stdio transport.

### `logging`

`level` and `format` are used by `main.py`. Supported formats are `text` and
the built-in simplified JSON format.

## Provider Examples

Keep one configured provider block unless all referenced environment variables
are available.

### OpenAI

```json
{
  "llm": {"provider": "openai", "model": "gpt-4o"},
  "providers": {
    "openai": {
      "base_url": "https://api.openai.com/v1",
      "api_key": "$OPENAI_API_KEY"
    }
  }
}
```

### OpenAI-compatible local endpoint

```json
{
  "llm": {"provider": "openai", "model": "llama3.2"},
  "providers": {
    "openai": {
      "base_url": "http://localhost:11434/v1",
      "api_key": "local"
    }
  }
}
```

### OpenAI Codex credential layout

```json
{
  "llm": {"provider": "openai_codex", "model": "gpt-4"},
  "providers": {
    "openai_codex": {
      "base_url": "https://api.openai.com/v1",
      "oauth_token": "$OPENAI_CODEX_TOKEN"
    }
  }
}
```
