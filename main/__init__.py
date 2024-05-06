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
SESSION = config("BQFoV44AZDPr_kmS47AeOTn4tclYnrlJZ3jnEl9FzyW3i-hZsjkYMkFM3JquZL8VfaSS-Lm38QQXL4av5K3CtoNYfPgvGJetogk0tozMFD2o-rjSr2XX3Z2AeeMpVCJt6hNqs2doG6_IfyIQEw_WluXwkvCY5Ll1J3-uXtzF0jmfT4-rtNryaKR85L2mWCqaH0LOrERYUyNbiJ_jFroYmMRVX86xtnfpjWd3kjFOFTWcW3OYnvEy6lT_2-HCESfL3Ry2eM66_Lh6hCyv7QB5xPciG1k9-NCSUeZMAgWkffetuJSleMZ1CnV7Sofy5PqeKvLSdaAnTgNguxxLeIKwJeDyiiHm1QAAAAGUDDinAA", default=None)
FORCESUB = config("savebotmhpv", default=None)
AUTH = config("6778796199", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

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
