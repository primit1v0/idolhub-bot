#!/usr/bin/env bash
#
# install_audit_tools.sh - Install security audit tools via pipx
#
# This script installs the following tools:
#   - bandit: Security issue scanner
#   - safety: Dependency vulnerability checker
#   - semgrep: Static analysis security testing
#   - pip-audit: Python package vulnerability scanner
#
# Prerequisites:
#   - Python 3.11+ installed
#   - pipx installed (or will be installed by this script)
#
# Usage:
#   ./scripts/install_audit_tools.sh

set -euo pipefail

# ============================================================================
# Configuration
# ============================================================================

readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m'

readonly TOOLS=(
    "bandit"
    "safety"
    "semgrep"
    "pip-audit"
)

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

check_pipx() {
    if command -v pipx &> /dev/null; then
        log_success "✓ pipx already installed"
        return 0
    fi
    return 1
}

install_pipx() {
    log_warning "pipx not found. Installing pipx..."
    
    if command -v apt &> /dev/null; then
        log_info "Installing via apt..."
        sudo apt update
        sudo apt install -y pipx
    else
        log_info "Installing via pip..."
        python3 -m pip install --user pipx
    fi
    
    pipx ensurepath
    log_success "✓ pipx installed"
    log_warning "⚠ You may need to restart your shell or run: source ~/.bashrc"
}

verify_pipx() {
    if ! command -v pipx &> /dev/null; then
        log_error "✗ pipx installation failed or not in PATH"
        log_warning "Try running: export PATH=\"\$HOME/.local/bin:\$PATH\""
        exit 1
    fi
}

is_tool_installed() {
    local tool_name="$1"
    pipx list 2>/dev/null | grep -q "package $tool_name"
}

install_tool() {
    local tool_name="$1"
    
    log_info "Installing $tool_name..."
    
    if is_tool_installed "$tool_name"; then
        log_success "✓ $tool_name already installed"
        return 0
    fi
    
    if pipx install "$tool_name"; then
        log_success "✓ $tool_name installed successfully"
        return 0
    else
        log_error "✗ Failed to install $tool_name"
        return 1
    fi
}

verify_tool() {
    local tool_name="$1"
    local version_flag="${2:---version}"
    
    if command -v "$tool_name" &> /dev/null; then
        local version
        version=$("$tool_name" "$version_flag" 2>&1 | head -n1)
        log_success "✓ $tool_name: $version"
        return 0
    else
        log_error "✗ $tool_name: NOT FOUND"
        return 1
    fi
}

print_next_steps() {
    echo ""
    log_success "=== All tools installed successfully ==="
    echo ""
    log_info "Next steps:"
    echo "1. Run audit: ./scripts/run_audit.sh"
    echo "2. Or manually: bandit -r . && semgrep --config=auto ."
    echo ""
}

print_troubleshooting() {
    echo ""
    log_error "=== Some tools failed to install ==="
    echo ""
    log_warning "Troubleshooting:"
    echo "1. Ensure pipx is in PATH: export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo "2. Restart your shell: source ~/.bashrc"
    echo "3. Try manual install: pipx install <tool-name>"
    echo ""
}

# ============================================================================
# Main
# ============================================================================

main() {
    log_info "=== Installing Security Audit Tools ==="
    echo ""
    
    # Check and install pipx
    if ! check_pipx; then
        install_pipx
        echo ""
    fi
    
    verify_pipx
    
    # Install tools
    echo ""
    log_info "Installing audit tools..."
    echo ""
    
    local failed=0
    for tool in "${TOOLS[@]}"; do
        if ! install_tool "$tool"; then
            ((failed++))
        fi
        echo ""
    done
    
    # Verify installations
    echo ""
    log_info "=== Verifying installations ==="
    echo ""
    
    local verification_failed=0
    verify_tool "bandit" || ((verification_failed++))
    verify_tool "safety" || ((verification_failed++))
    verify_tool "semgrep" "--version" || ((verification_failed++))
    verify_tool "pip-audit" || ((verification_failed++))
    
    # Print results
    if [[ $verification_failed -eq 0 ]]; then
        print_next_steps
        exit 0
    else
        print_troubleshooting
        exit 1
    fi
}

# Run main function
main "$@"