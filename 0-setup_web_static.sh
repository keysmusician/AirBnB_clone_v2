#!/usr/bin/env bash
# Configures web servers for the deployment of static content

# Install Nginx
apt update
apt -y install nginx

# Create static content
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Air BnB Clone 0x03. Web static test" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/

# Configure Nginx
sed -i '37i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Launch nginx
service nginx restart
