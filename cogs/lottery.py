from discord.ext import commands
from lottery.controller import LotteryController
import configparser

class Lottery(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        config = configparser.ConfigParser()
        config.read('tokens.cfg')
        id = config.get('WEBHOOK', 'id')
        if int(id) == message.author.id and message.channel.id == 1006251363799400519:
            dc = LotteryController()
            dc.save(message.content)

    @commands.group()
    async def lottery(self, ctx):
        ctx.lottery_con = LotteryController()
        pass

    @lottery.command(name="last")
    async def lottery_last(self, ctx):
        pass

    @lottery.command(name="next")
    async def lottery_next(self, ctx):
        pass

    @lottery.command(name="join")
    async def lottery_join(self, ctx, *numbers: int):
        pass
def setup(bot):
    bot.add_cog(Lottery(bot))