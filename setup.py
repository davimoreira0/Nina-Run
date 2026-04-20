#!/usr/bin/env python3
"""
Nina-Run - Ferramenta Profissional de Pentesting
Versão: 1.26
GitHub: https://github.com/davimoreira0
"""

from colorama import Fore, Style
import time
import os
import sys
import random


# ============================================================================
# ASCII ART E INTERFACE
# ============================================================================

ASCII_ART = """"""

VERSION = "1.26"
GITHUB_URL = "https://github.com/davimoreira0"


# ============================================================================
# FUNÇÃO PARA CARREGAR ARTES ALEATÓRIAS
# ============================================================================

def load_random_ascii_art():
    """
    Carrega uma arte ASCII aleatória do arquivo ascii_arts.
    
    Returns:
        str: Uma arte ASCII aleatória ou a arte padrão se houver erro.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ascii_arts_file = os.path.join(script_dir, "assets", "ascii_arts")
        
        if not os.path.exists(ascii_arts_file):
            return ASCII_ART
        
        with open(ascii_arts_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Separa as artes usando as labels de tipo "Segunda arte:", "Terceira arte:", etc
        arts = []
        current_art = []
        lines = content.split('\n')
        
        for line in lines:
            # Verifica se a linha é um marcador de seção (ex: "Segunda arte:", "Terceira arte:")
            if 'arte:' in line.lower():
                if current_art:
                    art_text = '\n'.join(current_art).strip()
                    if art_text:
                        arts.append(art_text)
                current_art = []
            else:
                if line or current_art:  # Inclui linhas vazias no meio, mas corta no fim
                    current_art.append(line)
        
        # Não esqueça da última arte
        if current_art:
            art_text = '\n'.join(current_art).strip()
            if art_text:
                arts.append(art_text)
        
        # Se encontrou artes, retorna uma aleatória
        if arts:
            return random.choice(arts)
        else:
            return ASCII_ART
            
    except Exception as e:
        print(f"{Fore.RED}[!] Erro ao carregar artes: {str(e)}{Style.RESET_ALL}")
        return ASCII_ART
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


# ============================================================================
# FUNÇÕES DE INTERFACE
# ============================================================================

def print_banner():
    """Displays the initial banner of the application with a random ASCII art."""
    random_art = load_random_ascii_art()
    print(Fore.WHITE + Style.BRIGHT + random_art + Style.RESET_ALL)
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


# ============================================================================
# LOOP PRINCIPAL
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
        
        elif user_lower in ("exit", "quit"):
            print(f"{Fore.RED}[*] Shutting down application...{Style.RESET_ALL}")
            break
        
        else:
            print(f"{Fore.RED}[!] Command not found: {user_input}{Style.RESET_ALL}")


# ============================================================================
# PONTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()