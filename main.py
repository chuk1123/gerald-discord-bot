import discord
from discord.ext import commands, tasks
from datetime import datetime, date
import os
import random
from canvas import find_tasks, find_cookies
import asyncio
import pytz
from helper import get_day, update_day

client = discord.Client()

try:
    day_num = int(get_day())
except:
    day_num = None #Initialized to none type
cookies = None
myers_messages = [
"(☞ຈل͜ຈ)☞ Y'all are really weird!",
"How's your weekend?",
"Y'all are really quiet!"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 
    daily_task.start()
    if day_num == None:
        message_channel = client.get_channel(969617708561870848)
        user_id = "511881695029493760"
        await message_channel.send(f"<@{user_id}> **Initialize day with !changeday**")

@tasks.loop(hours=24)
async def daily_task():
    message_channel = client.get_channel(969586867513217064)
    week_day_num = date.today().weekday()
    if week_day_num in [0, 1, 3]:
        await message_channel.send("!newday")
        await message_channel.send("!tasks")

@daily_task.before_loop
async def before():
    for _ in range(60*60*24):  # loop the whole day
        utc_now = pytz.utc.localize(datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))

        if pst_now.hour == 8:  # 24 hour format
            print('It is 8. Time to start the loop')
            return
        await asyncio.sleep(1)# wait a second before looping again. You can make it more 

@client.event
async def on_message(message):
    global day_num
    if message.content.startswith('!newday'):
        print(message.author)
        print('New Day Request')
        if day_num == None:
            await message.channel.send('No day set yet...')
            return
        day_num = int(day_num) + 1
        update_day(day_num)
        await message.channel.send('Changed Day Number To: ' + str(day_num))

    if message.content.startswith('!day'):
        if day_num != None:
            await message.channel.send('Day Number: ' + str(day_num))
        else:
            await message.channel.send("No day set yet...")

    if message.content.startswith('!changeday'):

        print(message.author)
        print('Change Day Request')

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel
        
        await message.channel.send('Enter Day Number: ')
        msg = await client.wait_for('message', check=check)
        msg = msg.content
        num = int(msg)
        day_num = num
        update_day(num)
        await message.channel.send('Changed Day Number To: ' + str(day_num))

    if message.content.startswith('!hello'):
        print(message.author)
        print('Hello Request')
        await message.channel.send('Hey Party People!')

    if message.content.startswith('!talk'):
        print(message.author)
        print('Talk Request')
        await message.channel.send(random.choice(myers_messages))

    if message.content.startswith('!tasks'):
        global cookies
        url = 'https://iusd.instructure.com/courses/104033/pages/unit-5-day-'+str(day_num)+'-work'
        print(message.author)
        print('Task Request')
        tasks = find_tasks(url, cookies)
        if tasks == []:
            print('Finding new cookies...')
            cookies = find_cookies()
            tasks = find_tasks(url, cookies)

        await message.channel.send("Here's your tasks: ")
        for task in tasks: #Task = [Task, Link]
            await message.channel.send(task[0])
            if task[1]: #If there contains a link
                await message.channel.send('Link: ' + task[1])
            else:
                continue

    if message.content.startswith('!party'):
        print(message.author)
        print('Party Request')

        await message.channel.send('Hey! Party People!!!', file=discord.File('myers.png'))

client.run('OTY4OTA3MzA4ODExODE2OTgx.YmlrPw.Z-EtIYiqORR2alkyemKe85f9nMY')