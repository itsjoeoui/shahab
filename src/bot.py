import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

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

bot.run(TOKEN)
