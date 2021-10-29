import os
import discord
from discord import NotFound
from datetime import datetime

async def timebetween(message):
  msg = message.content;
  params = msg.split()

  if len(params) != 3:
    return "Utilisation : $timebetween [id1] [id2]"
  
  try:
    message_1 = await message.channel.fetch_message(params[1])
  except NotFound:
    return "L'ID du premier message est invalide"
  try:
    message_2 = await message.channel.fetch_message(params[2])
  except NotFound:
    return "L'ID du second message est invalide"
  time_1 = message_1.created_at
  time_2 = message_2.created_at
  delta = time_2 - time_1
  return "Temps entre les deux messages : " + str(delta)