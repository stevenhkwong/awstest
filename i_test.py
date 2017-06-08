#!/usr/bin/python

import boto.ec2
import os
import sys, getopt

debug = 0
default_key = 'XXXXX'
default_secret = 'XXXXX'
path = "/var/www/html/" 
files = [path + "i_destroy.py",   path + "index.php" , path + "i_start.py", path + "i_status.py"  , path + "i_test.py" ]
argv = None

def usage():
	print 'i_test.py [-h -l] [-r -l] -k key -s secret'
	print '  -h - this help'

def testaws():
	try:
		regions = boto.ec2.regions()
	except Exception, e:
		print "failed to get regions!!\n"
		sys.exit(2)
	#
	if regions == None:
		print "no regions!!\n"
		sys.exit(2)

	print "Available regions:"
	for r in regions:
		print "  - %s" % (r)

def testfiles():
	print "Files:"
	for file in files:
		if not os.path.exists(file):
			sys.exit(2)
		print "  - %s ok" % (file)
			
		
testaws()
testfiles()




