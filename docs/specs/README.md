# Active Specifications

This directory contains **active** technical specifications for the idolhub project. These documents guide current and future development work.

## Current Specifications

### Phase 1: Configuration Hardening ✅ COMPLETE
- **File:** [`phase1-config-validation-design.md`](phase1-config-validation-design.md)
- **Status:** Implemented and tested (113/113 tests passing)
- **Completion:** June 7, 2026
- **Summary:** Pydantic-based configuration validation with zero-tolerance approach

### Phase 2: Secrets Management 📋 NEXT
- **File:** [`phase2-secrets-management-design.md`](phase2-secrets-management-design.md)
- **Status:** Planned (design complete, ready for implementation)
- **Estimated:** 3 weeks, 15+ new tests
- **Summary:** Secure secrets backend (Vault/AWS) with rotation and audit logging

## Document Structure

Each specification document should include:

1. **Status** - Current state (Proposed/In Progress/Complete)
2. **Objectives** - What the phase aims to accomplish
3. **Architecture** - High-level design and components
4. **Implementation Plan** - Step-by-step guide with timeline
5. **Testing Strategy** - Test requirements and coverage
6. **Success Criteria** - Clear acceptance criteria
7. **Migration Guide** - How to upgrade from previous phase

## Historical Specifications

Older specifications and planning documents are archived in [`../superpowers/`](../superpowers/). These are kept for historical reference but are not active guides for current work.

### Archived Documents
- 39-item foundation hardening specification (superseded by phased approach)
- Original implementation workflow (superseded by phase-specific designs)
- Historical design documents from initial development

## For AI Agents

**Before starting work:**
1. Read [`../AGENT_GUIDE.md`](../AGENT_GUIDE.md) - Complete agent handbook
2. Check [`../BASELINE.md`](../BASELINE.md) - Current project status
3. Review the relevant phase specification in this directory
4. Follow the implementation plan exactly as documented

**Critical Rules:**
- Only implement features from **active** specifications (this directory)
- Do not implement features from historical documents without approval
- Always run tests before and after changes
- Never bypass validation or hardcode secrets
- Update documentation as you implement

## Adding New Specifications

When creating a new phase specification:

1. **File naming:** `phase{N}-{feature-name}-design.md`
2. **Location:** This directory (`docs/specs/`)
3. **Template:** Follow the structure of existing phase documents
4. **Review:** Get approval before marking as "active"
5. **Update:** Add entry to this README

## Questions?

- For development guidelines: [`../EXECUTION_PROTOCOL.md`](../EXECUTION_PROTOCOL.md)
- For configuration help: [`../CONFIG.md`](../CONFIG.md)
- For contributing: [`../CONTRIBUTING.md`](../CONTRIBUTING.md)
- For next steps: [`../NEXT_PHASE.md`](../NEXT_PHASE.md)

---

**Last Updated:** 2026-06-07  
**Maintained By:** Project Team
