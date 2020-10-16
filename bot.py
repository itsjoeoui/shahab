import os
import discord
from dotenv import load_dotenv
from modules import geocoding
from modules import wolframalpha
from modules import webstatus
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def address(ctx, *args):
    keyword = ' '.join(args) 
    await ctx.send(geocoding.get_full_address(keyword))

@bot.command()
async def wolfram(ctx, *args):
    keyword = ' '.join(args) 
    await ctx.send(f'Searching {keyword} on WolframAlpha...')
    wolframalpha.get_full_result(keyword)
    await ctx.send(file=discord.File('cache/wolfram_result.jpg', f'{keyword}.jpg'))

@bot.command()
async def solve(ctx, *args):
    keyword = ' '.join(args) 
    result = wolframalpha.get_short_result(keyword)
    await ctx.send(wolframalpha.get_short_result(keyword))
    if result == 'No short answer available':
        await ctx.send('Retrieving a long answer...')
        wolframalpha.get_full_result(keyword)
        await ctx.send(file=discord.File('cache/wolfram_result.jpg', f'{keyword}.jpg'))

@bot.command()
async def status(ctx, *args):
    keyword = ' '.join(args) 
    if webstatus.get_status(keyword):
        await ctx.send(f'{keyword} is currently up!')
    else:
        await ctx.send(f'{keyword} is down or invalid :(')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "bruh" in message.content.lower():
        await message.channel.send('Bruh')

    await bot.process_commands(message)

bot.run(TOKEN)
