"""
Feature Extraction
Transforms wav files into .mfc files

References: https://github.com/syhw/timit_tools
"""

import os, util, sys
from subprocess import call

USAGE = """
Usage:
	python feature_extraction.py [$dataset_folder] [--debug]

Example:
	python feature_extraction.py dataset/train
"""

MFC_EXTENSION = '.mfc'

def print_debug(debug, string):
	if debug:
		print string

def process(folder, debug):
	# run through all the folders and files in the path "folder"
	codetrscp_content = ''
	trainscp_content = ''
	for bdir, _, files in os.walk(folder):
		for fname in files:
			if fname[-4:] != '.wav':
				continue
			wav_fname = bdir + '/' + fname
			mfcc_fname = bdir + '/' + fname[:-4] + MFC_EXTENSION
			codetrscp_content += wav_fname + ' ' + mfcc_fname + '\n'
			trainscp_content += mfcc_fname + '\n'
			util.print_debug(debug, "Dealt with file '"+ wav_fname + "'")
	
	# listing all .wav for mfcc extraction process
	f = open('files/codetr.scp','w')
	f.write(str(codetrscp_content))
	f.close()

	# listing all .mfc for modelling process
	f = open('files/train.scp','w')
	f.write(str(trainscp_content))
	f.close()

	call(['HCopy', '-C', 'config/conf-extraction', '-S', 'files/codetr.scp'])


if len(sys.argv) > 1:
	debug = False

	if '--help' in sys.argv:
		print util.GROUP_NAME
		print USAGE
		sys.exit(0)
	if '--debug' in sys.argv:
		debug = True

	l = filter(lambda x: not '--' in x[0:2], sys.argv)
	folder_name = '.'
	if len(l) > 1:
		folder_name = l[1]
	process(folder_name, debug)
	print "Feature extraction completed for folder '" + folder_name + "'"
else:
	print 'Add --help for help'