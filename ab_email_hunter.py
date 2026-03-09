#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import os
import time

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[97m'
M = '\033[95m'
X = '\033[0m'

def banner():
    os.system('clear')
    print(f"""{R}
╔══════════════════════════════════════════╗
║                                          ║
║  {Y} ███████╗███╗  ███╗ █████╗ ██╗██╗   {R}  ║
║  {Y} ██╔════╝████╗████║██╔══██╗██║██║   {R}  ║
║  {Y} █████╗  ██╔███╔██║███████║██║██║   {R}  ║
║  {Y} ██╔══╝  ██║╚█╔╝██║██╔══██║██║██║   {R}  ║
║  {Y} ███████╗██║ ╚╝ ██║██║  ██║██║█████╗{R}  ║
║                                          ║
║  {G}  ★───────────────────────────★     {R}║
║  {C}      AB-EMAIL HUNTER v2.0          {R}║
║  {G}  ★───────────────────────────★     {R}║
║                                          ║
║  {M}      Made by: Abdullah Balouch     {R}║
║  {W}      Google Dork + Web Scanner     {R}║
║                                          ║
╚══════════════════════════════════════════╝
{X}""")

def google_dork(domain):
    print(f"\n{Y}[⚡] Google Dorking: {domain}{X}\n")
    emails = set()
    dorks = [
        f'site:{domain} email',
        f'site:{domain} contact',
        f'site:{domain} "@{domain}"',
    ]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    for dork in dorks:
        try:
            url = f"https://www.google.com/search?q={requests.utils.quote(dork)}"
            r = requests.get(url, headers=headers, timeout=10)
            found = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', r.text)
            found = [e for e in found if not any(e.endswith(x) for x in ['.png','.jpg','.gif','.svg','.jpeg'])]
            emails.update(found)
            print(f"  {G}[+]{W} Dork: {Y}{dork}{X}")
            time.sleep(2)
        except Exception as e:
            print(f"  {R}[!] Error: {e}{X}")
    return emails

def web_scan(url):
    print(f"\n{Y}[⚡] Web Scanning: {url}{X}\n")
    emails = set()
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10)
        found = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', r.text)
        found = [e for e in found if not any(e.endswith(x) for x in ['.png','.jpg','.gif','.svg','.jpeg'])]
        emails.update(found)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            if 'mailto:' in link['href']:
                emails.add(link['href'].replace('mailto:','').strip())
    except Exception as e:
        print(f"  {R}[!] Error: {e}{X}")
    return emails

def main():
    banner()
    print(f"{C}Enter Target Domain: {Y}", end="")
    domain = input().strip()
    domain = domain.replace('https://','').replace('http://','').replace('www.','')
    url = 'https://' + domain

    print(f"\n{R}{'='*44}{X}")
    print(f"{G}[★] AB-Email Hunter Started!{X}")
    print(f"{Y}    Target: {domain}{X}")
    print(f"{R}{'='*44}{X}")

    all_emails = set()
    web_emails = web_scan(url)
    all_emails.update(web_emails)
    dork_emails = google_dork(domain)
    all_emails.update(dork_emails)

    print(f"\n{R}{'='*44}{X}")
    if all_emails:
        print(f"{G}[+] Total Emails Found: {Y}{len(all_emails)}{X}\n")
        for i, email in enumerate(all_emails, 1):
            print(f"  {G}[{i}]{W} {email}{X}")
    else:
        print(f"{R}[!] No emails found!{X}")

    print(f"\n{R}{'='*44}{X}")
    print(f"{G}[✓] Scan Complete!{X}")
    print(f"{M}    By Abdullah Balouch{X}")
    print(f"{R}{'='*44}{X}\n")

main()
