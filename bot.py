########################################
############# DISCORD BOT ##############
########################################

# imported necessary packages

import os
import pprint
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')

# Event listeners for the bot
@bot.event
async def on_ready():
    print("Bot is ready.")
    print(f"Logged in as: {bot.user.name} ID: {bot.user.id}")
    print(f"Online in Guilds:")
    for server in bot.guilds:
        print(f"Guild name: {server.name}")
        print(f"Guild ID: {server.id}")

async def on_message(message):
    if 'coffee' in message.content.lower():
        await message.channel.send('buy it yourself')
    if message.author == bot.user:
        return

    news = [grabber(links, subtext)]

    if message.content == 'newspaper':
        response = random.choice(news)
        await message.channel.send(response)

@bot.command(name="load")
@commands.has_role("Newspaper Admin")
async def load(ctx, extension):
    if extension == "":
        await ctx.send("Please enter a valid cog.")
    try:
        bot.load_extension(extension)
        await ctx.send(f"Loaded {extension}!")
    except Exception as error:
        await ctx.send(f"Failed to load Cog {extension}. Reason: {error}")


@bot.command(name="unload")
@commands.has_role("Newspaper Admin")
async def unload(ctx, extension):
    if extension == "":
        await ctx.send("Please enter a valid cog.")
    try:
        bot.unload_extension(extension)
        await ctx.send(f"Unloaded {extension}!")
    except Exception as error:
        await ctx.send(f"Failed to unload Cog {extension}. Reason: {error}")


@bot.command(name="reload")
@commands.has_role("Newspaper Admin")
async def reload(ctx, extension):
    if extension == "":
        await ctx.send("Please enter a valid cog.")
    try:
        bot.unload_extension(extension)
        bot.load_extension(extension)
        await ctx.send(f"Reloaded {extension}!")
    except Exception as error:
        await ctx.send(f"Failed to reload Cog {extension}. Reason: {error}")


@bot.command(name="logout")
@commands.has_role("Newspaper Admin")
async def logout(ctx):
    await ctx.send("<a:jnl:856740626170904606> Logging Out")
    await bot.logout()

if __name__ == "__main__":
    extensions = {"news","general"}
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f"Loaded Cog {extension} successfully")
        except Exception as error:
            print(f"Failed to load Cog {extension}. Reason: {error}")

bot.run('TOKEN')
