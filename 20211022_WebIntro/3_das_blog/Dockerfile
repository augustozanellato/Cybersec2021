FROM socialgeek/basewebimage

MAINTAINER Zane Durkin <zane@zemptech.com>

RUN \
    export MYSQL_PASS=$(openssl rand -hex 100) && \
    echo $MYSQL_PASS > /root/pass_root && \
    export MYSQL_PASS=$(openssl rand -hex 100) && \
    echo $MYSQL_PASS > /root/pass_web

COPY other/db.sql /root/db.sql

RUN \
    sed -i 's/<password_web>/'$(cat /root/pass_web)'/g' /root/db.sql && \
    sed -i 's/<password_root>/'$(cat /root/pass_root)'/g' /root/db.sql

RUN \
    /bin/sh -c "usr/bin/mysqld_safe &" && \
    sleep 5 && \
    mysql -u root < /root/db.sql

RUN \
    sed -i 's/mysqli.default_socket=/mysqli.default_socket=\/run\/mysqld\/mysqld.sock/' /etc/php7/php.ini

COPY web /var/www/html

# set up php file with password
RUN sed -i 's/<password_web>/'$(cat /root/pass_web)'/g' /var/www/html/inc/db_init.php

RUN \
    rm /root/db.sql && \
    rm /root/pass_web && \
    rm /root/pass_root
