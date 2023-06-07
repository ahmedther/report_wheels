#!/bin/sh

set -e


# python manage.py runserver 0.0.0.0:8000

ln -snf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo Asia/Kolkata > /etc/timezone

mkdir /var/log/uwsgi

touch /var/log/uwsgi/reports_wheels.log

python manage.py collectstatic --noinput

until python -c "import psycopg2; psycopg2.connect('dbname=$POSTGRES_DB user=$POSTGRES_USER host=$POSTGRES_HOST password=$POSTGRES_PASSWORD port=$POSTGRES_PORT')" &>/dev/null; do
    echo "Waiting for PostgreSQL to become available..."
    sleep 1
done

uwsgi --ini /reports_wheels/uwsgi/uwsgi.ini
