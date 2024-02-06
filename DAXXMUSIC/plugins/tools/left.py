from pyrogram import Client 
from pyrogram import filters 
from DAXXMUSIC import app

@app.on_chat_member_updated(filters.chat) def member update handler (client, update, user):

chat id update.chat.id member name user first name if userfirst name else "Unknown User

message f'fmember name} is bnde ne apka group left kr diya hai😕"

client send message(chat id, message)
