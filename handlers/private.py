# ❰ᴀᴅɪᴛʏᴀ✘ᴘʟᴀʏᴇʀ❱
# ❰ᴀᴅɪᴛʏᴀ✘ʜᴀʟᴅᴇʀ❱

import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text="**❰ᴀᴅɪᴛʏᴀ✘ᴘʟᴀʏᴇʀ❱ sᴜᴘᴇʀ ғᴀsᴛ ᴍᴜsɪᴄ\nᴘʟᴀʏᴇʀ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [sʜᴀɪʟᴇɴᴅʀᴀ](t.me/Shailendra34)  ...**".format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**❰ᴀᴅɪᴛʏᴀ✘ᴘʟᴀʏᴇʀ❱ sᴜᴘᴇʀ ғᴀsᴛ\nʜɪɢʜ ǫᴜᴀʟɪᴛʏ » ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ\nʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [sʜᴀɪʟᴇɴᴅʀᴀ](t.me/Shailendra34) ...**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💥", url=f"https://t.me/YAARO_KI_YAARII"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**❰ᴀᴅɪᴛʏᴀ✘ᴘʟᴀʏᴇʀ❱ sᴜᴘᴇʀ ғᴀsᴛ\nʜɪɢʜ ǫᴜᴀʟɪᴛʏ » ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ\nʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [sʜᴀɪʟᴇɴᴅʀᴀ](t.me/Shailendra34) ...**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ʜᴇʀᴇ »» ғᴏʀ ᴍᴏʀᴇ 💞", url=f"https://t.me/MODMENUMAKING"
                    )
                ]
            ]
        ),
    )
