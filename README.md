# idolhub

Lightweight personal assistant built with PocketFlow, Telegram, FastAPI, and MCP. The project favors small dependencies, explicit configuration, and local SQLite storage with enterprise-grade security hardening.

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://python.org)
[![uv](https://img.shields.io/badge/package%20manager-uv-purple)](https://docs.astral.sh/uv/)
[![PocketFlow](https://img.shields.io/badge/framework-PocketFlow-orange)](https://github.com/The-Pocket/PocketFlow)
[![Tests](https://img.shields.io/badge/tests-113%2F113%20passing-brightgreen)](tests/)
[![Security](https://img.shields.io/badge/security-Phase%201%20Complete-success)](AUDIT_FINDINGS.md)

## 🎯 Current Status

**Phase 1 Complete**: Configuration Hardening ✅
- **113/113 tests passing** (100% pass rate)
- Pydantic-based configuration validation
- Single source of truth: `config.json`
- Zero tolerance for validation errors
- Hot-reload capability for config changes

### Core Features
- **Multi-mode operation**: Telegram bot, REST API, and MCP stdio
- **Provider flexibility**: OpenAI-compatible provider selection
- **Extensibility**: Tool, skill, and plugin extension points
- **Memory stack**: SQLite history, EAV facts/preferences, FTS5 threading, auto-pruning
- **Semantic memory**: Optional sqlite-vec for vector search
- **Context fusion**: RRF across facts, FTS5, and semantic results
- **Security**: Prompt-injection filtering, memory-write gating, bubblewrap sandboxing

See [PHASE1_COMPLETION.md](PHASE1_COMPLETION.md) for detailed completion report and [AUDIT_FINDINGS.md](AUDIT_FINDINGS.md) for comprehensive security audit.

## 🔒 Security & Configuration

### Configuration Policy

`config.example.json` is tracked. `config.json` is local-only and ignored by Git.

```bash
cp config.example.json config.json
```

**Key Security Features**:
- ✅ Pydantic validation for all configuration sections
- ✅ Environment variable resolution (`$VARIABLE` syntax)
- ✅ Telegram token format validation (bot_id:token)
- ✅ Provider URL validation (HTTPS required)
- ✅ Secret masking in API responses
- ✅ Hot-reload with validation
- ✅ Secrets overwrite protection

Edit local `config.json` to select one provider. Secrets remain outside the repository and are supplied through environment variables. Every `$VARIABLE` left in local `config.json` must exist in the environment.

**Never commit**:
- `config.json`
- `.env` or other secret files
- `data/` databases
- logs
- `workspace/` contents

## 🚀 Quick Start

```bash
git clone https://github.com/primit1v0/idolhub-bot.git
cd idolhub-bot

# Copy and configure
cp config.example.json config.json

# Install dependencies
uv sync

# Set environment variables
export TELEGRAM_BOT_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
export OPENAI_API_KEY="sk-..."

# Run in bot mode
uv run python main.py bot
```

Install the optional vector extension when local semantic memory is enabled:

```bash
uv sync --extra vector
```

Then set `memory.long_term.backend` to `sqlite_vec` in local `config.json`.

## 🎮 Modes

```bash
uv run python main.py bot   # Telegram bot mode
uv run python main.py api   # REST API mode
uv run python main.py mcp   # MCP stdio mode
```

CLI mode overrides `app.mode`. MCP currently uses stdio transport; `mcp.port` is not used.

## 📁 Project Structure

```text
idolhub/
├── main.py                          # Entry point
├── config.example.json              # Configuration template
├── pyproject.toml                   # Project dependencies
├── PHASE1_COMPLETION.md             # Phase 1 completion report
├── AUDIT_FINDINGS.md                # Security audit findings
├── core/
│   ├── agent.py                     # Main agent orchestration
│   ├── bot.py                       # Telegram bot implementation
│   ├── config.py                    # Config loader (backward compat)
│   ├── config_schema.py             # Pydantic models ✨ NEW
│   ├── config_validator.py          # Validation logic ✨ NEW
│   ├── config_reloader.py           # Hot-reload capability ✨ NEW
│   ├── event_bus.py                 # Event system
│   ├── llm.py                       # LLM client factory
│   └── rag_filter.py                # RAG filtering
├── memory/
│   ├── memory_gate.py               # Memory write gating
│   └── sqlite_store.py              # SQLite + FTS5 + vector
├── api/
│   ├── server.py                    # FastAPI application
│   └── routes/
│       ├── chat.py                  # Chat endpoint
│       ├── config.py                # Config management API
│       └── health.py                # Health checks
├── mcp_server/
│   └── server.py                    # MCP stdio server
├── skills/
│   └── loader.py                    # Skill discovery
├── plugins/
│   └── loader.py                    # Plugin system
├── tools/
│   ├── heartbeat.py                 # Heartbeat tool
│   ├── registry.py                  # Tool registry
│   └── sandbox.py                   # Sandboxed execution
├── scripts/                         # Automation scripts ✨ NEW
│   ├── install_audit_tools.sh       # Install audit tools
│   ├── run_audit.sh                 # Run full audit
│   ├── fix_test_fixtures.py         # Fixture migration
│   ├── fix_all_test_configs.sh      # Batch config fixes
│   └── fix_all_inline_configs.py    # Config replacement
├── systemd/                         # Systemd service templates
├── tests/                           # Test suite (113 tests)
│   ├── conftest.py                  # Centralized fixtures ✨ NEW
│   ├── test_config_*.py             # Config validation tests ✨ NEW
│   └── ...
├── docs/
│   ├── BASELINE.md                  # Current baseline
│   ├── NEXT_PHASE.md                # Next phase handoff
│   ├── CONFIG.md                    # Configuration reference
│   ├── DEPENDENCIES.md              # Dependency decisions
│   ├── CONTRIBUTING.md              # Contributing guide
│   ├── EXECUTION_PROTOCOL.md        # Execution guidelines ✨ NEW
│   └── specs/
│       ├── phase1-config-validation-design.md ✨ NEW
│       └── HARDENING_IMPLEMENTATION_WORKFLOW.md ✨ NEW
└── dashboard/                       # WebUI (deferred)
```

## 🔧 Extension Points

### Skills

Markdown files in `skills.dir` are discovered automatically. They require YAML frontmatter containing `name`, `description`, and optional parameters.

### Plugins

Python classes in `plugins.dir` are instantiated automatically. Supported hook methods:
- `before_message`, `after_message`
- `before_reply`, `after_reply`
- `on_error`, `on_tool_call`

### Tools

Built-in tools are registered explicitly in `tools/registry.py`. Adding a tool requires:
1. Implementing the function
2. Adding its OpenAI-compatible schema to `TOOLS_SCHEMA`
3. Adding the function to `TOOLS_MAPPING`
4. Adding tests

`tools.dir` is currently schema-only and is not auto-discovered.

## 🏭 Production Deployment

Systemd templates under `systemd/` use `@IDOLHUB_*@` placeholders. `scripts/setup.sh` renders the bot service with the target user, repository directory, and machine-local environment file. Secrets remain outside the repository.

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run audit tools
./scripts/run_audit.sh
```

## 📚 Documentation

### Core Documentation
- [Phase 1 Completion Report](PHASE1_COMPLETION.md) - Detailed completion status
- [Security Audit Findings](AUDIT_FINDINGS.md) - Comprehensive security audit
- [Current Baseline](docs/BASELINE.md) - Authoritative feature status
- [Next Phase](docs/NEXT_PHASE.md) - Next phase handoff
- [Configuration Reference](docs/CONFIG.md) - Complete config guide
- [Execution Protocol](docs/EXECUTION_PROTOCOL.md) - Development guidelines

### Technical Specifications
- [Phase 1 Design](docs/specs/phase1-config-validation-design.md) - Technical design
- [Hardening Workflow](docs/specs/HARDENING_IMPLEMENTATION_WORKFLOW.md) - Implementation workflow
- [Active Specifications](docs/specs/) - All active specs
- [Dependency Decisions](docs/DEPENDENCIES.md) - Dependency rationale
- [Contributing Guide](docs/CONTRIBUTING.md) - How to contribute

### Audit & Scripts
- [Latest Audit](hasilaudit.md) - Historical audit results
- [Audit Tools README](scripts/README_AUDIT.md) - Audit tools documentation
- [Fix Tests Guide](scripts/FIX_TESTS_GUIDE.md) - Manual fix guide
- [Historical Specs](docs/superpowers/) - Historical specifications

## 🗺️ Roadmap

| Phase | Status | Scope | Tests |
|---|---|---|---|
| **Phase 1** | ✅ **Complete** | Configuration Hardening with Pydantic validation | 113/113 passing |
| **Phase 2** | 🔄 Next | Secrets Management (Vault/AWS Secrets Manager) | TBD |
| **Phase 3** | 📋 Planned | Input Sanitization & Rate Limiting | TBD |
| **Phase 4** | 📋 Planned | Enhanced Logging & Monitoring | TBD |
| **Phase 5** | 📋 Planned | Security Headers & CORS Hardening | TBD |

### Completed Features
- ✅ Core runtime, APIs, extension systems
- ✅ Security controls and memory stack
- ✅ Pydantic configuration validation
- ✅ Environment variable resolution
- ✅ Hot-reload capability
- ✅ Comprehensive test coverage (113 tests)
- ✅ Automated audit tools
- ✅ Complete documentation

### Proposed Features
- 🔄 Secrets management (Phase 2)
- 📋 Input sanitization (Phase 3)
- 📋 Rate limiting (Phase 3)
- 📋 Enhanced logging (Phase 4)
- 📋 Security headers (Phase 5)

### Deferred Features
- ⏸️ Dashboard WebUI
- ⏸️ Voice integration
- ⏸️ Multi-agent orchestration
- ⏸️ Additional RAG backends

## 📊 Test Coverage

```
113 tests passing (100%)
- Configuration: 15 tests
- Agent: 12 tests
- Memory: 20 tests
- API: 7 tests
- LLM: 5 tests
- Tools: 8 tests
- Plugins: 6 tests
- Skills: 5 tests
- MCP: 4 tests
- Integration: 31 tests
```

## 🔐 Security Standards

- ✅ OWASP Top 10 (2021) - Configuration Security
- ✅ CWE-20 - Input Validation
- ✅ CWE-798 - Hard-coded Credentials (removed)
- ✅ CWE-522 - Insufficiently Protected Credentials
- ✅ Principle of Least Privilege
- ✅ Defense in Depth
- ✅ Fail Securely
- ✅ Secure by Default

## 📝 License

All rights reserved.

---

**Last Updated**: 2026-06-07  
**Version**: Phase 1 Complete  
**Maintainer**: [@primit1v0](https://github.com/primit1v0)