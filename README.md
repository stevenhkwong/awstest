# awstest
Manage AWS EC2 instances with Boto
Dockerfile provides an instance of web service on apache/php 

	# unittest - docker run swong/stevenhkwong_awstest  unittest

	# i_start.py - launch EC2 instances
		             i_start.py [-h] -q number of instances -k aws_keyid -s aws_key_secret

	# i_destroy.py - terminates EC2 instances
		             i_destroy.py [-h -a] -i instance -k aws_keyid -s aws_key_secret

	# i_status.py - show status of EC2 instances
		             i_status.py [-h] -k aws_keyid -s aws_key_secret


