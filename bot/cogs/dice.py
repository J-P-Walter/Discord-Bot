from discord.ext import commands
import random

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="Rolls a d4")
    async def d4(self, ctx):
        num = random.randrange(1, 5)
        await ctx.send(num)

    @commands.command(brief="Rolls a d6")
    async def d6(self, ctx):
        num = random.randrange(1, 7)
        await ctx.send(num)

    @commands.command(brief="Rolls a d8")
    async def d8(self, ctx):
        num = random.randrange(1, 9)
        await ctx.send(num)

    @commands.command(brief="Rolls a d10")
    async def d10(self, ctx):
        num = random.randrange(1, 11)
        await ctx.send(num)

    @commands.command(brief="Rolls a d12")
    async def d12(self, ctx):
        num = random.randrange(1, 13)
        await ctx.send(num)

    @commands.command(brief="Rolls a d100")
    async def d100(self, ctx):
        num = random.randrange(1, 101)
        await ctx.send(num)


def setup(bot):
    bot.add_cog(Dice(bot))