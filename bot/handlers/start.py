from pyrogram import filters
from pyrogram.types import Message
from bot import bot

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("Send a video file (MP4/MKV) to start hardmuxing.")
