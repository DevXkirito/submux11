from pyrogram import Client
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("hardmux-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

from .handlers import start, video, subtitle, logo, settings, encode
