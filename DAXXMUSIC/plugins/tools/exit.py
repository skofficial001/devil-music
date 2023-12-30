from pyrogram import Client 
from pyrogram.types import InlineKeyboard Button, InlineKeyboard Markup 
from pyrogram import filters 
from DAXXMUSIC Import bot as app

@app.on_chat_member _updated(filters.chat)
def member_update_handler(client, update, user):
chat_id = update.chat.id
member_name = user.first name if user.first name else "Unknown User"
message_text=fHey everyone, (member_name) just dropped the mic and left the group! Catch you on the flip side!
inline_keyboard= InlineKeyboard Markup([[Inli nekeyboardButton("Close", callback_data="close")]])
client.send_message(chat_id, message text, reply_markup-inline_keyboard)
