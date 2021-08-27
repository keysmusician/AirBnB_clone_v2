#!/usr/bin/env bash
# Configures web servers for the deployment of static content

# Install Nginx
apt update
apt -y install nginx

# Create static content
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Holberton School Air BnB Clone 0x03. Web static test" > \
/data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/

# Configure Nginx
cat > /etc/nginx/sites-available/default <<"EOF"
server {
    add_header X-Served-By $HOSTNAME;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOF

# Launch nginx
service nginx restart
