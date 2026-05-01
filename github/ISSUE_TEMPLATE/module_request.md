---
name: New Module Request
about: Suggest a new pentesting tool to be added to Nina-Run
title: '[MODULE] '
labels: enhancement, new-module
assignees: ''

---

## Tool Information
<!-- Provide details about the tool you'd like to see added: -->

**Tool Name**: 
**Current Availability**: [e.g., Available in apt, GitHub repo, needs compilation]
**Official Website/Repository**: 
**License**: 

## Tool Description
<!-- What does this tool do? What type of security testing is it used for? -->

## Why Should This Tool Be Added?
<!-- Explain the value this tool would add to Nina-Run users: -->

## Installation
<!-- How is this tool typically installed? -->
```bash
# Example installation commands
sudo apt-get install toolname
# OR
git clone https://github.com/example/toolname.git
```

## Basic Usage
<!-- What are the basic commands for this tool? -->
```bash
# Basic command syntax
toolname <target>
# Example
toolname example.com
```

## Proposed Parameters
<!-- What parameters should the Nina-Run module support? -->

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| TARGET | Yes | - | Target to scan |
| PORT | No | 80 | Target port |
| OUTPUT | No | output.txt | Output file |

## Example Module Usage
<!-- Show how this would look in Nina-Run: -->
```
┌──(anonymous@nina)-[~]
└─$ use toolname

┌──(anonymous@nina)-[toolname]
└─$ set target example.com
[+] TARGET set to: example.com

┌──(anonymous@nina)-[toolname]
└─$ run
[*] Starting toolname scan...
```

## Potential Challenges
<!-- Are there any known challenges with integrating this tool? -->
- [ ] Requires root privileges
- [ ] Complex installation process
- [ ] Many dependencies
- [ ] Requires API keys
- [ ] Other: 

## Willingness to Contribute
- [ ] I can implement this module myself
- [ ] I can help test the module
- [ ] I can provide documentation
- [ ] I'm just suggesting the idea

## Additional Information
<!-- Add any other information, screenshots, or examples here. -->
