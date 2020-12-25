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
        vc = ctx.voice_client
        if not vc or not vc.is_playing():
            return await ctx.send("I am not currently playing anything!")
        elif vc.is_paused():
            return
        vc.pause()
        await ctx.send(f'{ctx.author}: Paused the song!')

    @commands.command()
    async def resume(self, ctx):
        vc = ctx.voice_client
        if not vc or not vc.is_connected():
            return await ctx.send("I am not currently playing anything!")
        elif not vc.is_paused():
            return
        vc.resume()
        await ctx.send(f'{ctx.author}: Resumed the song!')

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(client):
    client.add_cog(Music(client))
