# 🔓 Nina-Run - Professional Penetration Testing Tool

<div align="center">
  <img src="assets/logo.png">
</div>

![Version](https://img.shields.io/badge/version-2.26-blue)
![Language](https://img.shields.io/badge/language-Python%203-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Under%20Development-orange)

Nina-Run is a professional and modular penetration testing tool developed in Python, designed to facilitate security testing and infrastructure reconnaissance. With an interactive interface inspired by Metasploit, it offers a complete set of modules for analyzing and attacking networks and web applications.

---

## ⚡ Quick Installation

```bash
# 1. Clone the repository
git clone https://github.com/davimoreira0/nina-run.git
cd nina-run

# 2. Install Python dependency
python3 -m venv venv
source venv/bin/activate
pip install colorama

# 3. Install system tools (Ubuntu/Debian)
chmod +x install.sh
./install.sh

# 4. Run
python3 setup.py
```

---

## 🎮 Basic Usage

```bash
# List available modules
modules

# Enter a module
use nmap

# Inside the module: view/configure options
show options
set rhost 192.168.1.1

# Execute
run

# Return to main menu
back
```

---

## 📦 Available Modules (19)

| Module | Tool | Description |
|--------|------------|-----------|
| `nmap` | nmap | Port and service scan |
| `dirb` | dirb | Web directory discovery |
| `whois` | whois | Domain information |
| `whatweb` | whatweb | Technology identification |
| `host` | host | DNS resolution |
| `traceroute` | traceroute | Route tracing |
| `medusa` | medusa | SSH brute force |
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

## 💡 Examples

**Network scan:**
```
use nmap
set rhost 192.168.1.100
run
```

**Directory discovery:**
```
use dirb
set url http://alvo.com
run
```

**SSH brute force:**
```
use medusa
set host 192.168.1.50
set username admin
set wordlist /usr/share/wordlists/rockyou.txt
run
```

---
## 📊 Statistics

- **Lines of Code**: ~3000+ (in development)
- **Implemented Modules**: 19
- **Main Classes**: 19 (NmapModule, DirbModule, WhoisModule, WhatwebModule, HostModule, TracerouteModule, MedusaModule, Hping3Module, LbdModule, SkipfishModule, SslscanModule, SqlinjectionModule, Sublist3rModule, TheharvesterModule, NiktoModule, CewlModule, SshModule, MetagoofilModule, NetdiscoverModule)
- **Interface Functions**: 20+
- **External Tools**: 18+ tools
- **Python Dependencies**: 1 (colorama)

---
## IMPORTANT

**Nina-Run is an educational tool intended ONLY for authorized security testing.** Use on systems without explicit authorization is ILLEGAL.

## Responsibilities

- ✅ Use ONLY on systems you own or have explicit permission to test
- ✅ Obtain written authorization before any security testing
- ✅ Respect local laws and data protection regulations
- ✅ Document all security findings responsibly
- ✅ Report vulnerabilities through appropriate channels

## What NOT to do

- ❌ Do not use on unauthorized systems
- ❌ Do not access third-party data
- ❌ Do not execute destructive attacks
- ❌ Do not publish exploits without responsible disclosure
- ❌ Do not violate data protection or privacy laws

## Disclaimer

Nina-Run authors are not responsible for:
- Damages caused by misuse of the tool
- Legal violations resulting from its use
- Data loss or affected systems
- Any malicious activity

**Use at your own risk. You are responsible for your actions.**

---

## 👨‍💻 Author

**Davi Moreira** - [@davimoreira0](https://github.com/davimoreira0)
**Email:** - moreiradavi336@gmail.com

## Project Status
⚠️ **This project is still under active development.** New features and modules are being added continuously. Some features may change or be improved in future versions.

---

Thank you for using **Nina-Run**! For questions, suggestions or bugs, contact via GitHub Issues.

Happy Hacking! 🔓🛡️
![Views](https://github.com/davimoreira0/Nina-Run/blob/gh-stats/views-report-last-14-days-badge.svg) |
![Clones](https://github.com/davimoreira0/Nina-Run/blob/gh-stats/clones-report-last-14-days-badge.svg) |
