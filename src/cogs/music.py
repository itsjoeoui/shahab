import wavelink
import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        # Initiate our nodes. For this example we will use one server.
        # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
        await self.bot.wavelink.initiate_node(host='0.0.0.0',
                                              port=2333,
                                              rest_uri='http://127.0.0.1:2333',
                                              password='youshallnotpass',
                                              identifier='TEST',
                                              region='us_east')

    @commands.command(name='connect')
    async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except AttributeError:
                embed = discord.Embed(color=discord.Color.red())
                embed.title = 'Please join a voice channel!'
                await ctx.send(embed=embed)                
                raise discord.DiscordException('No channel to join. Please either specify a valid channel or join one.')
        
        embed = discord.Embed(color=discord.Color.blue())
        embed.title = f'Connecting to **`{channel.name}`**'

        player = self.bot.wavelink.get_player(ctx.guild.id)
        await ctx.send(embed=embed)
        await player.connect(channel.id)

    @commands.command(name='disconnect', aliases=['bye'])
    async def _disconnect(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)

        if not player.is_connected:
            embed = discord.Embed(color=discord.Color.red())
            embed.title = 'I am not connected to any voice channel...'
        else:
            embed = discord.Embed(color=discord.Color.blue())
            embed.title = 'Bye~ \U0001F44B'

        await ctx.send(embed=embed)
        await player.disconnect()

    @commands.command()
    async def play(self, ctx, *, query: str):
        tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{query}')

        if not tracks:
            embed = discord.Embed(color=discord.Color.red())
            embed.title = 'Could not find any songs with that query :('
            return await ctx.send(embed=embed)

        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_connected:
            await ctx.invoke(self.connect_)

        if not player.is_playing:
            embed = discord.Embed(color=discord.Color.green())
            embed.title = 'Track Queued \U0001f44c'
            embed.description = str(tracks[0])

            await ctx.send(embed=embed)        
            await player.play(tracks[0])

def setup(bot):
    bot.add_cog(Music(bot))
