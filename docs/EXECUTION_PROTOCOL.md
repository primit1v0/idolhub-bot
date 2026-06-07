# Execution Protocol - Foundation Hardening

**Status:** Active  
**Created:** June 7, 2026  
**Purpose:** Step-by-step execution protocol for hardening implementation

## 🎯 Execution Rule

```
Execute 1 Phase → Audit → Verify → Commit+Push → Stop → Report
```

**DO NOT** proceed to next phase without completing this cycle.

## 📋 Phase Execution Checklist

### Phase 1: Configuration & Validation Foundation

**Items:** #5, #22, #23, #24  
**Duration:** 4-6 hours  
**Status:** ⏳ Ready to Execute

#### Pre-Execution
- [ ] Read `docs/specs/phase1-config-validation-design.md`
- [ ] Review current `core/config.py`
- [ ] Review `config.example.json`
- [ ] Ensure git working directory is clean

#### Implementation
- [ ] Create `core/config_schema.py` with Pydantic models
- [ ] Create `core/config_validator.py` with validation logic
- [ ] Create `core/config_reloader.py` with atomic reload
- [ ] Update `core/config.py` to use new validator
- [ ] Enforce runtime flags in relevant modules
- [ ] Write 15+ tests for config validation

#### Audit (Use Existing Tools)
```bash
# Run in idolhub directory
cd /home/sandi/PocketFlow/idolhub

# 1. Run full test suite
uv run pytest -v

# 2. Check code quality
uv run ruff check . --select F,I

# 3. Security scan with Bandit
.audit-tools/bin/bandit -r core memory tools api mcp_server -q

# 4. Security scan with Semgrep
HOME=.audit-tools/home .audit-tools/bin/semgrep \
  --config auto --error core memory tools api mcp_server

# 5. Dependency vulnerability check
.audit-tools/bin/pip-audit -r requirements.txt
```

#### Verify
- [ ] All tests pass (should be 82+ tests now)
- [ ] No Ruff errors
- [ ] No high-severity Bandit findings
- [ ] No Semgrep findings
- [ ] No pip-audit vulnerabilities
- [ ] Config validation works with `config.example.json`

#### Documentation
- [ ] Update `docs/BASELINE.md` with Phase 1 completion
- [ ] Update `docs/NEXT_PHASE.md` to point to Phase 2
- [ ] Update `hasilaudit.md` with new audit results

#### Commit & Push
```bash
# Stage changes
git add core/config_schema.py
git add core/config_validator.py
git add core/config_reloader.py
git add core/config.py
git add tests/test_config_*.py
git add docs/BASELINE.md
git add docs/NEXT_PHASE.md
git add hasilaudit.md

# Commit with clear message
git commit -m "feat(phase1): implement configuration validation foundation

- Add Pydantic schema validation (config_schema.py)
- Add config validator with env var substitution
- Add atomic config reloader with rollback
- Enforce runtime flags (debug, timezone, memory_enabled, etc)
- Add 15+ configuration validation tests
- Update baseline documentation

Items: #5, #22, #23, #24
Tests: 67 → 82+ passing
Audit: Clean (0 findings)"

# Push to GitHub
git push origin main
```

#### Stop & Report
```
✅ Phase 1 Complete

**Implemented:**
- Pydantic configuration schema
- Config validator with whitelists
- Atomic config reloader
- Runtime flag enforcement

**Tests:** 82+ passing (was 67)
**Audit:** Clean (0 findings)
**Commit:** [commit hash]

**Next:** Phase 2 - Provider & Dependency Validation
**Duration:** 2-3 hours
**Items:** #20, #25
```

---

### Phase 2: Provider & Dependency Validation

**Items:** #20, #25  
**Duration:** 2-3 hours  
**Status:** ⏸️ Waiting for Phase 1

#### Pre-Execution
- [ ] Verify Phase 1 is complete and pushed
- [ ] Read Phase 2 design (to be created)
- [ ] Review current provider code

#### Implementation
- [ ] Create `core/dependencies.py` with DI container
- [ ] Create `providers/validator.py` for startup checks
- [ ] Update provider initialization to use DI
- [ ] Add provider health checks
- [ ] Write tests for DI and validation

#### Audit → Verify → Document → Commit → Push → Stop → Report
(Same process as Phase 1)

---

### Phase 3: Security & Access Control

**Items:** #1, #3, #4, #26, #27, #28, #29, #30  
**Duration:** 6-8 hours  
**Status:** ⏸️ Waiting for Phase 2

#### Pre-Execution
- [ ] Verify Phase 2 is complete and pushed
- [ ] Read Phase 3 design (to be created)
- [ ] Review current security code

#### Implementation
- [ ] Implement Telegram access control
- [ ] Implement API authentication
- [ ] Implement user identity boundaries
- [ ] Create unified authorization gate
- [ ] Enhance prompt-injection filtering
- [ ] Add input validation and normalization
- [ ] Add negation-aware memory approval
- [ ] Add dangerous content detection
- [ ] Write 25+ security tests

#### Audit → Verify → Document → Commit → Push → Stop → Report
(Same process as Phase 1)

---

### Phase 4: Tool System Hardening

**Items:** #2, #11-19  
**Duration:** 8-10 hours  
**Status:** ⏸️ Waiting for Phase 3

---

### Phase 5: Plugin & Skill System Hardening

**Items:** #7-10  
**Duration:** 3-4 hours  
**Status:** ⏸️ Waiting for Phase 4

---

### Phase 6: Memory System Hardening

**Items:** #31-35  
**Duration:** 4-6 hours  
**Status:** ⏸️ Waiting for Phase 3

---

### Phase 7: API & Service Hardening

**Items:** #6, #21, #36-38  
**Duration:** 4-5 hours  
**Status:** ⏸️ Waiting for Phase 2, 3

---

### Phase 8: Observability & Testing

**Items:** #39  
**Duration:** 3-4 hours  
**Status:** ⏸️ Waiting for all phases

---

## 🚨 Critical Rules

1. **ONE PHASE AT A TIME** - Do not skip ahead
2. **AUDIT EVERY PHASE** - Use all 5 audit tools
3. **VERIFY BEFORE COMMIT** - All checks must pass
4. **COMMIT ATOMICALLY** - One phase = one commit
5. **PUSH IMMEDIATELY** - Don't accumulate local changes
6. **STOP AFTER PUSH** - Report and wait for next instruction
7. **UPDATE DOCS** - Baseline and audit results every phase

## 📊 Progress Tracking

| Phase | Status | Tests | Commit | Date |
|---|---|---|---|---|
| 1. Configuration | ⏳ Ready | 67 → 82+ | - | - |
| 2. Providers | ⏸️ Waiting | - | - | - |
| 3. Security | ⏸️ Waiting | - | - | - |
| 4. Tools | ⏸️ Waiting | - | - | - |
| 5. Plugins/Skills | ⏸️ Waiting | - | - | - |
| 6. Memory | ⏸️ Waiting | - | - | - |
| 7. API/Service | ⏸️ Waiting | - | - | - |
| 8. Observability | ⏸️ Waiting | - | - | - |

**Current:** Phase 1 ready to execute  
**Total Progress:** 0/39 items (0%)

## 🛠️ Audit Tools Reference

All tools are already installed via pipx and uv:

```bash
# Location of audit tools
.audit-tools/bin/bandit
.audit-tools/bin/semgrep
.audit-tools/bin/pip-audit

# Python tools via uv
uv run pytest
uv run ruff
```

## 📝 Commit Message Template

```
feat(phase<N>): <short description>

- <change 1>
- <change 2>
- <change 3>

Items: #<item1>, #<item2>, ...
Tests: <old_count> → <new_count> passing
Audit: Clean (0 findings) | <N> findings accepted
```

## 🎯 Success Criteria Per Phase

- [ ] All items in phase implemented
- [ ] All new tests pass
- [ ] No test regressions
- [ ] All 5 audit tools pass (or findings documented)
- [ ] Documentation updated
- [ ] Changes committed and pushed
- [ ] Report submitted

## 🚀 Ready to Start

**Current Phase:** Phase 1  
**Next Action:** Execute Phase 1 implementation  
**Estimated Time:** 4-6 hours  
**Expected Outcome:** 82+ tests passing, clean audit

---

**Last Updated:** June 7, 2026  
**Protocol Version:** 1.0
