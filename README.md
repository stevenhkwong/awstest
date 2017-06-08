# awstest
Manage AWS EC2 instances with Boto
Dockerfile provides an instance of web service on apache/php  
Available on dockerhub as swong/awstest:master


	# unittest - docker run swong/awstest:master  unittest

	# web application - docker run -d 80:80 swong/awstest:master

	# i_start.py - launch EC2 instances
		             i_start.py [-h] -q number of instances -k aws_keyid -s aws_key_secret

	# i_destroy.py - terminates EC2 instances
		             i_destroy.py [-h -a] -i instance -k aws_keyid -s aws_key_secret

	# i_status.py - show status of EC2 instances
		             i_status.py [-h] -k aws_keyid -s aws_key_secret


