#!/bin/sh

set -e


# python manage.py runserver 0.0.0.0:8000

ln -snf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo Asia/Kolkata > /etc/timezone

mkdir /var/log/uwsgi

touch /var/log/uwsgi/reports_wheels.log

python manage.py collectstatic --noinput

while true; do
  # Check if PostgreSQL server is available
  /py/bin/python /reports_wheels/scripts/check_postgres.py

  if [ $? -eq 0 ]; then
    break  # Break the loop if connection successful
  fi

  sleep 1
done

uwsgi --ini /reports_wheels/uwsgi/uwsgi.ini
