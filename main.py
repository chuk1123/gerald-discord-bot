"""
Gerald the Penguin Discord Bot

A fun, personality-driven Discord bot featuring Gerald the sensational penguin.
Includes interactive commands, a hunger system, and server utilities.

Author: Kevin Chu (chuk1123)
License: MIT
"""

import os
import random

import discord
from discord.ext import commands
from discord.ui import Select, View
from discord.commands import Option

# Configure bot intents - we need members intent for role_members command
intents = discord.Intents.default()
intents.members = True  # Required for accessing member information
bot = discord.Bot(intents=intents)

# List to store guild IDs where the bot is active
guild_ids = []

# Gerald's hunger level (3-8 range) - resets on bot restart
# TODO: Consider persisting this to a database for continuity
hunger_level = random.randint(3, 8)


def get_role_options(guild):
    """
    Generate a list of Discord SelectOptions for all roles in a guild.

    Args:
        guild (discord.Guild): The Discord guild to get roles from

    Returns:
        list[discord.SelectOption]: List of SelectOption objects for dropdown menu
    """
    roles = guild.roles
    options = []
    for r in roles:
        options.append(discord.SelectOption(
            label=str(r),
            value=str(r)
        ))
    return options


@bot.event
async def on_ready():
    """
    Event handler called when the bot successfully connects to Discord.
    Collects all guild IDs and logs connection status.
    """
    for guild in bot.guilds:
        guild_ids.append(guild.id)
    print('We have logged in!')
    print(f'Gerald is active in {len(guild_ids)} server(s)')


@bot.slash_command(description='say hi to Gerald')
async def hi(ctx, name=None):
    """
    Greet Gerald and get introduced to the sensational penguin!

    Args:
        ctx: Discord command context
        name (str, optional): Name to personalize the greeting
    """
    await ctx.respond('Hi, I am Gerald the sensational penguin!')
    if name != None:
        await ctx.respond(f'Hi {name}, I am Gerald the sensational penguin!')


@bot.slash_command(description='feed me my favorite food')
async def feed(ctx, food):
    """
    Feed Gerald his favorite foods and watch his hunger decrease.

    Favorite foods: fish, krill, squid, pizza
    Hunger level decreases by 1 with each successful feeding.

    Args:
        ctx: Discord command context
        food (str): The food item to feed Gerald
    """
    global hunger_level
    food = food.lower()
    favorite_food = ["fish", "krill", "squid", "pizza"]

    # Check if Gerald is already full
    if hunger_level <= 0:
        await ctx.respond("I am full!")
        return

    # Check if the food is something Gerald likes
    if food in favorite_food:
        hunger_level -= 1
        await ctx.respond(f"I ate {food}! \nHunger Level: {hunger_level}")
    else:
        await ctx.respond("I don't want to eat that!")


@bot.slash_command(description='hee hee hee haa')
async def laugh(ctx):
    """
    Gerald's signature laugh with custom emoji.

    Args:
        ctx: Discord command context
    """
    await ctx.respond('hee hee hee haa\n' + "<:heheheha:981746390805913670>")


@bot.slash_command(description='basketball')
async def afishy(ctx):
    """
    Gerald shares his love for basketball (in Spanish!).

    Args:
        ctx: Discord command context
    """
    await ctx.respond('El baloncesto es el mejor deporte!')


@bot.slash_command(description='Gerald talks')
async def talk(ctx):
    """
    Have a conversation with Gerald. His responses vary and are influenced by hunger.

    When hunger_level > 3, Gerald may express hunger or ask to eat you!

    Args:
        ctx: Discord command context
    """
    messages = [
        'You are phenomenal!',
        'You are absolutely sensational!',
        'Get good.',
        "I am a penguin.",
        '\ (•◡•) /'
    ]

    # Add hunger-related messages if Gerald is hungry
    if hunger_level > 3:
        messages.extend(["I'm hungry.", "Can I eat you?"])

    message = random.choice(messages)
    await ctx.respond(message)


@bot.slash_command(description='how hungry I am')
async def show_hunger_level(ctx):
    """
    Display Gerald's current hunger level.

    Args:
        ctx: Discord command context
    """
    await ctx.respond(f"Hunger Level: {str(hunger_level)}")


@bot.slash_command(description='list members of role')
async def role_members(ctx):
    """
    Interactive command to list all members with a specific role.

    Presents a dropdown menu with all server roles. When a role is selected,
    displays all members who have that role (showing nicknames if available).

    Args:
        ctx: Discord command context
    """
    guild = bot.get_guild(ctx.guild.id)
    select = Select(placeholder='Choose a role', options=get_role_options(guild))

    async def select_callback(interaction):
        """
        Callback function when user selects a role from dropdown.

        Args:
            interaction: Discord interaction object from the select menu
        """
        role = discord.utils.get(guild.roles, name=select.values[0])
        members = role.members
        member_list = []

        # Build list of member names (prefer nickname over username)
        for mem in members:
            if mem.nick == None:
                member_list.append(str(mem.name))
            else:
                member_list.append(str(mem.nick))

        await interaction.response.send_message(
            f'{role}:\n' + "\n".join(member for member in member_list)
        )

    select.callback = select_callback
    view = View(timeout=10)  # 10 second timeout for interaction
    view.add_item(select)
    await ctx.respond("Choose a role!", view=view)


@bot.slash_command(name='greet', description='Greet someone!')
async def greet(ctx, name=''):
    """
    Simple greeting command.

    Args:
        ctx: Discord command context
        name (str, optional): Name to greet. If empty, sends generic greeting.
    """
    if name == '':
        await ctx.respond('Hey!')
    else:
        await ctx.respond(f'Hello {name}!')


# Get Discord bot token from environment variable
TOKEN = os.environ.get("TOKEN")

# Security warning: Remove this in production!
# TODO: Remove token logging - security risk
print("BOT TOKEN:", TOKEN)

# Start the bot
bot.run(TOKEN)
