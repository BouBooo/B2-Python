#!/usr/bin/python3.6
#1b-dic.py
#XIMENES CLEMENT/NICOLAS FLORENT
#User stock des prenoms dans liste + trier par ordre alphabétique
#16/10/2018

#Regex
import re
pattern = re.compile('^[a-zA-Z]*$')

#Incrementation
liste = []
user = ''

#Boucle qui enregistre les saisies de prénoms
user = input('Veuillez insérer un nom (q pour quitter): ')
while user != 'q' :
	if pattern.match(user):
		liste.append(user)
		liste.sort()
		user = input('Veuillez insérer un nom (q pour quitter): ')
	else: 
		print("Veuillez n'insérer que des lettres pour le prénom")
print(liste)



