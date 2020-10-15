import os
import discord
from dotenv import load_dotenv
from modules import geocoding

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

    if "bruh" in message.content.lower():
        await message.channel.send('Bruh')

    if "/address" == wordlist[0]:
        await message.channel.send(geocoding.get_full_address(" ".join(wordlist[1:])))

client.run(TOKEN)
