#!/usr/bin/python3.6



# Import des modules
import signal
import shutil
from shutil import make_archive
import gzip
import os
import sys
import datetime

chemin_arr = os.path.expanduser('/root/data/')
chemin_dep = os.path.expanduser('/root/B2-Python/scripts/')
nom_archive = os.path.expanduser('/root/backup')


#Verif des droits sur le fichier
if os.access(chemin_arr, os.W_OK and os.R_OK):
	#Création archive	
	try:
		make_archive(nom_archive, 'gztar', chemin_dep)	
		shutil.move(nom_archive + '.tar.gz', chemin_arr)
		sys.stdout.write('Une archive a bien été crée. Elle se trouve dans' + chemin_arr + '. \n')
	except:
		sys.stderr.write('Une sauvegarde du même nom existe déjà \n')
	
else:
	sys.stderr.write('Vous n\'avez pas les droits nécessaire')


#except OSError:
#	sys.stderr.write('Le fichier existe déjà')
#	raise
