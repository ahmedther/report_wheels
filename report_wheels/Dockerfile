FROM python:3.12.0b1-alpine3.18

LABEL maintainer='ahmed'

ENV PYTHONUNBUFFERED 1

WORKDIR /reports_wheels

COPY ./ ./


RUN apk update \
    && apk upgrade \
    && apk add --no-cache postgresql-dev git \
    && git clone https://github.com/ahmedther/report_wheels.git \ 
    && python3 -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install --no-cache --no-cache-dir -r ./requirements.txt  \
    && chmod -R 777 /reports_wheels \
    && mkdir /var/log/uwsgi \
    && touch /var/log/uwsgi/reports_wheels.log  \ 
    && apk del .build-deps \
    && apk del build-base \
    && apk del git \
    && rm -rf /var/cache/apk/* \
    && apk autoremove


ENV SERVER_DJANGO_ON=9009


ENV PATH="/reports_wheels/scripts:/py/bin:$PATH"


CMD ["./scripts/py_run.sh"]
