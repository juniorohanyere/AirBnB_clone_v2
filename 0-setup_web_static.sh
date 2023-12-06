#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

# install Nginx if it not already installed
sudo mkdir -p /data/web_static/releases/test/

# create the folder /data/ if it doesn’t already exist
# create the folder /data/web_static/ if it doesn’t already exist
# create the folder /data/web_static/releases/ if it doesn’t already exist
# create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# create the folder /data/web_static/shared/ if it doesn’t already exist
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html > /dev/null

# create a fake HTML file /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# create a symbolic link /data/web_static/current linked to the...
# .../data/web_static/releases/test/ folder. If the symbolic link already...
# ...exists, it should be deleted and recreated every time the script is ran.
sudo chown -R ubuntu:ubuntu /data/

# give ownership of the /data/ folder to the ubuntu user AND group (you can
# assume this user and group exist). This should be recursive; everything
# inside should be created/owned by this user/group.
sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static
# (ex: https://mydomainname.tech/hbnb_static).
# don’t forget to restart Nginx after updating the configuration:
sudo service nginx restart

