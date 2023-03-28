import os
import discord
from discord import NotFound

async def whisper(message, client):
  sender = message.author
  channel = message.channel
  #w_chan = client.get_channel(904449461856657488)
  msg = message.content.split()
  if message.mentions:
    mentions = message.mentions
    await message.delete()
  else:
    await message.delete()
    await sender.send("Erreur : tu dois ping une personne à whisper")
    return

  if len(mentions) > 1:
    await sender.send("Erreur : tu ne peux whisper qu'une seule personne à la fois")
    return

  receiver = mentions[0];
  msg = message.content.split()
  del msg[:2]
  await receiver.send("**" + sender.name + "**" + " t'a whisper, voici son message : \n\"" + " ".join(msg) + "\"")
  await channel.send("**" + sender.name + "** a envoyé un whisper à **" + receiver.name + "**")
  #await w_chan.send("**" + sender.name + "** a envoyé un whisper à **" + receiver.name + "**, voici le message :\n\"" + " ".join(msg) + "\"")
  return