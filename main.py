import os
import discord
import random
import multimsg
from whisper import whisper
from timestamp import timebetween
from keepalive import keepalive
from hangman import hangman

client = discord.Client(activity=discord.Game(name='regarder le peuple m\'utiliser'))

@client.event
async def on_ready():
  print('Logged as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hangman'):
    await message.channel.send(hangman(message))

  if message.content.startswith('$timebetween'):
    await message.channel.send(await timebetween(message))
  
  if message.content.startswith('$whisper'):
    await whisper(message, client);
  
  if message.content.startswith('$multimsg'):
    await multimsg.multimsg(message, client);

keepalive()
client.run(os.environ['TOKEN'])