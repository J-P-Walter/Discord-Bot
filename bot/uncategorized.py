from discord.ext import commands
import discord

@commands.command()
async def games(ctx, *game_name: str):
    games_count = len(game_name)
    bot = ctx.bot
    if games_count == 0:
        embed = discord.Embed(title="Our games")
        for command in bot.get_cog("Games").get_commands():
            embed.add_field(name=command.name, value=command.help, inline=False)
    elif games_count == 1:
        game = game_name[0]
        all_commands = bot.get_cog("Games").get_commands()
        chosen_command = None
        for command in all_commands:
            if game == command.name:
                chosen_command = command
                break
        embed = discord.Embed(title=chosen_command.name, description=chosen_command.help)

        game_char_length = len(game)
        for c in bot.get_cog("Games").walk_commands():
            command_string = str(c)
            if game == command_string[:game_char_length] and len(command_string) > game_char_length:
                embed.add_field(name=c.name, value=c.help, inline=False)

        
    else:
        await ctx.send("Choose one gaame")

    await ctx.send(embed=embed)