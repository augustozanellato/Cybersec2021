FROM richarvey/nginx-php-fpm:1.8.2

MAINTAINER Zane Durkin <zane@zemptech.com>

# set up nginx
RUN sed -i 's/root \/usr\/share\/nginx\/html/root \/var\/www\/html/g' /etc/nginx/sites-enabled/default.conf
RUN rm /var/www/html/*

COPY web /var/www/html
