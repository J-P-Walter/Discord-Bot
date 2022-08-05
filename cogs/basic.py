from discord.ext import commands
from TextToOwO.owo import text_to_owo
import discord
from util import notify_user

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Please check with !help for the usage of this " 
            "command or talk to your admin")

    @commands.command(brief="P O N G")
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.command(brief="Converts text to 'owo' text")
    async def owo(self, ctx, *, message):
        await ctx.send(text_to_owo(message))

    @commands.command(brief="Creates invite link")
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max=1)
        await ctx.send(link)

    @commands.command()
    async def poke(self, ctx, member : discord.Member = None):
        if member is not None:
            message = "%s poked you!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("User @ to poke someone")

def setup(bot):
    bot.add_cog(Basic(bot))