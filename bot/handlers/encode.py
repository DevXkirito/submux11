from pyrogram import filters
from bot import bot
from pyrogram.types import CallbackQuery
from bot.utils.mongo import get_user, update_user
from bot.config import FONT_PATH
import asyncio
import os

@bot.on_callback_query()
async def handle_encoding(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data

    doc = get_user(user_id)
    crf = doc.get("crf", 23)
    codec = doc.get("codec", "libx264")
    preset = doc.get("preset", "medium")
    fontsize = doc.get("fontsize", 24)

    if data == "toggle_crf":
        crf = 28 if crf == 23 else 23
        update_user(user_id, {"crf": crf})
    elif data == "toggle_codec":
        codec = "libx265" if codec == "libx264" else "libx264"
        update_user(user_id, {"codec": codec})
    elif data == "toggle_preset":
        preset = {"medium": "fast", "fast": "slow", "slow": "medium"}[preset]
        update_user(user_id, {"preset": preset})
    elif data == "toggle_fontsize":
        fontsize = 32 if fontsize == 24 else 24
        update_user(user_id, {"fontsize": fontsize})
    elif data == "start_encoding":
        video = doc.get("video")
        subtitle = doc.get("subtitle")
        logo = doc.get("logo")

        out_path = video.rsplit(".", 1)[0] + "_muxed.mp4"
        vf_chain = f"subtitles='{subtitle}'"

        if logo:
            vf_chain += ",overlay=W-w-10:10"

        vf_chain += f",drawtext=fontfile='{FONT_PATH}':text='©Watermark':x=W-tw-10:y=10:fontsize={fontsize}:fontcolor=white@0.8"

        cmd = [
            "ffmpeg", "-i", video,
            *(["-i", logo] if logo else []),
            "-filter_complex", vf_chain,
            "-c:v", codec, "-preset", preset, "-crf", str(crf), out_path
        ]

        process = await asyncio.create_subprocess_exec(*cmd)
        await process.communicate()
        await client.send_document(user_id, out_path)
        return

    await callback_query.answer()
    await callback_query.message.delete()
    from .settings import show_settings
    await show_settings(client, callback_query.message)
