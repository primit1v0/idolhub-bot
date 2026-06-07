# Phase 1: Configuration & Validation Foundation - Design Document

**Status:** Design Phase  
**Created:** June 7, 2026  
**Items:** #5, #22, #23, #24  
**Estimated Duration:** 4-6 hours

## Overview

Phase 1 establishes the configuration validation foundation that all other hardening phases depend on. This phase makes configuration reliable, validated, and enforceable at runtime.

## Goals

1. **Strict Schema Validation** - All config must conform to Pydantic models
2. **Atomic Updates** - Config changes apply atomically or rollback
3. **Runtime Enforcement** - All config flags actually control behavior
4. **Fail-Fast Validation** - Invalid configs rejected at startup

## Current State Analysis

### What Works
- `config.example.json` exists and is tracked
- `config.json` is local-only and gitignored
- `core/config.py` loads config from JSON
- Environment variable substitution works (`$VARIABLE`)

### What's Missing
- No Pydantic schema validation
- No atomic reload mechanism
- Several flags accepted but not enforced:
  - `app.debug`
  - `app.timezone`
  - `agent.memory_enabled`
  - `tools.dir`
  - `plugins.enabled`
  - `api.enabled`
  - `mcp.enabled`
  - `mcp.port` (stdio only currently)
- No validation of provider/tool/plugin names
- No clear error messages for misconfigurations

## Design Decisions

### 1. Pydantic Models (#22)

**Location:** `core/config_schema.py` (new file)

**Structure:**
```python
from pydantic import BaseModel, Field, validator
from typing import Literal, Optional

class AppConfig(BaseModel):
    mode: Literal["bot", "api", "mcp"]
    debug: bool = False
    timezone: str = "UTC"
    
    @validator("timezone")
    def validate_timezone(cls, v):
        # Validate against pytz timezones
        pass

class AgentConfig(BaseModel):
    max_iterations: int = Field(ge=1, le=100)
    tools_enabled: bool = True
    filter_enabled: bool = True
    gating_enabled: bool = True
    memory_enabled: bool = True

class TelegramConfig(BaseModel):
    token: str
    allowed_users: list[int] = []
    parse_mode: Literal["Markdown", "HTML", "MarkdownV2"] = "Markdown"

class LLMConfig(BaseModel):
    provider: str
    model: str
    temperature: float = Field(ge=0.0, le=2.0)
    max_tokens: int = Field(ge=1)
    # ... other LLM settings

class ProviderConfig(BaseModel):
    api_key: str
    base_url: Optional[str] = None
    # Provider-specific fields

class MemoryConfig(BaseModel):
    # Short-term and long-term memory settings
    pass

class SkillsConfig(BaseModel):
    dir: str = "skills"
    enabled: bool = True

class ToolsConfig(BaseModel):
    enabled: bool = True
    dir: str = "tools"

class PluginsConfig(BaseModel):
    dir: str = "plugins"
    enabled: bool = True

class APIConfig(BaseModel):
    enabled: bool = True
    host: str = "0.0.0.0"
    port: int = Field(ge=1, le=65535)
    cors_origins: list[str] = []

class MCPConfig(BaseModel):
    enabled: bool = True
    port: int = Field(ge=1, le=65535)

class LoggingConfig(BaseModel):
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    format: str

class Config(BaseModel):
    app: AppConfig
    agent: AgentConfig
    telegram: TelegramConfig
    llm: LLMConfig
    providers: dict[str, ProviderConfig]
    memory: MemoryConfig
    skills: SkillsConfig
    tools: ToolsConfig
    plugins: PluginsConfig
    api: APIConfig
    mcp: MCPConfig
    logging: LoggingConfig
    
    @validator("providers")
    def validate_provider_exists(cls, v, values):
        # Ensure llm.provider exists in providers dict
        pass
```

**Benefits:**
- Type safety
- Automatic validation
- Clear error messages
- JSON schema generation for docs
- IDE autocomplete support

### 2. Configuration Validator (#22, #24)

**Location:** `core/config_validator.py` (new file)

**Responsibilities:**
- Load and parse JSON
- Substitute environment variables
- Validate against Pydantic schema
- Check provider/tool/plugin name whitelists
- Provide detailed error messages

**Key Functions:**
```python
def load_config(path: str = "config.json") -> Config:
    """Load and validate configuration."""
    pass

def validate_provider_whitelist(config: Config) -> None:
    """Ensure selected provider is configured."""
    pass

def validate_capability_whitelists(config: Config) -> None:
    """Validate tool/plugin/skill names against available."""
    pass

def substitute_env_vars(data: dict) -> dict:
    """Replace $VARIABLE with environment values."""
    pass
```

### 3. Atomic Configuration Reloader (#5)

**Location:** `core/config_reloader.py` (new file)

**Design:**
- Load new config into temporary object
- Validate fully before applying
- Swap atomically if valid
- Rollback on any error
- Emit events for config changes

**Key Functions:**
```python
async def reload_config(path: str = "config.json") -> tuple[bool, str]:
    """
    Reload configuration atomically.
    Returns (success, message).
    """
    pass

def get_current_config() -> Config:
    """Get current active configuration."""
    pass

def register_config_change_handler(handler: Callable) -> None:
    """Register callback for config changes."""
    pass
```

**Reload Trigger Options:**
1. API endpoint: `POST /api/config/reload`
2. Signal handler: `SIGHUP`
3. File watcher (optional, future)

### 4. Runtime Flag Enforcement (#23)

**Changes Required:**

#### `app.debug`
- **Current:** Accepted but ignored
- **New:** Control debug logging, error verbosity, stack traces
- **Location:** `core/logging.py`, error handlers

#### `app.timezone`
- **Current:** Accepted but ignored
- **New:** Set timezone for timestamps in logs, memory, responses
- **Location:** `core/logging.py`, `memory/sqlite_store.py`

#### `agent.memory_enabled`
- **Current:** Accepted but ignored
- **New:** Actually disable memory reads/writes when False
- **Location:** `core/agent.py`, memory calls

#### `tools.dir`
- **Current:** Accepted but not used
- **New:** Load custom tools from this directory (future)
- **Note:** Keep as placeholder for now, document as "not implemented"

#### `plugins.enabled`
- **Current:** Accepted but not enforced
- **New:** Skip plugin loading entirely when False
- **Location:** `plugins/loader.py`

#### `api.enabled`
- **Current:** Accepted but not enforced
- **New:** Prevent API server startup when False
- **Location:** `main.py`, mode selection

#### `mcp.enabled`
- **Current:** Accepted but not enforced
- **New:** Prevent MCP server startup when False
- **Location:** `main.py`, mode selection

#### `mcp.port`
- **Current:** Accepted but not used (stdio only)
- **New:** Document as "stdio only, port reserved for future"
- **Note:** No implementation change yet

### 5. Fail-Fast Capability Whitelists (#24)

**Validation Points:**

1. **Provider Validation**
   - Selected `llm.provider` must exist in `providers` dict
   - Provider must have required fields (api_key, etc.)
   - Fail at startup if missing

2. **Tool Validation**
   - If `tools.enabled`, validate tool names
   - Check against built-in tool registry
   - Warn about unknown tools (don't fail)

3. **Plugin Validation**
   - If `plugins.enabled`, scan plugin directory
   - Validate plugin class structure
   - Fail if plugin directory doesn't exist

4. **Skill Validation**
   - If `skills.enabled`, scan skill directory
   - Validate YAML frontmatter
   - Fail if skill directory doesn't exist

## Implementation Plan

### Step 1: Create Pydantic Schema (60 min)
1. Create `core/config_schema.py`
2. Define all config models
3. Add validators for complex fields
4. Test schema with current `config.example.json`

**Tests:**
- `test_config_schema_valid.py` - Valid configs pass
- `test_config_schema_invalid.py` - Invalid configs fail with clear errors

### Step 2: Create Validator (45 min)
1. Create `core/config_validator.py`
2. Implement `load_config()` with Pydantic validation
3. Implement environment variable substitution
4. Implement capability whitelists
5. Update `core/config.py` to use new validator

**Tests:**
- `test_config_validator_env_vars.py` - Env var substitution
- `test_config_validator_whitelists.py` - Provider/tool validation
- `test_config_validator_errors.py` - Error message quality

### Step 3: Implement Atomic Reloader (60 min)
1. Create `core/config_reloader.py`
2. Implement `reload_config()` with rollback
3. Add config change event system
4. Add API endpoint for reload
5. Add SIGHUP signal handler

**Tests:**
- `test_config_reloader_success.py` - Valid reload succeeds
- `test_config_reloader_rollback.py` - Invalid reload rolls back
- `test_config_reloader_events.py` - Change events fire

### Step 4: Enforce Runtime Flags (90 min)
1. Update `core/logging.py` for `app.debug` and `app.timezone`
2. Update `core/agent.py` for `agent.memory_enabled`
3. Update `plugins/loader.py` for `plugins.enabled`
4. Update `main.py` for `api.enabled` and `mcp.enabled`
5. Document unimplemented flags in `BASELINE.md`

**Tests:**
- `test_runtime_flags_debug.py` - Debug mode changes behavior
- `test_runtime_flags_timezone.py` - Timezone affects timestamps
- `test_runtime_flags_memory.py` - Memory can be disabled
- `test_runtime_flags_plugins.py` - Plugins can be disabled
- `test_runtime_flags_modes.py` - API/MCP can be disabled

### Step 5: Update Documentation (30 min)
1. Update `config.example.json` with comments
2. Update `docs/CONFIG.md` with new validation rules
3. Update `docs/BASELINE.md` with enforced flags
4. Add migration guide for existing configs

## Testing Strategy

### Unit Tests (15 tests minimum)
- Schema validation (valid/invalid cases)
- Environment variable substitution
- Capability whitelist validation
- Atomic reload (success/failure)
- Runtime flag enforcement

### Integration Tests (5 tests minimum)
- Full config load and validation
- Config reload during runtime
- Mode selection based on flags
- Provider validation at startup

### Test Coverage Target
- `core/config_schema.py`: 100%
- `core/config_validator.py`: 95%
- `core/config_reloader.py`: 90%
- Overall Phase 1 code: 95%

## Migration Guide

### For Existing Configs

1. **Backup current config:**
   ```bash
   cp config.json config.json.backup
   ```

2. **Validate against new schema:**
   ```bash
   uv run python -c "from core.config_validator import load_config; load_config()"
   ```

3. **Fix validation errors:**
   - Add missing required fields
   - Fix type mismatches
   - Remove unknown fields

4. **Test reload:**
   ```bash
   curl -X POST http://localhost:8000/api/config/reload
   ```

### Breaking Changes

- None expected - new validation is additive
- Existing valid configs should continue to work
- Invalid configs will now fail fast with clear errors

## Success Criteria

- [ ] All config sections have Pydantic models
- [ ] `load_config()` validates against schema
- [ ] Environment variables are substituted correctly
- [ ] Provider/tool/plugin whitelists are validated
- [ ] Config can be reloaded atomically via API
- [ ] Invalid reloads rollback without affecting runtime
- [ ] All runtime flags are enforced or documented as unimplemented
- [ ] 15+ new tests pass
- [ ] No test regressions
- [ ] Documentation updated

## Risks & Mitigations

### Risk: Breaking existing configs
**Mitigation:** Additive validation only, maintain backward compatibility

### Risk: Performance impact of validation
**Mitigation:** Validate once at startup and on reload, cache result

### Risk: Complex error messages
**Mitigation:** Use Pydantic's built-in error formatting, add custom messages

## Next Phase Dependencies

Phase 2 (Provider Validation) depends on:
- ✅ Strict config schema
- ✅ Provider whitelist validation
- ✅ Clear error messages

Phase 3 (Security) depends on:
- ✅ Runtime flag enforcement
- ✅ Atomic config updates
- ✅ Validated configuration state

## References

- Current config: `config.example.json`
- Current loader: `core/config.py`
- Pydantic docs: https://docs.pydantic.dev/
- Baseline spec: `docs/BASELINE.md`
