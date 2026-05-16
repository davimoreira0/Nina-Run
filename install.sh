#!/bin/bash

# ==============================================================================
# Nina-Run - Tool Installation Script
# ==============================================================================
# This script installs all system dependencies required to run the
# Nina-Run penetration testing tool.
# ==============================================================================

set -e  # Exit if any command fails

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "${GREEN}================================================${NC}"
    echo -e "${GREEN}$1${NC}"
    echo -e "${GREEN}================================================${NC}"
}

print_success() {
    echo -e "${GREEN}[✓] $1${NC}"
}

print_error() {
    echo -e "${RED}[✗] $1${NC}"
}

print_info() {
    echo -e "${YELLOW}[*] $1${NC}"
}

# Check if running as root
if [[ $EUID -ne 0 ]]; then
    print_error "This script must be run with root privileges (use 'sudo')"
    exit 1
fi

print_header "Installing Dependencies - Nina-Run"

# Update package list
print_info "Updating package list..."
apt update -y

# Install tools
print_info "Installing security tools..."

TOOLS=(
    "nmap"
    "dirb"
    "whois"
    "whatweb"
    "host"
    "traceroute"
    "medusa"
    "hping3"
    "lbd"
    "skipfish"
    "sqlmap"
    "sslscan"
    "sublist3r"
    "theharvester"
    "nikto"
    "cewl"
    "ssh"
    "metagoofil"
    "netdiscover"
)

for tool in "${TOOLS[@]}"; do
    if ! command -v "$tool" &> /dev/null; then
        print_info "Installing $tool..."
        apt install -y "$tool" || print_error "Failed to install $tool"
    else
        print_success "$tool is already installed"
    fi
done

print_header "Installation Complete!"
print_success "All dependencies have been installed successfully!"
print_info "You can now run: python3 setup.py"
