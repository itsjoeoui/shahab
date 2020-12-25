import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import ctypes
import ctypes.util

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='/')

discord.opus.load_opus(ctypes.util.find_library('opus'))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "bruh" in message.content.lower():
        await message.channel.send('Bruh')

    await client.process_commands(message)

client.run(TOKEN)
