#!/usr/bin/env bash
#script to install and configure nginx
#apt-get -y update
#apt-get -y install nginx
#ufw allow 'Nginx HTTP'
if [ ! -d "/data/" ]; then
    sudo mkdir "/data/"
fi

if [ ! -d "/data/web_static/" ]; then
    sudo mkdir "/data/web_static/"
fi

if [ ! -d "/data/web_static/releases/" ]; then
    sudo mkdir "/data/web_static/releases/"
fi

if [ ! -d "/data/web_static/shared/" ]; then
    sudo mkdir "/data/web_static/shared"
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    sudo mkdir "/data/web_static/releases/test/"
fi

sudo chown ubuntu:ubuntu /etc/nginx/sites-available/default

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

if [ -L "/data/web_static/releases/test/" ]; then
    sudo rm "/data/web_static/releases/test/"
fi

if [ ! -d "/data/web_static/current" ]; then
    sudo mkdir "/data/web_static/current"
fi

ls -s "/data/web_static/current" "/data/web_static/releases/test/"

sudo chown -R ubuntu:ubuntu "/data/"

sudo echo 'server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;
    location / {
        add_header X-Served-By $HOSTNAME;
    }
    location /hbnb_static/ {
        alias /data/web_static/current/
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
' > /etc/nginx/sites-available/default

sudo service nginx restart