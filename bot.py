########################################
############# DISCORD BOT ##############
########################################

# imported necessary packages

import os
import pprint
import random
import discord
from dotenv import load_dotenv
from grabber import *
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')

# Event listeners for the bot


@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="Sample Embed", url="https://searx.be/",
                          description="This is an embed that will show how to build an embed and the different components", color=discord.Color.orange())
    await ctx.send(embed=embed)

@bot.command()
async def newspaper(ctx):
    news = grabber(links, subtext)
    response = random.choice(news)
    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

async def on_message(message):
    if 'coffee' in message.content.lower():
        await message.channel.send('buy it yourself')
    if message.author == bot.user:
        return

    news = [grabber(links, subtext)]

    if message.content == 'newspaper':
        response = random.choice(news)
        await message.channel.send(response)

bot.run('OTkwNjU3Mjk4ODA2NDkzMjA1.GvqcL5.FxjxncvPhkICmYuCwmF4BvwlVr_muTTaNy57hc')
