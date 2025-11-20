# 🤖 Bio Shield Bot

A powerful Telegram bot that protects groups from bio links, usernames, and spam in real-time.

## Features
- 🔍 Real-time bio scanning
- ⚠️ 3 Warning system  
- 🔇 Auto mute after 3 warnings
- 👥 Whitelist system
- 📊 Admin commands
- 🛡️ Sleep protection for 24/7 uptime

## Deployment

### Render.com
1. Fork this repository
2. Go to [Render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repo
5. Use these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`

## Bot Commands

### Admin Commands
- `/biolink on/off` - Enable/disable protection
- `/whitelistadd` - Add user to whitelist  
- `/whitelistremove` - Remove user from whitelist
- `/warnings` - Check user warnings
- `/resetwarns` - Reset user warnings

### Owner Commands
- `/stats` - Bot statistics
- `/broadcast` - Broadcast message
- `/groups` - All groups list

## Support
For support, contact [Owner](https://t.me/insaanova)