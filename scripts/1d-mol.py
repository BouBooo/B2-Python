#!/usr/bin/python3.6





import random as rd

nombreTire = rd.randint(0, 100)

nombreTape = 0
nombreEssais = 0

def message():
     return print("A la prochaine ! - La solution était ",nombreTire)

while nombreTape != nombreTire:
	print('Tapez un nombre:')
	nombreEssais += 1
	nombreTape = int(input())
	if nombreTape > nombreTire:
		print('Trop grand')
	elif nombreTape < nombreTire:
		print('Trop petit')
	else:
		print('C\'est gagne, le nombre etait ' + str(nombreTire) + ' trouve en ' + str(nombreEssais) + ' coups')
		message()
