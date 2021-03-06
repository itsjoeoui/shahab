import os
from datetime import datetime as dt
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('shotguns /help'))
    bot.load_extension('cogs.admin')
    bot.load_extension('cogs.music')
    bot.load_extension('cogs.others')
    print('We have logged in as {0.user}'.format(bot))

    @tasks.loop(minutes=10)
    async def update_countdown():
        dayleft = (dt(2021, 6, 3) - dt.now()).days+1
        channel = bot.get_channel(817116049325424700)
        await channel.edit(name=f"Semester Count: {dayleft}")

    update_countdown.start()

@bot.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
        return

    if message.content.lower() == 'bruh':
        await message.channel.send('bruh')

    if message.channel.id == 817549986857746492:
        await message.delete()
        await message.channel.send(message.content)

    await bot.process_commands(message)

bot.run(TOKEN)
