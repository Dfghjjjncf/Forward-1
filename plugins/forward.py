from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message
from main import LOGGER, AUTH_USERS
from config import Config
import time
import os


@Client.on_message(
    filters.user(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("forward")
)
async def forward(bot, m: Message):
    msg = await bot.ask(m.chat.id, "**Forward any message from the Target channel\nBot should be admin at both the Channels**")
    t_chat = msg.forward_from_chat.id
    msg1 = await bot.ask(m.chat.id, "**Send Starting Message From Where you want to Start forwarding**")
    msg2 = await bot.ask(m.chat.id, "**Send Ending Message from same chat**")
    i_chat = msg1.forward_from_chat.id
    s_msg = int(msg1.forward_from_message_id)
    f_msg = int(msg2.forward_from_message_id)+1
    stats = await m.reply_text('Forwarding started. . .\n\nPress /restart to Stop and /log to get log TXT file.')
    try:
        for i in range(s_msg, f_msg):
            try:
                msg = await bot.get_messages(i_chat, i)
                if msg.video or msg.document:
                    caption = msg.caption if msg.caption else msg.video.file_name if msg.video else msg.document.file_name
                    await msg.copy(t_chat, caption=f"**{caption}**")
                    time.sleep(4)
            except Exception:
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await stats.edit_text(f"Forwarding completed !!")
