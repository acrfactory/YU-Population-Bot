import discord
import pandas
# from dateTime import dateTime

sheet = pandas.read_csv('2023EECS_TIMES.csv')

testData1 = sheet.iloc[:,0:1].values
testData2 = sheet.iloc[:,2:3].values
testData3 = sheet.iloc[:,3:4].values

w = sheet.loc[(sheet["1800"] == 1.0) & (sheet["Location"] == "WSC") ]


# TODO Output user's query (based on user_message)
async def query_func(message, user_message):
    if user_message == "countClasses":
            await message.channel.send("ere")

        

# TODO Output proper help information (depending on what user_message is)
async def help_func(message, user_message):
    await message.channel.send("hi")

    