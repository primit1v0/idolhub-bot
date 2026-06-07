# Agent Guide for idolhub-bot

**Target Audience**: AI Agents (Codex, Antigravity, and other assistants)  
**Purpose**: Comprehensive guide for working on idolhub-bot without breaking baseline  
**Last Updated**: 2026-06-07  
**Current Phase**: Phase 1 Complete ✅

---

## 🎯 Critical Rules - READ FIRST

### DO NOT BREAK THESE RULES

1. **NEVER modify files without running tests first**
   ```bash
   pytest tests/ -v
   ```

2. **NEVER commit without verifying all tests pass**
   ```bash
   pytest tests/ -q --tb=no
   # Must show: "113 passed"
   ```

3. **NEVER bypass Pydantic validation**
   - All config changes must pass `AppConfig.model_validate()`
   - Use `core/config_validator.py` for validation logic

4. **NEVER hardcode secrets**
   - Use environment variables: `$VARIABLE_NAME`
   - Never commit `config.json`, `.env`, or secrets

5. **ALWAYS use centralized test fixtures**
   - Import from `tests/conftest.py`
   - Use `valid_test_config_data` fixture

6. **ALWAYS run audit before committing**
   ```bash
   ./scripts/run_audit.sh
   ```

---

## 📋 Project Status

### Phase 1: Configuration Hardening ✅ COMPLETE

**Status**: 113/113 tests passing (100%)

**Completed Features**:
- ✅ Pydantic validation for all config sections
- ✅ Environment variable resolution (`$VAR` syntax)
- ✅ Telegram token format validation (bot_id:token)
- ✅ Provider URL validation (HTTPS required)
- ✅ System prompt validation (min 10 chars)
- ✅ Memory path validation (non-empty)
- ✅ Auto-prune limits (min 100 messages)
- ✅ Secret masking in API responses
- ✅ Hot-reload with validation
- ✅ Secrets overwrite protection

**Key Files Created**:
- `core/config_schema.py` - Pydantic models
- `core/config_validator.py` - Validation logic
- `core/config_reloader.py` - Hot-reload capability
- `tests/conftest.py` - Centralized fixtures
- `PHASE1_COMPLETION.md` - Completion report
- `AUDIT_FINDINGS.md` - Security audit

**Validation Rules**:
```python
# Telegram token format
pattern: r'^\d+:[A-Za-z0-9_-]+$'
example: "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"

# Provider base_url
must be: valid HTTP/HTTPS URL
example: "https://api.openai.com/v1"

# System prompt
min_length: 10 characters
example: "You are a helpful assistant"

# Auto-prune limit
minimum: 100 messages
example: 1000
```

---

## 🚀 Phase 2: Secrets Management (NEXT)

**Status**: 📋 Planned  
**Priority**: Critical  
**Estimated Tests**: +15 tests

### Objectives

1. **Implement Secrets Backend**
   - HashiCorp Vault integration OR
   - AWS Secrets Manager integration
   - Fallback to environment variables

2. **Remove Secrets from Config**
   - Move all secrets to secrets backend
   - Keep only secret references in config.json
   - Example: `"api_key": "vault://openai/api_key"`

3. **Add Secrets Rotation**
   - Automatic rotation capability
   - Rotation without downtime
   - Audit logging for all secret access

4. **Implement Audit Logging**
   - Log all secret access attempts
   - Log rotation events
   - Alert on suspicious access patterns

### Implementation Steps

1. **Create Secrets Module** (`core/secrets.py`)
   ```python
   class SecretsManager:
       def get_secret(self, key: str) -> str
       def set_secret(self, key: str, value: str) -> None
       def rotate_secret(self, key: str) -> None
       def audit_log(self, action: str, key: str) -> None
   ```

2. **Update Config Validator**
   - Add secret reference resolution
   - Support `vault://`, `aws://`, `env://` prefixes
   - Validate secret references exist

3. **Add Tests** (`tests/test_secrets.py`)
   - Test secret retrieval
   - Test secret rotation
   - Test audit logging
   - Test fallback to env vars

4. **Update Documentation**
   - Add secrets setup guide
   - Update config.example.json
   - Add troubleshooting section

### Success Criteria

- [ ] All secrets moved to secrets backend
- [ ] Zero secrets in config.json
- [ ] Rotation works without downtime
- [ ] Audit logs capture all access
- [ ] All tests pass (128+ tests expected)
- [ ] Documentation complete

---

## 🔧 Workflow Execution

### Standard Development Workflow

```bash
# 1. Pull latest changes
cd /home/sandi/PocketFlow/idolhub
git pull origin main

# 2. Create feature branch (optional)
git checkout -b feature/your-feature-name

# 3. Make changes
# ... edit files ...

# 4. Run tests BEFORE committing
pytest tests/ -v

# 5. Run audit tools
./scripts/run_audit.sh

# 6. If tests pass, commit
git add -A
git commit -m "feat: your feature description"

# 7. Push to GitHub
git push origin main  # or your branch
```

### Emergency Rollback Workflow

```bash
# If you broke something:

# 1. Check what changed
git status
git diff

# 2. Restore specific file
git restore path/to/file.py

# 3. Or restore all changes
git restore .

# 4. Or revert last commit
git revert HEAD

# 5. Verify tests pass
pytest tests/ -v
```

### Hot-Reload Config Workflow

```bash
# 1. Edit config.json
vim config.json

# 2. Validate before reload
python -c "from core.config_validator import load_config; load_config('config.json')"

# 3. If valid, reload (API mode only)
curl -X POST http://localhost:8000/config -H "Content-Type: application/json" -d @config.json

# 4. Verify reload succeeded
curl http://localhost:8000/health
```

---

## 🛠️ Audit Scripts Usage

### Install Audit Tools

```bash
cd /home/sandi/PocketFlow/idolhub
./scripts/install_audit_tools.sh
```

**What it does**:
- Installs `ruff` (linter/formatter)
- Installs `bandit` (security scanner)
- Verifies installation

### Run Full Audit

```bash
./scripts/run_audit.sh
```

**What it checks**:
1. **Ruff**: Code quality, imports, unused variables
2. **Bandit**: Security vulnerabilities
3. **Pytest**: All 113 tests
4. **Coverage**: Test coverage report

**Expected Output**:
```
=== Ruff Check ===
All checks passed!

=== Bandit Security Scan ===
No issues identified.

=== Pytest ===
113 passed in 5.47s

=== Coverage ===
TOTAL: 95%
```

### Fix Test Fixtures

```bash
python scripts/fix_test_fixtures.py
```

**What it does**:
- Migrates inline configs to centralized fixtures
- Updates imports to use `conftest.py`
- Ensures consistency across tests

### Fix Test Configs (Batch)

```bash
./scripts/fix_all_test_configs.sh
```

**What it does**:
- Fixes path validation issues
- Updates token formats
- Fixes provider URLs
- Batch processes all test files

### Fix Inline Configs

```bash
python scripts/fix_all_inline_configs.py path/to/test_file.py
```

**What it does**:
- Replaces inline configs with fixture usage
- Ensures valid test data
- Updates to latest validation rules

---

## 📐 Architecture Decisions

### Configuration System

**Design**: Single source of truth with Pydantic validation

**Components**:
1. `config_schema.py` - Pydantic models (data structure)
2. `config_validator.py` - Validation logic (business rules)
3. `config_reloader.py` - Hot-reload (runtime updates)
4. `config.py` - Backward compatibility layer

**Flow**:
```
config.json → load_config() → resolve_env() → validate() → AppConfig
```

**Why Pydantic?**:
- Type safety at runtime
- Automatic validation
- Clear error messages
- JSON schema generation
- IDE autocomplete support

### Test Infrastructure

**Design**: Centralized fixtures with pytest

**Components**:
1. `conftest.py` - Shared fixtures
2. `test_config_*.py` - Config validation tests
3. `test_*.py` - Feature-specific tests

**Fixture Hierarchy**:
```
valid_test_config_data (base)
  ↓
mock_cfg (AppConfig instance)
  ↓
client (FastAPI test client)
  ↓
memory_store (initialized store)
```

**Why Centralized?**:
- DRY principle (Don't Repeat Yourself)
- Consistency across tests
- Easy to update validation rules
- Faster test execution

### Memory System

**Design**: Layered memory with multiple backends

**Layers**:
1. **Short-term**: SQLite + FTS5 (conversation history)
2. **Long-term**: sqlite-vec (semantic memory)
3. **Facts**: EAV model (entity-attribute-value)
4. **Preferences**: Key-value store

**Why Layered?**:
- Separation of concerns
- Different access patterns
- Optimized for each use case
- Easy to swap backends

---

## 🔒 Baseline Protection Rules

### What is the Baseline?

The baseline is the **current working state** of the project:
- All 113 tests passing
- All validation rules enforced
- All documentation up-to-date
- All audit tools passing

### How to Protect the Baseline

1. **NEVER commit failing tests**
   ```bash
   # Always check before commit
   pytest tests/ -q --tb=no
   ```

2. **NEVER bypass validation**
   ```python
   # ❌ WRONG
   config = {"telegram": {"token": "test"}}
   
   # ✅ CORRECT
   config = AppConfig.model_validate({
       "telegram": {"token": "123456:ABC-DEF..."}
   })
   ```

3. **NEVER hardcode values**
   ```python
   # ❌ WRONG
   api_key = "sk-1234567890"
   
   # ✅ CORRECT
   api_key = os.getenv("OPENAI_API_KEY")
   ```

4. **ALWAYS use fixtures**
   ```python
   # ❌ WRONG
   def test_something():
       cfg = AppConfig.model_validate({...})
   
   # ✅ CORRECT
   def test_something(valid_test_config_data):
       cfg = AppConfig.model_validate(valid_test_config_data)
   ```

5. **ALWAYS run audit before push**
   ```bash
   ./scripts/run_audit.sh && git push origin main
   ```

### Baseline Verification Checklist

Before committing, verify:
- [ ] All tests pass (`pytest tests/ -v`)
- [ ] Ruff passes (`ruff check .`)
- [ ] Bandit passes (`bandit -r . -ll`)
- [ ] No secrets in code (`git diff | grep -i "api_key\|token\|secret"`)
- [ ] Documentation updated (if needed)
- [ ] Commit message follows convention

---

## 📝 Commit Message Convention

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `perf`: Performance improvement
- `chore`: Maintenance tasks

### Examples

```bash
# Feature
git commit -m "feat(secrets): add HashiCorp Vault integration"

# Bug fix
git commit -m "fix(config): handle missing provider credentials"

# Documentation
git commit -m "docs: update Phase 2 implementation guide"

# Test
git commit -m "test(memory): add auto-prune validation tests"
```

---

## 🚨 Common Pitfalls

### 1. Invalid Token Format

**Problem**:
```python
"telegram": {"token": "test"}  # ❌ WRONG
```

**Solution**:
```python
"telegram": {"token": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"}  # ✅ CORRECT
```

### 2. Invalid Provider URL

**Problem**:
```python
"providers": {"openai": {"base_url": "dummy"}}  # ❌ WRONG
```

**Solution**:
```python
"providers": {"openai": {"base_url": "https://api.openai.com/v1"}}  # ✅ CORRECT
```

### 3. Short System Prompt

**Problem**:
```python
"agent": {"system_prompt": "sys"}  # ❌ WRONG (< 10 chars)
```

**Solution**:
```python
"agent": {"system_prompt": "You are a helpful assistant"}  # ✅ CORRECT
```

### 4. Empty Memory Path

**Problem**:
```python
"memory": {"long_term": {"path": ""}}  # ❌ WRONG
```

**Solution**:
```python
"memory": {"long_term": {"path": "./data/vectors.db"}}  # ✅ CORRECT
```

### 5. Low Auto-Prune Limit

**Problem**:
```python
"short_term": {"auto_prune_limit": 3}  # ❌ WRONG (< 100)
```

**Solution**:
```python
"short_term": {"auto_prune_limit": 1000}  # ✅ CORRECT
```

---

## 📚 Reference Documentation

### Core Documentation
- [PHASE1_COMPLETION.md](../PHASE1_COMPLETION.md) - Phase 1 details
- [AUDIT_FINDINGS.md](../AUDIT_FINDINGS.md) - Security audit
- [README.md](../README.md) - Project overview

### Technical Specs
- [phase1-config-validation-design.md](specs/phase1-config-validation-design.md)
- [HARDENING_IMPLEMENTATION_WORKFLOW.md](specs/HARDENING_IMPLEMENTATION_WORKFLOW.md)
- [EXECUTION_PROTOCOL.md](EXECUTION_PROTOCOL.md)

### Configuration
- [CONFIG.md](CONFIG.md) - Configuration reference
- [config.example.json](../config.example.json) - Config template

### Scripts
- [README_AUDIT.md](../scripts/README_AUDIT.md) - Audit tools
- [FIX_TESTS_GUIDE.md](../scripts/FIX_TESTS_GUIDE.md) - Fix guide

---

## 🤝 Working with Other Agents

### For Codex Agent

**Your strengths**: Code generation, refactoring, optimization

**How to help**:
1. Generate new features following existing patterns
2. Refactor code while maintaining tests
3. Optimize performance bottlenecks
4. Add type hints and documentation

**What to avoid**:
- Don't bypass validation
- Don't hardcode secrets
- Don't break existing tests
- Don't modify config schema without tests

### For Antigravity Agent

**Your strengths**: Architecture, system design, planning

**How to help**:
1. Design new features and phases
2. Review architecture decisions
3. Plan implementation workflows
4. Create technical specifications

**What to avoid**:
- Don't propose changes that break baseline
- Don't skip validation in designs
- Don't ignore security requirements
- Don't forget test coverage

### For Other Agents

**General guidelines**:
1. Read this guide completely before starting
2. Run tests before and after changes
3. Follow the workflow execution steps
4. Use audit scripts to verify quality
5. Ask for clarification if unsure

---

## 📞 Getting Help

### If Tests Fail

1. Read the error message carefully
2. Check if it's a validation error
3. Look for similar patterns in existing tests
4. Use `pytest -xvs` for detailed output
5. Check `tests/conftest.py` for fixtures

### If Audit Fails

1. Run `./scripts/run_audit.sh` to see details
2. Fix ruff issues: `ruff check . --fix`
3. Fix bandit issues: Review security warnings
4. Re-run audit to verify fixes

### If Confused About Architecture

1. Read `docs/specs/phase1-config-validation-design.md`
2. Check `core/config_schema.py` for data models
3. Check `core/config_validator.py` for validation logic
4. Look at existing tests for examples

---

## ✅ Quick Reference

### Must-Run Commands

```bash
# Before starting work
git pull origin main
pytest tests/ -v

# During development
pytest tests/test_your_feature.py -v

# Before committing
./scripts/run_audit.sh
pytest tests/ -q --tb=no

# After committing
git push origin main
```

### Must-Check Files

- `tests/conftest.py` - Test fixtures
- `core/config_schema.py` - Data models
- `core/config_validator.py` - Validation rules
- `PHASE1_COMPLETION.md` - Current status

### Must-Follow Rules

1. ✅ All tests must pass
2. ✅ All validation must be enforced
3. ✅ No secrets in code
4. ✅ Use centralized fixtures
5. ✅ Run audit before commit

---

**Remember**: When in doubt, run the tests. If tests pass, you're probably okay. If tests fail, you definitely broke something.

**Last Updated**: 2026-06-07  
**Maintained By**: Bob Shell (AI Assistant)  
**For**: Codex, Antigravity, and other AI agents
