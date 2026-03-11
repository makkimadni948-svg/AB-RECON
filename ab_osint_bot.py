#!/usr/bin/env python3
import requests, socket, logging, json, os, time
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8623058215:AAF3MJCB-BKjHEmab685GLayN01buwd6fqY"
logging.basicConfig(level=logging.WARNING)
USERS_FILE = "users.json"
user_last_cmd = {}

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE) as f: return json.load(f)
    return {}

def save_user(uid, uname, name):
    users = load_users()
    users[str(uid)] = {"username":uname,"name":name,"joined":datetime.now().strftime("%Y-%m-%d %H:%M"),"uses":users.get(str(uid),{}).get("uses",0)+1}
    with open(USERS_FILE,"w") as f: json.dump(users,f)

def is_rate_limited(uid):
    now = time.time()
    if uid in user_last_cmd and now - user_last_cmd[uid] < 5: return True
    user_last_cmd[uid] = now
    return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    keyboard = [
        [InlineKeyboardButton("🌐 IP Lookup", callback_data="menu_ip"), InlineKeyboardButton("📱 Phone", callback_data="menu_phone")],
        [InlineKeyboardButton("🔍 WHOIS", callback_data="menu_whois"), InlineKeyboardButton("⚡ Port Scan", callback_data="menu_scan")],
        [InlineKeyboardButton("🔗 Subdomains", callback_data="menu_sub"), InlineKeyboardButton("💻 Tech Detect", callback_data="menu_tech")],
        [InlineKeyboardButton("🔓 Admin Finder", callback_data="menu_admin"), InlineKeyboardButton("💉 Vuln Scan", callback_data="menu_vuln")],
        [InlineKeyboardButton("📧 Email Breach", callback_data="menu_email"), InlineKeyboardButton("📊 Full Recon", callback_data="menu_recon")],
        [InlineKeyboardButton("🌤 Weather", callback_data="menu_weather"), InlineKeyboardButton("👥 Users", callback_data="menu_users")],
    ]
    await update.message.reply_text(
        f"👋 *Salam {user.first_name}!*\n\n🔐 *AB OSINT Bot*\n👨‍💻 *Abdullah Balouch* | 🇵🇰 Multan\n\n⚡ _Select a tool:_",
        parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    msgs = {
        "menu_ip":"🌐 *IP Lookup*\nUsage: `/ip 8.8.8.8`",
        "menu_phone":"📱 *Phone*\nUsage: `/phone +923001234567`",
        "menu_whois":"🔍 *WHOIS*\nUsage: `/whois google.com`",
        "menu_scan":"⚡ *Port Scan*\nUsage: `/scan google.com`",
        "menu_sub":"🔗 *Subdomains*\nUsage: `/sub google.com`",
        "menu_tech":"💻 *Tech Detect*\nUsage: `/tech google.com`",
        "menu_admin":"🔓 *Admin Finder*\nUsage: `/admin google.com`",
        "menu_vuln":"💉 *Vuln Scan*\nUsage: `/vuln google.com`",
        "menu_email":"📧 *Email Breach*\nUsage: `/email test@gmail.com`",
        "menu_recon":"📊 *Full Recon*\nUsage: `/recon google.com`",
        "menu_weather":"🌤 *Weather*\nUsage: `/weather Multan`",
        "menu_users":"👥 *Users*\nUsage: `/users`",
    }
    await query.edit_message_text(msgs.get(query.data,"❓ Unknown")+"\n\n_🇵🇰 By Abdullah Balouch_", parse_mode="Markdown")

async def ip_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/ip 8.8.8.8`", parse_mode="Markdown"); return
    ip = context.args[0]
    await update.message.reply_text(f"🔍 Looking up {ip}...")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if r["status"] == "success":
            result = f"🌐 *IP Report*\n━━━━━━━━━━━━━━━━\n📍 IP: `{r.get('query')}`\n🌍 Country: {r.get('country')}\n🏙 City: {r.get('city')}\n📡 ISP: {r.get('isp')}\n⏰ TZ: {r.get('timezone')}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        else:
            result = f"❌ Invalid IP: {ip}"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def phone_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/phone +923001234567`", parse_mode="Markdown"); return
    number = context.args[0]
    await update.message.reply_text(f"📱 Analyzing {number}...")
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone
        parsed = phonenumbers.parse(number)
        result = f"📱 *Phone Report*\n━━━━━━━━━━━━━━━━\n📞 Number: `{number}`\n✅ Valid: {phonenumbers.is_valid_number(parsed)}\n🌍 Region: {geocoder.description_for_number(parsed,'en')}\n📡 Carrier: {carrier.name_for_number(parsed,'en') or 'Unknown'}\n⏰ TZ: {', '.join(timezone.time_zones_for_number(parsed))}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def whois_lookup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/whois google.com`", parse_mode="Markdown"); return
    domain = context.args[0]
    await update.message.reply_text(f"🔍 WHOIS for {domain}...")
    try:
        ip = socket.gethostbyname(domain)
        d = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        try:
            rdap = requests.get(f"https://rdap.org/domain/{domain}", timeout=5).json()
            events = rdap.get("events",[])
            created = next((e["eventDate"][:10] for e in events if e["eventAction"]=="registration"),"Unknown")
            expiry = next((e["eventDate"][:10] for e in events if e["eventAction"]=="expiration"),"Unknown")
        except:
            created = expiry = "Unknown"
        result = f"🔍 *WHOIS Report*\n━━━━━━━━━━━━━━━━\n🌐 Domain: `{domain}`\n📍 IP: `{ip}`\n🌍 Country: {d.get('country','N/A')}\n📡 ISP: {d.get('isp','N/A')}\n📅 Created: {created}\n⏰ Expires: {expiry}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def port_scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/scan google.com`", parse_mode="Markdown"); return
    domain = context.args[0]
    await update.message.reply_text(f"⚡ Scanning {domain}...")
    try:
        ip = socket.gethostbyname(domain)
        ports = {21:"FTP",22:"SSH",80:"HTTP",443:"HTTPS",3306:"MySQL",8080:"HTTP-Alt"}
        open_ports = []
        for port,svc in ports.items():
            s = socket.socket(); s.settimeout(1)
            if s.connect_ex((ip,port))==0: open_ports.append(f"✅ {port} — {svc}")
            s.close()
        result = f"⚡ *Port Scan*\n━━━━━━━━━━━━━━━━\n🎯 Target: `{domain}`\n📍 IP: `{ip}`\n\n{chr(10).join(open_ports) or '❌ No open ports'}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if not context.args:
        await update.message.reply_text("❌ Usage: `/weather Multan`", parse_mode="Markdown"); return
    city = " ".join(context.args)
    try:
        r = requests.get(f"https://wttr.in/{city}?format=3", timeout=5)
        await update.message.reply_text(f"🌤 *Weather*\n━━━━━━━━━━━━━━━━\n{r.text}\n🇵🇰 By Abdullah Balouch", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def email_breach(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/email test@gmail.com`", parse_mode="Markdown"); return
    email = context.args[0]
    await update.message.reply_text(f"📧 Checking {email}...")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", headers={"User-Agent":"AB-OSINT"}, timeout=5)
        if r.status_code==200:
            b = r.json()
            result = f"📧 *Email Breach*\n━━━━━━━━━━━━━━━━\n📨 `{email}`\n🚨 Found in {len(b)} breaches!\n\n{chr(10).join(['⚠️ '+x['Name'] for x in b[:5]])}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        elif r.status_code==404:
            result = f"📧 *Email Breach*\n━━━━━━━━━━━━━━━━\n✅ `{email}` Safe!\n🇵🇰 By Abdullah Balouch"
        else:
            result = "❌ API limit reached!"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def subdomain_finder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/sub google.com`", parse_mode="Markdown"); return
    domain = context.args[0]
    await update.message.reply_text(f"🔗 Finding subdomains for {domain}...")
    try:
        r = requests.get(f"https://crt.sh/?q=%.{domain}&output=json", timeout=10).json()
        subs = list(set([e["name_value"] for e in r if "*" not in e["name_value"]]))[:10]
        result = f"🔗 *Subdomains*\n━━━━━━━━━━━━━━━━\n🌐 `{domain}`\nFound: {len(subs)}\n\n{chr(10).join(['🔗 '+s for s in subs]) or '❌ None'}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def tech_detector(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/tech google.com`", parse_mode="Markdown"); return
    domain = context.args[0]
    await update.message.reply_text(f"💻 Detecting tech for {domain}...")
    try:
        r = requests.get(f"https://{domain}", headers={"User-Agent":"Mozilla/5.0"}, timeout=10)
        html = r.text.lower()
        h = {k.lower():v for k,v in r.headers.items()}
        cms = [x for x in ["WordPress","Joomla","Shopify","Magento"] if x.lower() in html]
        js = [x for x in ["React","Vue","jQuery","Bootstrap"] if x.lower() in html]
        result = f"💻 *Tech Detector*\n━━━━━━━━━━━━━━━━\n🌐 `{domain}`\n🖥 Server: {h.get('server','Hidden')}\n📦 CMS: {', '.join(cms) or 'Unknown'}\n🔧 JS: {', '.join(js) or 'Unknown'}\n🛡 CDN: {'Cloudflare' if 'cf-ray' in h else 'None'}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def admin_finder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/admin google.com`", parse_mode="Markdown"); return
    domain = context.args[0]
    await update.message.reply_text(f"🔓 Finding admin panels...")
    try:
        paths = ["/admin","/login","/wp-admin","/administrator","/cpanel","/dashboard","/phpmyadmin"]
        found = []
        for path in paths:
            try:
                r = requests.get(f"https://{domain}{path}", headers={"User-Agent":"Mozilla/5.0"}, timeout=3, allow_redirects=False)
                if r.status_code in [200,301,302,403]: found.append(f"✅ {path} [{r.status_code}]")
            except: pass
        result = f"🔓 *Admin Finder*\n━━━━━━━━━━━━━━━━\n🌐 `{domain}`\nFound: {len(found)}\n\n{chr(10).join(found) or '❌ None'}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def vuln_scanner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/vuln google.com`", parse_mode="Markdown"); return
    domain = context.args[0]
    await update.message.reply_text(f"💉 Scanning {domain}...")
    try:
        found = []
        r = requests.get(f"https://{domain}", timeout=5)
        h = {k.lower():v for k,v in r.headers.items()}
        if "x-frame-options" not in h: found.append("🟡 Missing X-Frame-Options")
        if "content-security-policy" not in h: found.append("🟡 Missing CSP Header")
        if "x-xss-protection" not in h: found.append("🟡 Missing XSS Protection")
        if "strict-transport-security" not in h: found.append("🟡 Missing HSTS")
        result = f"💉 *Vuln Scanner*\n━━━━━━━━━━━━━━━━\n🎯 `{domain}`\nFound: {len(found)}\n\n{chr(10).join(found) or '✅ No vulns'}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def full_recon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    save_user(user.id, user.username, user.first_name)
    if is_rate_limited(user.id):
        await update.message.reply_text("⏳ Wait 5 seconds!"); return
    if not context.args:
        await update.message.reply_text("❌ Usage: `/recon google.com`", parse_mode="Markdown"); return
    domain = context.args[0]
    await update.message.reply_text(f"📊 Full Recon for {domain}...\n⏳ Please wait...")
    try:
        ip = socket.gethostbyname(domain)
        d = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        try:
            res = requests.get(f"https://{domain}", headers={"User-Agent":"Mozilla/5.0"}, timeout=5)
            html = res.text.lower()
            cms = "WordPress" if "wp-content" in html else "Shopify" if "shopify" in html else "Unknown"
            server = res.headers.get("server","Hidden")
        except:
            cms = server = "Unknown"
        open_ports = []
        for port in [80,443,22,3306,8080]:
            s = socket.socket(); s.settimeout(1)
            if s.connect_ex((ip,port))==0: open_ports.append(str(port))
            s.close()
        result = f"📊 *Full Recon*\n━━━━━━━━━━━━━━━━\n🌐 `{domain}`\n📍 IP: `{ip}`\n🌍 {d.get('country','N/A')} — {d.get('city','N/A')}\n📡 ISP: {d.get('isp','N/A')}\n🖥 Server: {server}\n📦 CMS: {cms}\n⚡ Ports: {', '.join(open_ports) or 'None'}\n━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch"
        await update.message.reply_text(result, parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def show_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = load_users()
    if not users:
        await update.message.reply_text("❌ No users yet!"); return
    text = f"👥 *Users — {len(users)} total*\n━━━━━━━━━━━━━━━━\n\n"
    for uid,info in list(users.items())[:10]:
        text += f"👤 {info['name']} — Uses: {info['uses']}\n"
    await update.message.reply_text(text, parse_mode="Markdown")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 *Commands*\n━━━━━━━━━━━━━━━━\n"
        "🌐 `/ip 8.8.8.8`\n📱 `/phone +923001234567`\n"
        "🔍 `/whois google.com`\n⚡ `/scan google.com`\n"
        "🌤 `/weather Multan`\n📧 `/email test@gmail.com`\n"
        "🔗 `/sub google.com`\n💻 `/tech google.com`\n"
        "🔓 `/admin google.com`\n💉 `/vuln google.com`\n"
        "📊 `/recon google.com`\n👥 `/users`\n"
        "━━━━━━━━━━━━━━━━\n🇵🇰 By Abdullah Balouch",
        parse_mode="Markdown")

def main():
    print("🔐 AB OSINT Bot — Live!")
    print("🇵🇰 Abdullah Balouch — Multan Pakistan")
    print("✅ Bot Started!")
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
    app.add_handler(CommandHandler("vuln", vuln_scanner))
    app.add_handler(CommandHandler("recon", full_recon))
    app.add_handler(CommandHandler("users", show_users))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

main()
