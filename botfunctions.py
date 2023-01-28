import discord
import pandas
# TODO Output user's query (based on user_message)
async def query_func(message, user_message):
    await message.channel.send("hi")

# TODO Output proper help information (depending on what user_message is)
async def help_func(message, user_message):
    await message.channel.send("hi")


