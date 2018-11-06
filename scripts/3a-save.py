#!/usr/bin/python3.6



# Import des modules
import signal
import shutil
import gzip
import os
import sys
import subprocess



if os.access(path_data, os.W_OK and os.R_OK):
	#On crée l'archive
	shutil.make_archive(os.path.expanduser('/root/B2-Python/data/'), 'gztar', path_directory = os.path.expanduser('/root/B2-Python/scripts'))
