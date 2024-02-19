from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, AUTH_USERS
from config import Config
import os
import sys


@Client.on_message(
    filters.user(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("start")
)
async def Start_msg(bot, m: Message):
    await m.reply_photo(
    photo="https://telegra.ph/file/d77a3767a8d58da76f2df.jpg",
    caption = f"Hello [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n" +
    f"\nI am Auto Forwarder bot." +
    f"\nPress /help for More Info.",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🙋‍♂️Dev Ace", url="https://t.me/AceCallRobot")],
            [InlineKeyboardButton("Channel", url="https://t.me/WickedSkull")],
            [InlineKeyboardButton("Repo", url="https://github.com/imacekun/ACE-AUTO-FORWARD/")],
        ],
    )
    )


@Client.on_message(
    filters.user(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("help")
)
async def help_msg(bot, m: Message):   
    await m.reply_text(
        f"\n\nI can Forward message from one chat to another\n"+
        f"Available Commands are :"+
        f"\n\n/forward to start forwarding\n/log - To get Log file\n/restart - To Restart the bot"
    )

@Client.on_message(
    filters.user(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("restart")
)
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(
    filters.user(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("log")
)
async def log_msg(bot, m: Message):   
    await bot.send_document(m.chat.id, "log.txt")
