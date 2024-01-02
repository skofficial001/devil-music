from pyrogram import Client, filters
from pyrogram.types import Message
import traceback
import sys
import ast

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token="YOUR_BOT_TOKEN")

# Define the list of users who are allowed to use the /eval command
ALLOWED_USERS = [123456789, 987654321]  # Replace with your user IDs

# Check if the user is allowed to use the /eval command
def is_allowed(user_id):
    return user_id in ALLOWED_USERS

# Define the /eval command handler
@app.on_message(filters.command("eval") & filters.user(ALLOWED_USERS))
async def eval_command(client, message: Message):
    # Extract the code from the message
    code = message.text.split(" ", maxsplit=1)[1]

    try:
        # Parse the code to detect potential malicious code
        parsed_code = ast.parse(code)

        # Ensure the code doesn't contain dangerous operations
        for node in ast.walk(parsed_code):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                raise ValueError("Import statements are not allowed.")
            elif isinstance(node, ast.Attribute) and node.attr.startswith("__"):
                raise ValueError("Magic methods are not allowed.")
            elif isinstance(node, ast.Delete):
                raise ValueError("Delete statements are not allowed.")

        # Execute the code
        eval_locals = {}
        result = eval(compile(parsed_code, filename="<string>", mode="exec"), {}, eval_locals)

        # Send the result back to the user
        await message.reply_text(f"Result:\n```\n{result}\n```")

    except Exception as e:
        # If an exception occurs, send the traceback to the user
        traceback_text = traceback.format_exc()
        await message.reply_text(f"Error:\n```\n{traceback_text}\n```")

# Start the bot
app.run()
