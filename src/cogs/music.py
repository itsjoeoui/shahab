import discord
import wavelink
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.guild = bot.get_guild(754135767999185029)
        self.channel = bot.get_channel(819045649487626280)

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        # Initiate our nodes. For this example we will use one server.
        # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
        await self.bot.wavelink.initiate_node(host='127.0.0.1',
                                              port=2333,
                                              rest_uri='http://127.0.0.1:2333',
                                              password='youshallnotpass',
                                              identifier='TEST',
                                              region='us_central')

    @commands.command(name='connect')
    async def connect_(self, ctx):
        player = self.bot.wavelink.get_player(self.guild.id)
        await ctx.send(f'Connecting to **`{self.channel.name}`**')
        await player.connect(self.channel.id)

    @commands.command()
    async def play(self, ctx):
        query = "https://www.youtube.com/watch?v=DWcJFNfaw9c"

        tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{query}')
        
        if not tracks:
            return await ctx.send('Could not find any songs with that query.')

        player = self.bot.wavelink.get_player(self.guild.id)
        if not player.is_connected:
            await ctx.invoke(self.connect_)

        await ctx.send(f'Added {str(tracks[0])} to the queue.')
        await player.play(tracks[0])

def setup(bot):
    bot.add_cog(Music(bot))
