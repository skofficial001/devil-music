from pyrogram import Client, filters
import random
from DAXXMUSIC import app

def get_random_message(mood_percentage):
    if mood_percentage <= 30:
        return random.choice([
            "you are little bit happy😕",
            "what's with wrong you why you are sad🙁",
            "what's happened buddy why are you sad😟"
        ])
    elif mood_percentage <= 70:
        return random.choice([
            "😲wow your mood is happy",
            "hste rho ese hi hste hue aap bhut ache lgte ho☺",
            "I like it your Happiness😊"
        ])
    else:
        return random.choice([
            "Wow! your mood is oky😄",
            "Think and live positive😄😊",
            "me bgwan se yhi dua krti hu apka mood hmesa happy rhe😊"
        ])
        
@app.on_message(filters.command("mood", prefixes="/"))
def mood_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        
        mood_percentage = random.randint(10, 100)
        mood_message = get_random_message(mood_percentage)

        response = f"{name1}💀 = {mood_percentage}%"
    else:
        response = "Please enter your name after /mood command."
    app.send_message(message.chat.id, response)
