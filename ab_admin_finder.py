#!/usr/bin/env python3
import requests
import os
import sys
import time
import random

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[97m'
M = '\033[95m'
B = '\033[94m'
X = '\033[0m'

def banner():
    os.system('clear')
    
    # Matrix rain
    print(f"{G}", end="")
    for _ in range(3):
        print(''.join(random.choice(['0','1','█','░','▓','▒',' ',' ',' ']) for _ in range(44)))
        time.sleep(0.1)
    print(X)

    # Glitch
    glitch = "  >> LOADING AB-ADMIN-FINDER <<"
    for _ in range(3):
        g = ''.join(random.choice(['@','#','$','%']) if random.random()<0.3 else c for c in glitch)
        sys.stdout.write(f"\r{R}{g}{X}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\r{Y}{glitch}{X}\n")
    time.sleep(0.3)

    os.system('clear')

    lines = [
(R,"╔══════════════════════════════════════════╗"),
(R,"║                                          ║"),
(R,"║"+Y+"  █████╗ ██████╗ ███╗  ███╗██╗███╗  ██╗  "+R+"║"),
(R,"║"+Y+"  ██╔══█╗██╔══██╗████╗████║██║████╗ ██║  "+R+"║"),
(R,"║"+Y+"  ███████║██║  ██║██╔███╔██║██║██╔██╗██║  "+R+"║"),
(R,"║"+Y+"  ██╔══██║██║  ██║██║╚█╔╝██║██║██║╚████║  "+R+"║"),
(R,"║"+Y+"  ██║  ██║██████╔╝██║ ╚╝ ██║██║██║ ╚███║  "+R+"║"),
(R,"║                                          ║"),
(R,"║"+C+"  ██████╗ ██╗███╗  ██╗██████╗ ███████╗██████╗"+R+"║"),
(R,"║"+C+"  ██╔════╝██║████╗ ██║██╔══██╗██╔════╝██╔══██╗"+R+"║"),
(R,"║"+C+"  █████╗  ██║██╔██╗██║██║  ██║█████╗  ██████╔╝"+R+"║"),
(R,"║"+C+"  ██╔══╝  ██║██║╚████║██║  ██║██╔══╝  ██╔══██╗"+R+"║"),
(R,"║"+C+"  ██║     ██║██║ ╚███║██████╔╝███████╗██║  ██║"+R+"║"),
(R,"║                                          ║"),
(R,"║"+G+"  ╔══════════════════════════════════╗   "+R+"║"),
(R,"║"+M+"  ║   Made by : Abdullah Balouch    ║   "+R+"║"),
(R,"║"+W+"  ║   Hidden Admin Panel Hunter     ║   "+R+"║"),
(R,"║"+Y+"  ║   Ethical Hacking Tool v1.0     ║   "+R+"║"),
(R,"║"+G+"  ╚══════════════════════════════════╝   "+R+"║"),
(R,"║                                          ║"),
(R,"╚══════════════════════════════════════════╝"),
    ]

    for color, line in lines:
        for char in line:
            sys.stdout.write(color + char + X)
            sys.stdout.flush()
            time.sleep(0.005)
        print()

    # Loading bar
    print(f"\n{C}  Initializing Scanner...{X}")
    bar = ""
    for i in range(1, 41):
        bar += "█"
        sys.stdout.write(f"\r{G}  [{bar:<40}] {Y}{i*100//40}%{X}")
        sys.stdout.flush()
        time.sleep(0.03)
    print(f"\n\n{G}  >> SYSTEM READY — TARGET LOCKED <<{X}\n")
    time.sleep(0.5)

def scan(url):
    paths = [
        'admin', 'admin/', 'admin/login', 'admin/index',
        'administrator', 'administrator/login',
        'wp-admin', 'wp-admin/admin.php',
        'wp-login.php', 'wp-admin/login.php',
        'cpanel', 'cpanel/', 'whm',
        'dashboard', 'dashboard/login',
        'login', 'login.php', 'login.html',
        'user/login', 'account/login',
        'panel', 'panel/login', 'panel/admin',
        'controlpanel', 'control',
        'manager', 'manager/html',
        'phpmyadmin', 'phpMyAdmin', 'pma',
        'webadmin', 'webmaster',
        'admin1', 'admin2', 'admin3',
        'backend', 'backend/login',
        'moderator', 'moderator/login',
        'webmail', 'mail',
        'portal', 'portal/login',
        'secure', 'security',
        'adminarea', 'admincp',
        'bb-admin', 'adminbb',
        'siteadmin', 'sitemanager',
        'memberadmin', 'members/login',
        'user', 'users/admin',
        'system', 'system/login',
        'config', 'configuration',
        'setup', 'install',
        'console', 'server-status',
        'joomla/administrator',
        'administrator/index.php',
        'admin/controlpanel',
        'wp/wp-admin',
        'blog/wp-admin',
    ]

    found = []
    headers = {'User-Agent': 'Mozilla/5.0'}

    print(f"{R}{'═'*44}{X}")
    print(f"{G}[★] Scanning: {Y}{url}{X}")
    print(f"{C}[*] Total Paths: {Y}{len(paths)}{X}")
    print(f"{R}{'═'*44}{X}\n")

    for path in paths:
        full_url = f"{url}/{path}"
        try:
            r = requests.get(full_url, headers=headers, timeout=5, allow_redirects=True)
            if r.status_code == 200:
                print(f"  {G}[FOUND ✓]{W} {Y}{full_url}{G} → {r.status_code}{X}")
                found.append(full_url)
            elif r.status_code == 302:
                print(f"  {Y}[REDIRECT]{W} {full_url} → {r.status_code}{X}")
            else:
                print(f"  {R}[✗]{W} {full_url} → {r.status_code}{X}")
        except:
            print(f"  {R}[TIMEOUT]{W} {full_url}{X}")
        time.sleep(0.1)

    print(f"\n{R}{'═'*44}{X}")
    if found:
        print(f"{G}[+] Admin Pages Found: {Y}{len(found)}{X}\n")
        for f in found:
            print(f"  {G}[★]{W} {f}{X}")
    else:
        print(f"{R}[!] No admin pages found!{X}")
    print(f"{R}{'═'*44}{X}")
    print(f"{G}[✓] Scan Complete!{X}")
    print(f"{M}    By Abdullah Balouch{X}")
    print(f"{R}{'═'*44}{X}\n")

def main():
    banner()
    print(f"{C}Enter Target URL: {Y}", end="")
    url = input().strip()
    if not url.startswith('http'):
        url = 'https://' + url
    url = url.rstrip('/')
    scan(url)

main()
