#!/usr/bin/env python3
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
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
║  {Y} ██████╗ ██╗  ██╗ ██████╗ ███╗  ██╗  {R}║
║  {Y} ██╔══██╗██║  ██║██╔═══██╗████╗ ██║  {R}║
║  {Y} ██████╔╝███████║██║   ██║██╔██╗██║  {R}║
║  {Y} ██╔═══╝ ██╔══██║██║   ██║██║╚████║  {R}║
║  {Y} ██║     ██║  ██║╚██████╔╝██║ ╚███║  {R}║
║                                          ║
║  {G}  ★──────────────────────────────★  {R}║
║  {C}       AB-PHONE TRACKER v1.0        {R}║
║  {G}  ★──────────────────────────────★  {R}║
║                                          ║
║  {M}      Made by: Abdullah Balouch     {R}║
║  {W}      Phone Number Intelligence     {R}║
║                                          ║
╚══════════════════════════════════════════╝
{X}""")

def track_number(number):
    try:
        # Parse number
        parsed = phonenumbers.parse(number)
        
        # Valid check
        is_valid = phonenumbers.is_valid_number(parsed)
        is_possible = phonenumbers.is_possible_number(parsed)
        
        print(f"\n{R}{'='*44}{X}")
        print(f"{G}[★] AB-PHONE TRACKER Results{X}")
        print(f"{R}{'='*44}{X}\n")
        
        # Basic Info
        print(f"  {C}[1] Basic Info:{X}")
        print(f"      {W}Number      : {Y}{number}{X}")
        print(f"      {W}Valid       : {G if is_valid else R}{is_valid}{X}")
        print(f"      {W}Possible    : {G if is_possible else R}{is_possible}{X}")
        
        # Format
        intl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        natl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        print(f"      {W}Intl Format : {Y}{intl}{X}")
        print(f"      {W}Natl Format : {Y}{natl}{X}")
        
        # Location
        print(f"\n  {C}[2] Location Info:{X}")
        region = geocoder.description_for_number(parsed, 'en')
        country_code = parsed.country_code
        print(f"      {W}Region      : {Y}{region}{X}")
        print(f"      {W}Country Code: {Y}+{country_code}{X}")
        
        # Carrier
        print(f"\n  {C}[3] Network Info:{X}")
        carrier_name = carrier.name_for_number(parsed, 'en')
        print(f"      {W}Carrier     : {Y}{carrier_name if carrier_name else 'Unknown'}{X}")
        
        # Timezone
        print(f"\n  {C}[4] Timezone:{X}")
        timezones = timezone.time_zones_for_number(parsed)
        for tz in timezones:
            print(f"      {W}Timezone    : {Y}{tz}{X}")
        
        # Number Type
        print(f"\n  {C}[5] Number Type:{X}")
        num_type = phonenumbers.number_type(parsed)
        types = {
            0: "FIXED_LINE",
            1: "MOBILE",
            2: "FIXED_LINE_OR_MOBILE",
            3: "TOLL_FREE",
            4: "PREMIUM_RATE",
            6: "VOIP",
            7: "PERSONAL_NUMBER",
        }
        print(f"      {W}Type        : {Y}{types.get(num_type, 'UNKNOWN')}{X}")

        # IP API Location
        print(f"\n  {C}[6] Country Details:{X}")
        try:
            r = requests.get(f"https://restcountries.com/v3.1/callingcode/{country_code}", timeout=5)
            if r.status_code == 200:
                data = r.json()[0]
                print(f"      {W}Country     : {Y}{data.get('name', {}).get('common', 'N/A')}{X}")
                print(f"      {W}Capital     : {Y}{data.get('capital', ['N/A'])[0]}{X}")
                print(f"      {W}Region      : {Y}{data.get('region', 'N/A')}{X}")
                print(f"      {W}Currency    : {Y}{list(data.get('currencies', {}).keys())}{X}")
        except:
            pass

    except Exception as e:
        print(f"\n{R}[!] Error: {e}{X}")
        print(f"{Y}[!] Format: +92XXXXXXXXXX{X}")

def main():
    banner()
    print(f"{C}Enter Phone Number with country code:{X}")
    print(f"{Y}Example: +923001234567{X}\n")
    print(f"{C}Enter Number: {Y}", end="")
    number = input().strip()
    
    track_number(number)
    
    print(f"\n{R}{'='*44}{X}")
    print(f"{G}[✓] Scan Complete!{X}")
    print(f"{M}    By Abdullah Balouch{X}")
    print(f"{R}{'='*44}{X}\n")

main()
