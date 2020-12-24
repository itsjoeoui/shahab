import random
import discord
from discord.ext import commands
from cogs.utils import geocoding
from cogs.utils import wolframalpha

class Others(commands.Cog):

    RUN_STRINGS = (
        "Where do you think you're going?",
        "Huh? what? did they get away?",
        "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
        "Get back here!",
        "Not so fast...",
        "Look out for the wall!",
        "Don't leave me alone with them!!",
        "You run, you die.",
        "Jokes on you, I'm everywhere",
        "You're gonna regret that...",
        "You could also try /kickme, I hear that's fun.",
        "Go bother someone else, no-one here cares.",
        "You can run, but you can't hide.",
        "Is that all you've got?",
        "I'm behind you...",
        "You've got company!",
        "We can do this the easy way, or the hard way.",
        "You just don't get it, do you?",
        "Yeah, you better run!",
        "Please, remind me how much I care?",
        "I'd run faster if I were you.",
        "That's definitely the droid we're looking for.",
        "May the odds be ever in your favour.",
        "Famous last words.",
        "And they disappeared forever, never to be seen again.",
        "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person",
        "Yeah yeah, just tap /kickme already.",
        "Here, take this ring and head to Mordor while you're at it.",
        "Legend has it, they're still running...",
        "Unlike Harry Potter, your parents can't protect you from me.",
        "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
        "be the next Vader.",
        "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
        "Legend has it, they're still running.",
        "Keep it up, not sure we want you here anyway.",
        "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
        "NO RUNNING IN THE HALLWAYS!",
        "Hasta la vista, baby.",
        "Who let the dogs out?",
        "It's funny, because no one cares.",
        "Ah, what a waste. I liked that one.",
        "Frankly, my dear, I don't give a damn.",
        "My milkshake brings all the boys to yard... So run faster!",
        "You can't HANDLE the truth!",
        "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
        "Hey, look at them! They're running from the inevitable banhammer... Cute.",
        "Han shot first. So will I.",
        "What are you running after, a white rabbit?",
        "As The Doctor would say... RUN!",
    )

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def runs(self, ctx):
        await ctx.send(random.choice(self.RUN_STRINGS))

    @commands.command()
    async def address(self, ctx, *, args):
        await ctx.send(geocoding.get_full_address(args))

    @commands.command()
    async def wolfram(self, ctx, *, args):
        await ctx.send(f'Searching {args} on WolframAlpha...')
        wolframalpha.get_full_result(args)
        await ctx.send(file=discord.File('cache/wolfram_result.jpg', f'{args}.jpg'))

    @commands.command()
    async def solve(self, ctx, *, args):
        result = wolframalpha.get_short_result(args)
        await ctx.send(wolframalpha.get_short_result(args))
        if result == 'No short answer available':
            await ctx.send('Retrieving a long answer...')
            wolframalpha.get_full_result(args)
            await ctx.send(file=discord.File('cache/wolfram_result.jpg', f'{args}.jpg'))

    @commands.command()
    async def say(self, ctx, *, args):
        await ctx.send(args)

    @commands.command()
    async def source(self, ctx):
        await ctx.send('GitHub: https://github.com/itsjoeoui/discord')

def setup(client):
    client.add_cog(Others(client))
