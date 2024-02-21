import asyncio
from pyrogram import Client, filters

source_channel = int(-1001916629858)
target_channel = int(-1002089952728)

@Client.on_message(filters.channel & filters.chat(source_channel) & (filters.video | filters.document) & filters.incoming)
async def forward_media(client, message):
    if message.video or message.document:
        caption = message.caption if message.caption else message.video.file_name if message.video else message.document.file_name
        try:
            await message.copy(
              chat_id=target_channel,
              caption=f"**{caption}**")
        except Exception as e:
            print(f"Error forwarding message: {e}")
    else:
        pass
