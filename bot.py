import os
from pyrogram import Client, filters
from pyrogram.types import Message

# Replace with your actual credentials
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Pyrogram client initialization
app = Client(
    "private_link_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.photo & filters.channel)
async def handle_photo_in_channel(client: Client, message: Message):
    """
    Handles a photo message in a private channel by adding a public link.
    """
    try:
        # Check if the message has a message_id to prevent crashes
        if not message.message_id:
            print("Skipping message as it has no message_id.")
            return

        chat_id = str(message.chat.id)
        message_id = message.message_id

        # Construct the private channel link
        if chat_id.startswith('-100'):
            short_chat_id = chat_id.replace('-100', '')
            image_link = f"https://t.me/c/{short_chat_id}/{message_id}"
        else:
            image_link = f"https://t.me/c/{chat_id}/{message_id}"

        print(f"Generated private link: {image_link}")

        # Get original caption or use an empty string
        original_caption = message.caption if message.caption else ""
        
        # Create the new caption with the added link
        new_caption = f"{original_caption}\n\n[Image Link]({image_link})"

        # Edit the message's caption
        await message.edit_caption(caption=new_caption)
        print("Caption updated successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the bot
app.run()
