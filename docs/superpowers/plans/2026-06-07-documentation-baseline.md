# Documentation Baseline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:executing-plans` to execute this plan task-by-task.

**Goal:** Align all active documentation with the implemented idolhub baseline
and remove `config.json` from repository history.

**Architecture:** Use `docs/BASELINE.md` as the canonical status document.
Active references describe current behavior; historical specs and plans retain
provenance through explicit supersession banners.

**Tech Stack:** Markdown, JSON, TOML, Git, GitHub CLI.

---

### Task 1: Establish Canonical Baseline

**Files:**
- Create: `docs/BASELINE.md`
- Modify: `README.md`

- [x] Document implemented, deferred, and unscheduled scope.
- [x] Document the configuration ownership policy.
- [x] Replace obsolete project structure and roadmap entries.

### Task 2: Align Active References

**Files:**
- Modify: `docs/CONFIG.md`
- Modify: `docs/CONTRIBUTING.md`
- Modify: `docs/DEPENDENCIES.md`
- Modify: `dashboard/README.md`
- Modify: `config.example.json`
- Modify: `pyproject.toml`
- Modify: `.gitignore`
- Modify: `scripts/setup.sh`
- Modify: `systemd/idolhub.service.template`

- [x] Make `config.example.json` the only tracked configuration template.
- [x] Mark `config.json` as local and ignored.
- [x] Remove global phase numbering from active dependency and dashboard docs.
- [x] Ensure all documented paths and extension points match the code.

### Task 3: Refresh Audit Record

**Files:**
- Modify: `hasilaudit.md`

- [x] Record the latest test, Semgrep, pip-audit, Bandit, and Ruff results.
- [x] Replace local `file://` links with repository-relative paths.
- [x] Separate accepted legacy findings from clean phase-memory findings.

### Task 4: Mark Historical Material

**Files:**
- Modify: `docs/superpowers/specs/*.md`
- Modify: `docs/superpowers/plans/*.md`
- Delete: empty historical plan files

- [x] Add implemented/superseded banners.
- [x] State that old phase numbers are local historical labels.
- [x] State that tracked `config.json` instructions are obsolete.

### Task 5: Verify Documentation

- [x] Validate JSON and TOML.
- [x] Check Markdown links and referenced repository paths.
- [x] Search for contradictory active statements.
- [x] Run the full test suite.
- [x] Run security audit tools.

### Task 6: Rewrite And Publish Git History

- [ ] Commit documentation cleanup.
- [ ] Rewrite all repository refs to remove `config.json`.
- [ ] Force-push with lease through GitHub authentication.
- [ ] Verify local and GitHub `main` are identical.
- [ ] Verify no reachable commit contains `config.json`.
