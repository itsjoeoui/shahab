import os
from datetime import datetime as dt
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from pretty_help import PrettyHelp

load_dotenv()
TOKEN = os.getenv("DISCORD")

bot = commands.Bot(command_prefix="/",
                   help_command=PrettyHelp(show_index=False))


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("shotguns /help"))

    bot.load_extension("cogs.admin")
    bot.load_extension("cogs.games")
    bot.load_extension("cogs.math")
    bot.load_extension("cogs.others")
    bot.load_extension("cogs.stats")

    print("We have logged in as {0.user}".format(bot))

    @tasks.loop(minutes=10)
    async def update_countdown():
        semcount = (dt(2022, 05, 13) - dt.now()).days + 1
        channel = bot.get_channel(879538356214722600)
        await channel.edit(name=f"Semester Count: {semcount}")

    update_countdown.start()


@bot.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
        return

    if message.content.lower() == "bruh":
        await message.channel.send("bruh")

    if not message.guild and not message.content.startswith("/"):
        channel = bot.get_channel(817549986857746492)
        try:
            await channel.send(message.attachments[0].url)
        finally:
            await channel.send(message.content)

    await bot.process_commands(message)


bot.run(TOKEN)
