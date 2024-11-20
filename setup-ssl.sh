#!/bin/bash

# Update and install Apache
sudo apt update && sudo apt install apache2 -y

# Enable necessary modules
sudo a2enmod ssl rewrite

# Generate a self-signed certificate
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/apache-selfsigned.key \
    -out /etc/ssl/certs/apache-selfsigned.crt \
    -subj "/C=US/ST=YourState/L=YourCity/O=YourOrganization/OU=YourUnit/CN=18.225.72.151"

# Update default SSL configuration
sudo sed -i 's|SSLCertificateFile.*|SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt|' /etc/apache2/sites-available/default-ssl.conf
sudo sed -i 's|SSLCertificateKeyFile.*|SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key|' /etc/apache2/sites-available/default-ssl.conf

# Configure HTTP to HTTPS redirection
echo '<VirtualHost *:80>
ServerName 18.225.72.151
Redirect permanent / https://18.225.72.151/
</VirtualHost>' | sudo tee /etc/apache2/sites-available/000-default.conf

# Enable SSL site and restart Apache
sudo a2ensite default-ssl
sudo systemctl restart apache2
