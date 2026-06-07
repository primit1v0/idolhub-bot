# Historical Documentation

This directory contains **historical** specifications and planning documents from the initial development of idolhub. These documents are kept for reference only and are **not active guides** for current work.

## ⚠️ Important Notice

**DO NOT implement features from documents in this directory without explicit approval.**

All active specifications are in [`../specs/`](../specs/). Always check [`../BASELINE.md`](../BASELINE.md) and [`../NEXT_PHASE.md`](../NEXT_PHASE.md) for current project status.

## Contents

### Historical Specifications (`specs/`)

These are design documents from the initial development phases:

- `2026-06-06-async-pocketflow-agent-design.md` - Original async agent design
- `2026-06-06-entrypoint-systemd-design.md` - Service deployment design
- `2026-06-06-idolhub-design.md` - Initial project design
- `2026-06-07-database-auto-pruning-design.md` - Auto-pruning feature
- `2026-06-07-documentation-baseline-design.md` - Documentation structure
- `2026-06-07-fts5-context-threading-design.md` - FTS5 threading feature
- `2026-06-07-sqlite-vector-memory-design.md` - Vector memory design
- `2026-06-07-baseline-foundation-hardening.md` - Original 39-item hardening spec (superseded)
- `HARDENING_IMPLEMENTATION_WORKFLOW.md` - Original workflow (superseded)

### Historical Plans (`plans/`)

Planning documents and roadmaps from initial development.

## Why Keep These?

These documents provide:
- Historical context for design decisions
- Reference for implemented features
- Learning material for understanding the codebase evolution
- Audit trail for project development

## Current Active Documentation

For current work, always refer to:

1. **[`../AGENT_GUIDE.md`](../AGENT_GUIDE.md)** - Complete guide for AI agents
2. **[`../BASELINE.md`](../BASELINE.md)** - Current project status
3. **[`../NEXT_PHASE.md`](../NEXT_PHASE.md)** - Next phase handoff
4. **[`../specs/`](../specs/)** - Active specifications only

## Superseded Documents

### 39-Item Foundation Hardening

The original 39-item hardening specification has been **superseded** by a phased approach:

- **Phase 1:** Configuration Hardening ✅ Complete
- **Phase 2:** Secrets Management 📋 Next
- **Phase 3-5:** Future phases (planned)

The phased approach provides:
- Clearer scope per phase
- Better testability
- Incremental delivery
- Easier maintenance

### Original Implementation Workflow

The original workflow document has been superseded by phase-specific implementation plans in [`../specs/`](../specs/).

---

**Last Updated:** 2026-06-07  
**Purpose:** Historical reference only  
**For Current Work:** See [`../specs/`](../specs/)
