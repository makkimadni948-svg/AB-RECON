#!/usr/bin/env python3
import requests
import os
import time
import json
from bs4 import BeautifulSoup

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
    print(f"""{R}
╔══════════════════════════════════════════╗
║                                          ║
║  {Y}  ██████╗ ███████╗██╗███╗  ██╗████████╗{R}║
║  {Y}  ██╔══██╗██╔════╝██║████╗ ██║╚══██╔══╝{R}║
║  {Y}  ██║  ██║███████╗██║██╔██╗██║   ██║   {R}║
║  {Y}  ██║  ██║╚════██║██║██║╚████║   ██║   {R}║
║  {Y}  ██████╔╝███████║██║██║ ╚███║   ██║   {R}║
║                                          ║
║  {G}  ★──────────────────────────────★  {R}║
║  {C}        AB-OSINT Tool v1.0          {R}║
║  {G}  ★──────────────────────────────★  {R}║
║                                          ║
║  {M}      Made by: Abdullah Balouch     {R}║
║  {W}      Open Source Intelligence      {R}║
║                                          ║
╚══════════════════════════════════════════╝
{X}""")

def check_social_media(username):
    print(f"\n{C}[1] Social Media Hunt — @{username}{X}\n")
    
    platforms = {
        'GitHub': f'https://github.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'Instagram': f'https://instagram.com/{username}',
        'TikTok': f'https://tiktok.com/@{username}',
        'Reddit': f'https://reddit.com/user/{username}',
        'Pinterest': f'https://pinterest.com/{username}',
        'LinkedIn': f'https://linkedin.com/in/{username}',
        'YouTube': f'https://youtube.com/@{username}',
        'Telegram': f'https://t.me/{username}',
        'Medium': f'https://medium.com/@{username}',
    }
    
    found = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for platform, url in platforms.items():
        try:
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                print(f"  {G}[FOUND]{W} {platform}: {Y}{url}{X}")
                found.append(platform)
            else:
                print(f"  {R}[NOT FOUND]{W} {platform}{X}")
        except:
            print(f"  {Y}[TIMEOUT]{W} {platform}{X}")
        time.sleep(0.5)
    
    print(f"\n  {G}[+] Found on {len(found)} platforms!{X}")
    return found

def ip_lookup(target):
    print(f"\n{C}[2] IP & Location Info — {target}{X}\n")
    try:
        # Get IP
        try:
            import socket
            ip = socket.gethostbyname(target)
        except:
            ip = target
            
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()
        
        print(f"  {W}IP Address  : {Y}{ip}{X}")
        print(f"  {W}Country     : {Y}{data.get('country', 'N/A')}{X}")
        print(f"  {W}City        : {Y}{data.get('city', 'N/A')}{X}")
        print(f"  {W}ISP         : {Y}{data.get('isp', 'N/A')}{X}")
        print(f"  {W}Timezone    : {Y}{data.get('timezone', 'N/A')}{X}")
        print(f"  {W}Lat/Long    : {Y}{data.get('lat')}, {data.get('lon')}{X}")
    except Exception as e:
        print(f"  {R}[!] Error: {e}{X}")

def whois_lookup(domain):
    print(f"\n{C}[3] WHOIS Info — {domain}{X}\n")
    try:
        r = requests.get(f"https://api.whois.vu/?q={domain}", timeout=10)
        data = r.json()
        if 'whois' in data:
            lines = data['whois'].split('\n')[:15]
            for line in lines:
                if line.strip():
                    print(f"  {W}{line}{X}")
    except Exception as e:
        print(f"  {R}[!] Error: {e}{X}")

def email_breach_check(email):
    print(f"\n{C}[4] Email Breach Check — {email}{X}\n")
    try:
        r = requests.get(
            f"https://api.xposedornot.com/v1/check-email/{email}",
            timeout=10
        )
        if r.status_code == 200:
            data = r.json()
            if 'breaches' in data:
                print(f"  {R}[!] EMAIL LEAKED in:{X}")
                for breach in data['breaches']:
                    print(f"    {R}→{W} {breach}{X}")
            else:
                print(f"  {G}[✓] Email NOT found in any breach!{X}")
        else:
            print(f"  {G}[✓] Email appears safe!{X}")
    except Exception as e:
        print(f"  {R}[!] Error: {e}{X}")

def main():
    banner()
    
    print(f"{C}Choose Scan Type:{X}")
    print(f"  {Y}[1]{W} Username Hunt — Social Media")
    print(f"  {Y}[2]{W} Domain/IP Intelligence")
    print(f"  {Y}[3]{W} Email Breach Check")
    print(f"  {Y}[4]{W} Full OSINT — All in One")
    
    print(f"\n{C}Enter Choice: {Y}", end="")
    choice = input().strip()
    
    print(f"\n{R}{'='*44}{X}")
    
    if choice == '1':
        print(f"{C}Enter Username: {Y}", end="")
        username = input().strip()
        check_social_media(username)
        
    elif choice == '2':
        print(f"{C}Enter Domain/IP: {Y}", end="")
        target = input().strip()
        ip_lookup(target)
        whois_lookup(target)
        
    elif choice == '3':
        print(f"{C}Enter Email: {Y}", end="")
        email = input().strip()
        email_breach_check(email)
        
    elif choice == '4':
        print(f"{C}Enter Username: {Y}", end="")
        username = input().strip()
        print(f"{C}Enter Domain: {Y}", end="")
        domain = input().strip()
        print(f"{C}Enter Email: {Y}", end="")
        email = input().strip()
        
        check_social_media(username)
        ip_lookup(domain)
        whois_lookup(domain)
        email_breach_check(email)
    
    print(f"\n{R}{'='*44}{X}")
    print(f"{G}[✓] AB-OSINT Complete!{X}")
    print(f"{M}    By Abdullah Balouch{X}")
    print(f"{R}{'='*44}{X}\n")

main()
