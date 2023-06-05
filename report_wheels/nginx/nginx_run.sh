#!/bin/sh

set -e

ln -snf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo Asia/Kolkata > /etc/timezone

touch /etc/nginx/conf.d/default.conf 
touch /var/log/nginx/reports_wheels.log
touch /var/log/nginx/reports_wheels_log_error.log;
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
