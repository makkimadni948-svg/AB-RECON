#!/usr/bin/env python3
# ================================================
#   AB Forensics Kit v1.0
#   By Abdullah Balouch | Pakistan 🇵🇰
#   GitHub: makkimadni948-svg
#   For Rooted Termux Only!
#   For Educational & Ethical Use Only!
# ================================================

import os, subprocess, time
from datetime import datetime

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
C = '\033[96m'
W = '\033[97m'
X = '\033[0m'
BOLD = '\033[1m'

def banner():
    os.system('clear')
    print(f"""{R}{BOLD}
╔══════════════════════════════════════════════╗
║           AB Forensics Kit v1.0              ║
║        By Abdullah Balouch 🇵🇰               ║
║        GitHub: makkimadni948-svg             ║
║     ⚠️  Rooted Termux Only - Ethical Use!    ║
╚══════════════════════════════════════════════╝
{X}""")

def check_root():
    result = subprocess.run(['su', '-c', 'whoami'], capture_output=True, text=True)
    if 'root' in result.stdout:
        print(f"{G}[+] Root access confirmed! ✅{X}\n")
        return True
    else:
        print(f"{R}[!] Root access required! Tool will not work!{X}\n")
        return False

def save_report(title, content):
    folder = os.path.expanduser("~/ab_forensics_reports")
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{title}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as f:
        f.write("AB Forensics Kit v1.0\n")
        f.write("By Abdullah Balouch\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*50 + "\n\n")
        f.write(content)
    print(f"\n{G}[+] Report saved: {filename}{X}")

def deleted_files_recovery():
    os.system('clear')
    banner()
    print(f"{C}{BOLD}DELETED FILES RECOVERY{X}\n")
    print(f"{Y}[*] Scanning for recoverable files...{X}\n")
    paths = ["/sdcard/DCIM/.thumbnails", "/sdcard/.trash", "/data/media/0/.trash", "/sdcard/Android/data"]
    found = []
    report = "DELETED FILES SCAN\n\n"
    for path in paths:
        result = subprocess.run(f"su -c 'ls -la {path} 2>/dev/null'", shell=True, capture_output=True, text=True)
        if result.stdout.strip():
            print(f"{G}[+] Found in: {path}{X}")
            found.append(path)
            report += f"Path: {path}\n{result.stdout}\n\n"
        else:
            print(f"{R}[-] Empty: {path}{X}")
    result = subprocess.run("su -c 'find /sdcard -mtime -1 -type f 2>/dev/null | head -20'", shell=True, capture_output=True, text=True)
    if result.stdout:
        print(f"\n{C}Recently modified files:{X}\n{W}{result.stdout}{X}")
        report += f"Recent Files:\n{result.stdout}\n"
    print(f"\n{G}[+] Scan complete! Found {len(found)} recoverable locations{X}")
    save_report("deleted_files", report)
    input(f"\n{Y}[Press Enter to go back...]{X}")

def app_data_analyzer():
    os.system('clear')
    banner()
    print(f"{C}{BOLD}APP DATA ANALYZER{X}\n")
    app = input(f"{Y}[?] Enter app package name (e.g. com.whatsapp): {X}").strip()
    if not app:
        print(f"{R}[!] No app name provided!{X}")
        return
    print(f"\n{Y}[*] Analyzing {app}...{X}\n")
    report = f"APP ANALYSIS: {app}\n\n"
    for name, cmd in [
        ("App Info", f"su -c 'dumpsys package {app} 2>/dev/null | head -30'"),
        ("Data Files", f"su -c 'ls -la /data/data/{app}/ 2>/dev/null'"),
        ("Databases", f"su -c 'find /data/data/{app} -name \"*.db\" 2>/dev/null'"),
    ]:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(f"{G}[+] {name}:{X}\n{W}{result.stdout[:400]}{X}\n")
            report += f"{name}:\n{result.stdout}\n\n"
    save_report(f"app_{app}", report)
    input(f"\n{Y}[Press Enter to go back...]{X}")

def hidden_files_detector():
    os.system('clear')
    banner()
    print(f"{C}{BOLD}HIDDEN FILES DETECTOR{X}\n")
    print(f"{Y}[*] Scanning for hidden files...{X}\n")
    report = "HIDDEN FILES SCAN\n\n"
    result = subprocess.run("su -c 'find /sdcard -name \".*\" -type f 2>/dev/null | head -30'", shell=True, capture_output=True, text=True)
    if result.stdout:
        files = result.stdout.strip().split('\n')
        print(f"{G}[+] Hidden files found: {len(files)}{X}")
        for f in files[:15]:
            print(f"{Y}  -> {f}{X}")
        report += f"Hidden Files:\n{result.stdout}\n\n"
    result = subprocess.run("su -c 'find /sdcard -name \"*.apk\" 2>/dev/null'", shell=True, capture_output=True, text=True)
    if result.stdout:
        print(f"\n{R}[!] APK files found:{X}\n{W}{result.stdout}{X}")
        report += f"APK Files:\n{result.stdout}\n\n"
    else:
        print(f"{G}[+] No suspicious APKs found{X}")
    result = subprocess.run("su -c 'find /sdcard -name \".*\" -size +10M 2>/dev/null'", shell=True, capture_output=True, text=True)
    if result.stdout:
        print(f"\n{R}[!] Large hidden files:{X}\n{W}{result.stdout}{X}")
        report += f"Large Hidden Files:\n{result.stdout}\n"
    save_report("hidden_files", report)
    input(f"\n{Y}[Press Enter to go back...]{X}")

def network_forensics():
    os.system('clear')
    banner()
    print(f"{C}{BOLD}NETWORK FORENSICS{X}\n")
    print(f"{Y}[*] Analyzing active network connections...{X}\n")
    report = "NETWORK FORENSICS\n\n"
    for name, cmd in [
        ("Active Connections", "su -c 'netstat -tunapl 2>/dev/null | head -30'"),
        ("TCP Data", "su -c 'cat /proc/net/tcp 2>/dev/null | head -20'"),
        ("DNS Cache", "su -c 'cat /data/misc/net/resolv_cache 2>/dev/null'"),
    ]:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(f"{G}[+] {name}:{X}\n{W}{result.stdout[:400]}{X}\n")
            report += f"{name}:\n{result.stdout}\n\n"
        else:
            print(f"{Y}[*] {name}: Not accessible{X}")
    save_report("network_forensics", report)
    input(f"\n{Y}[Press Enter to go back...]{X}")

def ram_analyzer():
    os.system('clear')
    banner()
    print(f"{C}{BOLD}RAM ANALYZER{X}\n")
    print(f"{Y}[*] Analyzing RAM usage...{X}\n")
    report = "RAM ANALYSIS\n\n"
    result = subprocess.run("cat /proc/meminfo", shell=True, capture_output=True, text=True)
    if result.stdout:
        print(f"{G}[+] Memory Info:{X}")
        for line in result.stdout.split('\n')[:8]:
            print(f"{W}  {line}{X}")
        report += f"Memory Info:\n{result.stdout}\n\n"
    result = subprocess.run("su -c 'ps -A --sort=-%mem 2>/dev/null | head -15'", shell=True, capture_output=True, text=True)
    if result.stdout:
        print(f"\n{C}Top RAM processes:{X}\n{W}{result.stdout}{X}")
        report += f"Top Processes:\n{result.stdout}\n\n"
    result = subprocess.run("su -c 'ps -A 2>/dev/null | grep -E \"spy|keylog|monitor|record\"'", shell=True, capture_output=True, text=True)
    if result.stdout:
        print(f"{R}[!] Suspicious processes:{X}\n{W}{result.stdout}{X}")
        report += f"Suspicious:\n{result.stdout}\n"
    else:
        print(f"{G}[+] No suspicious processes found! ✅{X}")
        report += "No suspicious processes found!\n"
    save_report("ram_analysis", report)
    input(f"\n{Y}[Press Enter to go back...]{X}")

def system_info():
    os.system('clear')
    banner()
    print(f"{C}{BOLD}SYSTEM INFO{X}\n")
    report = "SYSTEM INFO\n\n"
    for name, cmd in [
        ("Device Model", "su -c 'getprop ro.product.model 2>/dev/null'"),
        ("Android Version", "su -c 'getprop ro.build.version.release 2>/dev/null'"),
        ("Serial Number", "su -c 'getprop ro.serialno 2>/dev/null'"),
        ("Installed Apps", "su -c 'pm list packages 2>/dev/null | wc -l'"),
        ("Storage", "df -h /sdcard 2>/dev/null"),
        ("CPU", "cat /proc/cpuinfo 2>/dev/null | grep 'model name' | head -1"),
    ]:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout.strip():
            print(f"{G}[+] {name}:{X} {W}{result.stdout.strip()[:80]}{X}")
            report += f"{name}: {result.stdout.strip()}\n"
    save_report("system_info", report)
    input(f"\n{Y}[Press Enter to go back...]{X}")

def main():
    banner()
    if not check_root():
        input("Press Enter to exit...")
        return
    while True:
        banner()
        print(f"{G}[+] Root Access: ACTIVE ✅{X}\n")
        print(f"""{B}{BOLD}
╔══════════════════════════════════════╗
║             MAIN MENU                ║
╠══════════════════════════════════════╣
║  1.  Deleted Files Recovery          ║
║  2.  App Data Analyzer               ║
║  3.  Hidden Files Detector           ║
║  4.  Network Forensics               ║
║  5.  RAM Analyzer                    ║
║  6.  System Info                     ║
║  7.  Exit                            ║
╚══════════════════════════════════════╝{X}""")
        choice = input(f"\n{Y}[?] Select option: {X}").strip()
        if choice == '1': deleted_files_recovery()
        elif choice == '2': app_data_analyzer()
        elif choice == '3': hidden_files_detector()
        elif choice == '4': network_forensics()
        elif choice == '5': ram_analyzer()
        elif choice == '6': system_info()
        elif choice == '7':
            print(f"\n{G}Goodbye! By Abdullah Balouch 🇵🇰{X}\n")
            break
        else:
            print(f"{R}[!] Invalid option!{X}")
            time.sleep(1)

main()
