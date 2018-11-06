#!/usr/bin/python3.6
#2a-mol.py
#XIMENES Clément / NICOLAS Florent
#Jeu du plus ou moins en démon
#25/10/2018


#Importation de modules
import random
import re
import signal


#Regex
pattern = re.compile('^([0-9]|10)$')

#Var
coup = 0
win = False

#Generation d'un nombre random
randomNum = int(random.randint(0,10))

#Fonction qui affiche la solution et au revoir
def message():
    return print('Au revoir! La solution était {0}'.format(randomNum))
    exit()

 #Ecrire dans un file
def write_in_file(msg):
  file = open("plusoumoins.txt", "w")
  file.write(msg)
  file.close()

#Lire dans un file
def read_in_file():
  file = open("plusoumoins.txt", "r")
  msg = file.readline().strip()
  file.close()
  return msg

#Fonction si CTRL + C
def quitGame(sig, frame):
        print('\nEt on quitte ça proprement svp!')
        exit()

signal.signal(signal.SIGINT, quitGame)


userNum = write_in_file('Insérez un nombre entre 0 et 10 : ' )


while win is False :
    userNum = read_in_file()
    if userNum == 10:
        break
    elif userNum > randomNum:
        write_in_file('Trop grand ')
    elif userNum < randomNum:
        write_in_file('Trop petit ')
    #Sinon on affiche win, on set le end en win
    else:
        write_in_file(message())
        end = True
