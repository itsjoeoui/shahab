import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('my Tesla /help'))
    bot.load_extension('cogs.admin')
    bot.load_extension('cogs.music')
    bot.load_extension('cogs.others')
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
        return

    if message.content.lower() == 'bruh':
        await message.channel.send('bruh')

    await bot.process_commands(message)

bot.run(TOKEN)
