#!/usr/bin/env python3
import os
import socket
import subprocess
import requests
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
║  {Y}     ░█████╗░██████╗       {R}            ║
║  {Y}     ██╔══██╗██╔══██╗      {R}            ║
║  {Y}     ███████║██████╔╝      {R}            ║
║  {Y}     ██╔══██║██╔══██╗      {R}            ║
║  {Y}     ██║  ██║██████╔╝      {R}            ║
║                                          ║
║  {C}  ╦═╗ ╔═╗ ╔═╗ ╔═╗ ╔╗╔     {R}            ║
║  {C}  ╠╦╝ ║╣  ║   ║ ║ ║║║     {R}            ║
║  {C}  ╩╚═ ╚═╝ ╚═╝ ╚═╝ ╝╚╝     {R}            ║
║                                          ║
║  {G}    ★ AB-RECON Tool v1.0 ★           {R}║
║  {M}    Made by: Abdullah Balouch        {R}║
║  {W}    Ethical Hacking & Recon          {R}║
╚══════════════════════════════════════════╝
{X}""")

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return "Not Found"

def get_location(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()
        return {
            "Country": data.get("country", "N/A"),
            "City": data.get("city", "N/A"),
            "ISP": data.get("isp", "N/A"),
            "Lat/Long": f"{data.get('lat')}, {data.get('lon')}"
        }
    except:
        return {}

def get_dns(domain):
    try:
        result = subprocess.run(
            ["nslookup", domain],
            capture_output=True, text=True
        )
        return result.stdout
    except:
        return "DNS lookup failed"

def port_scan(ip):
    print(f"\n{Y}[⚡] Scanning Top Ports...{X}\n")
    common_ports = [21,22,23,25,53,80,443,8080,8443,3306]
    open_ports = []
    for port in common_ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
                print(f"  {G}[OPEN]{X} Port {Y}{port}{X}")
            s.close()
        except:
            pass
    if not open_ports:
        print(f"  {R}No open ports found!{X}")

def main():
    banner()
    print(f"{C}Enter Target Domain/IP: {Y}", end="")
    target = input().strip()
    print(X)

    print(f"{R}{'='*44}{X}")
    print(f"{G}[★] AB-RECON Started — Target: {Y}{target}{X}")
    print(f"{R}{'='*44}{X}\n")
    time.sleep(1)

    # IP
    ip = get_ip(target)
    print(f"{C}[1] IP Address   {W}→ {G}{ip}{X}")

    # Location
    print(f"\n{C}[2] Location Info:{X}")
    loc = get_location(ip)
    for k, v in loc.items():
        print(f"  {W}{k}: {Y}{v}{X}")

    # DNS
    print(f"\n{C}[3] DNS Info:{X}")
    dns = get_dns(target)
    print(f"{W}{dns}{X}")

    # Ports
    print(f"\n{C}[4] Open Ports:{X}")
    port_scan(ip)

    print(f"\n{R}{'='*44}{X}")
    print(f"{G}[✓] AB-RECON Complete!{X}")
    print(f"{M}    By Abdullah Balouch{X}")
    print(f"{R}{'='*44}{X}\n")

main()
