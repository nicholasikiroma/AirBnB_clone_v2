#!/usr/bin/env bash
# sets up web servers for the deployment of web_static


sudo apt-get -y update
sudo apt-get -y install nginx

#--configure firewall
sudo ufw allow 'Nginx HTTP'

#--created the dir
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

#--adds test string
echo "<h1>Testing server config...</h1>" > /data/web_static/releases/test/index.html

#--create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default


sudo service nginx restart
