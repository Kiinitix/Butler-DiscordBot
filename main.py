#bot for discord server.......

import discord
import os
import sys
import requests
from dotenv import load_dotenv
import random
from key_alive import keep_alive

load_dotenv()

client= discord.Client() #instance of a client
@client.event  #registering event
async def on_ready():   #when the bot is ready to be used
  print('We have logged in as {0.user}'.format(client))


#if the bot receives a message
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if 'happy birthday' in message.content.lower():
    for i in range(0,10
    ):
        await message.channel.send('Happy Birthday! 🎈🎉')
  superhero=['Ant-Man', 'Aquaman', 'Asterix', 'The Atom', 'The Avengers', 'Batgirl', 'Batman', 'Black Canary', 'Black Panther', 'Captain America', 'Daredevil', 'The Defenders', 'Doc Davage', 'Ghost Rider', 'Green Arrow', 'Green Lantern', 'Hawkeye','Hellboy', 'Hulk', 'Iron Fist', 'Iron Man', 'Robin', 'The Shadow', 'Spider-Man', 'Super Man', 'Thor', 'Wolverine','x-Men']
  name=random.choice(superhero)
  if message.content.startswith('$butler'):
    await message.channel.send('Hello %s'%name)
  if message.content in ['love you butler', 'Love you butler']:
    await message.channel.send('Love you too boss!')
  a=["I am a human from the future",'Bingpot!',"Cool. Cool cool cool cool cool cool cool",'no doubt no doubt no doubt no doubt.']
  if message.content == '99!':
    response = random.choice(a)
    await message.channel.send(response)
  elif message.content == 'raise-exception':
    raise discord.DiscordException
  

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

keep_alive()
client.run(os.environ['TOKEN'])




