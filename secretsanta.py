import discord
import os
import random
from randomise import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.id == "264423375542157312":
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODU3MTgxNDM1NjI2Mzg5NTQ1.YNL2aw.V_adMHoTEeqXImxEg5vmfSF9vjE')