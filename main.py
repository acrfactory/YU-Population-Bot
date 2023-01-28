import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = "MTA2ODkxOTg2ODQyMzkzODA1OA.Gx_qoK.zxNBIFAr5M8MyfcRAPGkPVxkNQVxNqJ5ZfGfoc"

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
