import discord
import botfunctions

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = "MTA2ODkxOTg2ODQyMzkzODA1OA.GU7tRN.-fd79inUt1_F8L7IpyKGZx4gu4XHpJAQkZUKFw"

@client.event
async def on_ready():
    print(f"{client.user} is now running")


# 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    date = str(message.created_at)#Date the message sent
    # Help command
    if user_message.startswith("!"):
        # Make the appropriate help 
        await botfunctions.help_func(message, user_message[1:])

    # Query command
    if user_message.startswith("?"):
        await botfunctions.query_func(message, user_message[1:])

client.run(TOKEN)