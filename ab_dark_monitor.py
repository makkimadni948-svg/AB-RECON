#!/usr/bin/env python3
import requests
import hashlib
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
║  {Y}  ██████╗  █████╗ ██████╗ ██╗  ██╗   {R}  ║
║  {Y}  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝   {R}  ║
║  {Y}  ██║  ██║███████║██████╔╝█████╔╝    {R}  ║
║  {Y}  ██║  ██║██╔══██║██╔══██╗██╔═██╗    {R}  ║
║  {Y}  ██████╔╝██║  ██║██║  ██║██║  ██╗   {R}  ║
║                                          ║
║  {G}  ★────────────────────────────★    {R} ║
║  {C}      AB-DARK MONITOR v1.0          {R}║
║  {G}  ★────────────────────────────★    {R} ║
║                                          ║
║  {M}      Made by: Abdullah Balouch     {R}║
║  {W}      Dark Web Leak Checker         {R}║
║                                          ║
╚══════════════════════════════════════════╝
{X}""")

def check_email(email):
    print(f"\n{Y}[⚡] Checking Email: {email}{X}\n")
    try:
        headers = {
            'User-Agent': 'AB-DarkMonitor',
            'hibp-api-key': 'free'
        }
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        r = requests.get(url, headers=headers, timeout=10)
        
        if r.status_code == 200:
            breaches = r.json()
            print(f"{R}[!] EMAIL LEAKED! Found in {len(breaches)} breaches!{X}\n")
            for breach in breaches:
                print(f"  {R}[BREACH]{W} {breach['Name']} {Y}({breach['BreachDate']}){X}")
        elif r.status_code == 404:
            print(f"{G}[✓] Good News! Email NOT found in any breach!{X}")
        elif r.status_code == 401:
            print(f"{Y}[!] API Key needed — checking alternative...{X}")
            check_email_alternative(email)
        else:
            print(f"{R}[!] Error: {r.status_code}{X}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{X}")

def check_email_alternative(email):
    try:
        url = f"https://api.xposedornot.com/v1/check-email/{email}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if 'breaches' in data:
                print(f"{R}[!] EMAIL LEAKED in these sites:{X}\n")
                for breach in data['breaches']:
                    print(f"  {R}[BREACH]{W} {breach}{X}")
            else:
                print(f"{G}[✓] Email NOT found in any breach!{X}")
        else:
            print(f"{G}[✓] Email appears safe!{X}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{X}")

def check_password(password):
    print(f"\n{Y}[⚡] Checking Password Strength + Leaks...{X}\n")
    
    # Strength check
    strength = 0
    tips = []
    
    if len(password) >= 8:
        strength += 1
    else:
        tips.append("8+ characters use karo")
    
    if any(c.isupper() for c in password):
        strength += 1
    else:
        tips.append("Capital letter add karo")
        
    if any(c.islower() for c in password):
        strength += 1
    else:
        tips.append("Small letter add karo")
        
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        tips.append("Number add karo")
        
    if any(c in '!@#$%^&*' for c in password):
        strength += 1
    else:
        tips.append("Special character add karo (!@#$)")

    levels = {1: f"{R}Very Weak", 2: f"{R}Weak", 3: f"{Y}Medium", 4: f"{G}Strong", 5: f"{G}Very Strong"}
    print(f"  {W}Strength: {levels.get(strength, R+'Unknown')}{X}")
    
    if tips:
        print(f"\n  {Y}Tips:{X}")
        for tip in tips:
            print(f"    {W}→ {tip}{X}")

    # HIBP Password check
    try:
        sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix, suffix = sha1[:5], sha1[5:]
        r = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=10)
        
        if suffix in r.text:
            count = [line.split(':')[1] for line in r.text.splitlines() if line.startswith(suffix)][0]
            print(f"\n  {R}[!] PASSWORD LEAKED! Found {count.strip()} times in breaches!{X}")
            print(f"  {R}[!] Change this password immediately!{X}")
        else:
            print(f"\n  {G}[✓] Password NOT found in any breach!{X}")
    except Exception as e:
        print(f"\n  {R}[!] Leak check error: {e}{X}")

def main():
    banner()
    
    print(f"{C}Choose Option:{X}")
    print(f"  {Y}[1]{W} Check Email Breach")
    print(f"  {Y}[2]{W} Check Password Leak")
    print(f"  {Y}[3]{W} Check Both")
    print(f"\n{C}Enter Choice: {Y}", end="")
    choice = input().strip()

    if choice == '1':
        print(f"\n{C}Enter Email: {Y}", end="")
        email = input().strip()
        print(f"\n{R}{'='*44}{X}")
        check_email(email)
        
    elif choice == '2':
        print(f"\n{C}Enter Password: {Y}", end="")
        password = input().strip()
        print(f"\n{R}{'='*44}{X}")
        check_password(password)
        
    elif choice == '3':
        print(f"\n{C}Enter Email: {Y}", end="")
        email = input().strip()
        print(f"\n{C}Enter Password: {Y}", end="")
        password = input().strip()
        print(f"\n{R}{'='*44}{X}")
        check_email(email)
        check_password(password)

    print(f"\n{R}{'='*44}{X}")
    print(f"{G}[✓] Scan Complete!{X}")
    print(f"{M}    By Abdullah Balouch{X}")
    print(f"{R}{'='*44}{X}\n")

main()
