# Security Policy

## Supported Versions

As Nina-Run is currently under active development (version 2.26), we only support the latest version. Please ensure you are using the most recent release.

| Version | Supported          |
| ------- | ------------------ |
| 2.26    | :white_check_mark: |
| < 2.26  | :x:                |

## Reporting a Vulnerability

We take the security of Nina-Run seriously. If you discover a security vulnerability, please follow the responsible disclosure process outlined below.

### Responsible Disclosure Process

1. **Do NOT** open a public issue on GitHub for security vulnerabilities
2. **Email** the security team directly at: moreiradavi336@gmail.com
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact of the vulnerability
   - Suggested fix (if any)

### Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 5 business days
- **Fix & Release**: Timeline depends on severity (see below)

### Severity Classification

| Severity | Description | Response Time |
|----------|-------------|---------------|
| Critical | Remote code execution, privilege escalation | 7 days |
| High | Data leakage, authentication bypass | 14 days |
| Medium | Information disclosure, DoS | 30 days |
| Low | Best practice violations | 60 days |

## Security Best Practices for Users

### Important Notice

Nina-Run is a penetration testing tool intended **ONLY** for authorized security testing. Misuse of this tool may result in:

- Legal consequences
- Criminal charges
- Civil liability
- Permanent damage to systems

### User Responsibilities

- [ ] Obtain explicit written authorization before testing any system
- [ ] Use only on systems you own or have permission to test
- [ ] Document all testing activities
- [ ] Report findings responsibly through proper channels
- [ ] Do not test production systems without explicit approval
- [ ] Respect rate limits and avoid causing denial of service

### Safe Testing Environment

We strongly recommend:

1. Using isolated lab environments (VMs, containers)
2. Testing on dedicated penetration testing platforms like:
   - [HackTheBox](https://www.hackthebox.com/)
   - [TryHackMe](https://tryhackme.com/)
   - [VulnHub](https://www.vulnhub.com/)
   - Your own local lab

## Security Features in Nina-Run

Nina-Run includes several security considerations:

- Input validation to prevent command injection
- Clear warnings before destructive operations
- Graceful error handling
- No persistent storage of sensitive data
- No network callbacks or telemetry

## Third-Party Dependencies

Nina-Run relies on external security tools. Ensure these are:
- Installed from official repositories
- Kept up to date
- Used in accordance with their security policies

## Contact

For security-related inquiries:
- Email: moreiradavi336@gmail.com
- GitHub: [@davimoreira0](https://github.com/davimoreira0)

---

**Last Updated**: 2026-05-01  
**Policy Version**: 1.0
