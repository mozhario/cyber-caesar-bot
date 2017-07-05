# Cyber Caesar Bot

Ave! I am a Telegram Bot client for Cyber Caesar encryption service.
I live at [@cyber_caesar_bot](https://t.me/cyber_caesar_bot)

### Available commands

 - /encrypt <text> # <key>
 - /decrypt <text> # <key>
 - /break <encrypted-text>

Note that you should use "#" character as the parameters delimiter.

### Installation

1. Create tg bot and get your own api token ([guide](https://core.telegram.org/bots#3-how-do-i-create-a-bot))
2. Place your token to the CAESAR_TG_TOKEN env variable (.env files are supported).
3. Install dependencies using
```
pip install -r requirements.txt
```
Recommended to use virtualenv.

4. Run. This can be achieved in two ways:
 - Configure bot to use polling and run bot.py from anywhere from console.
 - Deploy somewhere on the web and set your own webhook in the config.py