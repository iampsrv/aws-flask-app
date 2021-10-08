#!/bin/sh
virtualenv venv
cd /home/ubuntu/new/aws-flask-app
cd venv/bin
. activate
cd /home/ubuntu/new/aws-flask-app
pip install -r requirements.txt
python application.py
