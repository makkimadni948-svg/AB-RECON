#!/usr/bin/env python3
import os
import sys
import re
import PyPDF2
import docx

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
║  {Y}  ██████╗  ██████╗  ██████╗           {R}║
║  {Y}  ██╔══██╗██╔═══██╗██╔════╝           {R}║
║  {Y}  ██║  ██║██║   ██║██║                {R}║
║  {Y}  ██║  ██║██║   ██║██║                {R}║
║  {Y}  ██████╔╝╚██████╔╝╚██████╗           {R}║
║                                          ║
║  {G}  ★──────────────────────────────★  {R}║
║  {C}      AB-DOC EXTRACTOR v1.0          {R}║
║  {G}  ★──────────────────────────────★  {R}║
║                                          ║
║  {M}      Made by: Abdullah Balouch      {R}║
║  {W}      PDF & Document Intelligence    {R}║
║                                          ║
╚══════════════════════════════════════════╝
{X}""")

def extract_emails(text):
    return list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}', text)))

def extract_links(text):
    return list(set(re.findall(r'https?://[^\s]+', text)))

def extract_phones(text):
    return list(set(re.findall(r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}', text)))

def extract_pdf(filepath):
    print(f"\n{Y}[⚡] Extracting PDF: {filepath}{X}\n")
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            
            # Metadata
            print(f"{C}[1] PDF Metadata:{X}")
            meta = reader.metadata
            if meta:
                print(f"  {W}Author   : {Y}{meta.get('/Author', 'N/A')}{X}")
                print(f"  {W}Creator  : {Y}{meta.get('/Creator', 'N/A')}{X}")
                print(f"  {W}Producer : {Y}{meta.get('/Producer', 'N/A')}{X}")
                print(f"  {W}Created  : {Y}{meta.get('/CreationDate', 'N/A')}{X}")
                print(f"  {W}Modified : {Y}{meta.get('/ModDate', 'N/A')}{X}")
            
            # Pages
            pages = len(reader.pages)
            print(f"  {W}Pages    : {Y}{pages}{X}")
            
            # Text extraction
            print(f"\n{C}[2] Extracting Text...{X}")
            full_text = ""
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    full_text += text
            
            print(f"  {G}[+] Text extracted: {len(full_text)} characters{X}")
            
            # Emails
            print(f"\n{C}[3] Emails Found:{X}")
            emails = extract_emails(full_text)
            if emails:
                for email in emails:
                    print(f"  {G}[+]{W} {email}{X}")
            else:
                print(f"  {R}No emails found{X}")
            
            # Links
            print(f"\n{C}[4] Links Found:{X}")
            links = extract_links(full_text)
            if links:
                for link in links[:10]:
                    print(f"  {G}[+]{W} {link}{X}")
            else:
                print(f"  {R}No links found{X}")
            
            # Phone numbers
            print(f"\n{C}[5] Phone Numbers Found:{X}")
            phones = extract_phones(full_text)
            if phones:
                for phone in phones:
                    print(f"  {G}[+]{W} {phone}{X}")
            else:
                print(f"  {R}No phone numbers found{X}")
                
            # Preview
            print(f"\n{C}[6] Text Preview (First 500 chars):{X}")
            print(f"{W}{full_text[:500]}{X}")
            
    except Exception as e:
        print(f"{R}[!] Error: {e}{X}")

def extract_docx(filepath):
    print(f"\n{Y}[⚡] Extracting DOCX: {filepath}{X}\n")
    try:
        doc = docx.Document(filepath)
        
        # Core properties
        print(f"{C}[1] Document Metadata:{X}")
        props = doc.core_properties
        print(f"  {W}Author   : {Y}{props.author}{X}")
        print(f"  {W}Created  : {Y}{props.created}{X}")
        print(f"  {W}Modified : {Y}{props.modified}{X}")
        print(f"  {W}Title    : {Y}{props.title}{X}")
        print(f"  {W}Subject  : {Y}{props.subject}{X}")
        
        # Text
        print(f"\n{C}[2] Extracting Text...{X}")
        full_text = "\n".join([para.text for para in doc.paragraphs])
        print(f"  {G}[+] Text extracted: {len(full_text)} characters{X}")
        
        # Emails
        print(f"\n{C}[3] Emails Found:{X}")
        emails = extract_emails(full_text)
        if emails:
            for email in emails:
                print(f"  {G}[+]{W} {email}{X}")
        else:
            print(f"  {R}No emails found{X}")
        
        # Links
        print(f"\n{C}[4] Links Found:{X}")
        links = extract_links(full_text)
        if links:
            for link in links[:10]:
                print(f"  {G}[+]{W} {link}{X}")
        else:
            print(f"  {R}No links found{X}")

        # Preview
        print(f"\n{C}[5] Text Preview:{X}")
        print(f"{W}{full_text[:500]}{X}")
        
    except Exception as e:
        print(f"{R}[!] Error: {e}{X}")

def main():
    banner()
    
    print(f"{C}Choose Option:{X}")
    print(f"  {Y}[1]{W} Extract from PDF")
    print(f"  {Y}[2]{W} Extract from DOCX")
    
    print(f"\n{C}Enter Choice: {Y}", end="")
    choice = input().strip()
    
    print(f"\n{C}Enter File Path: {Y}", end="")
    filepath = input().strip()
    
    print(f"\n{R}{'='*44}{X}")
    
    if choice == '1':
        extract_pdf(filepath)
    elif choice == '2':
        extract_docx(filepath)
    
    print(f"\n{R}{'='*44}{X}")
    print(f"{G}[✓] Extraction Complete!{X}")
    print(f"{M}    By Abdullah Balouch{X}")
    print(f"{R}{'='*44}{X}\n")

main()
