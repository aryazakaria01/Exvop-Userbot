from telethon.sessions import StringSession
from telethon import TelegramClient

import os
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

LOGS = logging.getLogger(__name__)

from userbot.config import Config

if os.environ.get("ENV", False):
   SESSION = general.get("SESSION")
   APP_ID = general.get("APP_ID")
   API_HASH = general.get("API_HASH")

APP_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION = Config.SESSION

bot = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
