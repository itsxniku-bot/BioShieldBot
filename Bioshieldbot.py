# ULTIMATE BIO SHIELD BOT - COMPLETE FULL VERSION
# 24/7 ANTI-SLEEP PROTECTION WITH ALL FEATURES

import re
import sqlite3
import asyncio
import logging
import requests
import time
import threading
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from aiogram.filters import Command
from flask import Flask
import urllib3
import aiohttp
from datetime import datetime

# =========================== ULTIMATE ANTI-SLEEP CONFIG =======================
BOT_TOKEN = "8321981151:AAEkUFM1sI-E32AOULrh7_7ASV9NJV0wMRA"
OWNER_ID = 6156257558
LOG_GROUP_ID = -1003433334668

# Aggressive anti-sleep settings
KEEP_ALIVE_INTERVAL = 25  # 25 seconds - Render ke 30 second timeout se kam
HEALTH_CHECK_INTERVAL = 10  # 10 seconds
EXTERNAL_PING_INTERVAL = 15  # 15 seconds

# =========================== MULTI-LAYER ANTI-SLEEP SYSTEM =======================

# Layer 1: Multiple Flask Servers - Different Ports
app = Flask(__name__)
app1 = Flask(__name__)
app2 = Flask(__name__)
app3 = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bio Shield - MAIN SERVER"

@app.route('/health')
def health():
    return f"✅ Healthy - {datetime.now().strftime('%H:%M:%S')}"

@app.route('/ping')
def ping():
    return f"🏓 Pong - {datetime.now().strftime('%H:%M:%S')}"

@app.route('/status')
def status():
    return "🟢 Bot Status: ACTIVE"

@app.route('/keepalive')
def keepalive():
    return "❤️ Keep Alive Active"

@app1.route('/')
def home1():
    return "🤖 Bio Shield - BACKUP 1"

@app1.route('/status')
def status1():
    return f"🟢 Active - {datetime.now().strftime('%H:%M:%S')}"

@app1.route('/health2')
def health2():
    return "✅ Backup Health OK!"

@app2.route('/')
def home2():
    return "🤖 Bio Shield - BACKUP 2"

@app2.route('/alive')
def alive2():
    return f"❤️ Alive - {datetime.now().strftime('%H:%M:%S')}"

@app3.route('/')
def home3():
    return "🤖 Bio Shield - BACKUP 3"

@app3.route('/check')
def check3():
    return f"🔍 Check OK - {datetime.now().strftime('%H:%M:%S')}"

def run_flask_app(port):
    """Run Flask app on specific port"""
    if port == 10000:
        app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
    elif port == 10001:
        app1.run(host='0.0.0.0', port=port, debug=False, threaded=True)
    elif port == 10002:
        app2.run(host='0.0.0.0', port=port, debug=False, threaded=True)
    elif port == 10003:
        app3.run(host='0.0.0.0', port=port, debug=False, threaded=True)

# Layer 2: External Monitoring URLs
MONITORING_URLS = [
    'https://api.telegram.org',
    'https://www.google.com',
    'https://www.cloudflare.com',
    'https://www.github.com',
    'https://www.wikipedia.org'
]

# Layer 3: Internal Health URLs
INTERNAL_URLS = [
    'http://0.0.0.0:10000/health',
    'http://0.0.0.0:10000/ping',
    'http://0.0.0.0:10001/status',
    'http://0.0.0.0:10002/alive',
    'http://0.0.0.0:10003/check'
]

# =========================== ULTIMATE KEEP ALIVE SYSTEM =======================
class UltimateKeepAlive:
    def __init__(self):
        self.cycle_count = 0
        self.last_external_check = 0
        self.last_bot_check = 0
        self.start_time = time.time()
        self.last_log_time = 0
    
    async def aggressive_keep_alive(self):
        """ULTIMATE ANTI-SLEEP - Multiple layers of protection"""
        print("🛡️ STARTING ULTIMATE ANTI-SLEEP SYSTEM...")
        
        while True:
            try:
                self.cycle_count += 1
                current_time = time.time()
                print(f"\n🔄 CYCLE {self.cycle_count} - {datetime.now().strftime('%H:%M:%S')}")
                
                # LAYER 1: Bot Self-Check (Every 30 seconds)
                if current_time - self.last_bot_check > 30:
                    try:
                        me = await bot.get_me()
                        print(f"🤖 Bot Status: ACTIVE (@{me.username})")
                        self.last_bot_check = current_time
                    except Exception as e:
                        print(f"❌ Bot Check Failed: {e}")
                
                # LAYER 2: Internal Health Pings (Every 25 seconds)
                internal_success = 0
                for url in INTERNAL_URLS:
                    try:
                        response = requests.get(url, timeout=5)
                        if response.status_code == 200:
                            internal_success += 1
                            print(f"✅ Internal: {url.split('/')[-1]} - OK")
                        else:
                            print(f"⚠️ Internal: {url} - Status {response.status_code}")
                    except Exception as e:
                        print(f"❌ Internal Failed: {url} - {e}")
                
                # LAYER 3: External Connectivity (Every 2 minutes)
                if current_time - self.last_external_check > 120:
                    external_success = 0
                    for url in MONITORING_URLS:
                        try:
                            response = requests.get(url, timeout=10)
                            if response.status_code == 200:
                                external_success += 1
                                print(f"🌐 External: {url.split('//')[-1]} - OK")
                        except Exception as e:
                            print(f"🌐 External Failed: {url}")
                    
                    print(f"🌐 External Connectivity: {external_success}/{len(MONITORING_URLS)}")
                    self.last_external_check = current_time
                
                # LAYER 4: Database Health Check
                try:
                    cur = DB.execute("SELECT COUNT(*) FROM groups")
                    group_count = cur.fetchone()[0]
                    print(f"🗃️ Database: OK (Groups: {group_count})")
                except Exception as e:
                    print(f"❌ Database Check Failed: {e}")
                
                # LAYER 5: Memory & Performance Check
                uptime = int(current_time - self.start_time)
                hours = uptime // 3600
                minutes = (uptime % 3600) // 60
                print(f"⏰ Uptime: {hours}h {minutes}m | Cycles: {self.cycle_count}")
                
                # LAYER 6: Telegram API Test Message (Every 30 minutes)
                if current_time - self.last_log_time > 1800:  # 30 minutes
                    try:
                        await self.send_health_report()
                        self.last_log_time = current_time
                    except:
                        pass
                
                print("🟢 ANTI-SLEEP CYCLE COMPLETED")
                print("=" * 60)
                
                # AGGRESSIVE SLEEP - 25 seconds only (Render timeout se kam)
                await asyncio.sleep(KEEP_ALIVE_INTERVAL)
                
            except Exception as e:
                print(f"💥 CRITICAL KEEP ALIVE ERROR: {e}")
                # Emergency recovery
                await asyncio.sleep(10)
    
    async def send_health_report(self):
        """Health report bhejna log group mein"""
        try:
            cur = DB.execute("SELECT COUNT(*) FROM groups")
            group_count = cur.fetchone()[0]
            
            cur = DB.execute("SELECT COUNT(*) FROM muted_users")
            muted_count = cur.fetchone()[0]
            
            cur = DB.execute("SELECT SUM(count) FROM warnings")
            warnings_count = cur.fetchone()[0] or 0
            
            uptime = int(time.time() - self.start_time)
            hours = uptime // 3600
            minutes = (uptime % 3600) // 60
            
            health_msg = (
                f"🟢 BOT HEALTH REPORT\n\n"
                f"• Uptime: {hours}h {minutes}m\n"
                f"• Groups: {group_count}\n"
                f"• Muted Users: {muted_count}\n"
                f"• Total Warnings: {warnings_count}\n"
                f"• Cycles: {self.cycle_count}\n"
                f"• Last Check: {datetime.now().strftime('%H:%M:%S')}\n"
                f"• Status: ACTIVE & RUNNING"
            )
            
            await bot.send_message(LOG_GROUP_ID, health_msg)
            print("📊 Health report sent to log group")
            
        except Exception as e:
            print(f"❌ Health report failed: {e}")

# =========================== BACKGROUND PINGERS =======================
async def continuous_internal_pinger():
    """Continuous internal pinging - har 20 seconds mein"""
    while True:
        try:
            for url in INTERNAL_URLS:
                try:
                    requests.get(url, timeout=3)
                except:
                    pass
            await asyncio.sleep(20)
        except:
            await asyncio.sleep(10)

async def continuous_external_pinger():
    """Continuous external pinging - har 30 seconds mein"""
    while True:
        try:
            for url in MONITORING_URLS[:2]:  # First 2 URLs only
                try:
                    requests.get(url, timeout=5)
                except:
                    pass
            await asyncio.sleep(30)
        except:
            await asyncio.sleep(15)

# =========================== BACKGROUND UNMUTE CHECKER =======================
async def background_unmute_checker():
    """Regularly check if muted users have been unmuted manually"""
    while True:
        try:
            await asyncio.sleep(30)
            
            cur = DB.execute("SELECT group_id, user_id FROM muted_users")
            muted_users = cur.fetchall()
            
            for group_id, user_id in muted_users:
                try:
                    member = await bot.get_chat_member(group_id, user_id)
                    
                    if member.status != 'restricted' or member.can_send_messages:
                        print(f"🔍 User {user_id} manually unmuted in group {group_id}, resetting warnings...")
                        unmute_user(group_id, user_id)
                        print(f"✅ Warnings reset for user {user_id} in group {group_id}")
                        
                except Exception as e:
                    continue
                    
        except Exception as e:
            print(f"❌ Error in background unmute checker: {e}")
            await asyncio.sleep(60)

# =========================== DATABASE SETUP =======================
def db_connect():
    conn = sqlite3.connect("bot.db", check_same_thread=False)
    cur = conn.cursor()

    # Groups table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            group_id INTEGER PRIMARY KEY,
            group_name TEXT,
            biolinks INTEGER DEFAULT 1,
            added_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Whitelist table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS whitelist (
            group_id INTEGER,
            user_id INTEGER,
            PRIMARY KEY (group_id, user_id)
        )
    """)

    # Warnings table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS warnings (
            group_id INTEGER,
            user_id INTEGER,
            count INTEGER DEFAULT 0,
            PRIMARY KEY (group_id, user_id)
        )
    """)

    # Muted users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS muted_users (
            group_id INTEGER,
            user_id INTEGER,
            PRIMARY KEY (group_id, user_id)
        )
    """)

    conn.commit()
    return conn

DB = db_connect()

# =========================== BOT INITIALIZATION =======================
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
keep_alive_system = UltimateKeepAlive()

# =========================== ESSENTIAL FUNCTIONS =======================
def ensure_group(gid, group_name=None):
    """Group ko database mein add karega"""
    cur = DB.execute("SELECT 1 FROM groups WHERE group_id=?", (gid,))
    if not cur.fetchone():
        DB.execute("INSERT INTO groups (group_id, group_name) VALUES (?, ?)", 
                  (gid, group_name or f"Group_{gid}"))
        DB.commit()
        print(f"✅ New group added to database: {gid}")
    elif group_name:
        DB.execute("UPDATE groups SET group_name=? WHERE group_id=?", (group_name, gid))
        DB.commit()

def get_filters(gid):
    ensure_group(gid)
    cur = DB.execute("SELECT biolinks FROM groups WHERE group_id=?", (gid,))
    result = cur.fetchone()
    return result[0] if result else 1

def is_whitelisted(gid, uid):
    cur = DB.execute("SELECT 1 FROM whitelist WHERE group_id=? AND user_id=?", (gid, uid))
    return cur.fetchone() is not None

def get_warnings(gid, uid):
    cur = DB.execute("SELECT count FROM warnings WHERE group_id=? AND user_id=?", (gid, uid))
    result = cur.fetchone()
    return result[0] if result else 0

def add_warning(gid, uid):
    current = get_warnings(gid, uid)
    if current == 0:
        DB.execute("INSERT INTO warnings (group_id, user_id, count) VALUES (?, ?, ?)", (gid, uid, 1))
    else:
        DB.execute("UPDATE warnings SET count=? WHERE group_id=? AND user_id=?", (current + 1, gid, uid))
    DB.commit()
    return current + 1

def reset_warnings(gid, uid):
    DB.execute("DELETE FROM warnings WHERE group_id=? AND user_id=?", (gid, uid))
    DB.commit()

def is_muted(gid, uid):
    cur = DB.execute("SELECT 1 FROM muted_users WHERE group_id=? AND user_id=?", (gid, uid))
    return cur.fetchone() is not None

def mute_user(gid, uid):
    DB.execute("INSERT OR IGNORE INTO muted_users (group_id, user_id) VALUES (?, ?)", (gid, uid))
    DB.commit()

def unmute_user(gid, uid):
    DB.execute("DELETE FROM muted_users WHERE group_id=? AND user_id=?", (gid, uid))
    DB.commit()
    reset_warnings(gid, uid)

async def is_admin(chat_id, user_id):
    """Check if user is admin"""
    try:
        member = await bot.get_chat_member(chat_id, user_id)
        return member.status in ['administrator', 'creator']
    except Exception as e:
        print(f"❌ Admin check error: {e}")
        return False

async def send_log(message: str):
    """Send message to log group"""
    try:
        await bot.send_message(LOG_GROUP_ID, message)
        print(f"📝 Log sent: {message}")
    except Exception as e:
        print(f"❌ Error sending log: {e}")

# =========================== DETECTION PATTERNS =======================
URL_REGEX = re.compile(r'https?://[^\s]+')
TELEGRAM_REGEX = re.compile(r't\.me/[^\s]+')
WHATSAPP_REGEX = re.compile(r'wa\.me/[^\s]+')
BOTNAME_REGEX = re.compile(r'@[a-zA-Z0-9_]*bot', re.IGNORECASE)
USERNAME_REGEX = re.compile(r'@[a-zA-Z0-9_]+')

# =========================== BIO SCANNER =======================
async def scan_user_bio(user_id):
    """Scan user bio for links"""
    try:
        user_info = await bot.get_chat(user_id)
        bio = user_info.bio or ""
        
        print(f"🔍 Scanning bio for user {user_id}: {bio}")
        
        if not bio:
            return None
        
        violations = []
        if URL_REGEX.search(bio):
            violations.append("URLs")
        if TELEGRAM_REGEX.search(bio):
            violations.append("Telegram links")
        if WHATSAPP_REGEX.search(bio):
            violations.append("WhatsApp links")
        if BOTNAME_REGEX.search(bio):
            violations.append("Bot usernames")
        if USERNAME_REGEX.search(bio):
            violations.append("Usernames")
        
        print(f"🔍 Violations found: {violations}")
        return violations if violations else None
        
    except Exception as e:
        print(f"❌ Error scanning user bio: {e}")
        return None

# =========================== START COMMAND =======================
@dp.message(Command("start"))
async def start_cmd(msg: Message):
    print(f"📨 Start command received from: {msg.from_user.first_name} in {msg.chat.type}")
    
    if msg.chat.type == "private":
        try:
            bot_username = (await bot.get_me()).username
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Owner", url="https://t.me/insaanova")],
                [InlineKeyboardButton(text="Help & Commands", callback_data="help_cmd")],
                [InlineKeyboardButton(text="Updates", url="https://t.me/friends_corner")],
                [InlineKeyboardButton(text="Add me to your group", url=f"https://t.me/{bot_username}?startgroup=true")],
                [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
            ])

            await msg.answer(
                f"Hey {msg.from_user.first_name}!\n\n"
                f"Welcome to Links Shield Bot\n\n"
                f"I protect your group from:\n"
                f"➠ Bio Links\n"
                f"➠ Usernames (@example)\n"
                f"➠ Bot Usernames (@bot)\n\n"
                f"Add me to your group & make me admin!", 
                reply_markup=kb
            )
            print("✅ Start message sent successfully!")
            
        except Exception as e:
            print(f"❌ Error sending start message: {e}")
    else:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
        ])
        
        start_msg = await msg.reply(
            "🤖 Links Shield Bot is active!\n\n"
            "I scan user bios in real-time when they message:\n"
            "➠ Bio Links\n"
            "➠ Usernames (@example)\n"
            "➠ Bot Usernames (@bot)\n\n"
            "Use /help for commands!",
            reply_markup=kb
        )
        
        await asyncio.sleep(20)
        try:
            await start_msg.delete()
        except:
            pass

# =========================== HELP COMMAND =======================
@dp.message(Command("help"))
async def help_cmd(msg: Message):
    print(f"📖 Help command received from: {msg.from_user.first_name} in {msg.chat.type}")
    
    if msg.chat.type == "private":
        if msg.from_user.id == OWNER_ID:
            help_text = """
<b>Links Shield Bot - Help & Commands</b>

<b>Owner Commands:</b>
➠ /stats - Bot statistics
➠ /broadcast - Broadcast message
➠ /groups - All groups list
➠ /restart - Restart bot

<b>Admin Commands:</b>
➠ /biolink on - Enable bio link protection
➠ /biolink off - Disable bio link protection  
➠ /biolink - Check current status
➠ /whitelistadd - Add user to whitelist
➠ /whitelistremove - Remove user from whitelist
➠ /whitelist - Show whitelisted users
➠ /warnings - Check user warnings
➠ /resetwarns - Reset user warnings

<b>Protection Features:</b>
➠ Real-time Bio Scanning (when user messages)
➠ Bio Links Detection
➠ Usernames (@example) Detection  
➠ Bot Usernames (@bot) Detection
➠ 3 Warning System
➠ Auto Mute after 3 warnings
➠ Whitelist System
            """
        else:
            help_text = """
<b>Links Shield Bot - Help & Commands</b>

<b>Admin Commands:</b>
➠ /biolink on - Enable bio link protection
➠ /biolink off - Disable bio link protection  
➠ /biolink - Check current status
➠ /whitelistadd - Add user to whitelist
➠ /whitelistremove - Remove user from whitelist
➠ /whitelist - Show whitelisted users
➠ /warnings - Check user warnings
➠ /resetwarns - Reset user warnings

<b>Protection Features:</b>
➠ Real-time Bio Scanning (when user messages)
➠ Bio Links Detection
➠ Usernames (@example) Detection  
➠ Bot Usernames (@bot) Detection
➠ 3 Warning System
➠ Auto Mute after 3 warnings
➠ Whitelist System
            """
        
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Back", callback_data="back_to_start"),
             InlineKeyboardButton(text="❌ Close", callback_data="close_help")]
        ])
        
        await msg.answer(help_text, reply_markup=kb, parse_mode="HTML")
    else:
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
        ])
        
        help_text = """
<b>🤖 Links Shield Bot - Group Commands</b>

<b>Admin Commands:</b>
➠ /biolink on/off - Enable/disable protection
➠ /whitelist - Manage whitelist
➠ /warnings - Check user warnings
➠ /resetwarns - Reset user warnings

<b>Protection Features:</b>
➠ Real-time Bio Scanning
➠ Bio Links Detection
➠ Usernames (@example) Detection  
➠ Bot Usernames (@bot) Detection
➠ 3 Warning System
➠ Auto Mute after 3 warnings
        """
        help_msg = await msg.reply(help_text, reply_markup=kb, parse_mode="HTML")
        
        await asyncio.sleep(20)
        try:
            await help_msg.delete()
        except:
            pass

# =========================== CALLBACK HANDLERS =======================
@dp.callback_query(F.data == "help_cmd")
async def help_callback(cq: CallbackQuery):
    print(f"📖 Help requested by: {cq.from_user.first_name}")
    
    if cq.from_user.id == OWNER_ID:
        help_text = """
<b>Links Shield Bot - Help & Commands</b>

<b>Owner Commands:</b>
➠ /stats - Bot statistics
➠ /broadcast - Broadcast message
➠ /groups - All groups list
➠ /restart - Restart bot

<b>Admin Commands:</b>
➠ /biolink on - Enable bio link protection
➠ /biolink off - Disable bio link protection  
➠ /biolink - Check current status
➠ /whitelistadd - Add user to whitelist
➠ /whitelistremove - Remove user from whitelist
➠ /whitelist - Show whitelisted users
➠ /warnings - Check user warnings
➠ /resetwarns - Reset user warnings

<b>Protection Features:</b>
➠ Real-time Bio Scanning (when user messages)
➠ Bio Links Detection
➠ Usernames (@example) Detection  
➠ Bot Usernames (@bot) Detection
➠ 3 Warning System
➠ Auto Mute after 3 warnings
➠ Whitelist System
        """
    else:
        help_text = """
<b>Links Shield Bot - Help & Commands</b>

<b>Admin Commands:</b>
➠ /biolink on - Enable bio link protection
➠ /biolink off - Disable bio link protection  
➠ /biolink - Check current status
➠ /whitelistadd - Add user to whitelist
➠ /whitelistremove - Remove user from whitelist
➠ /whitelist - Show whitelisted users
➠ /warnings - Check user warnings
➠ /resetwarns - Reset user warnings

<b>Protection Features:</b>
➠ Real-time Bio Scanning (when user messages)
➠ Bio Links Detection
➠ Usernames (@example) Detection  
➠ Bot Usernames (@bot) Detection
➠ 3 Warning System
➠ Auto Mute after 3 warnings
➠ Whitelist System
        """
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Back", callback_data="back_to_start"),
         InlineKeyboardButton(text="❌ Close", callback_data="close_help")]
    ])
    
    await cq.message.edit_text(help_text, reply_markup=kb, parse_mode="HTML")
    await cq.answer()

@dp.callback_query(F.data == "back_to_start")
async def back_to_start(cq: CallbackQuery):
    bot_username = (await bot.get_me()).username
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Owner", url="https://t.me/insaanova")],
        [InlineKeyboardButton(text="Help & Commands", callback_data="help_cmd")],
        [InlineKeyboardButton(text="Updates", url="https://t.me/friends_corner")],
        [InlineKeyboardButton(text="Add me to your group", url=f"https://t.me/{bot_username}?startgroup=true")],
        [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
    ])

    await cq.message.edit_text(
        f"Hey {cq.from_user.first_name}!\n\n"
        f"Welcome to Links Shield Bot\n\n"
        f"I protect your group from:\n"
        f"➠ Bio Links\n"
        f"➠ Usernames (@example)\n"
        f"➠ Bot Usernames (@bot)\n\n"
        f"Add me to your group & make me admin!", 
        reply_markup=kb
    )
    await cq.answer()

@dp.callback_query(F.data == "close_help")
async def close_help(cq: CallbackQuery):
    await cq.message.delete()
    await cq.answer("Help closed")

@dp.callback_query(F.data == "close_thanks")
async def close_thanks(cq: CallbackQuery):
    await cq.message.delete()
    await cq.answer("Message closed")

# =========================== MUTE/UNMUTE BUTTON HANDLERS ===========
@dp.callback_query(F.data.startswith("mute_"))
async def mute_user_callback(cq: CallbackQuery):
    """Mute user from button"""
    try:
        user_id = int(cq.data.split("_")[1])
        group_id = cq.message.chat.id
        
        if not await is_admin(group_id, cq.from_user.id):
            await cq.answer("❌ Only admins can use this!", show_alert=True)
            return
        
        await bot.restrict_chat_member(
            chat_id=group_id,
            user_id=user_id,
            permissions=types.ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False
            )
        )
        
        mute_user(group_id, user_id)
        
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔊 Unmute User", callback_data=f"unmute_{user_id}")],
            [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
        ])
        
        await cq.message.edit_reply_markup(reply_markup=kb)
        await cq.answer("✅ User muted successfully!")
        
    except Exception as e:
        print(f"❌ Error in mute callback: {e}")
        await cq.answer("❌ Failed to mute user!", show_alert=True)

@dp.callback_query(F.data.startswith("unmute_"))
async def unmute_user_callback(cq: CallbackQuery):
    """Unmute user from button"""
    try:
        user_id = int(cq.data.split("_")[1])
        group_id = cq.message.chat.id
        
        if not await is_admin(group_id, cq.from_user.id):
            await cq.answer("❌ Only admins can use this!", show_alert=True)
            return
        
        await bot.restrict_chat_member(
            chat_id=group_id,
            user_id=user_id,
            permissions=types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True
            )
        )
        
        unmute_user(group_id, user_id)
        
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔇 Mute User", callback_data=f"mute_{user_id}")],
            [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
        ])
        
        await cq.message.edit_reply_markup(reply_markup=kb)
        await cq.answer("✅ User unmuted successfully!")
        
    except Exception as e:
        print(f"❌ Error in unmute callback: {e}")
        await cq.answer("❌ Failed to unmute user!", show_alert=True)

# =========================== REAL-TIME BIO SCANNER HANDLER =========
@dp.message(F.chat.type.in_(["group", "supergroup"]))
async def handle_group_messages(msg: Message):
    """Handle all group messages - commands and bio scanning"""
    
    ensure_group(msg.chat.id, msg.chat.title)
    
    if msg.text and msg.text.startswith('/'):
        await handle_commands(msg)
        return
    
    await real_time_bio_scanner(msg)

async def handle_commands(msg: Message):
    """Handle all commands separately"""
    command = msg.text.split()[0].lower()
    
    if command == "/start":
        await start_cmd(msg)
    elif command == "/help":
        await help_cmd(msg)
    elif command == "/biolink":
        await bio_link_cmd(msg)
    elif command == "/whitelistadd":
        await whitelist_add_cmd(msg)
    elif command == "/whitelistremove":
        await whitelist_remove_cmd(msg)
    elif command == "/whitelist":
        await whitelist_show_cmd(msg)
    elif command == "/warnings":
        await warnings_cmd(msg)
    elif command == "/resetwarns":
        await reset_warns_cmd(msg)
    elif command == "/stats":
        await stats_cmd(msg)
    elif command == "/groups":
        await groups_cmd(msg)
    elif command == "/broadcast":
        await broadcast_cmd(msg)
    elif command == "/restart":
        await restart_cmd(msg)

async def real_time_bio_scanner(msg: Message):
    """Real-time bio scanner - when user sends ANY message, check their bio"""
    
    if msg.from_user.is_bot:
        return
    
    group_id = msg.chat.id
    user_id = msg.from_user.id
    
    print(f"🔍 Scanning bio for user {msg.from_user.first_name} in group {msg.chat.title}")
    
    if not get_filters(group_id):
        print("❌ Protection disabled in this group")
        return
    
    if is_whitelisted(group_id, user_id):
        print("✅ User is whitelisted, skipping")
        return
    
    try:
        if await is_admin(group_id, user_id):
            print("✅ User is admin, skipping")
            return
    except Exception as e:
        print(f"❌ Error checking admin status: {e}")
        return
    
    try:
        member = await bot.get_chat_member(group_id, user_id)
        if member.status == 'restricted' and not member.can_send_messages:
            print("✅ User is restricted, message deleted")
            try:
                await msg.delete()
            except:
                pass
            return
    except Exception as e:
        print(f"❌ Error checking user restrictions: {e}")
    
    print(f"🔍 Scanning bio for user {user_id}...")
    violations = await scan_user_bio(user_id)
    
    if violations:
        print(f"🚫 Violations found: {violations}")
        try:
            await msg.delete()
            print("✅ Message deleted successfully")
            
            warning_count = add_warning(group_id, user_id)
            print(f"✅ Warning added: {warning_count}/3")
            
            user_name = msg.from_user.first_name
            user_mention = f"<a href='tg://user?id={user_id}'>{user_name}</a>"
            username = f"@{msg.from_user.username}" if msg.from_user.username else "No username"
            
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🔇 Mute User", callback_data=f"mute_{user_id}")],
                [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
            ])
            
            warning_text = (
                f"⚠️ {user_mention}\n\n"
                f"<i>({user_id}) Remove your bio link. Not allowed here. Contact admin if you want to keep it.</i>\n\n"
                f"📊 Warning: {warning_count}/3\n"
                f"❌ 3 warnings = Auto Mute"
            )
            
            warning_msg = await bot.send_message(
                chat_id=group_id,
                text=warning_text,
                reply_markup=kb,
                parse_mode="HTML"
            )
            print("✅ Warning message sent successfully!")
            
            await send_log(
                f"🚫 Bio Violation\n"
                f"Group: {msg.chat.title}\n"
                f"User: {user_name} ({username})\n"
                f"ID: {user_id}\n"
                f"Violations: {', '.join(violations)}\n"
                f"Warnings: {warning_count}/3"
            )
            
            if warning_count >= 3:
                try:
                    await bot.restrict_chat_member(
                        chat_id=group_id,
                        user_id=user_id,
                        permissions=types.ChatPermissions(
                            can_send_messages=False,
                            can_send_media_messages=False,
                            can_send_other_messages=False,
                            can_add_web_page_previews=False
                        )
                    )
                    
                    mute_user(group_id, user_id)
                    
                    kb = InlineKeyboardMarkup(inline_keyboard=[
                        [InlineKeyboardButton(text="🔊 Unmute User", callback_data=f"unmute_{user_id}")],
                        [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
                    ])
                    
                    mute_text = (
                        f"🔇 {user_mention} has been muted!\n\n"
                        f"❌ Reason: 3/3 bio warnings\n"
                        f"📝 Remove links from bio & contact admins"
                    )
                    
                    await warning_msg.edit_text(
                        mute_text,
                        reply_markup=kb,
                        parse_mode="HTML"
                    )
                    
                    await send_log(
                        f"🔇 User Auto-Muted\n"
                        f"Group: {msg.chat.title}\n"
                        f"User: {user_name} ({username})\n"
                        f"ID: {user_id}\n"
                        f"Reason: 3/3 bio warnings"
                    )
                    
                except Exception as e:
                    print(f"❌ Error auto-muting user: {e}")
                    await warning_msg.edit_text(
                        f"❌ Failed to auto-mute {user_mention}. Please check my permissions!",
                        parse_mode="HTML"
                    )
            
            await asyncio.sleep(20)
            try:
                await warning_msg.delete()
                print("✅ Warning message deleted after 20 seconds")
            except Exception as e:
                print(f"❌ Error deleting warning message: {e}")
                
        except Exception as e:
            print(f"❌ Error in real-time bio scanner: {e}")
    else:
        print("✅ No violations found in bio")

# =========================== BIO LINK COMMAND ===============
@dp.message(Command("biolink"))
async def bio_link_cmd(msg: Message):
    print(f"🔧 BioLink command received from: {msg.from_user.first_name} in {msg.chat.type}")
    
    if msg.chat.type not in ["group", "supergroup"]:
        await msg.answer("❌ This command only works in groups!")
        return
    
    if not await is_admin(msg.chat.id, msg.from_user.id):
        await msg.reply("❌ Only admins can use this command!")
        return

    args = msg.text.split()
    if len(args) < 2:
        current_status = get_filters(msg.chat.id)
        status_text = "✅ ENABLED" if current_status else "❌ DISABLED"
        status_msg = await msg.reply(
            f"🔒 Bio Protection Status: {status_text}\n\n"
            f"Commands:\n"
            f"• /biolink on - Enable protection\n"
            f"• /biolink off - Disable protection"
        )
        
        await asyncio.sleep(20)
        try:
            await status_msg.delete()
        except:
            pass
        return

    action = args[1].lower()
    if action == "on":
        DB.execute("UPDATE groups SET biolinks=1 WHERE group_id=?", (msg.chat.id,))
        DB.commit()
        status_msg = await msg.reply("✅ Bio Protection has been ENABLED!\n\nI will now scan user bios when they send messages.")
        print(f"✅ Bio protection enabled in group: {msg.chat.id}")
        await send_log(f"✅ Bio Protection Enabled\nGroup: {msg.chat.title}\nID: {msg.chat.id}")
    
    elif action == "off":
        DB.execute("UPDATE groups SET biolinks=0 WHERE group_id=?", (msg.chat.id,))
        DB.commit()
        status_msg = await msg.reply("❌ Bio Protection has been DISABLED!")
        print(f"❌ Bio protection disabled in group: {msg.chat.id}")
        await send_log(f"❌ Bio Protection Disabled\nGroup: {msg.chat.title}\nID: {msg.chat.id}")
    
    else:
        status_msg = await msg.reply("❌ Invalid command! Use:\n• /biolink on\n• /biolink off")
    
    await asyncio.sleep(20)
    try:
        await status_msg.delete()
    except:
        pass

# =========================== WHITELIST COMMANDS ====================
@dp.message(Command("whitelistadd"))
async def whitelist_add_cmd(msg: Message):
    print(f"👤 Whitelistadd command received from: {msg.from_user.first_name} in {msg.chat.type}")
    
    if msg.chat.type not in ["group", "supergroup"]:
        await msg.answer("❌ This command only works in groups!")
        return
    
    if not await is_admin(msg.chat.id, msg.from_user.id):
        await msg.reply("❌ Only admins can use this command!")
        return

    if msg.entities:
        for entity in msg.entities:
            if entity.type == "text_mention" and entity.user:
                user_id = entity.user.id
                username = entity.user.username or "No username"
                
                DB.execute("INSERT OR IGNORE INTO whitelist (group_id, user_id) VALUES (?, ?)", (msg.chat.id, user_id))
                DB.commit()
                whitelist_msg = await msg.reply(f"✅ User @{username} (ID: {user_id}) added to whitelist!")
                await send_log(f"✅ User Whitelisted\nUser: @{username}\nID: {user_id}\nGroup: {msg.chat.title}")
                
                await asyncio.sleep(20)
                try:
                    await whitelist_msg.delete()
                except:
                    pass
                return

    if msg.reply_to_message:
        user_id = msg.reply_to_message.from_user.id
        username = msg.reply_to_message.from_user.username or "No username"
        
        DB.execute("INSERT OR IGNORE INTO whitelist (group_id, user_id) VALUES (?, ?)", (msg.chat.id, user_id))
        DB.commit()
        whitelist_msg = await msg.reply(f"✅ User @{username} (ID: {user_id}) added to whitelist!")
        await send_log(f"✅ User Whitelisted\nUser: @{username}\nID: {user_id}\nGroup: {msg.chat.title}")
        
        await asyncio.sleep(20)
        try:
            await whitelist_msg.delete()
        except:
            pass
        return

    args = msg.text.split()
    if len(args) > 1:
        user_input = args[1]
        
        if user_input.isdigit():
            user_id = int(user_input)
            try:
                user_info = await bot.get_chat(user_id)
                username = user_info.username or "No username"
                
                DB.execute("INSERT OR IGNORE INTO whitelist (group_id, user_id) VALUES (?, ?)", (msg.chat.id, user_id))
                DB.commit()
                whitelist_msg = await msg.reply(f"✅ User @{username} (ID: {user_id}) added to whitelist!")
                await send_log(f"✅ User Whitelisted\nUser: @{username}\nID: {user_id}\nGroup: {msg.chat.title}")
                
                await asyncio.sleep(20)
                try:
                    await whitelist_msg.delete()
                except:
                    pass
                return
            except:
                error_msg = await msg.reply("❌ Invalid user ID!")
                await asyncio.sleep(20)
                try:
                    await error_msg.delete()
                except:
                    pass
                return
        
        elif user_input.startswith('@'):
            username = user_input[1:]
            try:
                user_info = await bot.get_chat(f"@{username}")
                user_id = user_info.id
                
                DB.execute("INSERT OR IGNORE INTO whitelist (group_id, user_id) VALUES (?, ?)", (msg.chat.id, user_id))
                DB.commit()
                whitelist_msg = await msg.reply(f"✅ User @{username} (ID: {user_id}) added to whitelist!")
                await send_log(f"✅ User Whitelisted\nUser: @{username}\nID: {user_id}\nGroup: {msg.chat.title}")
                
                await asyncio.sleep(20)
                try:
                    await whitelist_msg.delete()
                except:
                    pass
                return
            except:
                error_msg = await msg.reply("❌ Invalid username!")
                await asyncio.sleep(20)
                try:
                    await error_msg.delete()
                except:
                    pass
                return
    
    usage_msg = await msg.reply("📝 Usage:\n• Reply to user with /whitelistadd\n• /whitelistadd @username\n• /whitelistadd user_id\n• /whitelistadd (with user mention)")
    await asyncio.sleep(20)
    try:
        await usage_msg.delete()
    except:
        pass

@dp.message(Command("whitelistremove"))
async def whitelist_remove_cmd(msg: Message):
    print(f"👤 Whitelistremove command received from: {msg.from_user.first_name} in {msg.chat.type}")
    
    if msg.chat.type not in ["group", "supergroup"]:
        await msg.answer("❌ This command only works in groups!")
        return
    
    if not await is_admin(msg.chat.id, msg.from_user.id):
        await msg.reply("❌ Only admins can use this command!")
        return

    if msg.entities:
        for entity in msg.entities:
            if entity.type == "text_mention" and entity.user:
                user_id = entity.user.id
                username = entity.user.username or "No username"
                
                DB.execute("DELETE FROM whitelist WHERE group_id=? AND user_id=?", (msg.chat.id, user_id))
                DB.commit()
                remove_msg = await msg.reply(f"❌ User @{username} (ID: {user_id}) removed from whitelist!")
                await send_log(f"❌ User Removed from Whitelist\nUser: @{username}\nID: {user_id}\nGroup: {msg.chat.title}")
                
                await asyncio.sleep(20)
                try:
                    await remove_msg.delete()
                except:
                    pass
                return

    if msg.reply_to_message:
        user_id = msg.reply_to_message.from_user.id
        username = msg.reply_to_message.from_user.username or "No username"
        
        DB.execute("DELETE FROM whitelist WHERE group_id=? AND user_id=?", (msg.chat.id, user_id))
        DB.commit()
        remove_msg = await msg.reply(f"❌ User @{username} (ID: {user_id}) removed from whitelist!")
        await send_log(f"❌ User Removed from Whitelist\nUser: @{username}\nID: {user_id}\nGroup: {msg.chat.title}")
        
        await asyncio.sleep(20)
        try:
            await remove_msg.delete()
        except:
            pass
        return

    args = msg.text.split()
    if len(args) > 1:
        user_input = args[1]
        
        if user_input.isdigit():
            user_id = int(user_input)
            DB.execute("DELETE FROM whitelist WHERE group_id=? AND user_id=?", (msg.chat.id, user_id))
            DB.commit()
            remove_msg = await msg.reply(f"❌ User ID {user_id} removed from whitelist!")
            await send_log(f"❌ User Removed from Whitelist\nUser ID: {user_id}\nGroup: {msg.chat.title}")
            
            await asyncio.sleep(20)
            try:
                await remove_msg.delete()
            except:
                pass
            return
        
        elif user_input.startswith('@'):
            username = user_input[1:]
            try:
                user_info = await bot.get_chat(f"@{username}")
                user_id = user_info.id
                
                DB.execute("DELETE FROM whitelist WHERE group_id=? AND user_id=?", (msg.chat.id, user_id))
                DB.commit()
                remove_msg = await msg.reply(f"❌ User @{username} (ID: {user_id}) removed from whitelist!")
                await send_log(f"❌ User Removed from Whitelist\nUser: @{username}\nID: {user_id}\nGroup: {msg.chat.title}")
                
                await asyncio.sleep(20)
                try:
                    await remove_msg.delete()
                except:
                    pass
                return
            except:
                error_msg = await msg.reply("❌ Invalid username!")
                await asyncio.sleep(20)
                try:
                    await error_msg.delete()
                except:
                    pass
                return
    
    usage_msg = await msg.reply("📝 Usage:\n• Reply to user with /whitelistremove\n• /whitelistremove @username\n• /whitelistremove user_id\n• /whitelistremove (with user mention)")
    await asyncio.sleep(20)
    try:
        await usage_msg.delete()
    except:
        pass

@dp.message(Command("whitelist"))
async def whitelist_show_cmd(msg: Message):
    print(f"👤 Whitelist command received from: {msg.from_user.first_name} in {msg.chat.type}")
    
    if msg.chat.type not in ["group", "supergroup"]:
        await msg.answer("❌ This command only works in groups!")
        return
    
    if not await is_admin(msg.chat.id, msg.from_user.id):
        await msg.reply("❌ Only admins can use this command!")
        return

    cur = DB.execute("SELECT user_id FROM whitelist WHERE group_id=?", (msg.chat.id,))
    users = cur.fetchall()
    
    if not users:
        no_users_msg = await msg.reply("No users in whitelist for this group.")
        await asyncio.sleep(20)
        try:
            await no_users_msg.delete()
        except:
            pass
        return
    
    whitelist_text = "📋 Whitelisted Users:\n\n"
    for user in users:
        user_id = user[0]
        try:
            user_info = await bot.get_chat(user_id)
            username = f"@{user_info.username}" if user_info.username else "No username"
            whitelist_text += f"• {username} (ID: {user_id})\n"
        except:
            whitelist_text += f"• User ID: {user_id}\n"
    
    whitelist_msg = await msg.reply(whitelist_text)
    
    await asyncio.sleep(20)
    try:
        await whitelist_msg.delete()
    except:
        pass

# ============================ WARNINGS COMMAND ======================
@dp.message(Command("warnings"))
async def warnings_cmd(msg: Message):
    """Check user warnings"""
    if msg.chat.type not in ["group", "supergroup"]:
        await msg.answer("❌ This command only works in groups!")
        return
    
    if not await is_admin(msg.chat.id, msg.from_user.id):
        await msg.reply("❌ Only admins can use this command!")
        return

    if msg.reply_to_message:
        user_id = msg.reply_to_message.from_user.id
        username = msg.reply_to_message.from_user.username or "No username"
        
        warning_count = get_warnings(msg.chat.id, user_id)
        
        warning_msg = await msg.reply(
            f"⚠️ Warning Status:\n"
            f"User: @{username}\n"
            f"ID: {user_id}\n"
            f"Warnings: {warning_count}/3"
        )
        
        await asyncio.sleep(20)
        try:
            await warning_msg.delete()
        except:
            pass
        return
    
    args = msg.text.split()
    if len(args) > 1:
        user_input = args[1]
        
        if user_input.isdigit():
            user_id = int(user_input)
            warning_count = get_warnings(msg.chat.id, user_id)
            
            warning_msg = await msg.reply(
                f"⚠️ Warning Status:\n"
                f"User ID: {user_id}\n"
                f"Warnings: {warning_count}/3"
            )
            
            await asyncio.sleep(20)
            try:
                await warning_msg.delete()
            except:
                pass
            return
        
        elif user_input.startswith('@'):
            username = user_input[1:]
            try:
                user_info = await bot.get_chat(f"@{username}")
                user_id = user_info.id
                warning_count = get_warnings(msg.chat.id, user_id)
                
                warning_msg = await msg.reply(
                    f"⚠️ Warning Status:\n"
                    f"User: @{username}\n"
                    f"ID: {user_id}\n"
                    f"Warnings: {warning_count}/3"
                )
                
                await asyncio.sleep(20)
                try:
                    await warning_msg.delete()
                except:
                    pass
                return
            except:
                error_msg = await msg.reply("❌ Invalid username!")
                await asyncio.sleep(20)
                try:
                    await error_msg.delete()
                except:
                    pass
                return
    
    usage_msg = await msg.reply("📝 Usage:\n• Reply to user with /warnings\n• /warnings @username\n• /warnings user_id")
    await asyncio.sleep(20)
    try:
        await usage_msg.delete()
    except:
        pass

# ============================ RESET WARNINGS COMMAND ================
@dp.message(Command("resetwarns"))
async def reset_warns_cmd(msg: Message):
    """Reset user warnings"""
    if msg.chat.type not in ["group", "supergroup"]:
        await msg.answer("❌ This command only works in groups!")
        return
    
    if not await is_admin(msg.chat.id, msg.from_user.id):
        await msg.reply("❌ Only admins can use this command!")
        return

    if msg.reply_to_message:
        user_id = msg.reply_to_message.from_user.id
        username = msg.reply_to_message.from_user.username or "No username"
        
        reset_warnings(msg.chat.id, user_id)
        unmute_user(msg.chat.id, user_id)
        
        reset_msg = await msg.reply(f"✅ Warnings reset for @{username}!")
        
        await asyncio.sleep(20)
        try:
            await reset_msg.delete()
        except:
            pass
        return
    
    args = msg.text.split()
    if len(args) > 1:
        user_input = args[1]
        
        if user_input.isdigit():
            user_id = int(user_input)
            reset_warnings(msg.chat.id, user_id)
            unmute_user(msg.chat.id, user_id)
            
            reset_msg = await msg.reply(f"✅ Warnings reset for user ID {user_id}!")
            
            await asyncio.sleep(20)
            try:
                await reset_msg.delete()
            except:
                pass
            return
        
        elif user_input.startswith('@'):
            username = user_input[1:]
            try:
                user_info = await bot.get_chat(f"@{username}")
                user_id = user_info.id
                reset_warnings(msg.chat.id, user_id)
                unmute_user(msg.chat.id, user_id)
                
                reset_msg = await msg.reply(f"✅ Warnings reset for @{username}!")
                
                await asyncio.sleep(20)
                try:
                    await reset_msg.delete()
                except:
                    pass
                return
            except:
                error_msg = await msg.reply("❌ Invalid username!")
                await asyncio.sleep(20)
                try:
                    await error_msg.delete()
                except:
                    pass
                return
    
    usage_msg = await msg.reply("📝 Usage:\n• Reply to user with /resetwarns\n• /resetwarns @username\n• /resetwarns user_id")
    await asyncio.sleep(20)
    try:
        await usage_msg.delete()
    except:
        pass

# ============================ OWNER COMMANDS ========================
@dp.message(Command("stats"))
async def stats_cmd(msg: Message):
    print(f"📊 Stats command received from: {msg.from_user.first_name}")
    
    if msg.from_user.id != OWNER_ID:
        await msg.answer("❌ You are not authorized to use this command!")
        return
    
    try:
        cur = DB.execute("SELECT COUNT(*) FROM groups")
        groups_count = cur.fetchone()[0]
        
        cur = DB.execute("SELECT SUM(count) FROM warnings")
        warnings_count = cur.fetchone()[0] or 0
        
        cur = DB.execute("SELECT COUNT(*) FROM muted_users")
        muted_count = cur.fetchone()[0]
        
        stats_text = f"""
📊 Bot Statistics

• Total Groups: {groups_count}
• Total Warnings: {warnings_count}
• Muted Users: {muted_count}
• Bot Uptime: Active
        """
        await msg.answer(stats_text)
        print("✅ Stats sent successfully!")
        
    except Exception as e:
        print(f"❌ Error in stats command: {e}")
        await msg.answer("❌ Error fetching statistics")

@dp.message(Command("groups"))
async def groups_cmd(msg: Message):
    print(f"📋 Groups command received from: {msg.from_user.first_name}")
    
    if msg.from_user.id != OWNER_ID:
        await msg.answer("❌ You are not authorized to use this command!")
        return
    
    try:
        cur = DB.execute("SELECT group_id, group_name FROM groups")
        groups = cur.fetchall()
        
        if not groups:
            await msg.answer("No groups found in database.")
            return
        
        groups_text = "📋 All Groups:\n\n"
        for group in groups:
            group_id = group[0]
            group_name = group[1]
            try:
                chat = await bot.get_chat(group_id)
                groups_text += f"• {chat.title} (ID: {group_id})\n"
            except:
                groups_text += f"• {group_name} (ID: {group_id})\n"
        
        await msg.answer(groups_text)
        print("✅ Groups list sent successfully!")
        
    except Exception as e:
        print(f"❌ Error in groups command: {e}")
        await msg.answer("❌ Error fetching groups list")

@dp.message(Command("broadcast"))
async def broadcast_cmd(msg: Message):
    print(f"📢 Broadcast command received from: {msg.from_user.first_name}")
    
    if msg.from_user.id != OWNER_ID:
        await msg.answer("❌ You are not authorized to use this command!")
        return
    
    args = msg.text.split(maxsplit=1)
    if len(args) < 2:
        await msg.answer("Usage: /broadcast <message>")
        return
    
    try:
        broadcast_msg = args[1]
        cur = DB.execute("SELECT group_id FROM groups")
        groups = cur.fetchall()
        
        success = 0
        failed = 0
        
        for group in groups:
            try:
                await bot.send_message(group[0], f"{broadcast_msg}")
                success += 1
            except Exception as e:
                print(f"❌ Failed to send to group {group[0]}: {e}")
                failed += 1
        
        await msg.answer(f"📢 Broadcast completed!\n• Success: {success}\n• Failed: {failed}")
        await send_log(f"📢 Broadcast Sent\nSuccess: {success}\nFailed: {failed}")
        print(f"✅ Broadcast sent to {success} groups, failed: {failed}")
        
    except Exception as e:
        print(f"❌ Error in broadcast command: {e}")
        await msg.answer("❌ Error sending broadcast")

@dp.message(Command("restart"))
async def restart_cmd(msg: Message):
    print(f"🔄 Restart command received from: {msg.from_user.first_name}")
    
    if msg.from_user.id != OWNER_ID:
        await msg.answer("❌ You are not authorized to use this command!")
        return
    
    await msg.answer("🔄 Bot restarting...")
    await send_log("🔄 Bot Restarting...")
    print("✅ Restart command executed")

# ============================ BOT ADDED TO GROUP =================
@dp.message(F.new_chat_members)
async def bot_added_to_group(msg: Message):
    """When bot is added to a group"""
    bot_id = (await bot.get_me()).id
    
    for member in msg.new_chat_members:
        if member.id == bot_id:
            print(f"🤖 Bot added to group: {msg.chat.title}")
            
            ensure_group(msg.chat.id, msg.chat.title)
            
            thanks_text = (
                "Thanks for adding me to this group! 🤖\n\n"
                "I scan user bios in real-time when they message:\n"
                "• Bio Links\n"
                "• Usernames (@example)\n"
                "• Bot Usernames (@bot)\n\n"
                "Make me admin and use /biolink on to start protection!"
            )
            
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="❌ Close", callback_data="close_thanks")]
            ])
            
            try:
                await msg.answer(thanks_text, reply_markup=kb)
                print(f"✅ Thanks message sent to group: {msg.chat.title}")
                
                adder_name = msg.from_user.first_name if msg.from_user else "Unknown"
                log_text = f"🤖 Bot Added\nGroup: {msg.chat.title}\nID: {msg.chat.id}\nBy: {adder_name}"
                await send_log(log_text)
                
            except Exception as e:
                print(f"❌ Error sending thanks message: {e}")

# ============================ BOT RUNNER ============================
async def main():
    print("🚀 Links Shield Bot is Starting...")
    print("🛡️ ULTIMATE ANTI-SLEEP PROTECTION ACTIVATED!")
    
    print("🤖 Bot starting...")
    try:
        me = await bot.get_me()
        print(f"✅ Bot @{me.username} is running!")
        print("📍 Bot ID:", me.id)
        print("👤 Owner ID:", OWNER_ID)
        print("📝 Log Group ID:", LOG_GROUP_ID)
        print("🌐 Multiple Ports: 10000, 10001, 10002, 10003")
        print("🔄 Keep Alive: AGGRESSIVE MODE (25 seconds)")
        print("🚀 Bot is now active and listening...")
        
        # Background unmute checker start karo
        asyncio.create_task(background_unmute_checker())
        print("✅ Background unmute checker started!")
        
        # ULTIMATE Keep Alive start karo
        asyncio.create_task(keep_alive_system.aggressive_keep_alive())
        print("✅ ULTIMATE Keep Alive started!")
        
        # Background pingers start karo
        asyncio.create_task(continuous_internal_pinger())
        asyncio.create_task(continuous_external_pinger())
        print("✅ Background pingers started!")
        
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Multiple Flask servers alag threads mein start karo
    from threading import Thread
    
    print("🔄 Starting Multiple Flask Servers...")
    
    ports = [10000, 10001, 10002, 10003]
    for port in ports:
        thread = Thread(target=run_flask_app, args=(port,))
        thread.daemon = True
        thread.start()
        print(f"✅ Flask server started on port {port}")
    
    print("🛡️ ALL ANTI-SLEEP SYSTEMS ACTIVATED!")
    print("=" * 60)
    
    # Bot start karo
    asyncio.run(main())
