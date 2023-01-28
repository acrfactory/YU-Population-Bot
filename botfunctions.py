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
async def help_func(message, user_message):
    await message.channel.send(COMMANDS)
