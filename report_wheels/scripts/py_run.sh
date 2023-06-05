#!/bin/sh

set -e

ln -snf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo Asia/Kolkata > /etc/timezone

python manage.py collectstatic --noinput

uwsgi --ini /reports_wheels/uwsgi/uwsgi.ini
