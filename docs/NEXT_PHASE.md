# Next Phase

**Status:** Proposed
**Updated:** June 7, 2026

This is the handoff document for the next work session. It applies to every
model and contributor, not only Codex.

## Read First

1. `docs/BASELINE.md`
2. `docs/NEXT_PHASE.md`
3. `docs/specs/2026-06-07-baseline-foundation-hardening.md`
4. The relevant code and tests before changing behavior

## Current Context

- The current baseline is implemented and remains the source of truth.
- The next phase is foundation hardening, not feature expansion.
- Dashboard WebUI remains deferred.
- The active specification contains 39 proposed work titles.
- Implementation schemas and task plans have not been written yet.

## Next Action

Review the 39 titles, choose one focused item, then write its design and
implementation plan before changing code.

## Scope Rules

- Keep changes small and aligned with existing project patterns.
- Do not combine unrelated titles into one implementation.
- Update the baseline only after behavior is implemented and verified.
- Keep `config.json`, secrets, databases, logs, and workspace data local.
- Historical files under `docs/superpowers/` are context only.
