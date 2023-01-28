import discord
import pandas
from datetime import datetime
sheet = pandas.read_csv('2023EECS_TIMES.csv')
dt = datetime.now()
date = dt.strftime('%A')[0]
COMMANDS = {
    "countClasses": "Given a building code & time, see the number of classes open",
    "listCodes": "List all building codes",
    "help": "List all commands"
}
BUILDING_CODES = {
    "WSC": "William Small Centre",
    "VH": "Veri Hall",
    "LAS": "Lassonde Building",
    "SC": "Stone College"
}
TIMES = set(["1800", "1830", "1900", "1930", "2000", "2030", "2100", "2130"])

# TODO Output user's query (based on user_message)
async def query_func(message, user_message):

    fields = user_message.split(" ")

    if len(fields) == 0 or fields[0] not in COMMANDS:
        # Invalid command
        await message.channel.send("Improper command, use the '!list' command to see query commands")

    # TODO countClasses
    elif fields[0] == "countClasses":
        await message.channel.send(sheet)

    elif fields[0] == "open":
        if len(fields) == 1 or fields[1] not in BUILDING_CODES:
            await message.channel.send("Improper building code")
            return
        if len(fields) == 2 or fields[2] not in TIMES:
            await message.channel.send("Improper time")
            return
        await message.channel.send(f"{BUILDING_CODES[fields[1]]} contains classes during {fields[2][:2]}:{fields[2][2:]}")

    elif fields[0] == "listCodes":
        for code, building in COMMANDS.items():
            await message.channel.send(f"{code}: {building}")

    elif fields[0] == "help":
        for command, desc in COMMANDS.items():
            await message.channel.send(f"{command}: {desc}")

    
