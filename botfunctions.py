import discord
import pandas
# from dateTime import dateTime

sheet = pandas.read_csv('2023EECS_TIMES.csv')

testData1 = sheet.iloc[:,0:1].values
testData2 = sheet.iloc[:,2:3].values
testData3 = sheet.iloc[:,3:4].values

w = sheet.loc[(sheet["Location"] == "WSC") & (sheet["1800"] == 1.0) ]


# TODO Output user's query (based on user_message)
async def query_func(message, user_message):
    messageList=user_message.split(" ")
    building = messageList[1]
    time = messageList[2]
    # weekday = messageList[3]

    # if messageList[0] == "countClasses":
        # message.channel.send(f"Building:{building}\nTime:{time}\nWeekday:{weekday}")
    w = sheet.loc[(sheet["Location"] == f"{building}") & (sheet[f"{time}"] == 1.0) ]
    numPeople = len(w)

    if(numPeople == 1 ):
        printMessage = f"There is {numPeople} class leaving {building} at {time}. Proceed with caution!"
    elif (numPeople == 0 ):
        printMessage = f"There are {numPeople} classes leaving {building} at {time}. Be extra careful!"
    elif (numPeople >=2 ):
        printMessage = f"There are {numPeople} classes leaving {building} at {time}. This building should be safe to walk near."
    await message.channel.send(printMessage)
        



        

# TODO Output proper help information (depending on what user_message is)
async def help_func(message, user_message):
    await message.channel.send("hi")

    