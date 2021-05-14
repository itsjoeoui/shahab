import discord
from discord.ext import commands
from cogs.utils import wolframalpha
import requests


class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wolfram(self, ctx, *args):
        """Searches on Wolfram|Alpha."""
        keyword = " ".join(args)
        wolframalpha.get_full_result(keyword)
        file = discord.File("cache/wolfram.jpg")
        embed = discord.Embed(color=discord.Color.red(), title=keyword)
        embed.set_image(url="attachment://wolfram.jpg")
        await ctx.send(file=file, embed=embed)

    @commands.command()
    async def solve(self, ctx, *args):
        """Shahab can solve everything!"""
        keyword = " ".join(args)
        result = wolframalpha.get_short_result(keyword)
        embed = discord.Embed(color=discord.Color.red(),
                              title=keyword,
                              description=result)
        await ctx.send(embed=embed)
        if result == "No short answer available":
            await ctx.send("Retrieving a long answer...")
            await self.wolfram(ctx, keyword)

    @commands.command()
    async def number(self, ctx, *, args):
        r = requests.get(f"http://numbersapi.com/{args}/math")
        if "<title>Error</title>" in r.text:
            await ctx.send("Invalid argument!")
        else:
            await ctx.send(r.text)


def setup(bot):
    bot.add_cog(Math(bot))
