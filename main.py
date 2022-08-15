import os
import random

import discord
from discord.ext import commands
from discord.ui import Select, View
from discord.commands import Option

intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)

guild_ids = []

hunger_level = random.randint(3, 8)

def get_role_options(guild):
    roles = guild.roles
    options=[]
    for r in roles:
        options.append(discord.SelectOption(
            label=str(r),
            value=str(r)
        ))
    return options

@bot.event
async def on_ready():
    for guild in bot.guilds:
        guild_ids.append(guild.id)
    print('We have logged in!')

@bot.slash_command( description='say hi to Gerald')
async def hi(ctx, name=None):
    await ctx.respond('Hi, I am Gerald the sensational penguin!')
    if name != None:
        await ctx.respond(f'Hi {name}, I am Gerald the sensational penguin!')

@bot.slash_command( description='feed me my favorite food')
async def feed(ctx, food):
    global hunger_level
    food = food.lower()
    favorite_food = ["fish", "krill", "squid", "pizza"]
    if hunger_level <= 0:
        await ctx.respond("I am full!")
        return

    if food in favorite_food:
        hunger_level -= 1
        await ctx.respond(f"I ate {food}! \nHunger Level: {hunger_level}")
    else:
        await ctx.respond("I don't want to eat that!")

@bot.slash_command( description='hee hee hee haa')
async def laugh(ctx):
    await ctx.respond('hee hee hee haa\n' + "<:heheheha:981746390805913670>")

@bot.slash_command( description='basketball')
async def afishy(ctx):
    await ctx.respond('El baloncesto es el mejor deporte!')

@bot.slash_command( description='Gerald talks')
async def talk(ctx):
    messages=[
        'You are phenomenal!',
        'You are absolutely sensational!',
        'Get good.',
        "I am a penguin.",
        '\ (•◡•) /'
    ]
    if hunger_level > 3:
        messages.extend(["I'm hungry.", "Can I eat you?"])
    message = random.choice(messages)
    await ctx.respond(message)

@bot.slash_command( description='how hungry I am')
async def show_hunger_level(ctx):
    await ctx.respond(f"Hunger Level: {str(hunger_level)}")

@bot.slash_command( description='list members of role')
async def role_members(ctx):
    guild = bot.get_guild(ctx.guild.id)
    select = Select(placeholder='Choose a role', options=get_role_options(guild))

    async def select_callback(interaction): # the function called when the user is done selecting options
        
        role=discord.utils.get(guild.roles, name=select.values[0])

        members = role.members
        member_list = []

        for mem in members:
            if mem.nick == None:
                member_list.append(str(mem.name))
            else:
                member_list.append(str(mem.nick))
        await interaction.response.send_message(f'{role}:\n' + "\n".join(member for member in member_list))

    select.callback = select_callback
    view = View(timeout=10)
    view.add_item(select)
    await ctx.respond("Choose a role!", view=view)
    
@bot.slash_command( name='greet', description='Greet someone!')
async def greet(ctx, name=''):
    if name == '':
        await ctx.respond('Hey!')
    else:
        await ctx.respond(f'Hello {name}!')

with open('bot_token.txt', 'r') as f:
    TOKEN = f.readline().strip()

bot.run(TOKEN)