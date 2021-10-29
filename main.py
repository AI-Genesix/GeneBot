import os
import discord
import random
from timestamp import timebetween
from keepalive import keepalive
from hangman import hangman

client = discord.Client(activity=discord.Game(name='regarder le peuple m\'utiliser'))

monster = ["Vampire", "Zombie", "Araignée", "Sorcière", "Faucheuse", "Momie", "Chauve-souris", "Rat", "Crapaud", "Tueur à gages", "Fantôme", "Basilic", "Loup-garou", "Croque-mitaine", "Démon", "Cyclope", "Détraqueur", "Goule", "Gargouille"]

adjective = ["abominable", "effrayant.e", "vorace", "espiègle", "farceur.se", "démoniaque", "velu.e", "hydropique", "taquin.e", "abject.e", "répulsif.ve", "assoiffé.e", "meurtrier.ère"]

@client.event
async def on_ready():
  print('Logged as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$rollname'):
      await message.channel.send("**{}**, ton nouveau pseudo est : ".format(message.author.name) + "**" + random.choice(monster) + " " + random.choice(adjective) + "**")

  if message.content.startswith('$hangman'):
    await message.channel.send(hangman(message))

  if message.content.startswith('$timebetween'):
    await message.channel.send(await timebetween(message))

keepalive()
client.run(os.environ['TOKEN'])