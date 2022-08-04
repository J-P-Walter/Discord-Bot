from discord.ext import commands
import aiohttp
import discord
import configparser
import praw
import random
from settings._global import REDDIT_ENABLED_SUBREDDITS, REDDIT_ENABLED_NSFW_SUBREDDITS

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        config = configparser.ConfigParser()
        config.read('tokens.cfg')
        reddit_id = config.get('REDDIT', 'reddit_id')
        reddit_secret = config.get('REDDIT', 'reddit_secret')
        self.reddit = praw.Reddit(client_id=reddit_id, client_secret=reddit_secret, user_agent="MyDiscordBot:%s:1.0" %reddit_id)
        

    @commands.command(breif="Random picture of a cat")
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow")
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat/")

                    await ctx.send(embed=embed)
    
    @commands.command(brief="Random picture of a dog")
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Woof")
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="http://random.dog/")

                    await ctx.send(embed=embed)

    @commands.command(brief="Random image from Reddit")
    async def random(self, ctx, subreddit: str = ""):
        async with ctx.channel.typing():
            if self.reddit:
                nsfw_flag = False
                chosen_subreddit = REDDIT_ENABLED_SUBREDDITS[0]
                if subreddit:
                    if subreddit in REDDIT_ENABLED_SUBREDDITS:
                       chosen_subreddit = subreddit
                    elif subreddit in REDDIT_ENABLED_NSFW_SUBREDDITS:
                        chosen_subreddit = subreddit
                        nsfw_flag = True
                    else:
                        await ctx.send("Please choose subreddit of the following list: %s " 
                        "NSFW: %s" %(", ".join(REDDIT_ENABLED_SUBREDDITS),", (".join(REDDIT_ENABLED_NSFW_SUBREDDITS)))
                        return
                    
                if nsfw_flag:
                    if not ctx.channel.is_nsfw():
                        await ctx.send("NSFW not allowed in this channel")
                        return 
                submissions = self.reddit.subreddit(chosen_subreddit).hot()
                post_to_pick = random.randint(1,10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)
                
            else:
                await ctx.sent("Not working")



def setup(bot):
    bot.add_cog(Images(bot))