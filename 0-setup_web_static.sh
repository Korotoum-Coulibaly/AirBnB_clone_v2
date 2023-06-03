#!/usr/bin/env bash
# Write a Bash Script that sets up your web servers for the deployment of web_static

#Install nginx if it's not already installed
sudo apt-get update
sudo apt-get -y install nginx

#create directories: (-p) create create subdirectories if they don't already exist
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

#create a fake HTML file with simple content,to test your Nginx conf
echo "<html>
        <head>
        </head>
        <body>
	  Holberton School
        </body>
       </html>" | tee /data/web_static/releases/test/index.html

#create a symbolic link
sudo ln -sf  /data/web_static/releases/test /data/web_static/current

#give ownership of the /data folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

#update the Nginx configuration to serve the content of /data/web/current to hbnb_static
sudo sed -i "38i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n" /etc/nginx/sites-available/default

#Restart Nginx
sudo service nginx restart
