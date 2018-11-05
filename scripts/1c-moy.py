#!/usr/bin/python3.6
#1c-moy.py
#XIMENES CLEMENT/NICOLAS FLORENT
#Demander une saisie utilisateur de plusieurs notes et prénoms + moyenne et top 5
#16/10/2018

#module pour trouver les 5 meilleurs notes
import heapq
#heapq.nlargest(10,my_dictionary.values())
 
#regex
import re
patternUser = re.compile('^[a-zA-Z]*$')
patternNote = re.compile('^[0-9]*$')

#incrementation
user=''
note=''
moyenne=0
somme=0


dict = {}

#boucle pour enregistrer les prénoms/notes
user = input('Insérez un prénom (q pour quitter): ')
while user != 'q' :
	if patternUser.match(user):
		note = input('Insérez une note : ')
		if patternNote.match(note):
			dict[user] = float(note)
			user = input('Insérez un prénom (q pour quitter): ')
		else:
			print("Veuillez insérer une note")
	else:
		print("Veuillez n'insérer que des lettres")
		user = input('Insérez un prénom (q pour quitter): ')

#calcul de la moyenne	
for notes in dict:
	somme = somme + float(dict[notes])
	moyenne = somme / len(dict)

#on cherche les 5 meilleurs notes
highest =  heapq.nlargest(5,dict.values())

print('La moyenne des notes est de {0} et les 5 meilleurs notes sont {1}'.format(moyenne, highest))	
         
	
