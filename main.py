import discord
def run_discord_bot() :
    TOKEN = "MTA2ODkxOTg2ODQyMzkzODA1OA.GRq0ET.xzmcJ32pPdzNAsEBTduHDNXKuLWDIK6M7exJPQ"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} is now running")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    if user_message.startswith("!"):
        message.channel.send("hi")

client.run()