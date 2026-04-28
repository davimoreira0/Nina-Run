#!/usr/bin/env python3
"""
Nina-Run - Profissional pentest tool
Versão: 2.26
GitHub: https://github.com/davimoreira0
"""

from colorama import Fore, Style
import time
import os
import sys


# ============================================================================
# ASCII ART AND INTERFACE
# ============================================================================

VERSION = "2.26"
GITHUB_URL = "https://github.com/davimoreira0"


# ============================================================================
# FUNCTION TO LOAD ASCII ART
# ============================================================================

def load_ascii_art():
    """
    Loads the ASCII art from the ascii_arts file.

    Returns:
        str: The ASCII art content or empty string if there's an error.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ascii_arts_file = os.path.join(script_dir, "assets", "ascii_arts")

        if not os.path.exists(ascii_arts_file):
            return ""

        with open(ascii_arts_file, 'r', encoding='utf-8') as f:
            return f.read()

    except Exception as e:
        print(f"{Fore.RED}[!] Error loading ASCII art: {str(e)}{Style.RESET_ALL}")
        return ""


# ============================================================================
# CLASSES
# ============================================================================

class NmapModule:
    """
    Module for nmap scan configuration and execution.
    
    Attributes:
        remote_host (str): IP address of the target.
    """
    
    def __init__(self):
        """Initializes the nmap module with default values."""
        self.remote_host = ""
    
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
    
    def show_options(self) -> str:
        """
        Returns the current options of the nmap module.
        
        Returns:
            str: Tabular formatting of options.
        """
        display_rhost = self.remote_host if self.remote_host else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
RHOST{'':<10}{display_rhost:<30}{'yes':<12}{'IP address of the target for attack':<40}
"""
        return options
    
    def run_scan(self) -> bool:
        """
        Executes nmap scan with the configured RHOST.
        
        Returns:
            bool: True if scan was executed, False if RHOST is not configured.
        """
        if not self.remote_host:
            print(f"{Fore.RED}[!] Error: RHOST must be configured before running scan{Style.RESET_ALL}")
            return False
        
        cmd = f"nmap -p- -A -T4 -v --script vuln {self.remote_host}"
        print(f"{Fore.RED}[*] Starting nmap scan...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")
        
        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Scan completed successfully!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing scan: {str(e)}{Style.RESET_ALL}")
            return False


class DirbModule:
    """
    Module for dirb directory discovery.
    
    Attributes:
        target_url (str): URL of the target website.
    """
    
    def __init__(self):
        """Initializes the dirb module with default values."""
        self.target_url = ""
    
    def set_target_url(self, url: str) -> bool:
        """
        Sets the target URL for directory discovery.
        
        Args:
            url (str): URL of the target website.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        if not url or not isinstance(url, str):
            print(f"{Fore.RED}[!] Error: invalid URL{Style.RESET_ALL}")
            return False
        
        self.target_url = url.strip()
        print(f"{Fore.GREEN}[+] URL set to: {self.target_url}{Style.RESET_ALL}")
        return True
    
    def show_options(self) -> str:
        """
        Returns the current options of the dirb module.
        
        Returns:
            str: Tabular formatting of options.
        """
        display_url = self.target_url if self.target_url else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
URL{'':<12}{display_url:<30}{'yes':<12}{'Target URL for directory discovery':<40}
"""
        return options
    
    def run_scan(self) -> bool:
        """
        Executes dirb scan with the configured URL.
        
        Returns:
            bool: True if scan was executed, False if URL is not configured.
        """
        if not self.target_url:
            print(f"{Fore.RED}[!] Error: URL must be configured before running scan{Style.RESET_ALL}")
            return False
        
        cmd = f"dirb {self.target_url}"
        print(f"{Fore.RED}[*] Starting dirb scan...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")
        
        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Scan completed successfully!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing scan: {str(e)}{Style.RESET_ALL}")
            return False


class WhoisModule:
    """
    Module for whois domain information lookup.
    
    Attributes:
        domain (str): Domain name to query (e.g., exemplo.com.br).
    """
    
    def __init__(self):
        """Initializes the whois module with default values."""
        self.domain = ""
    
    def set_domain(self, domain: str) -> bool:
        """
        Sets the domain name for whois query.
        
        Args:
            domain (str): Domain name to query.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        if not domain or not isinstance(domain, str):
            print(f"{Fore.RED}[!] Error: invalid domain{Style.RESET_ALL}")
            return False
        
        self.domain = domain.strip()
        print(f"{Fore.GREEN}[+] DOMAIN set to: {self.domain}{Style.RESET_ALL}")
        return True
    
    def show_options(self) -> str:
        """
        Returns the current options of the whois module.
        
        Returns:
            str: Tabular formatting of options.
        """
        display_domain = self.domain if self.domain else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
DOMAIN{'':<9}{display_domain:<30}{'yes':<12}{'Domain name to query (e.g., domain.com.br)':<40}
"""
        return options
    
    def run_whois(self) -> bool:
        """
        Executes whois query with the configured domain.
        
        Returns:
            bool: True if query was executed, False if domain is not configured.
        """
        if not self.domain:
            print(f"{Fore.RED}[!] Error: DOMAIN must be configured before running whois{Style.RESET_ALL}")
            return False
        
        cmd = f"whois {self.domain}"
        print(f"{Fore.RED}[*] Starting whois lookup...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")
        
        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Whois lookup completed successfully!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing whois: {str(e)}{Style.RESET_ALL}")
            return False


class WhatwebModule:
    """
    Module for whatweb website technology identification.
    
    Attributes:
        domain (str): Domain name to analyze (e.g., globo.com.br).
    """
    
    def __init__(self):
        """Initializes the whatweb module with default values."""
        self.domain = ""
    
    def set_domain(self, domain: str) -> bool:
        """
        Sets the domain name for whatweb analysis.
        
        Args:
            domain (str): Domain name to analyze.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        if not domain or not isinstance(domain, str):
            print(f"{Fore.RED}[!] Error: invalid domain{Style.RESET_ALL}")
            return False
        
        self.domain = domain.strip()
        print(f"{Fore.GREEN}[+] DOMAIN set to: {self.domain}{Style.RESET_ALL}")
        return True
    
    def show_options(self) -> str:
        """
        Returns the current options of the whatweb module.
        
        Returns:
            str: Tabular formatting of options.
        """
        display_domain = self.domain if self.domain else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
DOMAIN{'':<9}{display_domain:<30}{'yes':<12}{'Domain name to analyze (e.g., domain.com.br)':<40}
"""
        return options
    
    def run_whatweb(self) -> bool:
        """
        Executes whatweb with the configured domain.
        
        Returns:
            bool: True if whatweb was executed, False if domain is not configured.
        """
        if not self.domain:
            print(f"{Fore.RED}[!] Error: DOMAIN must be configured before running whatweb{Style.RESET_ALL}")
            return False
        
        cmd = f"whatweb {self.domain}"
        print(f"{Fore.RED}[*] Starting whatweb analysis...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")
        
        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Whatweb analysis completed successfully!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing whatweb: {str(e)}{Style.RESET_ALL}")
            return False


class HostModule:
    """
    Module for host DNS lookup and IP resolution.
    
    Attributes:
        domain (str): Domain name to query (e.g., globo.com.br).
    """
    
    def __init__(self):
        """Initializes the host module with default values."""
        self.domain = ""
    
    def set_domain(self, domain: str) -> bool:
        """
        Sets the domain name for host DNS lookup.
        
        Args:
            domain (str): Domain name to query.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        if not domain or not isinstance(domain, str):
            print(f"{Fore.RED}[!] Error: invalid domain{Style.RESET_ALL}")
            return False
        
        self.domain = domain.strip()
        print(f"{Fore.GREEN}[+] DOMAIN set to: {self.domain}{Style.RESET_ALL}")
        return True
    
    def show_options(self) -> str:
        """
        Returns the current options of the host module.
        
        Returns:
            str: Tabular formatting of options.
        """
        display_domain = self.domain if self.domain else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
DOMAIN{'':<9}{display_domain:<30}{'yes':<12}{'Domain name to query (e.g., domain.com.br)':<40}
"""
        return options
    
    def run_host(self) -> bool:
        """
        Executes host DNS lookup with the configured domain.
        
        Returns:
            bool: True if host was executed, False if domain is not configured.
        """
        if not self.domain:
            print(f"{Fore.RED}[!] Error: DOMAIN must be configured before running host{Style.RESET_ALL}")
            return False
        
        cmd = f"host {self.domain}"
        print(f"{Fore.RED}[*] Starting host DNS lookup...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")
        
        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Host DNS lookup completed successfully!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing host: {str(e)}{Style.RESET_ALL}")
            return False


class TracerouteModule:
    """
    Module for traceroute route tracing and latency analysis.
    
    Attributes:
        domain (str): Domain name to trace (e.g., tesla.com).
    """
    
    def __init__(self):
        """Initializes the traceroute module with default values."""
        self.domain = ""
    
    def set_domain(self, domain: str) -> bool:
        """
        Sets the domain name for traceroute analysis.
        
        Args:
            domain (str): Domain name to trace.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        if not domain or not isinstance(domain, str):
            print(f"{Fore.RED}[!] Error: invalid domain{Style.RESET_ALL}")
            return False
        
        self.domain = domain.strip()
        print(f"{Fore.GREEN}[+] DOMAIN set to: {self.domain}{Style.RESET_ALL}")
        return True
    
    def show_options(self) -> str:
        """
        Returns the current options of the traceroute module.
        
        Returns:
            str: Tabular formatting of options.
        """
        display_domain = self.domain if self.domain else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
DOMAIN{'':<9}{display_domain:<30}{'yes':<12}{'Domain name to trace (e.g., tesla.com)':<40}
"""
        return options
    
    def run_traceroute(self) -> bool:
        """
        Executes traceroute with the configured domain.
        
        Returns:
            bool: True if traceroute was executed, False if domain is not configured.
        """
        if not self.domain:
            print(f"{Fore.RED}[!] Error: DOMAIN must be configured before running traceroute{Style.RESET_ALL}")
            return False
        
        cmd = f"traceroute {self.domain}"
        print(f"{Fore.RED}[*] Starting traceroute analysis...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")
        
        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Traceroute analysis completed successfully!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing traceroute: {str(e)}{Style.RESET_ALL}")
            return False


class MedusaModule:
    """
    Module for medusa SSH brute force attacks.
    
    Attributes:
        host (str): IP address of the target machine.
        username (str): Target username for SSH login attempt.
        wordlist (str): Path to the password wordlist file.
    """
    
    def __init__(self):
        """Initializes the medusa module with default values."""
        self.host = ""
        self.username = ""
        self.wordlist = ""
    
    def set_host(self, host: str) -> bool:
        """
        Sets the target IP address.
        
        Args:
            host (str): IP address of the target.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        if not host or not isinstance(host, str):
            print(f"{Fore.RED}[!] Error: invalid host{Style.RESET_ALL}")
            return False
        
        self.host = host.strip()
        print(f"{Fore.GREEN}[+] HOST set to: {self.host}{Style.RESET_ALL}")
        return True
    
    def set_username(self, username: str) -> bool:
        """
        Sets the target username.
        
        Args:
            username (str): Username for SSH login attempt.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        if not username or not isinstance(username, str):
            print(f"{Fore.RED}[!] Error: invalid username{Style.RESET_ALL}")
            return False
        
        self.username = username.strip()
        print(f"{Fore.GREEN}[+] USERNAME set to: {self.username}{Style.RESET_ALL}")
        return True
    
    def set_wordlist(self, wordlist: str) -> bool:
        """
        Sets the path to the password wordlist.
        
        Args:
            wordlist (str): Path to the wordlist file.
            
        Returns:
            bool: True if valid, False otherwise.
        """
        if not wordlist or not isinstance(wordlist, str):
            print(f"{Fore.RED}[!] Error: invalid wordlist path{Style.RESET_ALL}")
            return False
        
        wordlist_path = wordlist.strip()
        
        # Check if the wordlist file exists
        if not os.path.exists(wordlist_path):
            print(f"{Fore.RED}[!] Error: wordlist file not found: {wordlist_path}{Style.RESET_ALL}")
            return False
        
        self.wordlist = wordlist_path
        print(f"{Fore.GREEN}[+] WORDLIST set to: {self.wordlist}{Style.RESET_ALL}")
        return True
    
    def show_options(self) -> str:
        """
        Returns the current options of the medusa module.
        
        Returns:
            str: Tabular formatting of options.
        """
        display_host = self.host if self.host else "(not configured)"
        display_username = self.username if self.username else "(not configured)"
        display_wordlist = self.wordlist if self.wordlist else "(not configured)"
        
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
HOST{'':<11}{display_host:<30}{'yes':<12}{'Target IP address':<40}
USERNAME{'':<8}{display_username:<30}{'yes':<12}{'Target SSH username':<40}
WORDLIST{'':<8}{display_wordlist:<30}{'yes':<12}{'Path to password wordlist':<40}
"""
        return options
    
    def run_medusa(self) -> bool:
        """
        Executes medusa SSH brute force attack with configured parameters.
        
        Returns:
            bool: True if medusa was executed, False if any required parameter is missing.
        """
        if not self.host:
            print(f"{Fore.RED}[!] Error: HOST must be configured before running medusa{Style.RESET_ALL}")
            return False
        
        if not self.username:
            print(f"{Fore.RED}[!] Error: USERNAME must be configured before running medusa{Style.RESET_ALL}")
            return False
        
        if not self.wordlist:
            print(f"{Fore.RED}[!] Error: WORDLIST must be configured before running medusa{Style.RESET_ALL}")
            return False
        
        cmd = f"medusa -h {self.host} -u {self.username} -P {self.wordlist} -M ssh -v 6 -f"
        print(f"{Fore.RED}[*] Starting medusa SSH brute force attack...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")
        
        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Medusa attack completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing medusa: {str(e)}{Style.RESET_ALL}")
            return False



class Hping3Module:
    """
    Module for hping3 packet crafting and flooding attacks.

    Attributes:
        target_ip (str): Target IP address.
        spoof_ip (str): Spoofed source IP address.
        count (int): Number of packets to send.
        port (int): Target port (default: 80).
    """

    def __init__(self):
        """Initializes the hping3 module with default values."""
        self.target_ip = ""
        self.spoof_ip = ""
        self.count = 10
        self.port = 80

    def set_target_ip(self, ip: str) -> bool:
        """
        Sets the target IP address.

        Args:
            ip (str): Target IP address.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not ip or not isinstance(ip, str):
            print(f"{Fore.RED}[!] Error: invalid target IP{Style.RESET_ALL}")
            return False
        self.target_ip = ip.strip()
        print(f"{Fore.GREEN}[+] TARGET_IP set to: {self.target_ip}{Style.RESET_ALL}")
        return True

    def set_spoof_ip(self, ip: str) -> bool:
        """
        Sets the spoofed source IP address.

        Args:
            ip (str): Spoofed source IP address.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not ip or not isinstance(ip, str):
            print(f"{Fore.RED}[!] Error: invalid spoof IP{Style.RESET_ALL}")
            return False
        self.spoof_ip = ip.strip()
        print(f"{Fore.GREEN}[+] SPOOF_IP set to: {self.spoof_ip}{Style.RESET_ALL}")
        return True

    def set_count(self, count: str) -> bool:
        """
        Sets the number of packets to send.

        Args:
            count (str): Number of packets.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            self.count = int(count)
            print(f"{Fore.GREEN}[+] COUNT set to: {self.count}{Style.RESET_ALL}")
            return True
        except ValueError:
            print(f"{Fore.RED}[!] Error: count must be a number{Style.RESET_ALL}")
            return False

    def set_port(self, port: str) -> bool:
        """
        Sets the target port.

        Args:
            port (str): Target port number.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            self.port = int(port)
            print(f"{Fore.GREEN}[+] PORT set to: {self.port}{Style.RESET_ALL}")
            return True
        except ValueError:
            print(f"{Fore.RED}[!] Error: port must be a number{Style.RESET_ALL}")
            return False

    def show_options(self) -> str:
        """
        Returns the current options of the hping3 module.

        Returns:
            str: Tabular formatting of options.
        """
        display_target = self.target_ip if self.target_ip else "(not configured)"
        display_spoof = self.spoof_ip if self.spoof_ip else "(not configured)"
        display_count = str(self.count)
        display_port = str(self.port)

        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
TARGET_IP{'':<6}{display_target:<30}{'yes':<12}{'Target IP address':<40}
SPOOF_IP{'':<7}{display_spoof:<30}{'yes':<12}{'Spoofed source IP address':<40}
COUNT{'':<10}{display_count:<30}{'yes':<12}{'Number of packets to send (default: 10)':<40}
PORT{'':<11}{display_port:<30}{'no':<12}{'Target port (default: 80)':<40}
"""
        return options

    def run_hping3(self) -> bool:
        """
        Executes hping3 with the configured parameters.

        Returns:
            bool: True if hping3 was executed, False if required parameters are missing.
        """
        if not self.target_ip:
            print(f"{Fore.RED}[!] Error: TARGET_IP must be configured before running hping3{Style.RESET_ALL}")
            return False
        if not self.spoof_ip:
            print(f"{Fore.RED}[!] Error: SPOOF_IP must be configured before running hping3{Style.RESET_ALL}")
            return False

        cmd = f"sudo hping3 -c {self.count} -S {self.target_ip} -a {self.spoof_ip} -p {self.port} --flood"
        print(f"{Fore.RED}[*] Starting hping3 flood attack...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Hping3 attack completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing hping3: {str(e)}{Style.RESET_ALL}")
            return False


class LbdModule:
    """
    Module for lbd (load balancer detector).

    Attributes:
        domain (str): Domain name to check for load balancing.
    """

    def __init__(self):
        """Initializes the lbd module with default values."""
        self.domain = ""

    def set_domain(self, domain: str) -> bool:
        """
        Sets the domain name for load balancer detection.

        Args:
            domain (str): Domain name to check.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not domain or not isinstance(domain, str):
            print(f"{Fore.RED}[!] Error: invalid domain{Style.RESET_ALL}")
            return False
        self.domain = domain.strip()
        print(f"{Fore.GREEN}[+] DOMAIN set to: {self.domain}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the lbd module.

        Returns:
            str: Tabular formatting of options.
        """
        display_domain = self.domain if self.domain else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
DOMAIN{'':<9}{display_domain:<30}{'yes':<12}{'Domain name to check for load balancing':<40}
"""
        return options

    def run_lbd(self) -> bool:
        """
        Executes lbd with the configured domain.

        Returns:
            bool: True if lbd was executed, False if domain is not configured.
        """
        if not self.domain:
            print(f"{Fore.RED}[!] Error: DOMAIN must be configured before running lbd{Style.RESET_ALL}")
            return False

        cmd = f"lbd {self.domain}"
        print(f"{Fore.RED}[*] Starting load balancer detection...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Load balancer detection completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing lbd: {str(e)}{Style.RESET_ALL}")
            return False


class SkipfishModule:
    """
    Module for skipfish web application security scanner.

    Attributes:
        target_url (str): Target URL to scan.
        output_dir (str): Output directory for results.
    """

    def __init__(self):
        """Initializes the skipfish module with default values."""
        self.target_url = ""
        self.output_dir = "report"

    def set_target_url(self, url: str) -> bool:
        """
        Sets the target URL for scanning.

        Args:
            url (str): Target URL to scan.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not url or not isinstance(url, str):
            print(f"{Fore.RED}[!] Error: invalid URL{Style.RESET_ALL}")
            return False
        self.target_url = url.strip()
        print(f"{Fore.GREEN}[+] TARGET_URL set to: {self.target_url}{Style.RESET_ALL}")
        return True

    def set_output_dir(self, output_dir: str) -> bool:
        """
        Sets the output directory for scan results.

        Args:
            output_dir (str): Output directory name.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not output_dir or not isinstance(output_dir, str):
            print(f"{Fore.RED}[!] Error: invalid output directory{Style.RESET_ALL}")
            return False
        self.output_dir = output_dir.strip()
        print(f"{Fore.GREEN}[+] OUTPUT_DIR set to: {self.output_dir}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the skipfish module.

        Returns:
            str: Tabular formatting of options.
        """
        display_url = self.target_url if self.target_url else "(not configured)"
        display_output = self.output_dir
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
TARGET_URL{'':<5}{display_url:<30}{'yes':<12}{'Target URL to scan':<40}
OUTPUT_DIR{'':<7}{display_output:<30}{'no':<12}{'Output directory (default: report)':<40}
"""
        return options

    def run_skipfish(self) -> bool:
        """
        Executes skipfish with the configured parameters.

        Returns:
            bool: True if skipfish was executed, False if required parameters are missing.
        """
        if not self.target_url:
            print(f"{Fore.RED}[!] Error: TARGET_URL must be configured before running skipfish{Style.RESET_ALL}")
            return False

        cmd = f"skipfish -o {self.output_dir} {self.target_url}"
        print(f"{Fore.RED}[*] Starting skipfish scan...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Skipfish scan completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing skipfish: {str(e)}{Style.RESET_ALL}")
            return False


class SslscanModule:
    """
    Module for sslscan SSL/TLS scanner.

    Attributes:
        target_ip (str): Target IP address to scan.
    """

    def __init__(self):
        """Initializes the sslscan module with default values."""
        self.target_ip = ""

    def set_target_ip(self, ip: str) -> bool:
        """
        Sets the target IP address for SSL/TLS scanning.

        Args:
            ip (str): Target IP address.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not ip or not isinstance(ip, str):
            print(f"{Fore.RED}[!] Error: invalid target IP{Style.RESET_ALL}")
            return False
        self.target_ip = ip.strip()
        print(f"{Fore.GREEN}[+] TARGET_IP set to: {self.target_ip}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the sslscan module.

        Returns:
            str: Tabular formatting of options.
        """
        display_ip = self.target_ip if self.target_ip else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
TARGET_IP{'':<6}{display_ip:<30}{'yes':<12}{'Target IP address for SSL/TLS scan':<40}
"""
        return options

    def run_sslscan(self) -> bool:
        """
        Executes sslscan with the configured target IP.

        Returns:
            bool: True if sslscan was executed, False if target IP is not configured.
        """
        if not self.target_ip:
            print(f"{Fore.RED}[!] Error: TARGET_IP must be configured before running sslscan{Style.RESET_ALL}")
            return False

        cmd = f"sslscan {self.target_ip}"
        print(f"{Fore.RED}[*] Starting sslscan...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] SSL scan completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing sslscan: {str(e)}{Style.RESET_ALL}")
            return False


class SqlinjectionModule:
    """
    Module for SQL injection testing using sqlmap.

    Attributes:
        target_url (str): Target URL to test for SQL injection.
    """

    def __init__(self):
        """Initializes the sqlinjection module with default values."""
        self.target_url = ""

    def set_target_url(self, url: str) -> bool:
        """
        Sets the target URL for SQL injection testing.

        Args:
            url (str): Target URL to test.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not url or not isinstance(url, str):
            print(f"{Fore.RED}[!] Error: invalid URL{Style.RESET_ALL}")
            return False
        self.target_url = url.strip()
        print(f"{Fore.GREEN}[+] TARGET_URL set to: {self.target_url}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the sqlinjection module.

        Returns:
            str: Tabular formatting of options.
        """
        display_url = self.target_url if self.target_url else "(not configured)"
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
TARGET_URL{'':<5}{display_url:<30}{'yes':<12}{'Target URL to test for SQL injection':<40}
"""
        return options

    def run_sqlinjection(self) -> bool:
        """
        Executes sqlmap with the configured target URL.

        Returns:
            bool: True if sqlmap was executed, False if target URL is not configured.
        """
        if not self.target_url:
            print(f"{Fore.RED}[!] Error: TARGET_URL must be configured before running sqlinjection{Style.RESET_ALL}")
            return False

        cmd = f"sqlmap -u {self.target_url} --batch"
        print(f"{Fore.RED}[*] Starting SQL injection test...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] SQL injection test completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing sqlmap: {str(e)}{Style.RESET_ALL}")
            return False


class Sublist3rModule:
    """
    Module for sublist3r subdomain enumeration.

    Attributes:
        domain (str): Domain name to enumerate subdomains.
        engine (str): Search engine to use (default: bing).
    """

    def __init__(self):
        """Initializes the sublist3r module with default values."""
        self.domain = ""
        self.engine = "bing"

    def set_domain(self, domain: str) -> bool:
        """
        Sets the domain name for subdomain enumeration.

        Args:
            domain (str): Domain name to enumerate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not domain or not isinstance(domain, str):
            print(f"{Fore.RED}[!] Error: invalid domain{Style.RESET_ALL}")
            return False
        self.domain = domain.strip()
        print(f"{Fore.GREEN}[+] DOMAIN set to: {self.domain}{Style.RESET_ALL}")
        return True

    def set_engine(self, engine: str) -> bool:
        """
        Sets the search engine for subdomain enumeration.

        Args:
            engine (str): Search engine to use (e.g., bing, google, yahoo).

        Returns:
            bool: True if valid, False otherwise.
        """
        if not engine or not isinstance(engine, str):
            print(f"{Fore.RED}[!] Error: invalid engine{Style.RESET_ALL}")
            return False
        self.engine = engine.strip()
        print(f"{Fore.GREEN}[+] ENGINE set to: {self.engine}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the sublist3r module.

        Returns:
            str: Tabular formatting of options.
        """
        display_domain = self.domain if self.domain else "(not configured)"
        display_engine = self.engine
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
DOMAIN{'':<9}{display_domain:<30}{'yes':<12}{'Domain name to enumerate subdomains':<40}
ENGINE{'':<9}{display_engine:<30}{'yes':<12}{'Search engine (default: bing)':<40}
"""
        return options

    def run_sublist3r(self) -> bool:
        """
        Executes sublist3r with the configured parameters.

        Returns:
            bool: True if sublist3r was executed, False if required parameters are missing.
        """
        if not self.domain:
            print(f"{Fore.RED}[!] Error: DOMAIN must be configured before running sublist3r{Style.RESET_ALL}")
            return False

        cmd = f"sublist3r -d {self.domain} -v -b -e {self.engine}"
        print(f"{Fore.RED}[*] Starting subdomain enumeration...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Subdomain enumeration completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing sublist3r: {str(e)}{Style.RESET_ALL}")
            return False


class TheharvesterModule:
    """
    Module for theHarvester email harvesting and reconnaissance.

    Attributes:
        domain (str): Domain name to search.
        limit (int): Maximum number of results (default: 100).
        engine (str): Search engine to use (default: bing).
        output_file (str): Output file name.
    """

    def __init__(self):
        """Initializes the theharvester module with default values."""
        self.domain = ""
        self.limit = 100
        self.engine = "bing"
        self.output_file = ""

    def set_domain(self, domain: str) -> bool:
        """
        Sets the domain name for email harvesting.

        Args:
            domain (str): Domain name to search.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not domain or not isinstance(domain, str):
            print(f"{Fore.RED}[!] Error: invalid domain{Style.RESET_ALL}")
            return False
        self.domain = domain.strip()
        print(f"{Fore.GREEN}[+] DOMAIN set to: {self.domain}{Style.RESET_ALL}")
        return True

    def set_limit(self, limit: str) -> bool:
        """
        Sets the maximum number of results.

        Args:
            limit (str): Maximum results limit.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            self.limit = int(limit)
            print(f"{Fore.GREEN}[+] LIMIT set to: {self.limit}{Style.RESET_ALL}")
            return True
        except ValueError:
            print(f"{Fore.RED}[!] Error: limit must be a number{Style.RESET_ALL}")
            return False

    def set_engine(self, engine: str) -> bool:
        """
        Sets the search engine for harvesting.

        Args:
            engine (str): Search engine to use.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not engine or not isinstance(engine, str):
            print(f"{Fore.RED}[!] Error: invalid engine{Style.RESET_ALL}")
            return False
        self.engine = engine.strip()
        print(f"{Fore.GREEN}[+] ENGINE set to: {self.engine}{Style.RESET_ALL}")
        return True

    def set_output_file(self, output_file: str) -> bool:
        """
        Sets the output file name.

        Args:
            output_file (str): Output file name.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not output_file or not isinstance(output_file, str):
            print(f"{Fore.RED}[!] Error: invalid output file{Style.RESET_ALL}")
            return False
        self.output_file = output_file.strip()
        print(f"{Fore.GREEN}[+] OUTPUT_FILE set to: {self.output_file}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the theharvester module.

        Returns:
            str: Tabular formatting of options.
        """
        display_domain = self.domain if self.domain else "(not configured)"
        display_limit = str(self.limit)
        display_engine = self.engine
        display_output = self.output_file if self.output_file else "(not configured)"

        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
DOMAIN{'':<9}{display_domain:<30}{'yes':<12}{'Domain name to search':<40}
LIMIT{'':<10}{display_limit:<30}{'no':<12}{'Maximum results (default: 100)':<40}
ENGINE{'':<9}{display_engine:<30}{'no':<12}{'Search engine (default: bing)':<40}
OUTPUT_FILE{'':<4}{display_output:<30}{'yes':<12}{'Output file name':<40}
"""
        return options

    def run_theharvester(self) -> bool:
        """
        Executes theHarvester with the configured parameters.

        Returns:
            bool: True if theharvester was executed, False if required parameters are missing.
        """
        if not self.domain:
            print(f"{Fore.RED}[!] Error: DOMAIN must be configured before running theharvester{Style.RESET_ALL}")
            return False
        if not self.output_file:
            print(f"{Fore.RED}[!] Error: OUTPUT_FILE must be configured before running theharvester{Style.RESET_ALL}")
            return False

        cmd = f"theHarvester -d {self.domain} -l {self.limit} -b {self.engine} -f {self.output_file}"
        print(f"{Fore.RED}[*] Starting email harvesting...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Email harvesting completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing theHarvester: {str(e)}{Style.RESET_ALL}")
            return False


class NiktoModule:
    """
    Module for nikto web server scanner.

    Attributes:
        target_url (str): Target URL to scan.
        output_file (str): Output file path.
    """

    def __init__(self):
        """Initializes the nikto module with default values."""
        self.target_url = ""
        self.output_file = "output/nikto.html"

    def set_target_url(self, url: str) -> bool:
        """
        Sets the target URL for scanning.

        Args:
            url (str): Target URL to scan.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not url or not isinstance(url, str):
            print(f"{Fore.RED}[!] Error: invalid URL{Style.RESET_ALL}")
            return False
        self.target_url = url.strip()
        print(f"{Fore.GREEN}[+] TARGET_URL set to: {self.target_url}{Style.RESET_ALL}")
        return True

    def set_output_file(self, output_file: str) -> bool:
        """
        Sets the output file path.

        Args:
            output_file (str): Output file path.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not output_file or not isinstance(output_file, str):
            print(f"{Fore.RED}[!] Error: invalid output file{Style.RESET_ALL}")
            return False
        self.output_file = output_file.strip()
        print(f"{Fore.GREEN}[+] OUTPUT_FILE set to: {self.output_file}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the nikto module.

        Returns:
            str: Tabular formatting of options.
        """
        display_url = self.target_url if self.target_url else "(not configured)"
        display_output = self.output_file
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
TARGET_URL{'':<5}{display_url:<30}{'yes':<12}{'Target URL to scan':<40}
OUTPUT_FILE{'':<4}{display_output:<30}{'no':<12}{'Output file path (default: output/nikto.html)':<40}
"""
        return options

    def run_nikto(self) -> bool:
        """
        Executes nikto with the configured parameters.

        Returns:
            bool: True if nikto was executed, False if required parameters are missing.
        """
        if not self.target_url:
            print(f"{Fore.RED}[!] Error: TARGET_URL must be configured before running nikto{Style.RESET_ALL}")
            return False

        cmd = f"sudo nikto -host {self.target_url} -output {self.output_file}"
        print(f"{Fore.RED}[*] Starting nikto scan...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Nikto scan completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing nikto: {str(e)}{Style.RESET_ALL}")
            return False


class CewlModule:
    """
    Module for cewl (custom word list generator).

    Attributes:
        target_url (str): Target URL to generate wordlist from.
        output_file (str): Output file for wordlist.
    """

    def __init__(self):
        """Initializes the cewl module with default values."""
        self.target_url = ""
        self.output_file = "passwords.txt"

    def set_target_url(self, url: str) -> bool:
        """
        Sets the target URL for wordlist generation.

        Args:
            url (str): Target URL to crawl.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not url or not isinstance(url, str):
            print(f"{Fore.RED}[!] Error: invalid URL{Style.RESET_ALL}")
            return False
        self.target_url = url.strip()
        print(f"{Fore.GREEN}[+] TARGET_URL set to: {self.target_url}{Style.RESET_ALL}")
        return True

    def set_output_file(self, output_file: str) -> bool:
        """
        Sets the output file for the wordlist.

        Args:
            output_file (str): Output file name.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not output_file or not isinstance(output_file, str):
            print(f"{Fore.RED}[!] Error: invalid output file{Style.RESET_ALL}")
            return False
        self.output_file = output_file.strip()
        print(f"{Fore.GREEN}[+] OUTPUT_FILE set to: {self.output_file}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the cewl module.

        Returns:
            str: Tabular formatting of options.
        """
        display_url = self.target_url if self.target_url else "(not configured)"
        display_output = self.output_file
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
TARGET_URL{'':<5}{display_url:<30}{'yes':<12}{'Target URL to generate wordlist from':<40}
OUTPUT_FILE{'':<4}{display_output:<30}{'no':<12}{'Output file (default: passwords.txt)':<40}
"""
        return options

    def run_cewl(self) -> bool:
        """
        Executes cewl with the configured parameters.

        Returns:
            bool: True if cewl was executed, False if required parameters are missing.
        """
        if not self.target_url:
            print(f"{Fore.RED}[!] Error: TARGET_URL must be configured before running cewl{Style.RESET_ALL}")
            return False

        cmd = f"cewl {self.target_url} -w {self.output_file}"
        print(f"{Fore.RED}[*] Starting wordlist generation...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Wordlist generation completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing cewl: {str(e)}{Style.RESET_ALL}")
            return False


class SshModule:
    """
    Module for SSH connection.

    Attributes:
        username (str): Username for SSH connection.
        target_ip (str): Target IP address.
        use_legacy (bool): Use legacy algorithms for older SSH servers.
    """

    def __init__(self):
        """Initializes the ssh module with default values."""
        self.username = ""
        self.target_ip = ""
        self.use_legacy = False

    def set_username(self, username: str) -> bool:
        """
        Sets the username for SSH connection.

        Args:
            username (str): Username for SSH login.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not username or not isinstance(username, str):
            print(f"{Fore.RED}[!] Error: invalid username{Style.RESET_ALL}")
            return False
        self.username = username.strip()
        print(f"{Fore.GREEN}[+] USERNAME set to: {self.username}{Style.RESET_ALL}")
        return True

    def set_target_ip(self, ip: str) -> bool:
        """
        Sets the target IP address for SSH connection.

        Args:
            ip (str): Target IP address.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not ip or not isinstance(ip, str):
            print(f"{Fore.RED}[!] Error: invalid target IP{Style.RESET_ALL}")
            return False
        self.target_ip = ip.strip()
        print(f"{Fore.GREEN}[+] TARGET_IP set to: {self.target_ip}{Style.RESET_ALL}")
        return True

    def set_use_legacy(self, use_legacy: str) -> bool:
        """
        Sets whether to use legacy SSH algorithms.

        Args:
            use_legacy (str): 'true' or 'false'.

        Returns:
            bool: True if valid, False otherwise.
        """
        if use_legacy.lower() in ('true', 'yes', '1'):
            self.use_legacy = True
            print(f"{Fore.GREEN}[+] USE_LEGACY set to: true{Style.RESET_ALL}")
            return True
        elif use_legacy.lower() in ('false', 'no', '0'):
            self.use_legacy = False
            print(f"{Fore.GREEN}[+] USE_LEGACY set to: false{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}[!] Error: use_legacy must be true/false{Style.RESET_ALL}")
            return False

    def show_options(self) -> str:
        """
        Returns the current options of the ssh module.

        Returns:
            str: Tabular formatting of options.
        """
        display_username = self.username if self.username else "(not configured)"
        display_ip = self.target_ip if self.target_ip else "(not configured)"
        display_legacy = "true" if self.use_legacy else "false"

        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
USERNAME{'':<7}{display_username:<30}{'yes':<12}{'Username for SSH connection':<40}
TARGET_IP{'':<6}{display_ip:<30}{'yes':<12}{'Target IP address':<40}
USE_LEGACY{'':<5}{display_legacy:<30}{'no':<12}{'Use legacy SSH algorithms (default: false)':<40}
"""
        return options

    def run_ssh(self) -> bool:
        """
        Executes SSH connection with the configured parameters.

        Returns:
            bool: True if SSH was executed, False if required parameters are missing.
        """
        if not self.username:
            print(f"{Fore.RED}[!] Error: USERNAME must be configured before running ssh{Style.RESET_ALL}")
            return False
        if not self.target_ip:
            print(f"{Fore.RED}[!] Error: TARGET_IP must be configured before running ssh{Style.RESET_ALL}")
            return False

        if self.use_legacy:
            cmd = f"ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa {self.username}@{self.target_ip}"
        else:
            cmd = f"ssh {self.username}@{self.target_ip}"

        print(f"{Fore.RED}[*] Starting SSH connection...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] SSH session ended!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing ssh: {str(e)}{Style.RESET_ALL}")
            return False


class MetagoofilModule:
    """
    Module for metagoofil - metadata extraction and document harvesting.

    Attributes:
        domain (str): Domain to search for documents.
        file_type (str): File type to search for (e.g., pdf, doc, xls).
        limit (int): Maximum number of files to download.
        output_dir (str): Output directory for downloaded files.
    """

    def __init__(self):
        """Initializes the metagoofil module with default values."""
        self.domain = ""
        self.file_type = ""
        self.limit = 10
        self.output_dir = "sitefile"

    def set_domain(self, domain: str) -> bool:
        """
        Sets the domain to search for documents.

        Args:
            domain (str): Domain name to search.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not domain or not isinstance(domain, str):
            print(f"{Fore.RED}[!] Error: invalid domain{Style.RESET_ALL}")
            return False
        self.domain = domain.strip()
        print(f"{Fore.GREEN}[+] DOMAIN set to: {self.domain}{Style.RESET_ALL}")
        return True

    def set_file_type(self, file_type: str) -> bool:
        """
        Sets the file type to search for.

        Args:
            file_type (str): File type (e.g., pdf, doc, xls, ppt).

        Returns:
            bool: True if valid, False otherwise.
        """
        if not file_type or not isinstance(file_type, str):
            print(f"{Fore.RED}[!] Error: invalid file type{Style.RESET_ALL}")
            return False
        self.file_type = file_type.strip()
        print(f"{Fore.GREEN}[+] FILE_TYPE set to: {self.file_type}{Style.RESET_ALL}")
        return True

    def set_limit(self, limit: str) -> bool:
        """
        Sets the maximum number of files to download.

        Args:
            limit (str): Maximum number of files.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            self.limit = int(limit)
            print(f"{Fore.GREEN}[+] LIMIT set to: {self.limit}{Style.RESET_ALL}")
            return True
        except ValueError:
            print(f"{Fore.RED}[!] Error: limit must be a number{Style.RESET_ALL}")
            return False

    def set_output_dir(self, output_dir: str) -> bool:
        """
        Sets the output directory for downloaded files.

        Args:
            output_dir (str): Output directory name.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not output_dir or not isinstance(output_dir, str):
            print(f"{Fore.RED}[!] Error: invalid output directory{Style.RESET_ALL}")
            return False
        self.output_dir = output_dir.strip()
        print(f"{Fore.GREEN}[+] OUTPUT_DIR set to: {self.output_dir}{Style.RESET_ALL}")
        return True

    def show_options(self) -> str:
        """
        Returns the current options of the metagoofil module.

        Returns:
            str: Tabular formatting of options.
        """
        display_domain = self.domain if self.domain else "(not configured)"
        display_file_type = self.file_type if self.file_type else "(not configured)"
        display_limit = str(self.limit)
        display_output = self.output_dir

        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
DOMAIN{'':<9}{display_domain:<30}{'yes':<12}{'Domain to search for documents':<40}
FILE_TYPE{'':<6}{display_file_type:<30}{'yes':<12}{'File type (e.g., pdf, doc, xls)':<40}
LIMIT{'':<10}{display_limit:<30}{'yes':<12}{'Maximum files to download':<40}
OUTPUT_DIR{'':<5}{display_output:<30}{'no':<12}{'Output directory (default: sitefile)':<40}
"""
        return options

    def run_metagoofil(self) -> bool:
        """
        Executes metagoofil with the configured parameters.

        Returns:
            bool: True if metagoofil was executed, False if required parameters are missing.
        """
        if not self.domain:
            print(f"{Fore.RED}[!] Error: DOMAIN must be configured before running metagoofil{Style.RESET_ALL}")
            return False
        if not self.file_type:
            print(f"{Fore.RED}[!] Error: FILE_TYPE must be configured before running metagoofil{Style.RESET_ALL}")
            return False

        cmd = f"metagoofil -d {self.domain} -t {self.file_type} -l {self.limit} -o {self.output_dir}"
        print(f"{Fore.RED}[*] Starting metagoofil document search...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Metagoofil search completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing metagoofil: {str(e)}{Style.RESET_ALL}")
            return False


class NetdiscoverModule:
    """
    Module for netdiscover - network host discovery.

    This module runs in passive mode and does not require any parameters.
    """

    def __init__(self):
        """Initializes the netdiscover module."""
        pass

    def show_options(self) -> str:
        """
        Returns the current options of the netdiscover module.

        Returns:
            str: Information about the module.
        """
        options = f"""
{Fore.CYAN}{'Name':<15}{'Current Setting':<30}{'Required':<12}{'Description':<40}{Style.RESET_ALL}
{'-' * 97}
{'(no options)':<15}{'':<30}{'':<12}{'Passive network discovery - no options required':<40}
"""
        return options

    def run_netdiscover(self) -> bool:
        """
        Executes netdiscover in passive mode.

        Returns:
            bool: True if netdiscover was executed, False otherwise.
        """
        cmd = "sudo netdiscover -p"
        print(f"{Fore.RED}[*] Starting netdiscover passive scan...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Command: {cmd}{Style.RESET_ALL}\n")

        try:
            os.system(cmd)
            print(f"\n{Fore.GREEN}[+] Netdiscover scan completed!{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[!] Error executing netdiscover: {str(e)}{Style.RESET_ALL}")
            return False


# ============================================================================
# INTERFACE FUNCTIONS
# ============================================================================

def print_banner():
    """Displays the initial banner of the application with the ASCII art."""
    ascii_art = load_ascii_art()
    print(Fore.WHITE + Style.BRIGHT + ascii_art + Style.RESET_ALL)
    print(f"{Fore.RED}Nina-Run, version: {VERSION}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}GitHub: {GITHUB_URL}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}Use '{Fore.RED}help{Fore.WHITE}' or '{Fore.RED}-h{Fore.WHITE}' for instructions{Style.RESET_ALL}\n")


def print_help():
    """Displays the help message."""
    help_text = f"""
{Fore.CYAN}{'AVAILABLE COMMANDS:':<40}{Style.RESET_ALL}
{'-' * 60}
{Fore.RED}help              {Style.RESET_ALL} Show this help menu
{Fore.RED}modules           {Style.RESET_ALL} List available modules
{Fore.RED}use <module>      {Style.RESET_ALL} Select a module to use (e.g., 'use nmap')
{Fore.RED}exit              {Style.RESET_ALL} Exit the application
{Fore.RED}-h                {Style.RESET_ALL} Shortcut for help
"""
    print(help_text)


def print_modules():
    """Displays the available modules."""
    modules_text = f"""
{Fore.CYAN}{'AVAILABLE MODULES:':<40}{Style.RESET_ALL}
{'-' * 60}
{Fore.RED}nmap              {Style.RESET_ALL} Network scanning and enumeration tool
{Fore.RED}dirb              {Style.RESET_ALL} Directory discovery and enumeration tool
{Fore.RED}whois             {Style.RESET_ALL} Domain information and WHOIS lookup tool
{Fore.RED}whatweb           {Style.RESET_ALL} Website technology identification tool
{Fore.RED}host              {Style.RESET_ALL} DNS lookup and IP resolution tool
{Fore.RED}traceroute        {Style.RESET_ALL} Route tracing and latency analysis tool
{Fore.RED}medusa            {Style.RESET_ALL} SSH brute force attack tool
{Fore.RED}hping3            {Style.RESET_ALL} Packet crafting and flooding attack tool
{Fore.RED}lbd               {Style.RESET_ALL} Load balancer detection tool
{Fore.RED}skipfish          {Style.RESET_ALL} Web application security scanner
{Fore.RED}sslscan           {Style.RESET_ALL} SSL/TLS scanner
{Fore.RED}sqlinjection      {Style.RESET_ALL} SQL injection testing tool
{Fore.RED}sublist3r         {Style.RESET_ALL} Subdomain enumeration tool
{Fore.RED}theharvester      {Style.RESET_ALL} Email harvesting and reconnaissance tool
{Fore.RED}nikto             {Style.RESET_ALL} Web server vulnerability scanner
{Fore.RED}cewl              {Style.RESET_ALL} Custom word list generator
{Fore.RED}ssh               {Style.RESET_ALL} SSH connection tool
{Fore.RED}metagoofil        {Style.RESET_ALL} Metadata extraction and document harvesting tool
{Fore.RED}netdiscover       {Style.RESET_ALL} Passive network host discovery tool
"""
    print(modules_text)


def process_nmap_module():
    """
    Processes the nmap module with an interactive loop.
    Allows configuring and viewing options.
    """
    nmap = NmapModule()
    
    print(f"{Fore.RED}[*] Entering nmap module...{Style.RESET_ALL}")
    
    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}nmap{Style.RESET_ALL}]
└─$ """
        
        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting nmap module...{Style.RESET_ALL}")
            break
        except EOFError:
            break
        
        if not user_input:
            continue
        
        user_lower = user_input.lower()
        
        if user_lower == "show options":
            print(nmap.show_options())
        
        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)
            
            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set RHOST <value>{Style.RESET_ALL}")
                continue
            
            param_name = parts[0].upper()
            param_value = parts[1]
            
            if param_name == "RHOST":
                nmap.set_remote_host(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")
        
        elif user_lower in ("run", "start"):
            nmap.run_scan()
        
        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break
        
        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)
        
        elif user_lower in ("help", "-h"):
            print_help()
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_dirb_module():
    """
    Processes the dirb module with an interactive loop.
    Allows configuring and viewing options.
    """
    dirb = DirbModule()
    
    print(f"{Fore.RED}[*] Entering dirb module...{Style.RESET_ALL}")
    
    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}dirb{Style.RESET_ALL}]
└─$ """
        
        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting dirb module...{Style.RESET_ALL}")
            break
        except EOFError:
            break
        
        if not user_input:
            continue
        
        user_lower = user_input.lower()
        
        if user_lower == "show options":
            print(dirb.show_options())
        
        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)
            
            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set URL <value>{Style.RESET_ALL}")
                continue
            
            param_name = parts[0].upper()
            param_value = parts[1]
            
            if param_name == "URL":
                dirb.set_target_url(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")
        
        elif user_lower in ("run", "start"):
            dirb.run_scan()
        
        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break
        
        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)
        
        elif user_lower in ("help", "-h"):
            print_help()
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_whois_module():
    """
    Processes the whois module with an interactive loop.
    Allows configuring and viewing options.
    """
    whois = WhoisModule()
    
    print(f"{Fore.RED}[*] Entering whois module...{Style.RESET_ALL}")
    
    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}whois{Style.RESET_ALL}]
└─$ """
        
        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting whois module...{Style.RESET_ALL}")
            break
        except EOFError:
            break
        
        if not user_input:
            continue
        
        user_lower = user_input.lower()
        
        if user_lower == "show options":
            print(whois.show_options())
        
        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)
            
            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set DOMAIN <value>{Style.RESET_ALL}")
                continue
            
            param_name = parts[0].upper()
            param_value = parts[1]
            
            if param_name == "DOMAIN":
                whois.set_domain(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")
        
        elif user_lower in ("run", "start"):
            whois.run_whois()
        
        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break
        
        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)
        
        elif user_lower in ("help", "-h"):
            print_help()
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_whatweb_module():
    """
    Processes the whatweb module with an interactive loop.
    Allows configuring and viewing options.
    """
    whatweb = WhatwebModule()
    
    print(f"{Fore.RED}[*] Entering whatweb module...{Style.RESET_ALL}")
    
    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}whatweb{Style.RESET_ALL}]
└─$ """
        
        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting whatweb module...{Style.RESET_ALL}")
            break
        except EOFError:
            break
        
        if not user_input:
            continue
        
        user_lower = user_input.lower()
        
        if user_lower == "show options":
            print(whatweb.show_options())
        
        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)
            
            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set DOMAIN <value>{Style.RESET_ALL}")
                continue
            
            param_name = parts[0].upper()
            param_value = parts[1]
            
            if param_name == "DOMAIN":
                whatweb.set_domain(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")
        
        elif user_lower in ("run", "start"):
            whatweb.run_whatweb()
        
        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break
        
        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)
        
        elif user_lower in ("help", "-h"):
            print_help()
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_host_module():
    """
    Processes the host module with an interactive loop.
    Allows configuring and viewing options.
    """
    host = HostModule()
    
    print(f"{Fore.RED}[*] Entering host module...{Style.RESET_ALL}")
    
    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}host{Style.RESET_ALL}]
└─$ """
        
        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting host module...{Style.RESET_ALL}")
            break
        except EOFError:
            break
        
        if not user_input:
            continue
        
        user_lower = user_input.lower()
        
        if user_lower == "show options":
            print(host.show_options())
        
        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)
            
            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set DOMAIN <value>{Style.RESET_ALL}")
                continue
            
            param_name = parts[0].upper()
            param_value = parts[1]
            
            if param_name == "DOMAIN":
                host.set_domain(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")
        
        elif user_lower in ("run", "start"):
            host.run_host()
        
        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break
        
        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)
        
        elif user_lower in ("help", "-h"):
            print_help()
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_traceroute_module():
    """
    Processes the traceroute module with an interactive loop.
    Allows configuring and viewing options.
    """
    traceroute = TracerouteModule()
    
    print(f"{Fore.RED}[*] Entering traceroute module...{Style.RESET_ALL}")
    
    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}traceroute{Style.RESET_ALL}]
└─$ """
        
        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting traceroute module...{Style.RESET_ALL}")
            break
        except EOFError:
            break
        
        if not user_input:
            continue
        
        user_lower = user_input.lower()
        
        if user_lower == "show options":
            print(traceroute.show_options())
        
        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)
            
            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set DOMAIN <value>{Style.RESET_ALL}")
                continue
            
            param_name = parts[0].upper()
            param_value = parts[1]
            
            if param_name == "DOMAIN":
                traceroute.set_domain(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")
        
        elif user_lower in ("run", "start"):
            traceroute.run_traceroute()
        
        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break
        
        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)
        
        elif user_lower in ("help", "-h"):
            print_help()
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_medusa_module():
    """
    Processes the medusa module with an interactive loop.
    Allows configuring and viewing options for SSH brute force attacks.
    """
    medusa = MedusaModule()
    
    print(f"{Fore.RED}[*] Entering medusa module...{Style.RESET_ALL}")
    
    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}medusa{Style.RESET_ALL}]
└─$ """
        
        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting medusa module...{Style.RESET_ALL}")
            break
        except EOFError:
            break
        
        if not user_input:
            continue
        
        user_lower = user_input.lower()
        
        if user_lower == "show options":
            print(medusa.show_options())
        
        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)
            
            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue
            
            param_name = parts[0].upper()
            param_value = parts[1]
            
            if param_name == "HOST":
                medusa.set_host(param_value)
            elif param_name == "USERNAME":
                medusa.set_username(param_value)
            elif param_name == "WORDLIST":
                medusa.set_wordlist(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")
        
        elif user_lower in ("run", "start"):
            medusa.run_medusa()
        
        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break
        
        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)
        
        elif user_lower in ("help", "-h"):
            print_help()
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_hping3_module():
    """
    Processes the hping3 module with an interactive loop.
    Allows configuring and viewing options for packet flooding attacks.
    """
    hping3 = Hping3Module()

    print(f"{Fore.RED}[*] Entering hping3 module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}hping3{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting hping3 module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(hping3.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "TARGET_IP":
                hping3.set_target_ip(param_value)
            elif param_name == "SPOOF_IP":
                hping3.set_spoof_ip(param_value)
            elif param_name == "COUNT":
                hping3.set_count(param_value)
            elif param_name == "PORT":
                hping3.set_port(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            hping3.run_hping3()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_lbd_module():
    """
    Processes the lbd module with an interactive loop.
    Allows configuring and viewing options for load balancer detection.
    """
    lbd = LbdModule()

    print(f"{Fore.RED}[*] Entering lbd module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}lbd{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting lbd module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(lbd.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set DOMAIN <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "DOMAIN":
                lbd.set_domain(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            lbd.run_lbd()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_skipfish_module():
    """
    Processes the skipfish module with an interactive loop.
    Allows configuring and viewing options for web application scanning.
    """
    skipfish = SkipfishModule()

    print(f"{Fore.RED}[*] Entering skipfish module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}skipfish{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting skipfish module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(skipfish.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "TARGET_URL":
                skipfish.set_target_url(param_value)
            elif param_name == "OUTPUT_DIR":
                skipfish.set_output_dir(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            skipfish.run_skipfish()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_sslscan_module():
    """
    Processes the sslscan module with an interactive loop.
    Allows configuring and viewing options for SSL/TLS scanning.
    """
    sslscan = SslscanModule()

    print(f"{Fore.RED}[*] Entering sslscan module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}sslscan{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting sslscan module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(sslscan.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set TARGET_IP <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "TARGET_IP":
                sslscan.set_target_ip(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            sslscan.run_sslscan()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_sqlinjection_module():
    """
    Processes the sqlinjection module with an interactive loop.
    Allows configuring and viewing options for SQL injection testing.
    """
    sqlinjection = SqlinjectionModule()

    print(f"{Fore.RED}[*] Entering sqlinjection module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}sqlinjection{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting sqlinjection module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(sqlinjection.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set TARGET_URL <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "TARGET_URL":
                sqlinjection.set_target_url(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            sqlinjection.run_sqlinjection()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_sublist3r_module():
    """
    Processes the sublist3r module with an interactive loop.
    Allows configuring and viewing options for subdomain enumeration.
    """
    sublist3r = Sublist3rModule()

    print(f"{Fore.RED}[*] Entering sublist3r module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}sublist3r{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting sublist3r module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(sublist3r.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "DOMAIN":
                sublist3r.set_domain(param_value)
            elif param_name == "ENGINE":
                sublist3r.set_engine(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            sublist3r.run_sublist3r()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_theharvester_module():
    """
    Processes the theharvester module with an interactive loop.
    Allows configuring and viewing options for email harvesting.
    """
    theharvester = TheharvesterModule()

    print(f"{Fore.RED}[*] Entering theharvester module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}theharvester{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting theharvester module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(theharvester.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "DOMAIN":
                theharvester.set_domain(param_value)
            elif param_name == "LIMIT":
                theharvester.set_limit(param_value)
            elif param_name == "ENGINE":
                theharvester.set_engine(param_value)
            elif param_name == "OUTPUT_FILE":
                theharvester.set_output_file(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            theharvester.run_theharvester()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_nikto_module():
    """
    Processes the nikto module with an interactive loop.
    Allows configuring and viewing options for web server scanning.
    """
    nikto = NiktoModule()

    print(f"{Fore.RED}[*] Entering nikto module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}nikto{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting nikto module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(nikto.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "TARGET_URL":
                nikto.set_target_url(param_value)
            elif param_name == "OUTPUT_FILE":
                nikto.set_output_file(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            nikto.run_nikto()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_cewl_module():
    """
    Processes the cewl module with an interactive loop.
    Allows configuring and viewing options for wordlist generation.
    """
    cewl = CewlModule()

    print(f"{Fore.RED}[*] Entering cewl module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}cewl{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting cewl module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(cewl.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "TARGET_URL":
                cewl.set_target_url(param_value)
            elif param_name == "OUTPUT_FILE":
                cewl.set_output_file(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            cewl.run_cewl()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_ssh_module():
    """
    Processes the ssh module with an interactive loop.
    Allows configuring and viewing options for SSH connections.
    """
    ssh = SshModule()

    print(f"{Fore.RED}[*] Entering ssh module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}ssh{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting ssh module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(ssh.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "USERNAME":
                ssh.set_username(param_value)
            elif param_name == "TARGET_IP":
                ssh.set_target_ip(param_value)
            elif param_name == "USE_LEGACY":
                ssh.set_use_legacy(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            ssh.run_ssh()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_metagoofil_module():
    """
    Processes the metagoofil module with an interactive loop.
    Allows configuring and viewing options for document harvesting.
    """
    metagoofil = MetagoofilModule()

    print(f"{Fore.RED}[*] Entering metagoofil module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}metagoofil{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting metagoofil module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(metagoofil.show_options())

        elif user_lower.startswith("set "):
            parts = user_input[4:].split(maxsplit=1)

            if len(parts) < 2:
                print(f"{Fore.RED}[!] Usage: set <PARAM> <value>{Style.RESET_ALL}")
                continue

            param_name = parts[0].upper()
            param_value = parts[1]

            if param_name == "DOMAIN":
                metagoofil.set_domain(param_value)
            elif param_name == "FILE_TYPE":
                metagoofil.set_file_type(param_value)
            elif param_name == "LIMIT":
                metagoofil.set_limit(param_value)
            elif param_name == "OUTPUT_DIR":
                metagoofil.set_output_dir(param_value)
            else:
                print(f"{Fore.RED}[!] Unknown parameter: {param_name}{Style.RESET_ALL}")

        elif user_lower in ("run", "start"):
            metagoofil.run_metagoofil()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


def process_netdiscover_module():
    """
    Processes the netdiscover module with an interactive loop.
    Runs passive network discovery with no required parameters.
    """
    netdiscover = NetdiscoverModule()

    print(f"{Fore.RED}[*] Entering netdiscover module...{Style.RESET_ALL}")

    while True:
        prompt = f"""┌──(anonymous@nina)-[{Fore.RED}netdiscover{Style.RESET_ALL}]
└─$ """

        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Exiting netdiscover module...{Style.RESET_ALL}")
            break
        except EOFError:
            break

        if not user_input:
            continue

        user_lower = user_input.lower()

        if user_lower == "show options":
            print(netdiscover.show_options())

        elif user_lower in ("run", "start"):
            netdiscover.run_netdiscover()

        elif user_lower == "back":
            print(f"{Fore.RED}[*] Returning to main menu...{Style.RESET_ALL}")
            break

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            sys.exit(0)

        elif user_lower in ("help", "-h"):
            print_help()

        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


# ============================================================================
# MAIN LOOP
# ============================================================================

def main():
    """Main function that controls the application flow."""
    print_banner()
    
    while True:
        prompt = """┌──(anonymous@nina)-[~]
└─$ """
        
        try:
            user_input = input(prompt).strip()
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[*] Shutting down...{Style.RESET_ALL}")
            break
        except EOFError:
            break
        
        if not user_input:
            continue
        
        user_lower = user_input.lower()
        
        if user_lower in ("help", "-h"):
            print_help()
        
        elif user_lower == "modules":
            print_modules()
        
        elif user_lower == "use nmap":
            process_nmap_module()
        
        elif user_lower == "use dirb":
            process_dirb_module()
        
        elif user_lower == "use whois":
            process_whois_module()
        
        elif user_lower == "use whatweb":
            process_whatweb_module()
        
        elif user_lower == "use host":
            process_host_module()
        
        elif user_lower == "use traceroute":
            process_traceroute_module()
        
        elif user_lower == "use medusa":
            process_medusa_module()

        elif user_lower == "use hping3":
            process_hping3_module()

        elif user_lower == "use lbd":
            process_lbd_module()

        elif user_lower == "use skipfish":
            process_skipfish_module()

        elif user_lower == "use sslscan":
            process_sslscan_module()

        elif user_lower == "use sqlinjection":
            process_sqlinjection_module()

        elif user_lower == "use sublist3r":
            process_sublist3r_module()

        elif user_lower == "use theharvester":
            process_theharvester_module()

        elif user_lower == "use nikto":
            process_nikto_module()

        elif user_lower == "use cewl":
            process_cewl_module()

        elif user_lower == "use ssh":
            process_ssh_module()

        elif user_lower == "use metagoofil":
            process_metagoofil_module()

        elif user_lower == "use netdiscover":
            process_netdiscover_module()

        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            break
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()