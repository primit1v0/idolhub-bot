#!/usr/bin/env bash
#
# run_audit.sh - Comprehensive security and quality audit for idolhub
#
# Prerequisites:
#   - pipx installed (sudo apt install pipx)
#   - Tools installed via pipx:
#     * pipx install bandit
#     * pipx install safety
#     * pipx install semgrep
#     * pipx install pip-audit
#
# Usage:
#   ./scripts/run_audit.sh [--fix]
#
# Options:
#   --fix    Auto-fix issues where possible (ruff only)

set -euo pipefail

# ============================================================================
# Configuration
# ============================================================================

readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m'

readonly PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
readonly AUDIT_REPORT="hasilaudit.md"
readonly TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# ============================================================================
# Functions
# ============================================================================

log_info() {
    echo -e "${BLUE}$1${NC}"
}

log_success() {
    echo -e "${GREEN}$1${NC}"
}

log_warning() {
    echo -e "${YELLOW}$1${NC}"
}

log_error() {
    echo -e "${RED}$1${NC}"
}

init_report() {
    cat > "$AUDIT_REPORT" << EOF
# idolhub Security & Quality Audit Report

**Generated:** $TIMESTAMP
**Project:** idolhub
**Location:** $PROJECT_ROOT

---

EOF
}

append_section() {
    local section_title="$1"
    
    {
        echo "## $section_title"
        echo ""
        echo '```'
    } >> "$AUDIT_REPORT"
}

close_section() {
    {
        echo '```'
        echo ""
    } >> "$AUDIT_REPORT"
}

run_pytest() {
    log_info "[1/6] Running pytest..."
    append_section "1. Test Suite (pytest)"
    
    if uv run pytest -v --tb=short 2>&1 | tee -a "$AUDIT_REPORT"; then
        log_success "✓ Tests: PASSED"
        PYTEST_STATUS="✅ PASSED"
    else
        log_error "✗ Tests: FAILED"
        PYTEST_STATUS="❌ FAILED"
    fi
    
    close_section
}

run_ruff() {
    log_info "[2/6] Running ruff..."
    append_section "2. Code Quality (ruff)"
    
    if [[ "$FIX_MODE" == true ]]; then
        echo "Running ruff with --fix..." | tee -a "$AUDIT_REPORT"
        if uv run ruff check --fix . 2>&1 | tee -a "$AUDIT_REPORT"; then
            log_success "✓ Ruff: PASSED (with fixes)"
            RUFF_STATUS="✅ PASSED (auto-fixed)"
        else
            log_warning "⚠ Ruff: FIXED with warnings"
            RUFF_STATUS="⚠️ FIXED (warnings remain)"
        fi
    else
        if uv run ruff check . 2>&1 | tee -a "$AUDIT_REPORT"; then
            log_success "✓ Ruff: PASSED"
            RUFF_STATUS="✅ PASSED"
        else
            log_error "✗ Ruff: FAILED"
            RUFF_STATUS="❌ FAILED"
        fi
    fi
    
    close_section
}

run_bandit() {
    log_info "[3/6] Running bandit..."
    append_section "3. Security Scan (bandit)"
    
    if bandit -r . -ll -f txt 2>&1 | tee -a "$AUDIT_REPORT"; then
        log_success "✓ Bandit: PASSED"
        BANDIT_STATUS="✅ PASSED"
    else
        log_error "✗ Bandit: FAILED"
        BANDIT_STATUS="❌ FAILED"
    fi
    
    close_section
}

run_semgrep() {
    log_info "[4/6] Running semgrep..."
    append_section "4. Static Analysis (semgrep)"
    
    if semgrep --config=auto --quiet . 2>&1 | tee -a "$AUDIT_REPORT"; then
        log_success "✓ Semgrep: PASSED"
        SEMGREP_STATUS="✅ PASSED"
    else
        log_error "✗ Semgrep: FAILED"
        SEMGREP_STATUS="❌ FAILED"
    fi
    
    close_section
}

run_pip_audit() {
    log_info "[5/6] Running pip-audit..."
    append_section "5. Dependency Audit (pip-audit)"
    
    if uv run pip-audit 2>&1 | tee -a "$AUDIT_REPORT"; then
        log_success "✓ pip-audit: PASSED"
        PIPAUDIT_STATUS="✅ PASSED"
    else
        log_error "✗ pip-audit: FAILED"
        PIPAUDIT_STATUS="❌ FAILED"
    fi
    
    close_section
}

run_safety() {
    log_info "[6/6] Running safety..."
    append_section "6. Vulnerability Check (safety)"
    
    if safety check --json 2>&1 | tee -a "$AUDIT_REPORT"; then
        log_success "✓ Safety: PASSED"
        SAFETY_STATUS="✅ PASSED"
    else
        log_warning "⚠ Safety: Check output for details"
        SAFETY_STATUS="⚠️ CHECK OUTPUT"
    fi
    
    close_section
}

write_summary() {
    {
        echo "---"
        echo ""
        echo "## Summary"
        echo ""
        echo "| Tool | Status |"
        echo "|------|--------|"
        echo "| pytest | $PYTEST_STATUS |"
        echo "| ruff | $RUFF_STATUS |"
        echo "| bandit | $BANDIT_STATUS |"
        echo "| semgrep | $SEMGREP_STATUS |"
        echo "| pip-audit | $PIPAUDIT_STATUS |"
        echo "| safety | $SAFETY_STATUS |"
        echo ""
        echo "**Report saved to:** \`$AUDIT_REPORT\`"
    } >> "$AUDIT_REPORT"
}

print_final_status() {
    echo ""
    log_info "=== Final Status ==="
    
    [[ "$PYTEST_STATUS" == *"FAILED"* ]] && \
        log_error "❌ Tests failed - review test output"
    
    [[ "$RUFF_STATUS" == *"FAILED"* ]] && \
        log_warning "⚠️  Code quality issues - run with --fix to auto-correct"
    
    [[ "$BANDIT_STATUS" == *"FAILED"* ]] && \
        log_error "❌ Security issues found - review bandit output"
    
    [[ "$SEMGREP_STATUS" == *"FAILED"* ]] && \
        log_error "❌ SAST issues found - review semgrep output"
}

check_exit_status() {
    if [[ "$BANDIT_STATUS" == *"FAILED"* ]] || [[ "$SEMGREP_STATUS" == *"FAILED"* ]]; then
        echo ""
        log_error "❌ Critical security issues found. Review $AUDIT_REPORT"
        exit 1
    else
        echo ""
        log_success "✅ Security checks passed. See $AUDIT_REPORT for details."
        exit 0
    fi
}

# ============================================================================
# Main
# ============================================================================

main() {
    # Parse arguments
    FIX_MODE=false
    [[ "${1:-}" == "--fix" ]] && FIX_MODE=true
    
    # Change to project root
    cd "$PROJECT_ROOT"
    
    # Header
    log_info "=== idolhub Security & Quality Audit ==="
    log_info "Started: $TIMESTAMP"
    echo ""
    
    # Initialize report
    init_report
    
    # Run all audits
    run_pytest
    run_ruff
    run_bandit
    run_semgrep
    run_pip_audit
    run_safety
    
    # Write summary
    write_summary
    
    # Print results
    echo ""
    log_info "=== Audit Complete ==="
    log_success "Report saved to: $AUDIT_REPORT"
    
    print_final_status
    check_exit_status
}

# Run main function
main "$@"