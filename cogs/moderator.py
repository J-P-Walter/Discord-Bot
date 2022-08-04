from discord.ext import commands
import discord
from settings._global import MOD_ROLE_NAME

def mods_or_owner():
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(MOD_ROLE_NAME))
    return commands.check(predicate)

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Kicks member")
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, reason: str = "Gottem"):
        if member is not None:
            await ctx.guild.kick(member, reason)
        else:      
            await ctx.send("Error: mention user by @")

    @commands.command(brief="Bans member")
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, reason: str = "Gottem"):
        if member is not None:
            await ctx.guild.ban(member, reason)
        else:      
            await ctx.send("Error: mention user by @")

    @commands.command(brief="Bans member")
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: str="", reason: str = "whoops"):
        if member == "":
            await ctx.send("Error: mention user by text")
            return
        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:     
                await ctx.guild.unban(b.user.name, reason)
                await ctx.send("User unbanned")
                return
        await ctx.send("User not found in ban list")
def setup(bot):
    bot.add_cog(Moderator(bot))