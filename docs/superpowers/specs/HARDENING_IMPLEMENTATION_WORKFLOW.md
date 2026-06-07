# Foundation Hardening Implementation Workflow

**Status:** Planning Phase  
**Created:** June 7, 2026  
**Purpose:** Structured implementation plan for 39 hardening items

## Overview

This document organizes the 39 foundation hardening items into logical phases with clear dependencies, priorities, and implementation order.

## Implementation Principles

1. **Small, Focused Changes** - One item at a time, fully tested
2. **Dependency-First** - Core infrastructure before dependent features
3. **Non-Breaking** - Maintain backward compatibility where possible
4. **Test-Driven** - Write tests before or alongside implementation
5. **Documentation-Synced** - Update docs with each change
6. **Aggressive Pace** - Baseline was built in 1 day, hardening should match that velocity

## Phase Organization

### Phase 1: Configuration & Validation Foundation (Items 5, 22, 23, 24)
**Priority:** Critical  
**Dependencies:** None  
**Estimated Duration:** 4-6 hours

**Rationale:** Configuration is the foundation. All other hardening depends on reliable, validated configuration.

**Items:**
- **#5: Atomic Configuration Updates**
  - Implement config reload without restart
  - Add validation before applying changes
  - Rollback on validation failure
  
- **#22: Strict Configuration Schema**
  - Define Pydantic models for all config sections
  - Add comprehensive validation rules
  - Generate JSON schema for documentation
  
- **#23: Runtime Enforcement for Configuration Flags**
  - Make all accepted-but-not-enforced flags functional
  - Add runtime checks for `app.debug`, `app.timezone`, etc.
  - Update tests to verify enforcement
  
- **#24: Fail-Fast Capability Whitelists**
  - Validate enabled capabilities at startup
  - Reject unknown provider/tool/plugin names
  - Clear error messages for misconfigurations

**Deliverables:**
- `core/config_validator.py` with Pydantic models
- `core/config_reloader.py` for atomic updates
- Updated `config.example.json` with schema annotations
- 15+ new configuration validation tests

---

### Phase 2: Provider & Dependency Validation (Items 20, 25)
**Priority:** High  
**Dependencies:** Phase 1 (config validation)  
**Estimated Duration:** 2-3 hours

**Rationale:** Validate external dependencies early to fail fast and provide clear error messages.

**Items:**
- **#20: Explicit Runtime Dependency Injection**
  - Create dependency container pattern
  - Inject LLM client, memory stores, tools
  - Enable easier testing and mocking
  
- **#25: Provider Startup Validation**
  - Validate API keys and connectivity at startup
  - Test provider endpoints before accepting requests
  - Cache validation results with TTL

**Deliverables:**
- `core/dependencies.py` with DI container
- `providers/validator.py` for startup checks
- Provider health check tests

---

### Phase 3: Security & Access Control (Items 1, 3, 4, 26, 27, 28, 29, 30)
**Priority:** Critical  
**Dependencies:** Phase 1, Phase 2  
**Estimated Duration:** 6-8 hours

**Rationale:** Security must be hardened before expanding tool permissions and API access.

**Items:**
- **#1: Telegram Access Default**
  - Default to deny-all for new users
  - Require explicit allowlist configuration
  - Add admin commands for user management
  
- **#3: API Authentication**
  - Implement API key or JWT authentication
  - Add rate limiting per key/user
  - Secure endpoint access control
  
- **#4: API User Identity Boundary**
  - Isolate user contexts in API mode
  - Prevent cross-user data leakage
  - Add user-scoped memory and history
  
- **#26: Unified Action Authorization Gate**
  - Single authorization check for all actions
  - Consistent permission model across modes
  - Audit logging for authorization decisions
  
- **#27: Stronger Prompt-Injection Filtering**
  - Enhance existing filter with more patterns
  - Add confidence scoring
  - Configurable sensitivity levels
  
- **#28: Input Normalization and Type Handling**
  - Sanitize all user inputs
  - Validate types before processing
  - Handle edge cases (empty, null, malformed)
  
- **#29: Negation-Aware Memory Approval**
  - Detect "don't remember" patterns
  - Respect user intent for memory writes
  - Add explicit forget commands
  
- **#30: Normalized Dangerous-Content Detection**
  - Detect harmful content patterns
  - Block or flag dangerous requests
  - Configurable content policy

**Deliverables:**
- `core/auth.py` with authentication system
- `core/authorization.py` with unified gate
- Enhanced `core/rag_filter.py`
- `core/input_validator.py`
- `core/content_policy.py`
- 25+ security tests

---

### Phase 4: Tool System Hardening (Items 2, 11, 12, 13, 14, 15, 16, 17, 18, 19)
**Priority:** High  
**Dependencies:** Phase 3 (authorization)  
**Estimated Duration:** 8-10 hours

**Rationale:** Tools are the primary attack surface. Must be secured and validated thoroughly.

**Items:**
- **#2: Tool Permission and Approval**
  - Per-tool permission model
  - User approval for sensitive operations
  - Audit trail for tool executions
  
- **#11: Skill and Tool Name Collision Protection**
  - Detect duplicate names at registration
  - Namespace isolation (built-in vs custom)
  - Clear error messages for conflicts
  
- **#12: Unified Tool Registration**
  - Single registry for all tool types
  - Consistent schema validation
  - Automatic documentation generation
  
- **#13: Startup Registry Validation**
  - Validate all tools at startup
  - Check schema completeness
  - Verify function signatures match schemas
  
- **#14: Tool Argument Validation**
  - Runtime validation of tool arguments
  - Type checking and coercion
  - Clear error messages for invalid args
  
- **#15: Tool Error Isolation**
  - Catch and wrap tool exceptions
  - Prevent tool errors from crashing agent
  - Structured error reporting to LLM
  
- **#16: Async-Safe Tool Execution**
  - Ensure all tools are async-compatible
  - Wrap sync tools in async executors
  - Prevent blocking the event loop
  
- **#17: Tool Timeout and Cancellation**
  - Per-tool timeout configuration
  - Graceful cancellation support
  - Resource cleanup on timeout
  
- **#18: Typed Tool Results**
  - Structured result objects
  - Success/failure status
  - Metadata (duration, tokens, etc.)
  
- **#19: Tool Output and Context Limits**
  - Limit tool output size
  - Truncate large results intelligently
  - Prevent context window overflow

**Deliverables:**
- `tools/registry_v2.py` with unified registration
- `tools/validator.py` for schema validation
- `tools/executor.py` with timeout/cancellation
- `tools/permissions.py` for approval system
- `tools/result.py` with typed results
- 30+ tool system tests

---

### Phase 5: Plugin & Skill System Hardening (Items 7, 8, 9, 10)
**Priority:** Medium  
**Dependencies:** Phase 4 (tool registry)  
**Estimated Duration:** 3-4 hours

**Rationale:** Plugins and skills extend the system. Must be validated and isolated.

**Items:**
- **#7: Plugin Enablement Enforcement**
  - Respect `plugins.enabled` flag
  - Skip loading when disabled
  - Clear logging of plugin state
  
- **#8: Plugin Contract Validation**
  - Validate plugin class structure
  - Check required methods exist
  - Verify hook signatures
  
- **#9: Plugin Load Failure Policy**
  - Continue startup on plugin failure
  - Log errors clearly
  - Disable failed plugins automatically
  
- **#10: Skill Metadata Validation**
  - Validate YAML frontmatter schema
  - Check required fields (name, description)
  - Validate parameter types

**Deliverables:**
- `plugins/validator.py`
- `skills/validator.py`
- Enhanced `plugins/loader.py`
- Enhanced `skills/loader.py`
- 15+ plugin/skill tests

---

### Phase 6: Memory System Hardening (Items 31, 32, 33, 34, 35)
**Priority:** High  
**Dependencies:** Phase 3 (authorization)  
**Estimated Duration:** 4-6 hours

**Rationale:** Memory is persistent state. Must be reliable, consistent, and secure.

**Items:**
- **#31: Functional Memory Enable and Disable Control**
  - Make `agent.memory_enabled` functional
  - Runtime toggle without restart
  - Clear memory state on disable
  
- **#32: SQLite Concurrency Settings**
  - Configure WAL mode for better concurrency
  - Set appropriate busy timeout
  - Add connection pooling
  
- **#33: Database Schema Versioning and Migrations**
  - Implement Alembic or custom migration system
  - Version tracking in database
  - Automatic migration on startup
  
- **#34: Cross-Store Retention Consistency**
  - Unified retention policy across stores
  - Consistent pruning schedules
  - Prevent orphaned data
  
- **#35: Embedding Dimension Validation**
  - Validate vector dimensions at ingestion
  - Reject mismatched dimensions
  - Clear error messages

**Deliverables:**
- `memory/migrations/` directory with migration scripts
- `memory/config.py` with concurrency settings
- Enhanced `memory/sqlite_store.py`
- `memory/retention.py` for unified policies
- 20+ memory system tests

---

### Phase 7: API & Service Hardening (Items 6, 21, 36, 37, 38)
**Priority:** Medium  
**Dependencies:** Phase 2, Phase 3  
**Estimated Duration:** 4-5 hours

**Rationale:** Production deployment requires robust service management and monitoring.

**Items:**
- **#6: API Import and Startup Separation**
  - Separate FastAPI app creation from startup
  - Enable testing without side effects
  - Lazy initialization of resources
  
- **#21: Clean PocketFlow Termination**
  - Graceful shutdown on SIGTERM/SIGINT
  - Complete in-flight requests
  - Close resources properly
  
- **#36: Unified Runtime Entrypoint and Service Installation**
  - Single `main.py` for all modes
  - Consistent CLI interface
  - Simplified systemd service setup
  
- **#37: Service Permissions, Enablement, and Boot Lifecycle**
  - Proper systemd service configuration
  - Non-root execution
  - Automatic restart on failure
  
- **#38: Real Readiness and Health Checks**
  - Distinguish startup from ready state
  - Deep health checks (DB, LLM, tools)
  - Kubernetes-compatible endpoints

**Deliverables:**
- Enhanced `main.py` with unified entrypoint
- `core/lifecycle.py` for shutdown handling
- `api/health.py` with deep checks
- Updated `systemd/` templates
- Service deployment documentation

---

### Phase 8: Observability & Testing (Item 39)
**Priority:** High  
**Dependencies:** All previous phases  
**Estimated Duration:** 3-4 hours

**Rationale:** Final hardening requires comprehensive testing and secure logging.

**Items:**
- **#39: Sensitive Log Redaction and Foundation Test Coverage**
  - Redact API keys, tokens, passwords in logs
  - Add structured logging with context
  - Achieve 90%+ test coverage for core modules
  - Add integration tests for all modes
  - Performance benchmarks for critical paths

**Deliverables:**
- `core/logging.py` with redaction
- Comprehensive test suite (target: 150+ tests)
- `tests/integration/` directory
- `tests/benchmarks/` directory
- Coverage report and CI integration

---

## Implementation Guidelines

### Before Starting Each Phase

1. **Review Dependencies** - Ensure prerequisite phases are complete
2. **Read Specifications** - Review relevant items in detail
3. **Design First** - Write design doc before coding (15-30 min max)
4. **Test Plan** - Define test cases upfront
5. **Update Baseline** - Check current state in `BASELINE.md`

### During Implementation

1. **One Item at a Time** - Complete fully before moving to next
2. **Test-Driven** - Write tests first or alongside code
3. **Small Commits** - Atomic changes with clear messages
4. **Documentation** - Update docs with each change
5. **Review** - Self-review before marking complete

### After Each Phase

1. **Run Full Test Suite** - Ensure no regressions
2. **Update BASELINE.md** - Document new capabilities
3. **Update NEXT_PHASE.md** - Mark phase complete, note next
4. **Security Audit** - Run Semgrep, Bandit, pip-audit
5. **Performance Check** - Verify no significant degradation

---

## Risk Management

### High-Risk Items (Require Extra Care)

- **#3: API Authentication** - Breaking change for existing API users
- **#4: API User Identity Boundary** - Complex isolation requirements
- **#26: Unified Authorization Gate** - Touches all execution paths
- **#33: Database Migrations** - Risk of data loss if not careful

### Mitigation Strategies

1. **Feature Flags** - Enable gradual rollout
2. **Backward Compatibility** - Maintain old behavior with deprecation warnings
3. **Backup Strategy** - Automatic database backups before migrations
4. **Rollback Plan** - Document rollback steps for each phase
5. **Staging Environment** - Test in non-production first

---

## Success Criteria

### Per-Phase Criteria

- All items in phase implemented and tested
- No test regressions
- Documentation updated
- Security audit passed
- Performance benchmarks met

### Overall Completion Criteria

- All 39 items implemented
- Test count increased to 150+
- Test coverage ≥90% for core modules
- Zero high-severity security findings
- All configuration flags functional
- Production deployment successful

---

## Timeline Estimate

| Phase | Duration | Cumulative |
|---|---|---|
| Phase 1: Configuration | 4-6 hours | 6 hours |
| Phase 2: Providers | 2-3 hours | 9 hours |
| Phase 3: Security | 6-8 hours | 17 hours |
| Phase 4: Tools | 8-10 hours | 27 hours |
| Phase 5: Plugins/Skills | 3-4 hours | 31 hours |
| Phase 6: Memory | 4-6 hours | 37 hours |
| Phase 7: API/Service | 4-5 hours | 42 hours |
| Phase 8: Observability | 3-4 hours | 46 hours |

**Total Estimated Duration:** 42-46 hours (~5-6 working days at 8 hours/day, or 2-3 days at aggressive pace)

**Note:** Timeline assumes experienced developer familiar with codebase. Baseline was built in 1 day, hardening should take 2-3 days with focused effort.

---

## Aggressive Implementation Strategy

### Day 1: Core Foundation (Phases 1-3)
- **Morning (4 hours):** Phase 1 + Phase 2
- **Afternoon (4 hours):** Phase 3 (Security)
- **Evening (2 hours):** Testing and documentation

### Day 2: Extensions & Memory (Phases 4-6)
- **Morning (4 hours):** Phase 4 (Tools) - first half
- **Afternoon (4 hours):** Phase 4 (Tools) - second half + Phase 5
- **Evening (2 hours):** Phase 6 (Memory)

### Day 3: Production & Polish (Phases 7-8)
- **Morning (4 hours):** Phase 7 (API/Service)
- **Afternoon (3 hours):** Phase 8 (Observability)
- **Evening (2 hours):** Final audit, documentation, deployment

**Total:** 3 days aggressive pace, or 5-6 days at normal pace

---

## Next Steps

1. ✅ Review this workflow (DONE)
2. Create Phase 1 detailed design doc
3. Set up project tracking (GitHub issues/milestones)
4. Begin Phase 1 implementation
5. Maintain momentum - one phase per session

---

## Appendix: Item Cross-Reference

Quick reference to find items by number:

| # | Title | Phase | Est. Time |
|---|---|---|---|
| 1 | Telegram Access Default | 3 | 45 min |
| 2 | Tool Permission and Approval | 4 | 90 min |
| 3 | API Authentication | 3 | 90 min |
| 4 | API User Identity Boundary | 3 | 90 min |
| 5 | Atomic Configuration Updates | 1 | 60 min |
| 6 | API Import and Startup Separation | 7 | 45 min |
| 7 | Plugin Enablement Enforcement | 5 | 30 min |
| 8 | Plugin Contract Validation | 5 | 45 min |
| 9 | Plugin Load Failure Policy | 5 | 45 min |
| 10 | Skill Metadata Validation | 5 | 45 min |
| 11 | Skill and Tool Name Collision Protection | 4 | 45 min |
| 12 | Unified Tool Registration | 4 | 90 min |
| 13 | Startup Registry Validation | 4 | 45 min |
| 14 | Tool Argument Validation | 4 | 60 min |
| 15 | Tool Error Isolation | 4 | 45 min |
| 16 | Async-Safe Tool Execution | 4 | 60 min |
| 17 | Tool Timeout and Cancellation | 4 | 75 min |
| 18 | Typed Tool Results | 4 | 45 min |
| 19 | Tool Output and Context Limits | 4 | 45 min |
| 20 | Explicit Runtime Dependency Injection | 2 | 90 min |
| 21 | Clean PocketFlow Termination | 7 | 60 min |
| 22 | Strict Configuration Schema | 1 | 90 min |
| 23 | Runtime Enforcement for Configuration Flags | 1 | 60 min |
| 24 | Fail-Fast Capability Whitelists | 1 | 45 min |
| 25 | Provider Startup Validation | 2 | 60 min |
| 26 | Unified Action Authorization Gate | 3 | 90 min |
| 27 | Stronger Prompt-Injection Filtering | 3 | 60 min |
| 28 | Input Normalization and Type Handling | 3 | 60 min |
| 29 | Negation-Aware Memory Approval | 3 | 45 min |
| 30 | Normalized Dangerous-Content Detection | 3 | 60 min |
| 31 | Functional Memory Enable and Disable Control | 6 | 45 min |
| 32 | SQLite Concurrency Settings | 6 | 45 min |
| 33 | Database Schema Versioning and Migrations | 6 | 120 min |
| 34 | Cross-Store Retention Consistency | 6 | 60 min |
| 35 | Embedding Dimension Validation | 6 | 30 min |
| 36 | Unified Runtime Entrypoint and Service Installation | 7 | 60 min |
| 37 | Service Permissions, Enablement, and Boot Lifecycle | 7 | 60 min |
| 38 | Real Readiness and Health Checks | 7 | 60 min |
| 39 | Sensitive Log Redaction and Foundation Test Coverage | 8 | 180 min |

**Total Individual Time:** ~42 hours
