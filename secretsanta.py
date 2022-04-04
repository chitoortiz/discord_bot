import discord
import os
import random
from randomise import *

client = discord.Client()

idPerson1 = ******************
idPerson2 = ******************

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('#who'): 
        if message.author.id == idPerson1:
            await message.author.send(Person1)
        if message.author.id == idPerson2:
            await message.author.send(Person2)


client.run(token)
