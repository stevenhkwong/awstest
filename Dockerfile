FROM centos7:v1

MAINTAINER Steven HK Wong version: 0.1

RUN yum clean all && echo "Container started: `date`" >> /tmp/run.log

ADD index.php /var/www/html/
ADD i_start.py /var/www/html/
ADD i_destroy.py /var/www/html/
ADD i_status.py /var/www/html/

EXPOSE 80

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
