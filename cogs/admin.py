from discord.ext import commands
import discord
import datetime
from settings._global import MOD_ROLE_NAME

def mods_or_owner():
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(MOD_ROLE_NAME))
    return commands.check(predicate)

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @mods_or_owner()
    async def foo(self, ctx):
        await ctx.send("A")

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx):
        guild = ctx.guild
        num_voice_channels = len(guild.voice_channels)
        num_text_channels = len(guild.text_channels)
        embed = discord.Embed(description="Server Status", color=discord.Color.blue())
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="# Voice Channels", value=num_voice_channels)
        embed.add_field(name="# Text Channels", value=num_text_channels)
        embed.set_footer(text=datetime.datetime.now()) 
        embed.set_author(name=self.bot.user.name)
        embed.add_field(name="Custom Emoji", value=guild.emojis[0] or "", inline=False)
        embed.set_image(url="https://i1.sndcdn.com/artworks-doULutRNuGLb4ou0-71NpIA-t500x500.jpg")
        embed.add_field(name="AFK Channel", value=guild.afk_channel)
        
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))