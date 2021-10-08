#!/bin/sh
virtualenv venv
cd ~/new/aws-flask-app
cd venv/bin
. activate
cd ~/new/aws-flask-app
pip install -r requirements.txt
python application.py
