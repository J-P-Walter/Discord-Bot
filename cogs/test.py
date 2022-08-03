from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *args):
        if len(args) > 0:
            await ctx.send(" ".join(args))
        else:
            await ctx.send("Error: please refer to !help")

def setup(bot):
    bot.add_cog(Test(bot))