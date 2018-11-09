#!/usr/bin/python3.6


#3a-save.py
#Effectuer une sauvegarde compressée et archivée dans un repertoire spécifique
#09/11/2018
#NICOLAS Florent / XIMENES Clément 


# Import des modules
import shutil
from shutil import make_archive
#import signal
import gzip
import os
import sys
import datetime


# Fonction si CTRL + C
# def quitProg(sig, frame):
# 	print('\nEt on quitte ça proprement svp!')
#       exit()
# signal.signal(signal.SIGINT, quitProg)


chemin_arr = os.path.expanduser('/root/data/')
chemin_dep = os.path.expanduser('/root/B2-Python/scripts/')
nom_archive = os.path.expanduser('/root/backup')


def createArchive():
	make_archive(nom_archive, 'gztar', chemin_dep)
	shutil.move(nom_archive + '.tar.gz', chemin_arr)
	sys.stdout.write('Une archive a bien été crée. Elle se trouve dans' + chemin_arr + '. \n')


def deleteArchive():
	os.remove('/root/data/backup.tar.gz')
	os.remove('/root/backup.tar.gz')
	sys.stdout.write('Votre ancienne sauvegarde a bien été supprimée.\n')


# Verif du droit d'écriture sur le fichier
if os.access(chemin_arr, os.W_OK):
	#Création archive	
	try:
		createArchive()
	#Une sauvegarde du meme existe déjà
	except:
		sys.stderr.write('Une sauvegarde du même nom existe déjà \n')
		userDelete = input('Voulez vous supprimer cette sauvegarde? (yes/no) \n')
		#L'user veut remplacer l'ancienne
		#Suppression de l'ancienne
		if userDelete == 'yes':
			deleteArchive()
			userCreate = input('Voulez vous créer une nouvelle sauvegarde? (yes/no) \n')
			#Création de la nouvelle sauvegarde
			if userCreate == 'yes':
				createArchive()
			#L'ancienne est supprimée mais l'user n'en effectue pas de nouvelle. (chelou)
			elif userCreate == 'no':
				sys.stdout.write('Quel interêt de supprimer l\'ancienne dans ce cas...\n')
			#Saisie incorrecte
			else:
				sys.stderr('Une erreur est survenue durant la création de la sauvegarde. \n')
		#L'user ne souhaite pas remplacer la sauvegarder existante
		elif userDelete == 'no':
			sys.stdout.write('Votre ancienne sauvegarde n\'a pas été supprimée.\n')
		#Erreur de saisie
		else:
			sys.stderr.write('Une erreur de saisie a été détectée.\n')			
else:
	sys.stderr.write('Vous n\'avez pas les droits nécessaire\n')
	

# except OSError:
# 	sys.stderr.write('Le fichier existe déjà')
# 	raise
