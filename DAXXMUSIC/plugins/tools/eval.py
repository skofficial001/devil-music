from pyrogram import Client, filters

app = Client("my_bot")

# Define a command to evaluate Python code
@app.on_message(filters.command("eval") & filters.me)
async def evaluate(_, message):
    try:
        # Extract the code from the command
        code = message.text.split(" ", 1)[1]
        
        # Execute the code using eval
        result = eval(code)

        # Send the result back as a message
        await message.edit_text(f"Result: {result}")

    except Exception as e:
        # Handle exceptions and send an error message
        await message.edit_text(f"Error: {e}") 
