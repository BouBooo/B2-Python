#!/usr/bin/python3.6


#2a-mol.py
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

#Fonction si CTRL + C
def quitGame(sig, frame):
	writefile('Au revoir! La solution était {0}'.format(randomNum))
	exit()

#Fonction écriture dans fichier
def writefile(msg):
        file = open("gamefile.txt", "w")
        file.write(msg)
        file.close()

#Fonction lecture fichier
def readfile():
        file = open("gamefile.txt", "r")
        msg = file.readline().strip()
        file.close
        return msg

signal.signal(signal.SIGINT, quitGame)



# Fonction qui fait tourner le jeu
def MoreOrLess(EndLoop):
    while(EndLoop is False):
        userInput = readfile()

        if(pattern.match(userInput)):
            userInput = int(userInput)

            if(userInput > randomNum):
                writefile("C'est moins")

            elif(userInput < randomNum):
                writefile("C'est plus")
            else:
                writefile('Felicitation\nLa solution etait '+str(randomNum)+'\nAu revoir !')
                finBoucle = True


EndLoop = False

writefile('Bonjour, veuillez entrer un nombre entre O et 10 : ')
MoreOrLess(EndLoop)

