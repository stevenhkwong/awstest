#!/usr/bin/python

import boto.ec2
import os
import sys, getopt

TAG = 'awstest'

debug = 0
default_key = 'XXXX'
default_secret = 'XXXX'
qty=0

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
	print 'i_start.py [-h] -q number_of_instances -k key -s secret'
	print '  -h - this help'
	


try:
#	opts, args = getopt.getopt(argv,"hqk:s:",["key=","secret="])
	opts, args = getopt.getopt(sys.argv[1:],"hq:k:s:",["key=","secret="])
except getopt.GetoptError:
	usage()
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		usage()
		sys.exit()
	elif opt in ("-q"):
		qty = int(arg)
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

min_count = 1
max_count = qty

reservation = conn.run_instances(
    'ami-162c2575', 
		key_name='acentos.pem',
    instance_type='t2.micro',
		min_count = min_count,
		max_count = max_count
)

print "reservation id: %s" % (reservation.id)

for instance in reservation.instances:
	print "id - %s" % (instance.id)
	print "ip - %s" % (instance.ip_address)
	instance.add_tag('name', TAG)


