import discord
from discord.ext import commands
import requests


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chess(self, ctx, *, args):
        """Displays your chess.com stats."""
        serviceurl = "https://api.chess.com/pub/player/"
        r = requests.get(serviceurl + args)
        data = r.json()
        description = f"""
        **Username:** {data['username']}
        **Player ID:** {data['player_id']}
        **Followers:** {data['followers']}
        **Country:** {data['country'].split('/')[-1]}
        **Status:** {data['status']}
        [View this profile on chess.com]({data['url']})
        """
        embed = discord.Embed(
            title=data["name"], color=discord.Color.green(), description=description
        )
        embed.set_thumbnail(url=data["avatar"])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Stats(bot))
