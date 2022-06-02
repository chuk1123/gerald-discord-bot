import os
import random

import discord
from discord.ext import commands

guild_ids = [959419758560804894]

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

def get_role(message, role):
    role = discord.utils.get(
    message.guild.roles, name=role)
    return role

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(guild_ids=guild_ids)
async def hi(ctx):
    await ctx.respond('Hi, I am Gerald the sensational penguin!')

@bot.slash_command(guild_ids=guild_ids, description='hee hee hee haa')
async def talk(ctx):
    await ctx.respond('hee hee hee haa\n' + "<:heheheha:981746390805913670>")

@bot.slash_command(guild_ids=guild_ids, description='basketball')
async def afishy(ctx):
    await ctx.respond('El baloncesto es el mejor deporte!')

@bot.slash_command(guild_ids=guild_ids, description='list of role members')
async def role_members(ctx, role=''):
    if role == '':
        await ctx.respond('Please specify role...')
        return

    role = role.title().strip()

    member_list = []
    try:
        members = get_role(ctx, role).members
    except:
        await ctx.respond('Role does not exist')
        return

    for mem in members:
        if mem.nick == None:
            member_list.append(str(mem.name))
        else:
            member_list.append(str(mem.nick))
    await ctx.respond(f'{role}:\n' + "\n".join(member for member in member_list))

@bot.slash_command(guild_ids=guild_ids, name='greet', description='Greet someone!')
async def greet(ctx, name=''):
    await ctx.respond(f'Hello {name}!')

bot.run('OTY4OTA3MzA4ODExODE2OTgx.GwxbBq.pd9zh_Dkn-TFG2ZMKWaOrS3pD7c4d8qsMTZyCA')