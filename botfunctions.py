import discord
import pandas
from datetime import datetime
sheet = pandas.read_csv('2023EECS_TIMES1.csv')
dt = datetime.now()
weekday = dt.strftime('%A')[0]
if weekday == "T":
    if dt.strftime("%A")[1] == "u":
        weekday = "R"
    if dt.strftime("%A")[0] == "S":
        weekday = "M"
# TODO Output user's query (based on user_message)
COMMANDS = {
    "countClasses": "Given a building code & time, see the number of classes open",
    "countClassesToday" : "See the numnber of classes opened today",
    "listCodes": "List all building codes",
    "help": "List all commands"
}
BUILDING_CODES = {
    "WSC": "William Small Centre",
    "VH": "Veri Hall",
    "LAS": "Lassonde Building",
    "SC": "Stong College"
}
TIMES = set(["1800", "1830", "1900", "1930", "2000", "2030", "2100", "2130"])
async def query_func(message, user_message):

    fields = user_message.split(" ")
    
    
    if len(fields) == 0 or fields[0] not in COMMANDS:
        # Invalid command
        await message.channel.send("Improper command, use the '!list' command to see query commands")
    building = fields[1]
    if fields[0] == ("countClassesToday"): #if the command asks for the number of classes on a certain day
        
        time = "2030"
        w = sheet.loc[(sheet["Location"] == f"{building}") & (
            sheet[f"{time}"] == 1.0) & (sheet["Day"] == f"{weekday}")]
        numPeople = len(w)

        if (numPeople == 1):
            printMessage = f"There is {numPeople} class leaving {building} at {time} on {weekday}. Safer to go around, but proceed with caution"
        elif (numPeople == 0):
            printMessage = f"There are {numPeople} classes leaving {building} at {time} on {weekday}. Maybe go around another building"
        elif (numPeople >= 2):
            printMessage = f"There are {numPeople} classes leaving {building} at {time} on {weekday}. Safer to go around, but proceed with caution"
        await message.channel.send(printMessage)
    elif fields[0] ==  ("countClasses"):
        time = fields[2]
        wday = fields[3]

        w = sheet.loc[(sheet["Location"] == f"{building}") & (
            sheet[f"{time}"] == 1.0) & (sheet["Day"] == f"{wday}")]
        numPeople = len(w)

        if (numPeople == 1):
            printMessage = f"There is {numPeople} class leaving {building} at {time} on {wday}. Safer to go around, but proceed with caution"
        elif (numPeople == 0):
            printMessage = f"There are {numPeople} classes leaving {building} at {time} on {wday}. Maybe go around another building"
        elif (numPeople >= 2):
            printMessage = f"There are {numPeople} classes leaving {building} at {time} on {wday}. Safer to go around, but proceed with caution"
        await message.channel.send(printMessage)
# TODO Output proper help information (depending on what user_message is)
 # ?contains <building code> <time>
    elif fields[0] == "contains":
        if len(fields) == 1 or fields[1] not in BUILDING_CODES:
            await message.channel.send("Improper building code")
            return
        if len(fields) == 2 or fields[2] not in TIMES:
            await message.channel.send("Improper time")
            return
        # TODO check
        if len(sheet.loc[ (sheet[fields[2]] == 1.0) & (sheet["Location"] == fields[1]) ]) != 0:
            await message.channel.send(f"{BUILDING_CODES[fields[1]]} contains classes during {fields[2][:2]}:{fields[2][2:]}")
        else:
            await message.channel.send(f"{BUILDING_CODES[fields[1]]} does not contain classes during {fields[2][:2]}:{fields[2][2:]}")

    # ?listCodes
    elif fields[0] == "listCodes":
        for code, building in COMMANDS.items():
            await message.channel.send(f"{code}: {building}")
# ?help
    elif fields[0] == "help":
        for command, desc in COMMANDS.items():
            await message.channel.send(f"{command}: {desc}")