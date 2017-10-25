#!/bin/bash
pip install -r requirements.txt
python manage.py migrate
#might want to modify this to clear the database, or have this run on build
python manage.py loaddata initial_data.json
exec "$@"