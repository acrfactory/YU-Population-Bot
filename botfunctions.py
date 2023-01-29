import discord
import pandas
from datetime import datetime
sheet = pandas.read_csv('2023EECS_TIMES.csv')
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
    "countClassesToday": "See the numnber of classes opened today",
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
    # building = fields[1]
    # if the command asks for the number of classes on a certain day
    if fields[0] == ("countClassesToday"):
        building = fields[1]

        timeOld = dt.strftime("%H%M")
        time = str(roundToHour(timeOld))

    
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
    elif fields[0] == ("countClasses"):
        time = fields[2]
        wday = fields[3]
        building = fields[1]

        w = sheet.loc[(sheet["Location"] == f"{building}") & (
            sheet[f"{time}"] == 1.0) & (sheet["Day"] == f"{wday}")]
        numPeople = len(w)

        if (numPeople == 1):
            printMessage = f"There is {numPeople} class leaving {building} at {time} on {wday}. Safer to go around, but proceed with caution."
        elif (numPeople == 0):
            printMessage = f"There are {numPeople} classes leaving {building} at {time} on {wday}. Maybe go around another building."
        elif (numPeople >= 2):
            printMessage = f"There are {numPeople} classes leaving {building} at {time} on {wday}. Safer to go around, but proceed with caution."
        await message.channel.send(printMessage)
    elif fields[0] == "listCodes":
        for code, building in BUILDING_CODES.items():
            await message.channel.send(f"{code}: {building}")

    # ?help
    elif fields[0] == "help":
        for command, desc in COMMANDS.items():
            await message.channel.send(f"{command}: {desc}")
# TODO Output proper help information (depending on what user_message is)

async def help_func(message, user_message):
    fields = user_message.split(" ")
    
    
    if (fields[0] == "help"):
        s="ALL COMMANDS\n==============\n"
        for key , value in COMMANDS.items():
            s += f"{key}: {value}\n"

    await message.channel.send(s)

def roundToHour(time):
    hour = int(time[0:2])
    mins = int(time[2:4])
    newMins = "00"
    if (mins >=45 and mins <60) :
        newMins = "00"
        return f"{hour+1}{newMins}"
    elif(mins >= 0 and mins <15):
        newMins == "00"
    elif (mins >=15 and mins < 30):
        newMins == "30"
    elif (mins >=30 and mins < 45):
        newMins == "30"
        
    return f"{time[0:2]}{newMins}"
