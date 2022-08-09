from discord.ext import commands
import random

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Flips a coin")
    async def coin(self, ctx):
        num = random.randint(0,1)
        await ctx.send("Heads" if num == 1 else "Tails")
    
    @commands.command(brief="Rolls a d6")
    async def roll(self, ctx):
        num = random.randrange(1, 7)
        await ctx.send(num)



def setup(bot):
    bot.add_cog(Gamble(bot))