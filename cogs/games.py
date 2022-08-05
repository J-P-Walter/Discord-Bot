from discord.ext import commands
from rps.parser import RockPaperScissorParser
from rps.model import RPS
from rps.controller import RPSGame

word = 'discord'
user_guesses = list()

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Play a game of Rock, Paper, Scissors",
    usage = "rock / paper / scissors")
    async def rps(self, ctx, user_choice: RockPaperScissorParser = RockPaperScissorParser(RPS.ROCK)):
        """
        Play a game of Rock, Paper, Scissors
        """
        game_instance = RPSGame()
        user_choice = user_choice.choice

        won, bot_choice = game_instance.run(user_choice)
        if won is None:
            message = "It's a tie!"
        elif won is True:
            message = "You won! %s vs %s" %(user_choice, bot_choice)
        else:
            message = "You lost! %s vs %s" %(user_choice, bot_choice)

        await ctx.send(message)




def setup(bot):
    bot.add_cog(Games(bot))