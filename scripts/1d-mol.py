#!/usr/bin/python3.6
#1q-mol.py
#Jeu du plus ou moins
#NICOLAS Florent
#23/10/2018

#imports
import re
import signal
import random as rd
from time import sleep

#initialisatio
nombreTire = rd.randint(0, 100)
nombreTape = 0
nombreEssais = 0


def message():
     return print('A la prochaine ! - La solution était ',nombreTire)

def quitGame(sig, frame):
	print('Nice try, allez salut')
	exit()

signal.signal(signal.SIGINT, quitGame)

while nombreTape != 'q': 
	while nombreTape != nombreTire:
		print('Tapez un nombre (q pour quitter):')
		nombreEssais += 1
		nombreTape = input()

		if str(nombreTape) == 'q':
			message()
			exit()		

		if int(nombreTape) > nombreTire:
			print('Trop grand')
		elif int(nombreTape) < nombreTire:
			print('Trop petit')
		else:
			print('C\'est gagne, le nombre etait ' + str(nombreTire) + ' trouve en ' + str(nombreEssais) + ' coups')
			message()

