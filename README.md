# awstest
Manage AWS EC2 instances with Boto
Dockerfile provides an instance of web service on apache/php  
Available on dockerhub as swong/awstest:master


	# unittest - docker run swong/awstest:master  unittest

	# web application - from docker.io: docker run -d 80:80 swong/awstest
											from codefresh.io: http://cf-aue1-docker-node-0037.cf-cd.com:32825/index.php

	# i_start.py - launch EC2 instances
		             i_start.py [-h] -q number of instances -k aws_keyid -s aws_key_secret

	# i_destroy.py - terminates EC2 instances
		             i_destroy.py [-h -a] -i instance -k aws_keyid -s aws_key_secret

	# i_status.py - show status of EC2 instances
		             i_status.py [-h] -k aws_keyid -s aws_key_secret


