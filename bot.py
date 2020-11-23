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
    await bot.change_presence(activity=discord.Game('my Tesla /help'))
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    name, discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@bot.command()
async def address(ctx, *, args):
    await ctx.send(geocoding.get_full_address(args))

@bot.command()
async def wolfram(ctx, *, args):
    await ctx.send(f'Searching {args} on WolframAlpha...')
    wolframalpha.get_full_result(args)
    await ctx.send(file=discord.File('cache/wolfram_result.jpg', f'{args}.jpg'))

@bot.command()
async def solve(ctx, *, args):
    result = wolframalpha.get_short_result(args)
    await ctx.send(wolframalpha.get_short_result(args))
    if result == 'No short answer available':
        await ctx.send('Retrieving a long answer...')
        wolframalpha.get_full_result(args)
        await ctx.send(file=discord.File('cache/wolfram_result.jpg', f'{args}.jpg'))

@bot.command()
async def status(ctx, *, args):
    if webstatus.get_status(args):
        await ctx.send(f'{args} is currently up!')
    else:
        await ctx.send(f'{args} is down or invalid :(')

@bot.command()
async def say(ctx, *, args):
    await ctx.send(args)

@bot.command()
async def source(ctx):
    await ctx.send('GitHub: https://github.com/itsjoeoui/discord')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "bruh" in message.content.lower():
        await message.channel.send('Bruh')

    await bot.process_commands(message)

bot.run(TOKEN)
