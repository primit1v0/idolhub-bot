# Security Audit Scripts

Automated security and quality audit tools for idolhub project.

## Quick Start

```bash
# 1. Install audit tools (one-time setup)
./scripts/install_audit_tools.sh

# 2. Run comprehensive audit
./scripts/run_audit.sh

# 3. Run audit with auto-fix (ruff only)
./scripts/run_audit.sh --fix
```

---

## Scripts Overview

### 1. `install_audit_tools.sh`

**Purpose:** One-time installation of all security audit tools via pipx.

**What it installs:**
- `bandit` - Python security issue scanner
- `safety` - Dependency vulnerability checker  
- `semgrep` - Static analysis security testing (SAST)
- `pip-audit` - Python package vulnerability scanner

**Prerequisites:**
- Python 3.11+
- Internet connection

**Usage:**
```bash
./scripts/install_audit_tools.sh
```

**What it does:**
1. Checks if pipx is installed (installs if missing)
2. Installs all 4 audit tools via pipx
3. Verifies installations
4. Shows next steps

**Output:**
- ✅ Success: All tools installed and verified
- ❌ Failure: Shows troubleshooting steps

---

### 2. `run_audit.sh`

**Purpose:** Run comprehensive security and quality audit, generate markdown report.

**What it checks:**
1. **pytest** - Test suite execution
2. **ruff** - Code quality and style (PEP 8, complexity, etc)
3. **bandit** - Security vulnerabilities (SQL injection, hardcoded secrets, etc)
4. **semgrep** - SAST analysis (OWASP Top 10, CWE patterns)
5. **pip-audit** - Known CVEs in dependencies
6. **safety** - Alternative dependency vulnerability check

**Usage:**
```bash
# Standard audit
./scripts/run_audit.sh

# Auto-fix ruff issues
./scripts/run_audit.sh --fix
```

**Output:**
- Console: Real-time colored output for each tool
- File: `hasilaudit.md` - Complete audit report with summary table

**Exit codes:**
- `0` - All critical checks passed
- `1` - Critical issues found (pytest, bandit, or semgrep failed)

---

## Audit Report Format

The generated `hasilaudit.md` includes:

```markdown
# idolhub Security & Quality Audit Report

**Generated:** 2026-06-07 04:00:00 UTC
**Project:** idolhub
**Location:** /home/sandi/PocketFlow/idolhub

---

## 1. Test Suite (pytest)
[output]

## 2. Code Quality (ruff)
[output]

## 3. Security Scan (bandit)
[output]

## 4. Static Analysis (semgrep)
[output]

## 5. Dependency Audit (pip-audit)
[output]

## 6. Vulnerability Check (safety)
[output]

---

## Summary

| Tool | Status |
|------|--------|
| pytest | ✅ PASSED |
| ruff | ❌ FAILED |
| bandit | ✅ PASSED |
| semgrep | ✅ PASSED |
| pip-audit | ✅ PASSED |
| safety | ⚠️ CHECK OUTPUT |
```

---

## Tool Details

### bandit
- **Severity levels:** `-ll` (low and above)
- **Scope:** Recursive scan of entire project
- **Common findings:** 
  - B201: Flask debug mode
  - B608: SQL injection risks
  - B105: Hardcoded passwords
  - B108: Insecure temp file usage

### semgrep
- **Config:** `--config=auto` (community rules)
- **Rulesets:** OWASP Top 10, CWE patterns, language-specific
- **Common findings:**
  - SQL injection
  - XSS vulnerabilities
  - Insecure deserialization
  - Path traversal

### pip-audit
- **Database:** PyPI Advisory Database + OSV
- **Scope:** All installed packages in current environment
- **Output:** CVE IDs, severity, affected versions

### safety
- **Database:** Safety DB (free tier)
- **Format:** JSON output for parsing
- **Note:** May require API key for full features

### ruff
- **Rules:** 100+ linters (pycodestyle, pyflakes, isort, etc)
- **Auto-fix:** `--fix` flag applies safe fixes
- **Config:** `.ruff.toml` or `pyproject.toml`

---

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Security Audit

on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install audit tools
        run: ./scripts/install_audit_tools.sh
      
      - name: Run audit
        run: ./scripts/run_audit.sh
      
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: audit-report
          path: hasilaudit.md
```

---

## Troubleshooting

### pipx not in PATH
```bash
export PATH="$HOME/.local/bin:$PATH"
source ~/.bashrc
```

### Tool not found after install
```bash
# Verify pipx installations
pipx list

# Reinstall specific tool
pipx uninstall bandit
pipx install bandit
```

### Permission denied
```bash
chmod +x scripts/*.sh
```

### uv not found (for pytest/ruff)
```bash
# Install uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Manual Tool Usage

If you prefer running tools individually:

```bash
# Security scan
bandit -r . -ll -f txt

# SAST analysis
semgrep --config=auto --quiet .

# Dependency audit
pip-audit

# Vulnerability check
safety check --json

# Code quality
ruff check .
ruff check --fix .

# Tests
pytest -v
```

---

## Best Practices

1. **Run before every commit** - Catch issues early
2. **Fix critical issues first** - Prioritize security over style
3. **Review false positives** - Use `# nosec` or `# noqa` sparingly
4. **Keep tools updated** - `pipx upgrade-all`
5. **Track trends** - Compare reports over time
6. **Automate in CI** - Fail builds on critical issues

---

## Related Files

- `audittools.md` - Original manual installation guide
- `hasilaudit.md` - Generated audit report (gitignored)
- `.ruff.toml` - Ruff configuration
- `pyproject.toml` - Project metadata and tool configs

---

## Support

For issues or questions:
1. Check tool documentation: `<tool> --help`
2. Review `hasilaudit.md` for detailed output
3. Consult `audittools.md` for manual setup
