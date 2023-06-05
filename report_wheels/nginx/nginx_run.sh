#!/bin/sh

set -e

touch /etc/nginx/conf.d/default.conf 
touch /var/log/nginx/reports_wheels.log
touch /var/log/nginx/reports_wheels_log_error.log;
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
