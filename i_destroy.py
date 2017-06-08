#!/usr/bin/python

import boto.ec2
import os
import sys, getopt

TAG = 'awstest'
debug = 0
all = False
theinstance = None
default_key = 'XXXXX'
default_secret = 'XXXXX'
argv = None

#try:
#	regions = boto.ec2.regions()
#except Exception, e:
#	print "failed to get regions!!\n"
#	sys.exit(2)
#
#if regions == None:
#	print "no regions!!\n"
#	sys.exit(2)
#
#print "Available regions:"
#for r in regions:
#	print "  - %s" % (r)
#
#

def usage():
	print 'i_destroy.py [-a] -k key -s secret'
	print '   -a - terminate all running instances'
	print '   -i instance-id - terminate instance instance-id '

try:
#	opts, args = getopt.getopt(argv,"hqk:s:",["key=","secret="])
	opts, args = getopt.getopt(sys.argv[1:],"hai:k:s:",["instance=", "key=","secret="])
except getopt.GetoptError:
	usage()
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		usage()
		sys.exit()
	elif opt in ("-a"):
		all = True
	elif opt in ("-i", "--instance"):
		theinstance = arg
	elif opt in ("-k", "--key"):
		default_key = arg
	elif opt in ("-s", "--secret"):
		default_secret = arg

if debug == 1:
	print "qty: " + str(qty) + " key: " + default_key + " secret: " + default_secret

try:
  conn = boto.ec2.connect_to_region("ap-southeast-2", aws_access_key_id=default_key, aws_secret_access_key=default_secret)
except Exception, e:
	print "failed: " + e
	sys.exit(2)

if conn == None:
	print "invalid connection!!\n"
	sys.exit(2)

if debug == 1:
	regions = conn.get_all_regions()
	for r in regions:
		print "  - %s" % (r)


reservations = conn.get_all_reservations()


for r in reservations:
	if debug == 1:
		print "reservation id: %s" % (r.id)
		print "ec2 instances: "
	for instance in r.instances:
		tag = ''
		if debug == 1:
			print "\tid - %s" % (instance.id)
			print "\tip - %s" % (instance.ip_address)
			print "\tstate - %s" % (instance.state)
		if instance.tags.has_key('name'):
			tag = instance.tags['name']
		if tag == TAG:
			if all == True or theinstance == instance.id:
				print "terminating - %s" % (instance.id)
				conn.terminate_instances(instance.id)


