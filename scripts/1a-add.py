#!/usr/bin/python3.6
#1a-add.py
#XIMENES CLEMENT/NICOLAS FLORENT
#Demander 2 nombres et afficher la somme
#16/10/2018


import re
pattern = re.compile('^[0-9]*$')

#Saisie des deux nombres
num1 = input('Entrez le premier nombre: ')
num2 = input('Entrez le second nombre: ')
 
#Somme des deux nombres et on verifie si ce sont des nombres qui ont été insérés
if pattern.match(num1) and pattern.match(num2):
	sum = int(num1) + int(num2)
	print('La somme de {0} et de {1} est de {2}'.format(num1, num2, sum))
else:
	print('Insérez seulement des nombres')
	




