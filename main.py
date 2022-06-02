import discord
from discord.ext import commands, tasks
from datetime import datetime, date
import os
import random
from canvas import find_tasks, find_cookies
import asyncio
import pytz
from helper import get_day, update_day

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

def get_penguin_role(message):
    penguin_role = discord.utils.get(
    message.guild.roles, id=981439948152528986)
    return penguin_role

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!hi'):
        await message.channel.send('Hi, I am Gerald the sensational penguin!')
    
    if message.content.startswith('!penguins') or message.content.startswith('!penguin'):
        await message.channel.send('Penguins:')
        penguins = []
        penguin_mem = get_penguin_role(message).members
        for penguin in penguin_mem:
            if penguin.nick == None:
                penguins.append(str(penguin.name))
            else:
                penguins.append(str(penguin.nick))
        await message.channel.send("\n".join(member for member in penguins))

    if message.content.startswith('!talk'):
        messages = ['hee hee hee haa']
        await message.channel.send(messages[0])
        await message.channel.send("<:heheheha:981746390805913670>")

client.run('OTY4OTA3MzA4ODExODE2OTgx.YmlrPw.Z-EtIYiqORR2alkyemKe85f9nMY')