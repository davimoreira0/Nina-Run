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
{Fore.RED}use <module>      {Style.RESET_ALL} Start the nmap module
{Fore.RED}modules           {Style.RESET_ALL} Show available modules
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