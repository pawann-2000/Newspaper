import discord
from discord.ext import commands
from grabber import *
import random
from embed import *
class news(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['news'])
    async def newspaper(self,ctx):
        news = grabber(links, subtext)
        response = random.choice(news)
        e = embed(response['title'],response['link'])
        await ctx.send(embed=e.getEmbed())

def setup(bot):
    bot.add_cog(news(bot))
