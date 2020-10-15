import os
import discord
from dotenv import load_dotenv
from modules import address
from modules import wolfram
from modules import solve
from modules import status

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    wordlist = message.content.split()
    keyword = ' '.join(wordlist[1:]) 

    if "bruh" in message.content.lower():
        await message.channel.send('Bruh')

    if "/address" == wordlist[0]:
        await message.channel.send(address.get_full_address(keyword))

    if "/wolfram" == wordlist[0]:
        await message.channel.send(f'Searching "{keyword}" on WolframAlpha...')
        wolfram.get_full_result(keyword)
        await message.channel.send(file=discord.File('cache/wolfram_result.jpg', f'{keyword}.jpg'))
        
    if "/solve" == wordlist[0]:
        await message.channel.send(solve.get_short_result(keyword))

    if "/status" == wordlist[0]:
        if status.get_status(keyword) == True:
            await message.channel.send(f'"{keyword}" is currently up!')
        else:
            await message.channel.send(f'"{keyword}" is down or invalid :(') 

client.run(TOKEN)
