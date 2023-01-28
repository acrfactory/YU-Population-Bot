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
async def query_func(message, user_message):

    messageList = user_message.split(" ")
    building = messageList[1]
    time = "2030"
    if messageList[0] == ("countClasses"): #if the command asks for the number of classes on a certain day

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


# TODO Output proper help information (depending on what user_message is)
async def help_func(message, user_message):
    await message.channel.send("hi")