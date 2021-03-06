#!/usr/bin/python3.6


#3b-opt.py
#Script précédent mais ajout d'options de lancement 
#NICOLAS Florent / XIMENES Clément
#11/11/2018


# Import des modules
import shutil
from shutil import make_archive
import signal
import gzip
import os
import sys
import argparse


#Func

def createArchive():
	make_archive(nom_archive, 'gztar', chemin_dep)

def moveArchive():
	shutil.move(nom_archive + '.tar.gz', chemin_arr)

def deleteArchive():
	os.remove('/root/data/backup.tar.gz')
	os.remove('/root/backup.tar.gz')

def chooseFolder():
        ap = argparse.ArgumentParser()
        ap.add_argument("-l", "--link", help="Entrez le lien du dossier que vous voulez sauvegarder")
        args = ap.parse_args()
        if args.link:
                return args.link
        else:
                return '/root/B2-Python/scripts/'


chemin_arr = os.path.expanduser('/root/data/')
chemin_dep = os.path.expanduser(chooseFolder())
nom_archive = os.path.expanduser('/root/backup')






# Verif du droit d'écriture sur le fichier
if os.access(chemin_arr, os.W_OK):
	#Création archive
	createArchive()
	
	if os.path.exists(chemin_arr + 'backup.tar.gz'):
		#Dezip des backup et lecture 
		with gzip.open(chemin_arr + '/backup.tar.gz', 'rb') as f:
			old_backup = f.read()
		with gzip.open(nom_archive + '.tar.gz', 'rb') as f:
                	new_backup = f.read()

		# On compare les deux save
		if old_backup != new_backup:
		# On supprime l'ancienne et on sauvegarde la nouvelle
			deleteArchive()
			sys.stdout.write('Votre ancienne sauvegarde étant différent de la nouvelle, a bien été supprimée et remplacée par la nouvelle.\n')
		else:
			sys.stderr.write('Une sauvegarde similaire existe déjà \n')
			userDelete = input('Voulez vous supprimer cette sauvegarde? (yes/no) \n')
                	#L'user veut remplacer l'ancienne
                	#Suppression de l'ancienne
			if userDelete == 'yes':
				deleteArchive()
				userCreate = input('Voulez vous créer une nouvelle sauvegarde? (yes/no) \n')
                        	#Création de la nouvelle sauvegarde
				if userCreate == 'yes':
					createArchive()
					moveArchive()
					sys.stdout.write('Une nouvelle archive a été créée, dans le repertoire : ' + chemin_arr + '. \n')
                        	#L'ancienne est supprimée mais l'user n'en effectue pas de nouvelle. (chelou)
				elif userCreate == 'no':
					sys.stdout.write('Quel interêt de supprimer l\'ancienne dans ce cas...\n')
                        	#Saisie incorrecte
				else:
					sys.stderr.write('Une erreur est survenue durant la création de la sauvegarde. \n')
                	#L'user ne souhaite pas remplacer la sauvegarder existante
			elif userDelete == 'no':
				sys.stdout.write('Votre ancienne sauvegarde n\'a pas été supprimée.\n')
                	#Erreur de saisie
			else:
				sys.stderr.write('Une erreur de saisie a été détectée.\n')

	else:
		moveArchive()
		sys.stdout.write('Votre archive a bien été déplacée dans le répertoire: ' + chemin_arr + '. \n') 
else:
	sys.stderr.write('Vous n\'avez pas les droits nécessaire\n')
	
