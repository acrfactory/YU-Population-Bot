print("hi")
import discord
import botfunctions
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = "MTA2ODkxOTg2ODQyMzkzODA1OA.GNoCVJ.LA2FlaNwASkqliN-pNsnkYC_FRAe0mH0ZmgaIQ"

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


    # Query command
    if user_message.startswith("?"):
        # Returns queried data
        await botfunctions.query_func(message, user_message[1:])

    
client.run(TOKEN)
