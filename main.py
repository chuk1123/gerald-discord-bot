import os
import random

import discord
from discord.ext import commands

guild_id = '959419758560804894'

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

def get_penguin_role(message):
    penguin_role = discord.utils.get(
    message.guild.roles, id=981439948152528986)
    return penguin_role

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(guild_ids=[guild_id], description='testing')
async def hi(ctx):
    await ctx.respond('Hi, I am Gerald the sensational penguin!')

@bot.slash_command(guild_ids=[guild_id], description='hee hee hee haa')
async def talk(ctx):
    await ctx.respond('hee hee hee haa\n' + "<:heheheha:981746390805913670>")
    
@bot.slash_command(guild_ids=[guild_id], description='list of penguins')
async def penguins(ctx):
    penguins = []
    penguin_mem = get_penguin_role(ctx).members
    for penguin in penguin_mem:
        if penguin.nick == None:
            penguins.append(str(penguin.name))
        else:
            penguins.append(str(penguin.nick))
    await ctx.respond('Penguins:\n' + "\n".join(member for member in penguins))

bot.run('OTY4OTA3MzA4ODExODE2OTgx.GwxbBq.pd9zh_Dkn-TFG2ZMKWaOrS3pD7c4d8qsMTZyCA')