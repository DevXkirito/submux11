from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from bot.utils.mongo import update_user, get_user

async def show_settings(client, message: Message):
    user_id = message.from_user.id
    doc = get_user(user_id)
    crf = doc.get("crf", 23)
    codec = doc.get("codec", "libx264")
    preset = doc.get("preset", "medium")
    fontsize = doc.get("fontsize", 24)

    keyboard = [
        [InlineKeyboardButton(f"CRF: {crf}", callback_data="toggle_crf")],
        [InlineKeyboardButton(f"Codec: {codec}", callback_data="toggle_codec")],
        [InlineKeyboardButton(f"Preset: {preset}", callback_data="toggle_preset")],
        [InlineKeyboardButton(f"Font Size: {fontsize}", callback_data="toggle_fontsize")],
        [InlineKeyboardButton("Start", callback_data="start_encoding")]
    ]
    await message.reply("Choose encoding settings:", reply_markup=InlineKeyboardMarkup(keyboard))
