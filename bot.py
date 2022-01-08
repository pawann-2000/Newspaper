import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event 
async def on_message(message):
    if 'ping' in message.content.lower():
        await message.channel.send('Ping successful')
    if 'Hi' in message.content():
        await message.channel.send('Hello')
    if 'coffee' in message.content.lower():
        await message.channel.send('buy it yourself')

client.run('TOKEN')

