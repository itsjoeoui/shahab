import discord
from discord.ext import commands
from chessdotcom import get_player_profile as gpp
from chessdotcom import is_player_online as ipo

class Stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chess(self, ctx, *, args):
        data = gpp(args).json
        description = f"""
        **Username:** {data['username']}
        **Player ID:** {data['player_id']}
        **Followers:** {data['followers']}
        **Country:** {data['country'].split('/')[-1]}
        **Status:** {data['status']}
        **Is Online:** {ipo(args).json['online']}
        [View this profile on chess.com]({data['url']})
        """
        embed = discord.Embed(
            title = data['name'],
            color = discord.Color.green(),
            description = description
        )
        embed.set_thumbnail(url=data['avatar'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Stats(bot))
