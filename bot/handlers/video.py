from pyrogram import filters
from pyrogram.types import Message
from bot import bot
from bot.utils.mongo import update_user

@bot.on_message(filters.video | filters.document.video)
async def handle_video(client, message: Message):
    video_path = await message.download()
    update_user(message.from_user.id, {"video": video_path})
    await message.reply("Now send a subtitle file (SRT/ASS).")
