#!/bin/sh

set -e

python manage.py collectstatic --noinput

uwsgi --ini /reports_wheels/uwsgi/uwsgi.ini
