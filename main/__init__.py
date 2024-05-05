#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("23615374", default=None, cast=int)
API_HASH = config("b215ecf4e58fc289ca33dbc97d875ffe", default=None)
BOT_TOKEN = config("6665207093:AAHgmOIcFH5I1oZvnzkn_YMg3wVkbSytIb8", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("savebotmhpv", default=None)
AUTH = config("6778796199", default=None, cast=int)

bot = TelegramClient('bot', 23615374, b215ecf4e58fc289ca33dbc97d875ffe).start(bot_token=6665207093:AAHgmOIcFH5I1oZvnzkn_YMg3wVkbSytIb8) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
