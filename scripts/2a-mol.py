#!/usr/bin/python3.6

#2a-mol.py
#Plus ou moins
#NICOLAS Florent / XIMENES Clément
#28/10.2018

# Import
import random
import re
import signal


# Fonction write
def write(msg):
    file = open("plusoumoins.txt", "w")
    file.write(msg)
    file.close()


# Fonction read
def read():
    file = open("plusoumoins.txt", "r")
    msg = file.readline().strip()
    file.close()
    return msg


# Fonction qui quitte le prog si on CTRL+C
def end_game(sig, frame):
    write('Et on quitte ça proprement svp! ')
    exit()

signal.signal(signal.SIGINT, end_game)


# Var
win = False
nbrRand = random.randint(0,10)

write('Veuillez choisir un nombre entre 0 et 10: ')

# Jeu
while win is False:
    # On regarde la saisie dans le fichier
    nbrSaisi = read()
    # On check que ce soit un int
    if re.match("^([0-9]|10)$", nbrSaisi):
        nbrSaisi = int(nbrSaisi)
        # Et qu'il ne soit pas au dessus de 10
        if nbrSaisi < 0 or nbrSaisi > 10:
            write('Entrez un nombre entre 0 et 10 ! : ')
            continue
        elif nbrSaisi > nbrRand:
            write('Trop grand ')
        elif nbrSaisi < nbrRand:
            write('Trop petit ')
        # Sinon win
        else:
            write('Tu as trouvé le nombre.')
            win = True
            exit()
