import discord
import pandas
BUILDING_CODES = set(["LAS", "LSB", "SC", "VH"])
async def query_func(message, user_message):
    # TODO query command
    # format: ?<building code>
    # note that user_message is a string without the ? in the beginning
    await message.channel.send("hi")

# TODO Output proper help information (depending on what user_message is)
async def help_func(message, user_message):
    # TODO list commands
    # TODO list building codes
    # TODO list query commands
    await message.channel.send("hi")


