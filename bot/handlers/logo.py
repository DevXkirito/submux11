from pyrogram import filters
from pyrogram.types import Message
from bot import bot
from bot.utils.mongo import update_user
from bot.handlers.settings import show_settings

@bot.on_message(filters.photo | (filters.document & filters.document.file_name.regex(r"\.(jpg|jpeg|png)$")))
async def handle_logo(client, message: Message):
    logo_path = await message.download()
    update_user(message.from_user.id, {"logo": logo_path})
    await show_settings(client, message)

@bot.on_message(filters.command("skip"))
async def skip_logo(client, message: Message):
    await show_settings(client, message)
