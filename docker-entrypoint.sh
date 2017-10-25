#!/bin/bash
pip install -r requirements.txt
python manage.py migrate
#might want to modify this to clear the database, or have this run on build
python manage.py loaddata initial_data.json
sleep 3 #TODO: this is just a quick fix to make it easier to pick up the postgres connection
exec "$@"