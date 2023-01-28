import discord
import pandas

sheet = pandas.read_csv('2023EECS_TIMES.csv')


# TODO Output user's query (based on user_message)
async def query_func(message, user_message):
    # TODO add query command to find if classes are open in a building
    # format: ?<building code> <time>
    # format of time in military (no colon)
    # Example ?VH 2100
    await message.channel.send(sheet)

# TODO Output proper help information (depending on what user_message is)
async def help_func(message, user_message):
    # TODO list commands
    # TODO list building codes
    # TODO list query commands
    await message.channel.send("hi")