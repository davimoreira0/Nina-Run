# 🔓 Nina-Run - Professional Penetration Testing Tool

<div align="center">
  <img src="assets/logo.png">
</div>

![Version](https://img.shields.io/badge/version-2.26-blue)
![Language](https://img.shields.io/badge/language-Python%203-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-In%20Development-orange)

**Nina-Run** is a professional and modular penetration testing (pentest) tool developed in Python. Designed to facilitate security testing and infrastructure reconnaissance, it offers an interactive interface inspired by Metasploit with a complete set of modules for analyzing and testing networks and web applications.

---

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#-usage)
- [Available Modules](#-available-modules)
- [Usage Examples](#-usage-examples)
- [Features](#-features)
- [Legal Notice](#-legal-notice)

---

## ⚡ Quick Start

Get up and running in 5 minutes:

```bash
# Clone the repository
git clone https://github.com/davimoreira0/Nina-Run.git
cd nina-run

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install --upgrade pip
pip install colorama

# Install system tools (Linux/Ubuntu/Debian)
chmod +x install.sh
sudo ./install.sh

# Run Nina-Run
python3 setup.py
```

✅ Done! The interactive interface will start.

---

## Prerequisites

Before installing Nina-Run, ensure your system meets the following requirements:

- **Operating System**: Linux (Ubuntu, Debian, or similar distributions)
- **Python**: Version 3.7 or higher
- **Security Tools**: Required tools will be installed automatically (nmap, dirb, whois, etc.)
- **Administrator Privileges**: Required to install system dependencies

Verify your Python version:
```bash
python3 --version
```

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/davimoreira0/nina-run.git
cd nina-run
```

### Step 2: Create Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Python Dependencies
```bash
pip install --upgrade pip
pip install colorama
```

### Step 4: Install System Tools (Ubuntu/Debian)
```bash
chmod +x install.sh
sudo ./install.sh
```

> **Note**: The script will ask for your administrator password to install the necessary security tools.

### Step 5: Run Nina-Run
```bash
python3 setup.py
```

Ready! The interactive interface of Nina-Run will be initialized.

---

## 🎮 Usage

### Main Commands

Nina-Run's interface works similarly to Metasploit. Here are the basic commands:

| Command | Description |
|---------|-------------|
| `modules` | List all available modules |
| `use <module>` | Load a specific module |
| `show options` | Display options of the active module |
| `set <param> <value>` | Configure a parameter |
| `run` | Execute the module with configured settings |
| `back` | Return to main menu |
| `help` | Display help |
| `exit` | Exit the tool |

### Basic Usage Flow

```bash
# 1. List available modules
modules

# 2. Select a module
use nmap

# 3. View module options
show options

# 4. Configure required parameters
set rhost 192.168.1.1

# 5. Execute the module
run

# 6. Return to main menu
back
```

---

## 📦 Available Modules (19)

| Module | Tool | Description |
|--------|------|-------------|
| `nmap` | nmap | Port and service scanning |
| `dirb` | dirb | Web directory discovery |
| `whois` | whois | Domain information |
| `whatweb` | whatweb | Technology identification |
| `host` | host | DNS resolution |
| `traceroute` | traceroute | Route tracing |
| `medusa` | medusa | SSH brute force attack |
| `hping3` | hping3 | Packet crafting |
| `lbd` | lbd | Load balancer detection |
| `skipfish` | skipfish | Web scanner |
| `sslscan` | sslscan | SSL/TLS analysis |
| `sqlinjection` | sqlmap | SQL Injection testing |
| `sublist3r` | sublist3r | Subdomain enumeration |
| `theharvester` | theHarvester | Email harvesting |
| `nikto` | nikto | Web vulnerability scanner |
| `cewl` | cewl | Wordlist generator |
| `ssh` | ssh | SSH connection |
| `metagoofil` | metagoofil | Metadata extraction |
| `netdiscover` | netdiscover | Host discovery |

---

## 💡 Usage Examples

### Example 1: Network Scan with Nmap
```bash
use nmap
set rhost 192.168.1.100
run
```
This example performs a complete port and service scan on the target.

### Example 2: Web Directory Discovery
```bash
use dirb
set url http://target.com
run
```
Discovers hidden directories and files on the web server.

### Example 3: SSH Brute Force Attack
```bash
use medusa
set host 192.168.1.50
set username admin
set wordlist /usr/share/wordlists/rockyou.txt
run
```
Attempts SSH authentication with different passwords from the wordlist.

### Example 4: Web Vulnerability Check
```bash
use nikto
set url http://target.com
run
```
Performs common vulnerability scanning on web applications.

---

## 📊 Features

- **Lines of Code**: ~3000+ (in development)
- **Implemented Modules**: 19
- **Main Classes**: 19 (NmapModule, DirbModule, WhoisModule, WhatwebModule, HostModule, TracerouteModule, MedusaModule, Hping3Module, LbdModule, SkipfishModule, SslscanModule, SqlinjectionModule, Sublist3rModule, TheharvesterModule, NiktoModule, CewlModule, SshModule, MetagoofilModule, NetdiscoverModule)
- **Interface Functions**: 20+
- **External Tools**: 18+ tools
- **Python Dependencies**: 1 (colorama)

---

## 🔐 Legal Notice

**⚠️ PLEASE READ BEFORE USING**

Nina-Run is an educational tool intended **ONLY** for authorized security testing. Use on systems without explicit authorization is **ILLEGAL**.

### ✅ Responsibilities

- ✅ Use ONLY on systems you own or have explicit permission to test
- ✅ Obtain written authorization before any security testing
- ✅ Respect local laws and data protection regulations
- ✅ Document all security findings responsibly
- ✅ Report vulnerabilities through appropriate channels

### ❌ What NOT to do

- ❌ Do not use on unauthorized systems
- ❌ Do not access third-party data
- ❌ Do not execute destructive attacks
- ❌ Do not publish exploits without responsible disclosure
- ❌ Do not violate data protection or privacy laws

### ⚖️ Disclaimer

The authors of Nina-Run **ARE NOT RESPONSIBLE** for:
- Damage caused by misuse of the tool
- Legal violations resulting from its use
- Data loss or affected systems
- Any malicious activity

**Use at your own risk. You are responsible for your actions.**

---

## 👨‍💻 Author

**Davi Moreira** - [@davimoreira0](https://github.com/davimoreira0)  
**Email**: moreiradavi336@gmail.com

---

## 📋 Project Status

⚠️ **This project is under active development.** New modules and features are being added continuously. Some features may undergo changes or improvements in future versions.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for using **Nina-Run**! For questions, suggestions, or bug reports, please contact us via [GitHub Issues](https://github.com/davimoreira0/nina-run/issues).

**Happy Hacking! 🔓🛡️**

