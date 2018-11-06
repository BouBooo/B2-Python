#!/usr/bin/python3.6



# Import des modules
import signal
import shutil
from shutil import make_archive
import gzip
import os
import sys


chemin_arr = os.path.expanduser('/root/data/')
chemin_dep = os.path.expanduser('/root/B2-Python/scripts/')
nom_archive = os.path.expanduser('/root/backup')

try:
	os.path.exists(chemin_arr + '/backup.tar.gz')
	make_archive(nom_archive, 'gztar', chemin_dep)
	shutil.move(nom_archive + '.tar.gz', chemin_arr)
except OSError:
	sys.stderr.write('Le fichier existe déjà')
	raise
