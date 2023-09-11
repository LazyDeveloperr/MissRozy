# (c) @LazyDeveloperr

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"**ʜᴇʀᴇ ɪꜱ ꜱʜᴀʀᴀʙʟᴇ ʟɪɴᴋ ᴏꜰ ᴛʜɪꜱ ꜰɪʟᴇ:**\n"
            f"https://t.me/{Config.BOT_USERNAME}?start=LazyDeveloperr_{str_to_b64(str(file_id))}\n"
            f"__ᴛᴏ ʀᴇᴛʀɪᴠᴇ ᴛʜᴇ ꜱᴛᴏʀᴇᴅ ꜰɪʟᴇ, ᴊᴜꜱᴛ ᴏᴘᴇɴ ᴛʜᴇ ʟɪɴᴋ !__\n\n"
            f"**✪ ʜᴇʀᴇ ɪꜱ ꜰᴀꜱᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ꜱᴛʀᴇᴀᴍ ʟɪɴᴋ:**\n"
            f"**[[ ᴊᴏɪɴ ᴅᴇᴠ ᴄʜᴀɴɴᴇʟ ](https://t.me/LazyDeveloper)]** - **[[ Sᵤ𝚋𝘴𝚌ᵣᵢ𝚋ₑ ](https://youtube.com/@LazyDeveloperr)]**\n",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="▶ ɢᴇɴ ꜱᴛʀᴇᴀᴍ / ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ", callback_data=f'generate_stream_link:{file_id}'
                    )
                ]
            ]
            ),
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await reply_forward(message, file_id)

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)


async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    await asyncio.sleep(2)

