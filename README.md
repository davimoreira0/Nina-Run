# 🔓 Nina-Run - Professional Penetration Testing Tool

![Version](https://img.shields.io/badge/version-1.26-blue)
![Language](https://img.shields.io/badge/language-Python%203-yellow)
![Status](https://img.shields.io/badge/status-Under%20Development-orange)
![License](https://img.shields.io/badge/license-MIT-green)

**Nina-Run** is a professional and modular penetration testing tool developed in Python, designed to facilitate security testing and infrastructure reconnaissance. With an interactive interface inspired by Metasploit, it offers a complete set of modules for analyzing and attacking networks and web applications.

---

## 📋 Table of Contents

- [Key Features](#key-features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Available Modules](#available-modules)
- [Project Structure](#project-structure)
- [Module Documentation](#module-documentation)
- [Usage Examples](#usage-examples)
- [Architecture and Design](#architecture-and-design)
- [Future Development](#future-development)
- [Contributing](#contributing)
- [Legal Notice](#legal-notice)
- [Author](#author)

---

## ✨ Key Features

### 🎯 Intuitive Interface
- Interactive menu inspired by Metasploit Framework
- Colored prompts for better user experience
- Shared modules system with consistent patterns
- Support for abbreviated commands and contextual help

### 🔧 Modularity
- Architecture based on object-oriented Python classes
- Each tool is an independent and reusable module
- Easy extension for new modules without modifying core code
- Consistent pattern: `set`, `show options`, `run` in each module

### 🎨 Visual Customization
- Random ASCII arts loaded from `assets/ascii_arts` file
- Complete colorization with `colorama` for better visibility
- Professional banners on startup
- Visual icons and indicators for different message types

### 🛡️ Comprehensive Information Gathering
- Network scanning with Nmap
- Web directory discovery with Dirb
- Domain lookup with Whois
- Technology identification with Whatweb
- DNS resolution with Host
- Route analysis with Traceroute
- SSH brute force testing with Medusa

### 🔐 Error Handling
- Robust user input validation
- Clear and colored error messages
- Graceful exception recovery
- Warnings before critical operations

---

## 💻 System Requirements

### Python Dependencies
- **Python 3.6+** (3.8 or higher recommended)
- **colorama** - For terminal colorization
  ```bash
  pip install colorama
  ```

### Required External Tools
The script depends on command-line tools already installed on the system:

| Tool | Module | Description |
|------|--------|-------------|
| `nmap` | Nmap | Network and port scanner |
| `dirb` | Dirb | Web directory discovery |
| `whois` | Whois | Domain information |
| `whatweb` | Whatweb | Web technology identification |
| `host` | Host | DNS resolution |
| `traceroute` | Traceroute | Network route analysis |
| `medusa` | Medusa | SSH brute force testing |

### Installing Dependencies on Linux (Debian/Ubuntu)
```bash
sudo apt-get update
sudo apt-get install nmap dirb whois whatweb traceroute
```

### Installing Medusa
```bash
# Debian/Ubuntu
sudo apt-get install medusa

# Or compile from source
git clone https://github.com/jmk-fosuhs/medusa.git
cd medusa
./configure && make && sudo make install
```

### Access Requirements
- **Elevated privileges** for some network operations (nmap with `-A`, traceroute)
- **Write permissions** in working directory for logs
- **Network connectivity** for remote testing

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/davimoreira0/nina-run.git
cd nina-run
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
# OR install manually
pip install colorama
```

### 3. Install System Tools
```bash
# Linux (Debian/Ubuntu)
sudo apt-get install nmap dirb whois whatweb traceroute medusa

# macOS (with Homebrew)
brew install nmap dirb whois whatweb traceroute
# Medusa can be compiled from source
```

### 4. Make Script Executable (Optional)
```bash
chmod +x setup.py
```

### 5. Run the Tool
```bash
python3 setup.py
# OR
python setup.py
# OR (if executable)
./setup.py
```

---

## 🎮 Quick Start

### Starting the Application
```bash
$ python3 setup.py

  Nina-Run Art (random)
  
Nina-Run, version: 1.26
GitHub: https://github.com/davimoreira0
Use 'help' or '-h' for instructions

┌──(anonymous@nina)-[~]
└─$ help
```

### Main Commands
```bash
# View help
help                    # Display list of available commands
-h                      # Shortcut for help

# Module management
modules                 # List all available modules
use <module>           # Enter a specific module
exit / quit            # Exit the application
```

### Inside a Module
Once inside a module, you have access to these commands:
```bash
show options           # Show current module configuration
set <PARAM> <value>   # Set a parameter
run / start           # Execute the module's scan/attack
back                  # Return to main menu
help / -h             # Show help
exit / quit           # Exit the application
```

### Practical Example: Nmap Scan
```bash
┌──(anonymous@nina)-[~]
└─$ use nmap
[*] Entering nmap module...

┌──(anonymous@nina)-[nmap]
└─$ show options
Name           Current Setting         Required    Description
---
RHOST          (not configured)        yes         IP address of the target for attack

┌──(anonymous@nina)-[nmap]
└─$ set rhost 192.168.1.100
[+] RHOST set to: 192.168.1.100

┌──(anonymous@nina)-[nmap]
└─$ run
[*] Starting nmap scan...
[*] Command: nmap -p- -A -T4 -v --script vuln 192.168.1.100

# ... nmap results ...
```

---

## 📦 Available Modules

### 1. **Nmap** - Network Scanning & Enumeration
**Description**: Powerful tool for network discovery, port enumeration and service identification.

**Parameters**:
- `RHOST` (required) - Target IP address

**Executed Command**:
```bash
nmap -p- -A -T4 -v --script vuln <RHOST>
```

**Use Cases**:
- Discover open ports on a target
- Identify service versions
- Run NSE vulnerability scripts
- Map network topology

---

### 2. **Dirb** - Directory Discovery & Enumeration
**Description**: Tool for discovering directories and files on web servers through brute force.

**Parameters**:
- `URL` (required) - Target website URL

**Executed Command**:
```bash
dirb <URL>
```

**Use Cases**:
- Discover hidden directories in web applications
- Find administrative pages
- Enumerate directory structure
- Identify backup configurations

---

### 3. **Whois** - Domain Information Lookup
**Description**: Query public domain information, including registrar, nameservers, and owner data.

**Parameters**:
- `DOMAIN` (required) - Domain name (e.g., example.com)

**Executed Command**:
```bash
whois <DOMAIN>
```

**Use Cases**:
- Gather information about domain owners
- Identify domain nameservers
- Find contact emails
- Determine registration and expiration dates

---

### 4. **Whatweb** - Website Technology Identification
**Description**: Identifies technologies, frameworks and CMS used on websites.

**Parameters**:
- `DOMAIN` (required) - Domain/URL to analyze (e.g., example.com)

**Executed Command**:
```bash
whatweb <DOMAIN>
```

**Use Cases**:
- Identify CMS versions
- Discover web frameworks (Django, Laravel, etc.)
- Find JavaScript libraries
- Detect WAFs (Web Application Firewalls)
- Recognize security patterns

---

### 5. **Host** - DNS Lookup & IP Resolution
**Description**: Performs DNS lookups to resolve domain names into IP addresses.

**Parameters**:
- `DOMAIN` (required) - Domain to resolve (e.g., example.com)

**Executed Command**:
```bash
host <DOMAIN>
```

**Use Cases**:
- Resolve domain names to IPs
- Discover MX records (email)
- Find multiple associated IPs
- Test DNS responsiveness

---

### 6. **Traceroute** - Route Tracing & Latency Analysis
**Description**: Traces the route of packets to a destination, showing latency at each hop.

**Parameters**:
- `DOMAIN` (required) - Domain/IP to trace (e.g., tesla.com)

**Executed Command**:
```bash
traceroute <DOMAIN>
```

**Use Cases**:
- Network topology mapping
- Identification of intermediate gateways
- Network latency analysis
- Detection of connectivity issues
- Discover ISPs involved in the path

---

### 7. **Medusa** - SSH Brute Force Attack
**Description**: Brute force testing tool for SSH, testing credentials against SSH servers.

**Parameters**:
- `HOST` (required) - IP of SSH server
- `USERNAME` (required) - User to attack
- `WORDLIST` (required) - Path to password file

**Executed Command**:
```bash
medusa -h <HOST> -u <USERNAME> -P <WORDLIST> -M ssh -v 6 -f
```

**Execution Parameters**:
- `-h` - Target host
- `-u` - Username
- `-P` - Password file
- `-M ssh` - SSH module
- `-v 6` - Maximum verbosity
- `-f` - Exit on first valid username/password found

**Use Cases**:
- SSH brute force testing
- Password policy validation
- Authorized penetration tests
- Default credential auditing

⚠️ **IMPORTANT**: Ensure the wordlist file exists and contains the passwords to test.

---

## 📁 Project Structure

```
nina-run/
├── setup.py              # Main script (executable)
├── README.md             # This file (under development)
├── requirements.txt      # Python dependencies (not included yet)
├── assets/
│   └── ascii_arts        # ASCII arts for banner (randomly loaded)
└── __pycache__/          # Python compiled cache (auto-generated)
```

### Structure Explanation

| File/Directory | Description |
|----------------|-------------|
| `setup.py` | Main file containing all application logic |
| `assets/ascii_arts` | Text file with multiple ASCII arts separated by markers |
| `__pycache__/` | Cache directory created by Python automatically |

---

## 📚 Module Documentation

### Class Architecture

Each module is implemented as a Python class with the following structure:

```python
class ModuleTemplate:
    """Module description"""
    
    def __init__(self):
        """Initialize with default values"""
        self.param = ""
    
    def set_param(self, value: str) -> bool:
        """
        Set a parameter
        Returns: True if valid, False otherwise
        """
    
    def show_options(self) -> str:
        """Return tabular formatting of options"""
    
    def run_module(self) -> bool:
        """Execute the tool/scan"""
```

### Validation Pattern

All modules implement robust validation:

```python
def set_param(self, value: str) -> bool:
    if not value or not isinstance(value, str):
        print(f"{Fore.RED}[!] Error: invalid input{Style.RESET_ALL}")
        return False
    
    self.param = value.strip()
    print(f"{Fore.GREEN}[+] PARAM set to: {self.param}{Style.RESET_ALL}")
    return True
```

### Execution Pattern

Each module follows the pattern:

1. Validation of prerequisites
2. Command construction
3. Visual feedback (command being executed)
4. Execution via `os.system()`
5. Success/error feedback

---

## 💡 Usage Examples

### Example 1: Complete Domain Reconnaissance

```bash
$ python3 setup.py

┌──(anonymous@nina)-[~]
└─$ use whois
[*] Entering whois module...

┌──(anonymous@nina)-[whois]
└─$ set domain example.com
[+] DOMAIN set to: example.com

┌──(anonymous@nina)-[whois]
└─$ run
[*] Starting whois lookup...
[*] Command: whois example.com

# Result: owner information, nameservers, dates, etc.

┌──(anonymous@nina)-[whois]
└─$ back
[*] Returning to main menu...

# Now use Host to resolve IP
┌──(anonymous@nina)-[~]
└─$ use host

┌──(anonymous@nina)-[host]
└─$ set domain example.com
[+] DOMAIN set to: example.com

┌──(anonymous@nina)-[host]
└─$ run
[*] Command: host example.com
# Result: 192.168.1.1
```

### Example 2: Complete Nmap Scanning

```bash
┌──(anonymous@nina)-[~]
└─$ modules

AVAILABLE MODULES:
---
nmap                  Network scanning and enumeration tool
...

┌──(anonymous@nina)-[~]
└─$ use nmap
[*] Entering nmap module...

┌──(anonymous@nina)-[nmap]
└─$ show options

Name           Current Setting         Required    Description
---
RHOST          (not configured)        yes         IP address of the target for attack

┌──(anonymous@nina)-[nmap]
└─$ set rhost 192.168.1.100
[+] RHOST set to: 192.168.1.100

┌──(anonymous@nina)-[nmap]
└─$ show options

Name           Current Setting         Required    Description
---
RHOST          192.168.1.100           yes         IP address of the target for attack

┌──(anonymous@nina)-[nmap]
└─$ run
[*] Starting nmap scan...
[*] Command: nmap -p- -A -T4 -v --script vuln 192.168.1.100

# Scanning 192.168.1.100 ...
# Result: open ports, versions, vulnerability scripts
```

### Example 3: Directory Discovery

```bash
┌──(anonymous@nina)-[~]
└─$ use dirb
[*] Entering dirb module...

┌──(anonymous@nina)-[dirb]
└─$ set url http://example.com
[+] URL set to: http://example.com

┌──(anonymous@nina)-[dirb]
└─$ run
[*] Starting dirb scan...
[*] Command: dirb http://example.com

# Result: discovered directories (/admin, /wp-admin, /config, etc.)
```

### Example 4: SSH Brute Force Test

```bash
┌──(anonymous@nina)-[~]
└─$ use medusa
[*] Entering medusa module...

┌──(anonymous@nina)-[medusa]
└─$ set host 192.168.1.50
[+] HOST set to: 192.168.1.50

┌──(anonymous@nina)-[medusa]
└─$ set username admin
[+] USERNAME set to: admin

┌──(anonymous@nina)-[medusa]
└─$ set wordlist /path/to/passwords.txt
[+] WORDLIST set to: /path/to/passwords.txt

┌──(anonymous@nina)-[medusa]
└─$ show options

Name           Current Setting                Required    Description
---
HOST           192.168.1.50                   yes         Target IP address
USERNAME       admin                          yes         Target SSH username
WORDLIST       /path/to/passwords.txt         yes         Path to password wordlist

┌──(anonymous@nina)-[medusa]
└─$ run
[*] Starting medusa SSH brute force attack...
[*] Command: medusa -h 192.168.1.50 -u admin -P /path/to/passwords.txt -M ssh -v 6 -f

# Result: valid credentials found (if any)
```

---

## 🏗️ Architecture and Design

### Architecture Pattern

Nina-Run uses a **modular architecture based on classes**:

```
┌─────────────────────────────────────────────┐
│           MAIN MENU (main)                  │
│   - Banner with random ASCII Art            │
│   - Command input loop                      │
└──────────────┬──────────────────────────────┘
               │
        ┌──────┴──────┐
        │   USE       │
        └──────┬──────┘
               │
        ┌──────┴─────────────────────┐
        ▼                            ▼
   ┌─────────┐              ┌──────────────┐
   │ Module  │              │ Module       │
   │ Class   │              │ Process Fn   │
   └────┬────┘              └──────┬───────┘
        │                         │
   ┌────┴──────────────────────────┴────┐
   │  set_param() - Validation          │
   │  show_options() - Display          │
   │  run_module() - Execute            │
   └────────────────────────────────────┘
```

### Execution Flow

1. **Initialization**
   - `print_banner()` - Loads random ASCII art
   - `main()` - Starts main loop

2. **Main Menu**
   - Waits for user command
   - Processes: `help`, `modules`, `use <module>`, `exit`

3. **Inside a Module**
   - Waits for user command
   - Processes: `set`, `show options`, `run`, `back`
   - Executes external tool via `os.system()`

4. **Exit**
   - Return to main menu with `back`
   - Exit with `exit` or Ctrl+C

### Design Patterns Used

| Pattern | Usage | Example |
|---------|-------|---------|
| **Class Pattern** | Module encapsulation | `NmapModule` |
| **Template Method** | Consistent interface | `set_param()`, `run_module()` |
| **Strategy Pattern** | Different validations | Each specific setter |
| **Factory Pattern** | Loading ASCII arts | `load_random_ascii_art()` |

---

## 📈 Future Development

### Planned Features

- [ ] **Complete logging** - Save results to log files
- [ ] **Command history** - Keep record of executions
- [ ] **Persistent configuration** - Save settings between sessions
- [ ] **Multiple workspaces** - Manage different projects
- [ ] **Database integration** - Store results
- [ ] **Automatic reports** - Generate PDFs with findings
- [ ] **Scan scheduling** - Scheduled tasks
- [ ] **External API integration** - VirusTotal, Shodan, etc.

### Planned New Modules

- [ ] **Metasploit integration** - Run exploits via Nina-Run
- [ ] **SQL injection** - Automated SQLi testing
- [ ] **XSS scanning** - XSS vulnerability detection
- [ ] **CMS exploitation** - WordPress, Joomla-specific exploitation
- [ ] **Reverse shell generator** - Reverse shell generation
- [ ] **Credential harvesting** - Credential extraction
- [ ] **SSL/TLS analysis** - Certificate analysis
- [ ] **API testing** - REST API security testing

### Interface Improvements

- [ ] **Graphical User Interface (GUI)** - Qt or Tkinter version
- [ ] **Auto-complete** - Command suggestion
- [ ] **Customizable themes** - Different color schemes
- [ ] **Better output rendering** - Improved result formatting

### Technical Optimizations

- [ ] **Parallel execution** - Run multiple scans simultaneously
- [ ] **Timeout handling** - Improved timeout management
- [ ] **Error recovery** - Failure recovery
- [ ] **Memory optimization** - Reduce RAM usage
- [ ] **Result caching** - Intelligent caching

---

## 🤝 Contributing

### Reporting Bugs

If you find a bug, please:

1. Check if the bug has already been reported in Issues
2. Create a new Issue describing:
   - Python version and OS
   - Nina-Run version
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots or logs (if applicable)

### Suggesting Features

To suggest new functionality:

1. Describe the use case
2. Explain why it would be useful
3. Suggest the implementation (if possible)

### Pull Request Process

1. Fork the repository
2. Create a branch: `git checkout -b feature/MyFeature`
3. Commit changes: `git commit -am 'Add MyFeature'`
4. Push to branch: `git push origin feature/MyFeature`
5. Open a Pull Request describing the changes

### Code Style

- Follow PEP 8
- Use type hints when possible
- Add docstrings to classes and functions
- Keep descriptive English names
- Limit lines to 100 characters

### Commit Pattern

```bash
# Feature
git commit -m "feat: add new SSH module"

# Bug fix
git commit -m "fix: correct input validation"

# Documentation
git commit -m "docs: update README with examples"

# Refactoring
git commit -m "refactor: improve class structure"
```

---

## ⚠️ Legal Notice

### IMPORTANT

**Nina-Run is an educational tool intended ONLY for authorized security testing.** Use on systems without explicit authorization is ILLEGAL.

### Responsibilities

- ✅ Use ONLY on systems you own or have explicit permission to test
- ✅ Obtain written authorization before any security testing
- ✅ Respect local laws and data protection regulations
- ✅ Document all security findings responsibly
- ✅ Report vulnerabilities through appropriate channels

### What NOT to do

- ❌ Do not use on unauthorized systems
- ❌ Do not access third-party data
- ❌ Do not execute destructive attacks
- ❌ Do not publish exploits without responsible disclosure
- ❌ Do not violate data protection or privacy laws

### Disclaimer

Nina-Run authors are not responsible for:
- Damages caused by misuse of the tool
- Legal violations resulting from its use
- Data loss or affected systems
- Any malicious activity

**Use at your own risk. You are responsible for your actions.**

---

## 👨‍💻 Author

**Davi Moreira**

- GitHub: [@davimoreira0](https://github.com/davimoreira0)
- Email: (add when available)
- Website: (add when available)

### Credits

- **Colorama**: For terminal color formatting
- **Penetration Testing Community**: Best practices inspiration
- **Metasploit Framework**: Interface inspiration
- **Kali Linux**: Reference tool

---

## 📄 License

This project is licensed under the MIT License - see below for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📞 Support

### Useful Resources

- 📖 [Nmap Documentation](https://nmap.org/book/)
- 📖 [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- 📖 [Python Security Best Practices](https://python.readthedocs.io/)
- 🎓 [HackTheBox](https://www.hackthebox.com/)
- 🎓 [TryHackMe](https://tryhackme.com/)

### Communities

- Stack Overflow (tag: pentesting, security)
- Reddit: r/Cybersecurity, r/HowToHack
- GitHub Discussions
- OWASP Community

---

## 🔄 Changelog

### v1.26 (Current - Under Development)
- ✅ Nmap module implemented
- ✅ Dirb module implemented
- ✅ Whois module implemented
- ✅ Whatweb module implemented
- ✅ Host module implemented
- ✅ Traceroute module implemented
- ✅ Medusa module implemented
- ✅ Dynamic module system
- ✅ Random ASCII art
- 🔄 README under development
- 🔄 Unit tests pending
- 🔄 Complete documentation pending

### v1.0 (Future)
- [ ] Stable version with all modules
- [ ] Complete testing
- [ ] Finalized documentation
- [ ] Automatic reports

---

## ❓ FAQ

### Q: Do I need root privileges?
**A:** Some commands (like Nmap with advanced flags) require elevated privileges. Run with `sudo` if needed.

### Q: Can I use it in production environments?
**A:** No! Use ONLY in authorized test environments. Certain scans can negatively impact the target.

### Q: What's the difference between Dirb and Whatweb?
**A:** Dirb discovers DIRECTORIES; Whatweb identifies TECHNOLOGIES used on the site.

### Q: How do I update to the latest version?
**A:** Use `git pull origin main` in the project directory.

### Q: Do I need to compile anything?
**A:** No! It's pure Python script. Just install the dependencies.

### Q: Why is Nmap scanning slow?
**A:** Nmap scans ALL 65535 ports (-p-). Use `-p 80,443` for specific ports.

### Q: Can I use it on Windows?
**A:** Yes, if you install external tools (Nmap, Dirb, etc.) on Windows.

### Q: How do I configure a custom wordlist for Medusa?
**A:** Pass the full path: `set wordlist /path/to/my/wordlist.txt`

---

## 📊 Statistics

- **Lines of Code**: ~1000+ (in development)
- **Implemented Modules**: 7
- **Main Classes**: 7 (NmapModule, DirbModule, WhoisModule, WhatwebModule, HostModule, TracerouteModule, MedusaModule)
- **Interface Functions**: 10+
- **External Tools**: 6+ tools
- **Python Dependencies**: 1 (colorama)

---

## 🎯 Project Objectives

Nina-Run was created with the following objectives:

1. **Education**: Learn about offensive security and tool development
2. **Practicality**: Unify multiple tools in a single interface
3. **Extensibility**: Easy to add new modules
4. **Professionalism**: Professional interface and design
5. **Community**: Tool for collective learning

---

## 🌟 Acknowledgments

Special thanks to:

- Tool creators: Nmap, Dirb, Whois, Whatweb, Medusa
- Offensive security community
- Everyone who reports bugs or suggests features
- You, for using Nina-Run!

---

## 📝 Additional Notes

### Recommended Development Environment

```bash
# Python 3.8+
python3 --version

# Virtual Environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run in development
python3 setup.py
```

### Common Issues

**Problem**: "module not found: colorama"
**Solution**: `pip install colorama`

**Problem**: "command not found: nmap"
**Solution**: `sudo apt-get install nmap`

**Problem**: Script very slow
**Solution**: Some scans take time. Be patient or use timeouts.

**Problem**: Access denied to wordlist
**Solution**: Check permissions: `chmod 644 wordlist.txt`

---

**README Version**: 1.0
**Last Update**: 2026-04-20
**Status**: Under Development ⚠️

---

Thank you for using **Nina-Run**! For questions, suggestions or bugs, contact via GitHub Issues.

Happy Hacking! 🔓🛡️
