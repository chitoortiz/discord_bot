import discord
import os
import random
from randomise import *

client = discord.Client()

idNacho = 264423375542157312
idSofía = 881858600929198110

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('#quien'): 
        if message.author.id == idNacho:
            await message.author.send(Nacho)
        if message.author.id == idSofía:
            await message.author.send(Sofía)


client.run('ODU3MTgxNDM1NjI2Mzg5NTQ1.YNL2aw.V_adMHoTEeqXImxEg5vmfSF9vjE')