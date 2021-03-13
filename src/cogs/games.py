import random
from discord.ext import commands


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, *, side=6):
        """Rolls a D6 by default. However, you can specify any number of sides by saying "/roll 69" for example."""
        chance = random.randint(1, 100)
        if chance <= 20:
            await ctx.send("Never gonna give you up, never gonna let you down...")
        else:
            await ctx.send(random.randint(1, side))

    @roll.error
    async def roll_error(self, ctx, error):
        if error:
            await ctx.send("Bad argument! Please enter a positive integer! (default=6)")


def setup(bot):
    bot.add_cog(Games(bot))
