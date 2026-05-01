# Contributing to Nina-Run

First off, thank you for considering contributing to Nina-Run! It's people like you that make this project a great tool for the security community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Guidelines](#development-guidelines)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Familiarity with penetration testing concepts
- Understanding of the tools Nina-Run wraps

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/nina-run.git
   cd nina-run
   ```
3. **Install Python dependencies**:
   ```bash
   pip install colorama
   ```
4. **Install system tools**:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```
5. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please:

- Check if the bug has already been reported in [Issues](https://github.com/davimoreira0/nina-run/issues)
- Ensure you're using the latest version (2.26)

When reporting a bug, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected behavior** vs actual behavior
- **Screenshots** (if applicable)
- **Environment details**: OS, Python version, tool versions
- **Sample code** or commands that trigger the issue

### Suggesting Enhancements

Enhancement suggestions are welcome! When suggesting:

- Use a clear, descriptive title
- Provide a detailed description of the proposed feature
- Explain why this enhancement would be useful
- List potential use cases
- Consider potential security implications

### Adding New Modules

Nina-Run's strength is its modular architecture. To add a new module:

1. **Follow the existing pattern**: Look at `NmapModule` or `DirbModule` as templates
2. **Required methods for each module**:
   - `__init__()`: Initialize with default values
   - `set_<param>()`: Parameter setters with validation
   - `show_options()`: Return formatted options table
   - `run_<tool>()`: Execute the external tool
3. **Add processing function**: Create `process_<module>_module()` function
4. **Update `print_modules()`**: Add your module to the list
5. **Add handler in `main()`**: Add `elif user_lower == "use yourmodule"`
6. **Document in README.md**: Add module description with parameters

#### Module Template

```python
class NewToolModule:
    """
    Module for [tool name] - [brief description].
    
    Attributes:
        param1 (str): Description of param1.
        param2 (str): Description of param2.
    """
    
    def __init__(self):
        """Initializes the module with default values."""
        self.param1 = ""
        self.param2 = "default_value"
    
    def set_param1(self, value: str) -> bool:
        """Sets param1 with validation."""
        if not value or not isinstance(value, str):
            print(f"{Fore.RED}[!] Error: invalid param1{Style.RESET_ALL}")
            return False
        self.param1 = value.strip()
        print(f"{Fore.GREEN}[+] PARAM1 set to: {self.param1}{Style.RESET_ALL}")
        return True
    
    def show_options(self) -> str:
        """Returns formatted options table."""
        # Implementation here
        pass
    
    def run_newtool(self) -> bool:
        """Executes the tool."""
        if not self.param1:
            print(f"{Fore.RED}[!] Error: PARAM1 must be configured{Style.RESET_ALL}")
            return False
        cmd = f"newtool {self.param1}"
        print(f"{Fore.RED}[*] Starting newtool...{Style.RESET_ALL}")
        os.system(cmd)
        return True
```

### Documentation

- Keep all documentation in English
- Update README.md when adding new features
- Include docstrings in all functions and classes
- Provide clear examples for complex features

### Testing

Before submitting:

- Test your changes locally
- Ensure existing modules still work
- Verify error handling works correctly
- Check that the script runs without syntax errors:
  ```bash
  python3 -m py_compile setup.py
  ```

## Development Guidelines

### Security Considerations

- **Never** introduce features that could be used maliciously without authorization
- Validate all user inputs to prevent command injection
- Sanitize parameters passed to external tools
- Include appropriate warnings for destructive operations
- Follow responsible disclosure for any security issues found

### Code Quality

- Write clear, readable code
- Comment complex logic
- Handle exceptions gracefully
- Provide meaningful error messages
- Use type hints where appropriate

### External Tool Integration

When adding tools that Nina-Run wraps:

- Ensure the tool is widely used in the security community
- Verify it's available in standard repositories (apt, brew, etc.)
- Document the exact command executed
- Include all relevant parameters users might need

## Style Guidelines

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with these specifics:

- **Indentation**: 4 spaces (no tabs)
- **Line length**: Maximum 100 characters
- **Imports**: Group standard library, third-party, and local imports
- **Naming**: 
  - Classes: `PascalCase` (e.g., `NmapModule`)
  - Functions: `snake_case` (e.g., `set_remote_host`)
  - Constants: `UPPER_CASE`
- **Docstrings**: Use triple double quotes for all public methods
- **Comments**: Explain "why", not "what"

### Example

```python
def set_remote_host(self, host: str) -> bool:
    """
    Sets the IP address of the target.
    
    Args:
        host (str): IP address of the target.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not host or not isinstance(host, str):
        print(f"{Fore.RED}[!] Error: invalid host{Style.RESET_ALL}")
        return False
    
    self.remote_host = host.strip()
    print(f"{Fore.GREEN}[+] RHOST set to: {self.remote_host}{Style.RESET_ALL}")
    return True
```

## Commit Messages

Use clear, descriptive commit messages following this format:

```
<type>: <short summary>

<body> (optional)

<footer> (optional)
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semi colons, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```
feat: add hping3 module for packet crafting

fix: correct input validation in nmap module

docs: update README with new modules

refactor: improve error handling in all modules
```

## Pull Request Process

1. **Update the README.md** with details of your changes if applicable
2. **Update documentation** for any changed functionality
3. **Ensure your code follows** our style guidelines
4. **Include screenshots** or examples if adding new features
5. **Reference any related issues** in your PR description

### PR Checklist

Before submitting:

- [ ] Code compiles without errors: `python3 -m py_compile setup.py`
- [ ] Follows PEP 8 style guidelines
- [ ] Includes docstrings for new functions/classes
- [ ] README.md updated if needed
- [ ] Commit messages follow our guidelines
- [ ] Branch is up to date with main

### PR Review Process

1. A maintainer will review your PR
2. Feedback will be provided if changes are needed
3. Once approved, your PR will be merged
4. Your contribution will be acknowledged in the changelog

## Questions?

- **General questions**: Open a [Discussion](https://github.com/davimoreira0/nina-run/discussions)
- **Bug reports**: Open an [Issue](https://github.com/davimoreira0/nina-run/issues)
- **Security issues**: See [SECURITY.md](SECURITY.md)
- **Email**: moreiradavi3377@gmail.com

## Recognition

Contributors will be:
- Listed in our changelog
- Mentioned in release notes
- Added to a contributors section (coming soon)

Thank you for contributing to Nina-Run! 🛡️

---

**Last Updated**: 2026-05-01  
**Contributing Guide Version**: 1.0
