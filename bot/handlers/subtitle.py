from pyrogram import filters
from pyrogram.types import Message
from bot import bot
import pysubs2
from bot.utils.mongo import update_user

@bot.on_message(filters.document & filters.document.file_name.regex(r"\.(srt|ass)$"))
async def handle_subtitle(client, message: Message):
    file_path = await message.download()
    if file_path.endswith(".srt"):
        subs = pysubs2.load(file_path)
        ass_path = file_path.replace(".srt", ".ass")
        subs.save(ass_path)
    else:
        ass_path = file_path
    update_user(message.from_user.id, {"subtitle": ass_path})
    await message.reply("Send logo image (PNG/JPG) or use /skip.")
