#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
if API_ID is None:
    # Handle the case where API_ID is not provided
    print("API_ID is not provided.")
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("BQFoV44AvEOL3lwjXyEZVm3rAR3EUML1CK8f05AO_oFw8JKc8kh01E4MjVauS1Xs90uvrm_PIm-0YX-UhBwj7EPgcoqVcyT6zmqyOH8jKZmm1IICXvBwFBPxySz4K4eDKr0W5fBJWNo3nWeb2hW3-mDYAQ3bA0gaedZtFOlHjmSG7Y1Ht6KbozOAnswZv07IkAHcFQwslRPfDjJQpVj7BbhmBT_wisGBS_QEWEZJQhBHhQ5_4fm3PMuOilGh7BmLb5ttn50NmUbUgqqKTx71tVUrnVjD5NJprjpllF-6BjVUsx1SPslUc_jYg4NkNJI7fYY62VabopV3NZbATaHZ5f0MBRw5KgAAAAGUDDinAA", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

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
