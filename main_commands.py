from discord.ext import commands
import configparser

bot = commands.Bot(command_prefix='!')

#Frameword
@commands.command()
async def ping(ctx):
    await ctx.send("Pong")

@commands.command(description="Provide arguments", brief="Repeats message")
async def hello(ctx, *args):
    if len(args) > 0:
        await ctx.send(" ".join(args))
    else:
        await ctx.send("Error: please refer to !help")




bot.add_command(ping)
bot.add_command(hello)

config = configparser.ConfigParser()
config.read('token.cfg')
token = config.get('TOKEN', 'token')
bot.run(token)