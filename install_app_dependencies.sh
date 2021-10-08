#!/bin/bash
sudo pip3 install virtualenv
cd /home/ubuntu/new/aws-flask-app
virtualenv venv
source venv/bin/activate
sudo pip3 install -r requirements.txt
chmod -R 777 *
