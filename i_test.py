#!/usr/bin/python

import boto.ec2
import os
import sys, getopt

debug = 0
qty = 0
line_mode = False
running_only = False
default_key = 'XXXXX'
default_secret = 'XXXXX'
argv = None

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




def usage():
  print 'i_test.py [-h -l] [-r -l] -k key -s secret'
  print '  -h - this help'
