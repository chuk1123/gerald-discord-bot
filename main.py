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

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@tasks.loop(hours=24)
async def daily_task():
    message_channel = client.get_channel(969586867513217064)
    week_day_num = date.today().weekday()
    if week_day_num in [0, 1, 3]:
        await message_channel.send("!newday")
        await message_channel.send("!tasks")
    if str(date.today()) == '2022-06-03':
        await asyncio.sleep(60)
        await message_channel.send("I SELF DESTRUCT!!!")

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
    pass

client.run('OTY4OTA3MzA4ODExODE2OTgx.YmlrPw.Z-EtIYiqORR2alkyemKe85f9nMY')