#!/usr/bin/python3.6
#1d-mol.py
#XIMENES CLEMENT/NICOLAS FLORENT
#Jeu du plus ou moins
#23/10/2018

#Import des modules
import re
import random
import signal
from time import sleep

#Regex
pattern = re.compile('^([0-9]|10)$')

#Generation d'un nombre random
randomNum = int(random.randint(0,10))

#Fonction d'au revoir + solution
def message() :
	return print('Au revoir! La solution était {0}'.format(randomNum))

#Fonction si CTRL + C	
def quitGame(sig, frame):
	print('\nEt on quitte ça proprement svp!')
	exit()

signal.signal(signal.SIGINT, quitGame)
coup = 0

#Boucle plus ou moins
userNum = input('Insérez un nombre entre 0 et 10  : ' )
while userNum != 'q' :
	coup += 1
	if pattern.match(userNum) :
		if int(userNum) < randomNum :
			print('Trop petit')
			userNum = input('Insérez un nombre entre 0 et 10 :')
		elif int(userNum) > randomNum :
			print('Trop grand')
			userNum = input('Insérez un nombre entre 0 et 10 :')
		else:
			print('Vous avez gagné en {0} coups'.format(coup))
			break
	else:
		print("Erreur! Veuillez n'insérer qu'un nombre entre 1 et 10")
		userNum = input('Insérez un nombre entre 0 et 10 :')
message()
