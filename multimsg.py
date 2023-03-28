import os
import discord
from replit import db

async def multimsg(message, client):
  msg = message.content
  o_chan = message.channel
  params = msg.split()

  if len(params) == 1:
    await o_chan.send("**$multimsg add [id]** pour ajouter un salon dans la liste\n**$multimsg remove [id]** pour supprimer un salon dans la liste\n**$multimsg list** pour afficher la liste des salons liés\n**$multimsg send [message]** pour envoyer un message aux salons liés\n**$multimsg purge** pour réinitialiser la liste")
    return
  
  if params[1] == "add":
    if len(params) != 3:
      await o_chan.send("Tu dois saisir un (et un seul) ID de channel")
      return

    g_chan = client.get_channel(int(params[2]))
    if g_chan == None:
      await o_chan.send("Aucun channel n'a pu être trouvé pour cet id")
    else:
      await o_chan.send("Channel trouvé. Nom : " + g_chan.name)
      if "chan_list" in db.keys():
        new_list = db["chan_list"]
        for n in new_list:
          if g_chan.id == n:
            await o_chan.send("Cet id est déjà enregistré dans la database")
            return
        new_list.append(g_chan.id)
        db["chan_list"] = new_list
        await o_chan.send("ID ajouté dans la database")
      else:
        new_list = [g_chan.id]
        db["chan_list"] = new_list
        await o_chan.send("ID ajouté dans la database")
    return

  if params[1] == "remove":
    if "chan_list" not in db.keys():
      await o_chan.send("La liste n'est pas initialisée")
      return

    if len(params) != 3:
      await o_chan.send("Tu dois saisir un (et un seul) ID de channel")
      return

    new_list = db["chan_list"]
    for n in new_list:
      if n == int(params[2]):
        g_chan = client.get_channel(n)
        await o_chan.send("ID trouvé. Nom du salon : " + g_chan.name)
        new_list.remove(g_chan.id)
        await o_chan.send("ID supprimé de la liste")
        return
    await o_chan.send("Cet ID n'a pas été enregistré dans la liste")
    return

  if params[1] == "list":
    if "chan_list" not in db.keys():
      await o_chan.send("La liste n'est pas initialisée")
      return
    await o_chan.send("Voici la liste des ID et leurs channels associés :")
    counter = 0
    new_list = db["chan_list"]
    for n in new_list:
      g_chan = client.get_channel(n)
      await o_chan.send(str(g_chan.id) + " => #" + g_chan.name)
      counter += 1
    if counter == 0:
      await o_chan.send("Il n'y a aucun ID d'enregistré dans la liste")
    return
  
  if params[1] == "send":
    if len(params) < 3:
      await o_chan.send("Vous devez saisir un message")
      return
    del params[:2]
    new_list = db["chan_list"]
    for n in new_list:
      g_chan = client.get_channel(n)
      await g_chan.send(" ".join(params))
    return

  if params[1] == "purge":
    if "chan_list" not in db.keys():
      await o_chan.send("La liste n'est pas initialisée")
      return
    del db["chan_list"]
    await o_chan.send("Liste purgée")
    return