from discord.ext import commands
from lottery.controller import LotteryController
import configparser
import discord

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
            numbers = [int(x) for x in message.content.split(',')]
            dc.save(numbers)

    @commands.group()
    async def lottery(self, ctx):
        ctx.lottery_con = LotteryController()
        pass

    @lottery.command(name="last")
    async def lottery_last(self, ctx):
        last_drawing = ctx.lottery_con.get_last_drawing()
        await ctx.send("Last Drawing: %s" %last_drawing.numbers_as_string())

    @lottery.command(name="next")
    async def lottery_next(self, ctx):
        c = self.bot.get_command("lottery tickets costs")
        await ctx.invoke(c)

    @lottery.group(name="tickets")
    async def lottery_tickets(self, ctx):
        pass

    @lottery_tickets.command(name="list")
    @commands.dm_only()
    async def lottery_tickets_list(self, ctx):
        embed = discord.Embed()
        for t in ctx.lottery_con.get_my_drawings(ctx.author):
            embed.add_field(name="Ticket", value=t.numbers_as_string())
        await ctx.send(embed=embed)
        

    @lottery_tickets.command(name="costs")
    async def lottery_tickets_cost(self, ctx):
        await ctx.send("Costs 5")

    @lottery.command(name="join")
    @commands.dm_only()
    async def lottery_join(self, ctx, *numbers: int):
        if len(numbers) != 6:
                await ctx.send("Need 6 numbers")
        duplicates = False
        oob = False

        for n in numbers:
            if numbers.count(n) > 1:
                duplicates = True
            if n > 49 or n < 1:
                oob = True
        
        if duplicates:
            await ctx.send("Need 6 unique numbers")
        if oob:
            await ctx.send("Need 6 numbers between 1 and 49")

        ctx.lottery_con.save(sorted(numbers), ctx.author)
        await ctx.send("You've entered the lottery")




def setup(bot):
    bot.add_cog(Lottery(bot))