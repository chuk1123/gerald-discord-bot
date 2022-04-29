import discord
import os
import random
import time
from canvas import find_tasks

client = discord.Client()

day_num = 9 # started on day 9
myers_messages = [
"(☞ຈل͜ຈ)☞ Y'all are really weird!",
"How's your weekend?",
"Y'all are really quiet!"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!newday'):
        global day_num
        day_num += 1
        await message.channel.send('Changed Day Number To: ' + str(day_num))

    if message.content.startswith('!changeday'):

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel
        
        await message.channel.send('Enter Day Number: ')
        msg = await client.wait_for('message', check=check)
        msg = msg.content
        num = int(msg)
        day_num = num
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
        url = 'https://iusd.instructure.com/courses/104033/pages/unit-5-day-'+str(day_num)+'-work'
        print(message.author)
        print('Task Request')
        tasks = find_tasks(url)
        await message.channel.send('Hey Party People!!!')
        await message.channel.send('Today will be a very easy day!')
        await message.channel.send("Here's your tasks: ")
        for task in tasks: #Task = [Task, Link]
            await message.channel.send(task[0])
            if task[1]: #If there contains a link
                await message.channel.send('Link: ' + task[1])
            else:
                continue

    if message.content.startswith('!party'):
        await message.channel.send('Hey! Party People!!!', file=discord.File('myers.png'))


client.run('OTY4OTA3MzA4ODExODE2OTgx.YmlrPw.Z-EtIYiqORR2alkyemKe85f9nMY')