from discord.ext import commands
import random

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        num = random.randrange(1, 101)
        await ctx.send(num)

def setup(bot):
    bot.add_cog(Gamble(bot))