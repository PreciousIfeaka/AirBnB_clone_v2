#!/usr/bin/env bash
# This script sets up my web servers for deployment of web_static folder.
# ...The conditions to be satisfied can be deciphered from the code.

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "Testing my process" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
exit 0
