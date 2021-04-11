import discord
from discord.ext import commands
import requests
from cogs.utils import openweather


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
        embed = discord.Embed(title=data["name"],
                              color=discord.Color.green(),
                              description=description)
        embed.set_thumbnail(url=data["avatar"])
        await ctx.send(embed=embed)

    @commands.command()
    async def weather(self, ctx, *, args="Montreal"):
        """Shows the weather. Montreal by default."""
        data = openweather.get_weather(args)

        if data["cod"] == "404":
            description = "**City not found!**"
            embed = discord.Embed(title=args,
                                  color=discord.Color.red(),
                                  description=description)
        else:
            title = f"""
            **City:** {data['name']} ({data['weather'][0]['main']}) 
            """
            description = f"""
            **Temp:** {data['main']['temp']} °C
            **Feels like:** {data['main']['feels_like']} °C
            **Min temp:** {data['main']['temp_min']} °C
            **Max temp:** {data['main']['temp_max']} °C
            """
            embed = discord.Embed(title=title,
                                  color=discord.Color.green(),
                                  description=description)
            url = (
                f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
            )
            embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Stats(bot))
