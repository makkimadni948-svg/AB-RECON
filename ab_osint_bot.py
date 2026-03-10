#!/usr/bin/env python3
import requests
import socket
import re
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8623058215:AAF3MJCB-BKjHEmab685GLayN01buwd6fqY"
logging.basicConfig(level=logging.WARNING)

# ── START ──
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔐 *AB OSINT Bot — Full Suite*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👨‍💻 Made by: *Abdullah Balouch*\n"
        "🇵🇰 Multan, Pakistan\n\n"
        "📋 *Commands:*\n\n"
        "🌐 /ip — IP Location\n"
        "📱 /phone — Phone Info\n"
        "🔍 /whois — Domain WHOIS\n"
        "⚡ /scan — Port Scanner\n"
        "🌤 /weather — Weather\n"
        "📧 /email — Email Breach\n"
        "🔗 /sub — Subdomain Finder\n"
        "💻 /tech — Tech Detector\n"
        "🔓 /admin — Admin Finder\n"
        "📊 /recon — Full Recon\n"
        "❓ /help — All Commands\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⚠️ *Ethical Use Only!*",
        parse_mode='Markdown'
    )

# ── HELP ──
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 *AB OSINT Bot — Commands*\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🌐 */ip 8.8.8.8*\n"
        "📱 */phone +923001234567*\n"
        "🔍 */whois google.com*\n"
        "⚡ */scan google.com*\n"
        "🌤 */weather Multan*\n"
        "📧 */email test@gmail.com*\n"
        "🔗 */sub google.com*\n"
        "💻 */tech google.com*\n"
        "🔓 */admin google.com*\n"
        "📊 */recon google.com*\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🇵🇰 By Abdullah Balouch",
        parse_mode='Markdown'
    )

# ── IP LOOKUP ──
async def ip_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /ip 8.8.8.8")
        return
    ip = context.args[0]
    await update.message.reply_text(f"🔍 Looking up {ip}...")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        d = r.json()
        if d['status'] == 'success':
            result = (
                f"🌐 *IP Lookup Report*\n"
                f"━━━━━━━━━━━━━━━━\n"
                f"📍 IP: `{d.get('query')}`\n"
                f"🌍 Country: {d.get('country')}\n"
                f"🏙 City: {d.get('city')}\n"
                f"📡 ISP: {d.get('isp')}\n"
                f"🏢 Org: {d.get('org')}\n"
                f"⏰ Timezone: {d.get('timezone')}\n"
                f"📌 Lat/Long: {d.get('lat')}, {d.get('lon')}\n"
                f"━━━━━━━━━━━━━━━━\n"
                f"🇵🇰 By Abdullah Balouch"
            )
        else:
            result = f"❌ Private/Invalid IP: {ip}"
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── PHONE ──
async def phone_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /phone +923001234567")
        return
    number = context.args[0]
    await update.message.reply_text(f"📱 Analyzing {number}...")
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone
        parsed = phonenumbers.parse(number)
        is_valid = phonenumbers.is_valid_number(parsed)
        region = geocoder.description_for_number(parsed, 'en')
        carrier_name = carrier.name_for_number(parsed, 'en')
        timezones = timezone.time_zones_for_number(parsed)
        result = (
            f"📱 *Phone OSINT Report*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"📞 Number: `{number}`\n"
            f"✅ Valid: {is_valid}\n"
            f"🌍 Region: {region}\n"
            f"📡 Carrier: {carrier_name or 'Unknown'}\n"
            f"⏰ Timezone: {', '.join(timezones)}\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🇵🇰 By Abdullah Balouch"
        )
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── WHOIS ──
async def whois_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /whois google.com")
        return
    domain = context.args[0]
    await update.message.reply_text(f"🔍 WHOIS lookup for {domain}...")
    try:
        ip = socket.gethostbyname(domain)
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        d = r.json()
        
        # Creation date via RDAP
        try:
            rdap = requests.get(f"https://rdap.org/domain/{domain}", timeout=5)
            rdap_data = rdap.json()
            events = rdap_data.get('events', [])
            created = next((e['eventDate'][:10] for e in events if e['eventAction'] == 'registration'), 'Unknown')
            expiry = next((e['eventDate'][:10] for e in events if e['eventAction'] == 'expiration'), 'Unknown')
        except:
            created = 'Unknown'
            expiry = 'Unknown'

        result = (
            f"🔍 *WHOIS Report*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🌐 Domain: `{domain}`\n"
            f"📍 IP: `{ip}`\n"
            f"🌍 Country: {d.get('country', 'N/A')}\n"
            f"🏙 City: {d.get('city', 'N/A')}\n"
            f"📡 ISP: {d.get('isp', 'N/A')}\n"
            f"🏢 Org: {d.get('org', 'N/A')}\n"
            f"📅 Created: {created}\n"
            f"⏰ Expires: {expiry}\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🇵🇰 By Abdullah Balouch"
        )
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── PORT SCAN ──
async def port_scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /scan google.com")
        return
    domain = context.args[0]
    await update.message.reply_text(f"⚡ Scanning {domain}...")
    try:
        ip = socket.gethostbyname(domain)
        common_ports = {21:'FTP',22:'SSH',23:'Telnet',25:'SMTP',
                       53:'DNS',80:'HTTP',443:'HTTPS',445:'SMB',
                       3306:'MySQL',3389:'RDP',8080:'HTTP-Alt',8443:'HTTPS-Alt'}
        open_ports = []
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(f"✅ {port} — {service}")
            sock.close()
        ports_text = '\n'.join(open_ports) if open_ports else "❌ No open ports"
        result = (
            f"⚡ *Port Scan Report*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🎯 Target: `{domain}`\n"
            f"📍 IP: `{ip}`\n\n"
            f"{ports_text}\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🇵🇰 By Abdullah Balouch"
        )
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── WEATHER ──
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /weather Multan")
        return
    city = ' '.join(context.args)
    try:
        r = requests.get(f"https://wttr.in/{city}?format=3", timeout=5)
        await update.message.reply_text(
            f"🌤 *Weather Report*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"{r.text}\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🇵🇰 By Abdullah Balouch",
            parse_mode='Markdown'
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── EMAIL BREACH ──
async def email_breach(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /email test@gmail.com")
        return
    email = context.args[0]
    await update.message.reply_text(f"📧 Checking {email}...")
    try:
        headers = {'User-Agent': 'AB-OSINT-Bot'}
        r = requests.get(
            f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
            headers=headers, timeout=5
        )
        if r.status_code == 200:
            breaches = r.json()
            breach_list = '\n'.join([f"⚠️ {b['Name']}" for b in breaches[:5]])
            result = (
                f"📧 *Email Breach Report*\n"
                f"━━━━━━━━━━━━━━━━\n"
                f"📨 Email: `{email}`\n"
                f"🚨 Found in {len(breaches)} breaches!\n\n"
                f"{breach_list}\n"
                f"━━━━━━━━━━━━━━━━\n"
                f"🇵🇰 By Abdullah Balouch"
            )
        elif r.status_code == 404:
            result = (
                f"📧 *Email Breach Report*\n"
                f"━━━━━━━━━━━━━━━━\n"
                f"📨 Email: `{email}`\n"
                f"✅ Not found in any breach!\n"
                f"━━━━━━━━━━━━━━━━\n"
                f"🇵🇰 By Abdullah Balouch"
            )
        else:
            result = f"❌ Could not check — API limit reached!"
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── SUBDOMAIN FINDER ──
async def subdomain_finder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /sub google.com")
        return
    domain = context.args[0]
    await update.message.reply_text(f"🔗 Finding subdomains for {domain}...")
    try:
        r = requests.get(
            f"https://crt.sh/?q=%.{domain}&output=json",
            timeout=10
        )
        data = r.json()
        subdomains = list(set([
            entry['name_value']
            for entry in data
            if '*' not in entry['name_value']
        ]))[:10]
        
        sub_list = '\n'.join([f"🔗 {s}" for s in subdomains]) if subdomains else "❌ No subdomains found"
        result = (
            f"🔗 *Subdomain Report*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🌐 Domain: `{domain}`\n"
            f"📊 Found: {len(subdomains)}\n\n"
            f"{sub_list}\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🇵🇰 By Abdullah Balouch"
        )
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── TECH DETECTOR ──
async def tech_detector(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /tech google.com")
        return
    domain = context.args[0]
    await update.message.reply_text(f"💻 Detecting tech for {domain}...")
    try:
        url = f"https://{domain}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10)
        html = r.text.lower()
        res_headers = {k.lower(): v for k, v in r.headers.items()}

        cms = []
        if 'wp-content' in html: cms.append('WordPress')
        if 'joomla' in html: cms.append('Joomla')
        if 'drupal' in html: cms.append('Drupal')
        if 'shopify' in html: cms.append('Shopify')
        if 'magento' in html: cms.append('Magento')

        js = []
        if 'react' in html: js.append('React.js')
        if 'vue' in html: js.append('Vue.js')
        if 'angular' in html: js.append('Angular')
        if 'jquery' in html: js.append('jQuery')
        if 'bootstrap' in html: js.append('Bootstrap')

        server = res_headers.get('server', 'Hidden')
        powered = res_headers.get('x-powered-by', 'Hidden')

        cdn = '✅ Cloudflare' if 'cf-ray' in res_headers else '❌ No CDN'
        https = '✅ HTTPS' if url.startswith('https') else '❌ No HTTPS'

        result = (
            f"💻 *Tech Detector Report*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🌐 Domain: `{domain}`\n"
            f"🖥 Server: {server}\n"
            f"⚡ Powered By: {powered}\n"
            f"📦 CMS: {', '.join(cms) or 'Unknown'}\n"
            f"🔧 JS: {', '.join(js) or 'Unknown'}\n"
            f"🛡 CDN: {cdn}\n"
            f"🔒 SSL: {https}\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🇵🇰 By Abdullah Balouch"
        )
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── ADMIN FINDER ──
async def admin_finder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /admin google.com")
        return
    domain = context.args[0]
    await update.message.reply_text(f"🔓 Finding admin panels for {domain}...")
    try:
        paths = [
            '/admin', '/login', '/wp-admin', '/administrator',
            '/admin/login', '/user/login', '/cpanel', '/webmail',
            '/phpmyadmin', '/admin.php', '/dashboard', '/manage'
        ]
        found = []
        headers = {'User-Agent': 'Mozilla/5.0'}
        for path in paths:
            try:
                url = f"https://{domain}{path}"
                r = requests.get(url, headers=headers, timeout=3, allow_redirects=False)
                if r.status_code in [200, 301, 302, 403]:
                    found.append(f"✅ {path} [{r.status_code}]")
            except:
                pass

        found_text = '\n'.join(found) if found else "❌ No admin panels found"
        result = (
            f"🔓 *Admin Finder Report*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🌐 Domain: `{domain}`\n"
            f"📊 Found: {len(found)}\n\n"
            f"{found_text}\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"⚠️ Ethical Use Only!\n"
            f"🇵🇰 By Abdullah Balouch"
        )
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── FULL RECON ──
async def full_recon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Usage: /recon google.com")
        return
    domain = context.args[0]
    await update.message.reply_text(f"📊 Full Recon starting for {domain}...\n⏳ Please wait...")
    try:
        ip = socket.gethostbyname(domain)
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        d = r.json()

        # Tech detect
        try:
            res = requests.get(f"https://{domain}", timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            html = res.text.lower()
            cms = 'WordPress' if 'wp-content' in html else 'Shopify' if 'shopify' in html else 'Unknown'
            server = res.headers.get('server', 'Hidden')
        except:
            cms = 'Unknown'
            server = 'Unknown'

        # Ports
        open_ports = []
        for port in [80, 443, 22, 3306, 8080]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(str(port))
            sock.close()

        result = (
            f"📊 *Full Recon Report*\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"🌐 Domain: `{domain}`\n"
            f"📍 IP: `{ip}`\n"
            f"🌍 Country: {d.get('country', 'N/A')}\n"
            f"🏙 City: {d.get('city', 'N/A')}\n"
            f"📡 ISP: {d.get('isp', 'N/A')}\n"
            f"🖥 Server: {server}\n"
            f"📦 CMS: {cms}\n"
            f"⚡ Open Ports: {', '.join(open_ports) or 'None'}\n"
            f"━━━━━━━━━━━━━━━━\n"
            f"⚠️ Ethical Use Only!\n"
            f"🇵🇰 By Abdullah Balouch"
        )
        await update.message.reply_text(result, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

def main():
    print("🔐 AB OSINT Bot — Full Suite")
    print("🇵🇰 By Abdullah Balouch — Multan Pakistan")
    print("✅ Bot is LIVE!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ip", ip_lookup))
    app.add_handler(CommandHandler("phone", phone_lookup))
    app.add_handler(CommandHandler("whois", whois_lookup))
    app.add_handler(CommandHandler("scan", port_scan))
    app.add_handler(CommandHandler("weather", weather))
    app.add_handler(CommandHandler("email", email_breach))
    app.add_handler(CommandHandler("sub", subdomain_finder))
    app.add_handler(CommandHandler("tech", tech_detector))
    app.add_handler(CommandHandler("admin", admin_finder))
    app.add_handler(CommandHandler("recon", full_recon))

    app.run_polling()

main()
