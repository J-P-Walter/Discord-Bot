from discord.ext import commands
import configparser

bot = commands.Bot(command_prefix='!')

#Frameword
@commands.command()
async def ping(ctx):
    await ctx.send("Pong")
bot.add_command(ping)

config = configparser.ConfigParser()
config.read('token.cfg')
token = config.get('TOKEN', 'token')
bot.run(token)