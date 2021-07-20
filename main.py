#We're no strangers to love
#You know the rules and so do I
#A full commitment's what I'm thinking of
#You wouldn't get this from any other guy
import discord
import os
import sys
import requests
from dotenv import load_dotenv
import random
from key_alive import keep_alive

load_dotenv()
#  just wanna tell you how I'm feeling
# Gotta make you understand
# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# Never gonna make you cry
# Never gonna say goodbye
# Never gonna tell a lie and hurt you

client= discord.Client() #instance of a client
@client.event  #registering event
async def on_ready():   #when the bot is ready to be used
  print('We have logged in as {0.user}'.format(client))
#   We've known each other for so long
# Your heart's been aching but you're too shy to say it
# Inside we both know what's been going on
# We know the game and we're gonna play it
# And if you ask me how I'm feeling
# Don't tell me you're too blind to see


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
  
# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# Never gonna make you cry
# Never gonna say goodbye
# Never gonna tell a lie and hurt you
# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# Never gonna make you cry
# Never gonna say goodbye
# Never gonna tell a lie and hurt you
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
# Never gonna give, never gonna give
# (Give you up)
# We've known each other for so long
# Your heart's been aching but you're too shy to say it
# Inside we both know what's been going on
# We know the game and we're gonna play it
# I just wanna tell you how I'm feeling
# Gotta make you understand
# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# Never gonna make you cry
# Never gonna say goodbye
# Never gonna tell a lie and hurt you
keep_alive()
client.run(os.environ['TOKEN'])

# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# Never gonna make you cry
# Never gonna say goodbye
# Never gonna tell a lie and hurt you
# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# Never gonna make you cry
# Never gonna say goodbye




