#!/usr/bin/env python3
import os
import sys
import time
import random
import subprocess

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[97m'
M = '\033[95m'
B = '\033[94m'
X = '\033[0m'

def clear():
    os.system('clear')

def run(cmd):
    os.system(cmd)

def typewriter(text, color, delay=0.02):
    for char in text:
        sys.stdout.write(color + char + X)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(text, delay=0.02):
    bar = ""
    print(f"\n{C}{text}{X}")
    for i in range(1, 41):
        bar += "█"
        sys.stdout.write(f"\r{G}[{bar:<40}] {Y}{i*100//40}%{X}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    clear()
    print(f"{G}", end="")
    for _ in range(2):
        print(''.join(random.choice(['0','1','█','░',' ',' ',' ']) for _ in range(44)))
        time.sleep(0.1)
    print(X)

    for _ in range(3):
        g = ''.join(random.choice(['@','#','$']) if random.random()<0.3 else c for c in "  >> LOADING AB-TOOLBOX <<  ")
        sys.stdout.write(f"\r{R}{g}{X}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    time.sleep(0.2)
    clear()

    lines = [
(R,"╔══════════════════════════════════════════╗"),
(R,"║                                          ║"),
(R,"║"+Y+"  ████████╗ ██████╗  ██████╗ ██╗         "+R+"║"),
(R,"║"+Y+"     ██╔══╝██╔═══██╗██╔═══██╗██║         "+R+"║"),
(R,"║"+Y+"     ██║   ██║   ██║██║   ██║██║         "+R+"║"),
(R,"║"+Y+"     ██║   ██║   ██║██║   ██║██║         "+R+"║"),
(R,"║"+Y+"     ██║   ╚██████╔╝╚██████╔╝███████╗    "+R+"║"),
(R,"║                                          ║"),
(R,"║"+C+"  ██████╗  ██████╗ ██╗  ██╗           "+R+"║"),
(R,"║"+C+"  ██╔══██╗██╔═══██╗╚██╗██╔╝           "+R+"║"),
(R,"║"+C+"  ██████╔╝██║   ██║ ╚███╔╝            "+R+"║"),
(R,"║"+C+"  ██╔══██╗██║   ██║ ██╔██╗            "+R+"║"),
(R,"║"+C+"  ██████╔╝╚██████╔╝██╔╝ ██╗           "+R+"║"),
(R,"║                                          ║"),
(R,"║"+G+"  ╔══════════════════════════════════╗"+R+"║"),
(R,"║"+M+"  ║    Made by : Abdullah Balouch    ║"+R+"║"),
(R,"║"+W+"  ║    20 Tools — One Toolbox        ║"+R+"║"),
(R,"║"+Y+"  ║    Ethical Hacking Suite v1.0    ║"+R+"║"),
(R,"║"+G+"  ╚══════════════════════════════════╝"+R+"║"),
(R,"║                                          ║"),
(R,"╚══════════════════════════════════════════╝"),
    ]

    for color, line in lines:
        for char in line:
            sys.stdout.write(color + char + X)
            sys.stdout.flush()
            time.sleep(0.004)
        print()

    loading_bar("  Initializing AB-TOOLBOX...", 0.02)
    print(f"\n{G}  >> ALL SYSTEMS READY — HACKER MODE ON <<{X}\n")
    time.sleep(0.5)

def install_menu():
    clear()
    print(f"{R}{'═'*44}{X}")
    print(f"{Y}       AB-TOOLBOX — AUTO INSTALLER{X}")
    print(f"{R}{'═'*44}{X}\n")

    print(f"{C}  CUSTOM TOOLS:{X}")
    print(f"  {Y}[1]{W}  AB-RECON")
    print(f"  {Y}[2]{W}  AB-OSINT")
    print(f"  {Y}[3]{W}  AB-Email Hunter")
    print(f"  {Y}[4]{W}  AB-Dark Monitor")
    print(f"  {Y}[5]{W}  AB-Phone Tracker")
    print(f"  {Y}[6]{W}  AB-Admin Finder")

    print(f"\n{C}  RECON TOOLS:{X}")
    print(f"  {Y}[7]{W}  Nmap")
    print(f"  {Y}[8]{W}  WhatWeb")
    print(f"  {Y}[9]{W}  Nikto")
    print(f"  {Y}[10]{W} Sublist3r")
    print(f"  {Y}[11]{W} theHarvester")

    print(f"\n{C}  EXPLOITATION TOOLS:{X}")
    print(f"  {Y}[12]{W} SQLMap")
    print(f"  {Y}[13]{W} Hydra")
    print(f"  {Y}[14]{W} WPScan")
    print(f"  {Y}[15]{W} Dirb")

    print(f"\n{C}  NETWORK TOOLS:{X}")
    print(f"  {Y}[16]{W} Netcat")
    print(f"  {Y}[17]{W} Wireshark")
    print(f"  {Y}[18]{W} Aircrack-ng")

    print(f"\n{C}  ADVANCED TOOLS:{X}")
    print(f"  {Y}[19]{W} Metasploit")
    print(f"  {Y}[20]{W} Beef-XSS")

    print(f"\n  {G}[A]{W}  Install ALL Tools")
    print(f"  {R}[0]{W}  Back to Main Menu")

    print(f"\n{C}Enter Choice: {Y}", end="")
    choice = input().strip()

    installs = {
        '1':  ("AB-RECON",         "echo 'Already in ~/ab_recon.py'"),
        '2':  ("AB-OSINT",         "echo 'Already in ~/ab_osint.py'"),
        '3':  ("AB-Email Hunter",  "pip install requests beautifulsoup4"),
        '4':  ("AB-Dark Monitor",  "echo 'Built-in hashlib + requests'"),
        '5':  ("AB-Phone Tracker", "pip install phonenumbers requests"),
        '6':  ("AB-Admin Finder",  "pip install requests"),
        '7':  ("Nmap",             "pkg install nmap -y"),
        '8':  ("WhatWeb",          "pkg install ruby -y && gem install whatweb"),
        '9':  ("Nikto",            "pkg install nikto -y"),
        '10': ("Sublist3r",        "pip install sublist3r"),
        '11': ("theHarvester",     "pip install theHarvester"),
        '12': ("SQLMap",           "pkg install sqlmap -y"),
        '13': ("Hydra",            "pkg install hydra -y"),
        '14': ("WPScan",           "pkg install ruby -y && gem install wpscan"),
        '15': ("Dirb",             "pkg install dirb -y"),
        '16': ("Netcat",           "pkg install netcat-openbsd -y"),
        '17': ("Wireshark",        "pkg install wireshark-gtk -y"),
        '18': ("Aircrack-ng",      "pkg install aircrack-ng -y"),
        '19': ("Metasploit",       "pkg install metasploit -y"),
        '20': ("Beef-XSS",         "pkg install beef-xss -y"),
    }

    if choice == 'A' or choice == 'a':
        for key, (name, cmd) in installs.items():
            print(f"\n{Y}[*] Installing: {name}{X}")
            run(cmd)
            print(f"{G}[✓] Done: {name}{X}")
            time.sleep(0.5)
        print(f"\n{G}[✓] ALL TOOLS INSTALLED!{X}")

    elif choice in installs:
        name, cmd = installs[choice]
        print(f"\n{Y}[*] Installing: {name}{X}")
        loading_bar(f"  Installing {name}...", 0.03)
        run(cmd)
        print(f"\n{G}[✓] {name} Installed!{X}")

    elif choice == '0':
        return

    input(f"\n{C}Press Enter to continue...{X}")

def tools_menu():
    clear()
    print(f"{R}{'═'*44}{X}")
    print(f"{Y}        AB-TOOLBOX — LAUNCH TOOLS{X}")
    print(f"{R}{'═'*44}{X}\n")

    print(f"{C}  CUSTOM TOOLS:{X}")
    print(f"  {Y}[1]{W}  AB-RECON")
    print(f"  {Y}[2]{W}  AB-OSINT")
    print(f"  {Y}[3]{W}  AB-Email Hunter")
    print(f"  {Y}[4]{W}  AB-Dark Monitor")
    print(f"  {Y}[5]{W}  AB-Phone Tracker")
    print(f"  {Y}[6]{W}  AB-Admin Finder")

    print(f"\n{C}  SYSTEM TOOLS:{X}")
    print(f"  {Y}[7]{W}  Nmap Scan")
    print(f"  {Y}[8]{W}  SQLMap")
    print(f"  {Y}[9]{W}  Hydra")
    print(f"  {Y}[10]{W} Sublist3r")
    print(f"  {Y}[11]{W} Nikto")
    print(f"  {Y}[12]{W} Dirb")
    print(f"  {Y}[13]{W} WPScan")
    print(f"  {Y}[14]{W} Netcat")
    print(f"  {Y}[15]{W} Aircrack-ng")

    print(f"\n  {R}[0]{W}  Back")
    print(f"\n{C}Enter Choice: {Y}", end="")
    choice = input().strip()

    if choice == '1':
        run("python ~/ab_recon.py")
    elif choice == '2':
        run("python ~/ab_osint.py")
    elif choice == '3':
        run("python ~/ab_email_hunter.py")
    elif choice == '4':
        run("python ~/ab_dark_monitor.py")
    elif choice == '5':
        run("python ~/ab_phone_tracker.py")
    elif choice == '6':
        run("python ~/ab_admin_finder.py")
    elif choice == '7':
        print(f"\n{C}Enter Target: {Y}", end="")
        t = input().strip()
        run(f"nmap -sV {t}")
    elif choice == '8':
        print(f"\n{C}Enter URL: {Y}", end="")
        t = input().strip()
        run(f"sqlmap -u {t} --dbs")
    elif choice == '9':
        print(f"\n{C}Enter Target: {Y}", end="")
        t = input().strip()
        run(f"hydra -h")
    elif choice == '10':
        print(f"\n{C}Enter Domain: {Y}", end="")
        t = input().strip()
        run(f"sublist3r -d {t}")
    elif choice == '11':
        print(f"\n{C}Enter URL: {Y}", end="")
        t = input().strip()
        run(f"nikto -h {t}")
    elif choice == '12':
        print(f"\n{C}Enter URL: {Y}", end="")
        t = input().strip()
        run(f"dirb {t}")
    elif choice == '13':
        print(f"\n{C}Enter URL: {Y}", end="")
        t = input().strip()
        run(f"wpscan --url {t}")
    elif choice == '14':
        print(f"\n{C}Enter IP:PORT: {Y}", end="")
        t = input().strip()
        run(f"nc {t}")
    elif choice == '15':
        run("aircrack-ng --help")

    input(f"\n{C}Press Enter to continue...{X}")

def main_menu():
    while True:
        banner()
        print(f"{R}{'═'*44}{X}")
        print(f"{Y}          AB-TOOLBOX MAIN MENU{X}")
        print(f"{R}{'═'*44}{X}\n")
        print(f"  {Y}[1]{W}  Install Tools")
        print(f"  {Y}[2]{W}  Launch Tools")
        print(f"  {Y}[3]{W}  Check Installed Tools")
        print(f"  {R}[0]{W}  Exit\n")
        print(f"{C}Enter Choice: {Y}", end="")
        choice = input().strip()

        if choice == '1':
            install_menu()
        elif choice == '2':
            tools_menu()
        elif choice == '3':
            clear()
            print(f"{R}{'═'*44}{X}")
            print(f"{Y}     INSTALLED TOOLS CHECK{X}")
            print(f"{R}{'═'*44}{X}\n")
            tools = ['nmap','sqlmap','hydra','nikto','dirb','netcat','aircrack-ng']
            for tool in tools:
                result = os.system(f"which {tool} > /dev/null 2>&1")
                if result == 0:
                    print(f"  {G}[✓]{W} {tool} — Installed{X}")
                else:
                    print(f"  {R}[✗]{W} {tool} — Not Installed{X}")
            
            py_tools = ['ab_recon.py','ab_osint.py','ab_email_hunter.py',
                       'ab_dark_monitor.py','ab_phone_tracker.py','ab_admin_finder.py']
            print()
            for tool in py_tools:
                if os.path.exists(os.path.expanduser(f"~/{tool}")):
                    print(f"  {G}[✓]{W} {tool} — Ready{X}")
                else:
                    print(f"  {R}[✗]{W} {tool} — Missing{X}")
            
            input(f"\n{C}Press Enter to continue...{X}")
        elif choice == '0':
            clear()
            print(f"\n{M}  Allah Hafiz — Abdullah Balouch!{X}\n")
            break

main_menu()
