import os
import random
import discord
from dotenv import load_dotenv
from modules import geocoding
from modules import wolframalpha
from modules import webstatus
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='/')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# TDL: Move all commands below into cogs
@client.command()
async def address(ctx, *, args):
    await ctx.send(geocoding.get_full_address(args))

@client.command()
async def wolfram(ctx, *, args):
    await ctx.send(f'Searching {args} on WolframAlpha...')
    wolframalpha.get_full_result(args)
    await ctx.send(file=discord.File('cache/wolfram_result.jpg', f'{args}.jpg'))

@client.command()
async def solve(ctx, *, args):
    result = wolframalpha.get_short_result(args)
    await ctx.send(wolframalpha.get_short_result(args))
    if result == 'No short answer available':
        await ctx.send('Retrieving a long answer...')
        wolframalpha.get_full_result(args)
        await ctx.send(file=discord.File('cache/wolfram_result.jpg', f'{args}.jpg'))

@client.command()
async def say(ctx, *, args):
    await ctx.send(args)

@client.command()
async def source(ctx):
    await ctx.send('GitHub: https://github.com/itsjoeoui/discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "bruh" in message.content.lower():
        await message.channel.send('Bruh')

    await client.process_commands(message)

client.run(TOKEN)
