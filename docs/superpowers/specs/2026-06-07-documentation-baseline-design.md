# Documentation Baseline Design

> **Status: Approved and active.**
>
> This specification defines the canonical documentation policy for the current
> idolhub baseline. Older specifications and plans are historical records.

## Goal

Keep repository documentation consistent with the implemented code and remove
all ambiguity around configuration ownership, feature status, and roadmap
numbering.

## Sources Of Truth

The documentation hierarchy is:

1. Current code and tests.
2. `config.example.json` for the runnable default configuration template.
3. `docs/BASELINE.md` for implemented and deferred scope.
4. Active reference documents: `README.md`, `docs/CONFIG.md`,
   `docs/DEPENDENCIES.md`, and `docs/CONTRIBUTING.md`.
5. Historical specifications and plans.

When a historical document conflicts with an active reference, the active
reference wins.

## Configuration Policy

- `config.example.json` is tracked and contains placeholders only.
- `config.json` is a required local runtime file.
- `config.json` is ignored by Git and must never be committed.
- Secrets remain outside the repository and are injected through environment
  variables.
- Git history must not contain `config.json`.

## Status Policy

The active roadmap uses three labels instead of global phase numbers:

- **Implemented**: present in code and covered by tests.
- **Deferred**: intentionally not started.
- **Not scheduled**: possible future work without an approved plan.

Historical phase numbers remain in old plans only. Their banners must state
that those numbers are local to the historical plan.

## Historical Documents

Historical specifications and non-empty plans remain available for provenance.
Each receives a status banner that:

- identifies it as implemented or superseded;
- points to `docs/BASELINE.md`;
- states that tracked `config.json` references are obsolete;
- states that unchecked boxes are not current implementation status.

Empty historical plan files are removed because they contain no recoverable
design or execution record.

## Verification

Documentation cleanup is complete when:

- active docs agree on configuration policy and feature status;
- tracked paths referenced by active docs exist;
- no active doc claims that `config.json` is tracked;
- tests and security audit results are recorded accurately;
- local `main` and GitHub `main` point to the same rewritten history;
- `git log --all -- config.json` returns no commits.
