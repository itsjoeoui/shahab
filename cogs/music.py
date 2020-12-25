from __future__ import unicode_literals
import discord
from discord.ext import commands
import youtube_dl

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, url):
        channel = await ctx.author.voice.channel.connect()

        ydl_opts = {
            'outtmpl': 'cache/music.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        channel.play(discord.FFmpegPCMAudio('cache/music.mp3'))
    
    @commands.command()
    async def pause(self, ctx):
        pass

    @commands.command()
    async def resume(self, ctx):
        pass 

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(client):
    client.add_cog(Music(client))
