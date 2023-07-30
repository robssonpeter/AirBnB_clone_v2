#!/usr/bin/env bash
#script to install and configure nginx
#apt-get -y update
#apt-get -y install nginx
#ufw allow 'Nginx HTTP'
if [ ! -d "/data/" ]; then
    mkdir "/data/"
fi

if [ ! -d "/data/web_static/" ]; then
    mkdir "/data/web_static/"
fi

if [ ! -d "/data/web_static/releases/" ]; then
    mkdir "/data/web_static/releases/"
fi

if [ ! -d "/data/web_static/shared/" ]; then
    mkdir "data/web_static/shared"
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    mkdir "/data/web_static/releases/test/"
fi

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

if [ -L "/data/web_static/releases/test/" ]; then
    rm "/data/web_static/releases/test/"
fi

ls -s "/data/web_static/current" "/data/web_static/releases/test/"

sudo chown -R "/data/" ubuntu:ubuntu

echo 'server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static/ {
        alias /data/web_static/current/
    }
}' > /etc/nginx/sites-available/default

sudo service nginx restart