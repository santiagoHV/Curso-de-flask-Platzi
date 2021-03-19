#!/usr/bin/bash

venv\Scripts\activate.bat

pip install -r requirements.txt

set FLASK_APP=main.py
set FLASK_DEBUG=1
set FLASK_ENV=development
set GOOGLE_CLOUD_PROJECT=flask-platzi-308122

flask run
