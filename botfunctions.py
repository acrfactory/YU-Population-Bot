print("hi")
import discord
import botfunctions
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = "MTA2ODkxOTg2ODQyMzkzODA1OA.G_sHKo.ZR73Fh4Z4M40ms-NVXUzP5AVWEmqL8L92jEptQ"

@client.event
async def on_ready():
    print(f"{client.user} is now running")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    date = str(message.created_at)     
    user_message = str(message.content)
    channel = str(message.channel)

    # Help command
    if user_message.startswith("!"):
        # Sends appropriate help message
        await botfunctions.help_func(message, user_message[1:])

    # Query command
    if user_message.startswith("?"):
        # Returns queried data
        await botfunctions.query_func(message, user_message[1:])

    
client.run(TOKEN)
