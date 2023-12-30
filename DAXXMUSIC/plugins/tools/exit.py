from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from DAXXMUSIC import app

@app.on_chat_member_updated(filters.chat)
def member_update_handler(client, update, user):
    chat_id = update.chat.id
    member_name = user.first_name if user.first_name else "Unknown User"
    message_text = f"Hey everyone, {member_name} just dropped the mic and left the group! Catch you on the flip side!"
    inline_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Close", callback_data="close")]])
    client.send_message(chat_id, text=message_text, reply_markup=inline_keyboard)
