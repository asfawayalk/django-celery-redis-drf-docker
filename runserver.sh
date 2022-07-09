#!/bin/bash
ROOT_PATH=$(dirname $(dirname $0))
cd $ROOT_PATH

#waiting for db
./wait-for-it.sh db:$DB_PORT

#create database if it is not there yet
python -c "from psycopg2 import connect; connect(dbname='postgres', user='$DB_USER', host='pgdb', password='$DB_PASSWORD').cursor().execute('create database $DB_NAME;')"

#install DB and fixtures
python manage.py makemigrations
python manage.py migrate

#python manage.py loaddata v1/accounts/fixtures/fixtures.json
# python manage.py loaddata v1/accounts/fixtures/gallery.json
# python manage.py loaddata v1/accounts/fixtures/triggertemplate.json
# python manage.py loaddata v1/accounts/fixtures/accounttemplate.json
# python manage.py loaddata v1/accounts/fixtures/complianceframework.json
# python manage.py loaddata v1/accounts/fixtures/compliancecontrol.json

while true; do
  echo "Re-starting Django runserver"
  python manage.py runserver 0.0.0.0:8000
  sleep 2
done
