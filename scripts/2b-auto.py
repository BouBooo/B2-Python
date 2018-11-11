#!/usr/bin/python3.6
#1a-add.py
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
randomNum = int(random.randint(0, 10))

#Fonction si CTRL + C
def quitGame(sig, frame):
        writefile('Au revoir! La solution était {0}'.format(randomNum))
        exit()

#Fonction écriture dans fichier
def writefile(msg):
        file = open("gamefileV2.txt", "w")
        file.write(msg)
        file.close()

#Fonction lecture fichier
def readfile():
        file = open("gamefileV2.txt", "r")
        msg = file.readline().strip()
        file.close
        return msg

signal.signal(signal.SIGINT, quitGame)



# Fonction qui fait tourner le jeu
def MoreOrLess(EndLoop, GuessMin, GuessMax):
        while(EndLoop is False):
                BotInput = random.randint(GuessMin,GuessMax)
                writefile(str(BotInput))
                userInput = readfile()
                if(pattern.match(userInput)):
                        userInput = int(userInput)

                        if(userInput > randomNum):
                                GuessMax = int(userInput)
                                writefile('Vous avez proposé {0}, c\'est moins'.format(userInput))

                        elif(userInput < randomNum):
                                GuessMin = int(userInput)
                                writefile('Vous avez proposé {0}, c\'est plus'.format(userInput))
                        else:
                                writefile('Felicitations\nLa solution etait '+str(randomNum)+'\nSalut !\n')



EndLoop = False
GuessMin = 0
GuessMax = 10
BotInput = random.randint(GuessMin, GuessMax)

MoreOrLess(EndLoop, GuessMin, GuessMax)

