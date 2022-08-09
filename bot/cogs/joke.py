from tkinter.messagebox import QUESTION
from discord.ext import commands
import discord
import json 
import os
from settings._global import *
import random


async def get_joke():
    with open(os.path.join(DATA_DIR, 'jokes.json')) as joke_file:
        jokes = json.load(joke_file)
        joke = random.choice(list(jokes))

        setup = joke['question']
        punchline = joke['answer']
    joke_file.close()
    return setup, punchline

class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Tells a joke")
    async def joke(self, ctx):
        setup, punchline = await get_joke()
        await ctx.send(setup)
        await ctx.send(punchline)

def setup(bot):
    bot.add_cog(Joke(bot))