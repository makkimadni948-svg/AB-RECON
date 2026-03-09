#!/usr/bin/env python3
import subprocess
import socket
import os
import time

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
C = '\033[96m'
W = '\033[97m'
X = '\033[0m'

def banner():
    os.system('clear')
    print(f"""{R}
╔══════════════════════════════════════╗
║  {Y}  ███╗   ██╗███████╗████████╗       {R}║
║  {Y}  ████╗  ██║██╔════╝╚══██╔══╝       {R}║
║  {Y}  ██╔██╗ ██║█████╗     ██║          {R}║
║  {Y}  ██║╚██╗██║██╔══╝     ██║          {R}║
║  {Y}  ██║ ╚████║███████╗   ██║          {R}║
║  {C}     Network Scanner v2.0          {R}║
║  {G}     Made by: Abdullah Balouch     {R}║
║  {W}     Ethical Hacking Tool          {R}║
╚══════════════════════════════════════╝{X}
""")

def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def scan_network(network):
    print(f"{C}[*]{W} Target Network : {Y}{network}.0/24{X}")
    print(f"{C}[*]{W} Scanning Started...\n{X}")
    found = []
    for i in range(1, 255):
        ip = f"{network}.{i}"
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            print(f"  {G}[+] FOUND {W}→ {Y}{ip}{G} ● Online{X}")
            found.append(ip)

    print(f"\n{R}{'='*42}{X}")
    print(f"{G}[✓] Scan Complete! Total Devices: {Y}{len(found)}{X}")
    print(f"{R}{'='*42}{X}")

def main():
    banner()
    my_ip = get_my_ip()
    print(f"{C}[*]{W} Your IP Address : {Y}{my_ip}{X}\n")
    time.sleep(1)
    network = ".".join(my_ip.split(".")[:3])
    scan_network(network)

main()
