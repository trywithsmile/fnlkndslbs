import os
from pyrogram import Client, filters
from pyrogram.types import Message

# API Keys aur Bot Token ko environment variables se lenge
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Pyrogram client ko initialize karein
app = Client(
    "private_link_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.photo & filters.channel)
async def handle_photo_in_channel(client: Client, message: Message):
    try:
        chat_id = str(message.chat.id)
        message_id = message.message_id

        if chat_id.startswith('-100'):
            short_chat_id = chat_id.replace('-100', '')
            image_link = f"https://t.me/c/{short_chat_id}/{message_id}"
        else:
            image_link = f"https://t.me/c/{chat_id}/{message_id}"

        original_caption = message.caption if message.caption else ""
        new_caption = f"{original_caption}\n\n[Image Link]({image_link})"

        await message.edit_caption(caption=new_caption)

    except Exception as e:
        print(f"Error: {e}")

# Bot ko chalu karein
app.run()
