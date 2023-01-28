import discord
import pandas
from datetime import datetime

sheet = pandas.read_csv('2023EECS_TIMES.csv')

dt = datetime.now()
date = dt.strftime('%A')[0]
if date == "T":
    if dt.strftime("%A")[1] == "u":
        date = "R"

testData1 = sheet.iloc[:, 0:1].values
testData2 = sheet.iloc[:, 2:3].values
testData3 = sheet.iloc[:, 3:4].values

w = sheet.loc[(sheet["Location"] == "WSC") & (sheet["1800"] == 1.0)]


# TODO Output user's query (based on user_message)
async def query_func(message, user_message):

    messageList = user_message.split(" ")
    building = messageList[1]
    time = messageList[2]

    if messageList[0] == ("countClassesToday"): #if the command asks for the number of classes today (default)
        # if messageList[0] == "countClasses":
        # message.channel.send(f"Building:{building}\nTime:{time}\nWeekday:{weekday}")
        w = sheet.loc[(sheet["Location"] == f"{building}") & (
            sheet[f"{time}"] == 1.0) & (sheet["Day"] == f"{date}")]
        numPeople = len(w)

        if (numPeople == 1):
            printMessage = f"There is {numPeople} class leaving {building} at {time} on {date}. Safer to go around, but proceed with caution"
        elif (numPeople == 0):
            printMessage = f"There are {numPeople} classes leaving {building} at {time} on {date}. Maybe go around another building"
        elif (numPeople >= 2):
            printMessage = f"There are {numPeople} classes leaving {building} at {time} on {date}. Safer to go around, but proceed with caution"
        await message.channel.send(printMessage)

    elif messageList[0] == ("countClasses"): #if the command asks for the number of classes on a certain day
        weekday = messageList[3]


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
