#!/usr/bin/env bash
# This script sets up my web servers for deployment of web_static folder.
#...The conditions to be satisfied can be deciphered from the code.

prev_path="/data/web_static/releases/test/"
sym_link="/data/web_static/current"

sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "Testing my process" > /data/web_static/releases/test/index.html

if [ -L "$sym_link" ];
then
        rm -rf "$sym_link"
fi
# Above condition deletes the symbolic link if it exists

sudo ln -s "$prev_path" "$sym_link"
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '58i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
