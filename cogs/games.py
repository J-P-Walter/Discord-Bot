from discord.ext import commands
import discord

from rps.parser import RockPaperScissorParser
from rps.model import RPS
from rps.controller import RPSGame

from hangman.controller import HangmanGame

from gaw.controller import GuessAWordGame

hangman_games = {}
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

    @commands.command(brief="Play a game of hangman")
    @commands.dm_only()
    async def hm(self, ctx, guess: str):
        player_id = ctx.author.id
        hangman_instance = HangmanGame()
        game_over, won = hangman_instance.run(player_id, guess)

        if game_over:
            game_over_message = "You did not win"
            if won:
                game_over_message = "You won"

            hangman_instance.reset(player_id)
            await ctx.send(game_over_message)
            await ctx.send("The word was %s" %hangman_instance.get_secret_word())
            
        else:
            await ctx.send("Progress: %s" %hangman_instance.get_progress_string())
            await ctx.send("Guesses so far %s" %hangman_instance.get_guess_string())  

    @commands.group()
    async def gaw(self, ctx):
        ctx.gaw_game = GuessAWordGame()

    @gaw.command(name="start")
    async def start(self, ctx, *members: discord.Member):
        players = list()
        for m in members:
            players.append(m)
        channel = await ctx.gaw_game.start_game(ctx.guild, ctx.author, players)
        if channel is None:
            await ctx.send("You already have a game, please close it first")
        else:
            game = ctx.gaw_game.fetch_game()
            await ctx.send("Have fun!")
            await channel.send("The category is %s with a word length of %s" %(game.category, len(game.word)))



    @gaw.command(name="guess")
    async def guess(self, ctx, guess: str):
        channel_id = ctx.channel.id
        result, hint = ctx.gaw_game.guess(channel_id, guess)
        if result is None:
            await ctx.send("Not allowed in this channel")
        elif result is True:
            await ctx.send("You won!")
        elif result is False and hint != "":
            await ctx.send("Guess was close")

def setup(bot):
    bot.add_cog(Games(bot))