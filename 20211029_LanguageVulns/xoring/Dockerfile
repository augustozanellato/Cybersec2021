FROM ubuntu:latest

RUN apt-get update && apt-get install -y nginx
RUN mkdir -p /var/www/html/
ADD . /var/www/html/
RUN rm /var/www/html/Dockerfile
RUN mv /var/www/html/nginx_conf /etc/nginx/sites-available/xoring
RUN ln -s /etc/nginx/sites-available/xoring /etc/nginx/sites-enabled
CMD service nginx restart && tail -f /var/log/nginx/error.xoring.log
