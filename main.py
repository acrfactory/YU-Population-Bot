import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = ""

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
        await message.channel.send("hi")

client.run(TOKEN)
