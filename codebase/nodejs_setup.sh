#!/bin/bash
yum update -y

echo "Setting up NodeJS Environment"
curl https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash

echo 'export NVM_DIR="/home/ec2-user/.nvm"' >> /home/ec2-user/.bashrc
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm' >> /home/ec2-user/.bashrc

# Dot source the files to ensure that variables are available within the current shell
. /home/ec2-user/.nvm/nvm.sh
. /home/ec2-user/.bashrc

# Install NVM, NPM, Node.JS & Grunt
nvm alias default v12.7.0
nvm install v12.7.0
nvm use v12.7.0

