
import asyncio
from time import time
from datetime import datetime
from IyaadXmusic.config import BOT_USERNAME, UPDATES_CHANNEL, ZAID_SUPPORT
from IyaadXmusic.helpers.filters import command
from IyaadXmusic.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/899cf677d90a10b907a15.png",
        caption=f"""**ᴀ I'ᴍ Fᴀsᴛ Tᴇʟᴇɢʀᴀᴍ Mᴜsɪᴄ ʙᴏᴛ Wɪᴛʜ Cᴏᴏʟ Dᴇsɪɢɴ Eɴᴊᴏʏ Wɪᴛʜ ᴛʜɪs Aᴡᴇsᴏᴍᴇ Bᴏᴛ ...
💞 Tʜɪs Aᴡᴇsᴏᴍᴇ ʙᴏᴛ 
Mᴀᴅᴇ Wɪᴛʜ ♥️ ʙʏ  [Sᴏᴍᴀʟɪʙᴏᴛs](t.me/Somalibots) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ", url=f"https://telegra.ph/Copyright-11-23"
                    ),
                    InlineKeyboardButton(
                        "Tʜᴇ Dᴇᴠɪʟ 😈", url="https://t.me/YaamiinTor"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🇮🇳", url="https://t.me/{Somalibots_help}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b85744e817cd61d906f71.jpg",
        caption=f"""ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💞", url=f"https://t.me/Somalibots_help")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4c098ec0d9fb56a89f3c7.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Oᴡɴᴇʀ 💞", url=f"https://t.me/YaamiinTor")
                ]
            ]
        ),
    )
