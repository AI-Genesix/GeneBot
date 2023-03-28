from replit import db
import os
import discord
import random
from hangman_list import wordlist

words_array = wordlist.split(',');


error_message = "ta commande est incorrecte\nUtilise **$hangman help** pour obtenir une liste de commandes."

help_message = "voici les commandes que tu peux utiliser avec **Hangman** :\n**$hangman help** : affiche la liste des commandes $hangman\n**$hangman start** : démarre une partie de Hangman rien que pour toi\n**$hangman [lettre]** : si tu as une partie en cours, joue un tour avec la lettre donnée"

###################################

def hangman(message):
  msg = message.content
  hangman_params = msg.split()
  hangman_message = "**{}**".format(message.author.name) + ', '

  if len(hangman_params) != 2:
    hangman_message += error_message 
    return hangman_message

  if hangman_params[1] == 'help':
    hangman_message += help_message
    return hangman_message

  if hangman_params[1] == 'start':
    hangman_message += hangman_start(message)
    return hangman_message
  
  if hangman_params[1] == 'remove':
    hangman_message += hangman_remove(message)
    return hangman_message
  
  return hangman_message + hangman_game(message)

###################################

def hangman_start(message):
  message_return = ''
  player_name = message.author.name;

  if player_name in db.keys():
    message_return += "tu as déjà une partie en cours. Utilise **$hangman [lettre]** pour jouer un coup."
    return message_return

  random_word = random.choice(words_array);
  random_word_hidden = []

  for i in range(len(random_word)):
    random_word_hidden.append('?')

  game = [random_word_hidden, random_word, 9]
  db[player_name] = game
  message_return = message_return + "ta partie a été créée\nVoici le mot caché : " + " ".join(random_word_hidden) + "\nIl te reste 9 essais"
  return message_return

###################################

def hangman_remove(message):
  player_name = message.author.name;
  if player_name in db.keys():
    del db[player_name]
    return "partie supprimée"
  return "pas de partie trouveée"

###################################

def hangman_game(message):
  player_name = message.author.name
  message_return = ''

  if player_name not in db.keys():
    return "tu n'as pas de partie en cours.\nUtilise **$hangman start** pour en débuter une."

  msg = message.content
  args = msg.split()

  if len(args[1]) != 1 or args[1].isalpha() == False:
    return "tu ne dois saisir qu'une seule lettre (et pas de chiffre)"

  current_game = db[player_name]
  current_hword = current_game[0]
  current_rword = list(current_game[1])
  current_lives = current_game[2]

  count = 0;
  valid = 0;
  for n in current_rword:
    if args[1].upper() == n:
      current_hword[count] = n
      valid += 1
    count += 1

  if valid == 0:
    current_lives -= 1
    message_return += "la lettre **" + args[1] + "** n'est pas dans ton mot caché\nIl te reste " + str(current_lives) + " vie(s)."
    if current_lives == 0:
        message_return += "\n\nTa partie est terminée. Tu peux en relancer une si tu le souhaites.\nTon mot caché était : **" + current_game[1] + "**."
        del db[player_name]
        return message_return

  else:
    message_return += "la lettre **" + args[1] + "** est dans ton mot caché\nVoici l'état de ton mot : " + " ".join(current_hword) + "\nIl te reste " + str(current_lives) + " vie(s)."

    end_game = 0;
    for n in current_hword:
      if n == '?':
        end_game += 1

    if end_game == 0:
      message_return += "\n\nBravo, tu as trouvé ton mot caché : **" + current_game[1] + "**.\nTa partie est terminée. Tu peux en relancer une si tu le souhaites."
      del db[player_name]
      return message_return

  current_game[0] = current_hword
  current_game[2] = current_lives
  db[player_name] = current_game

  return message_return


