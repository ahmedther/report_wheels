FROM nginx:alpine3.17-slim

LABEL maintainer='ahmed'

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./nginx_run.sh ./nginx_run.sh
COPY ./uwsgi_params /etc/nginx/uwsgi_params

RUN chmod 777 ./nginx_run.sh  && \
    ln -snf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo Asia/Kolkata > /etc/timezone

CMD ["./nginx_run.sh"]
  