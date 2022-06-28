import discord
from discord.ext import commands

class general(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['speed','connection'])
    async def ping(self, ctx):
        print("Ponged !")
        await ctx.send(f":eyes: Ping = {round(self.bot.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(general(bot))