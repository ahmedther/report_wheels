#!/bin/sh

set -e

ln -snf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo Asia/Kolkata > /etc/timezone

mkdir /var/log/uwsgi

touch /var/log/uwsgi/reports_wheels.log

python manage.py collectstatic --noinput

uwsgi --ini /reports_wheels/uwsgi/uwsgi.ini
