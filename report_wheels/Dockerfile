# Build stage
FROM python:3.11-alpine as builder

LABEL maintainer='ahmed'

ENV PYTHONUNBUFFERED 1

WORKDIR /reports_wheels


RUN apk update \
    && apk upgrade \
    && apk add --no-cache git \
    && mkdir temp \
    && git clone https://github.com/ahmedther/report_wheels.git ./temp \
    && mv ./temp/report_wheels/* . \
    && rm -rf ./temp \
    && python3 -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install psycopg2-binary \
    && /py/bin/pip install --no-cache --no-cache-dir -r ./requirements.txt  \
    && chmod -R 777 /reports_wheels \
    && mkdir /var/log/uwsgi \
    && touch /var/log/uwsgi/reports_wheels.log  \ 
    && apk del .build-deps \
    && apk del build-base \
    && apk del git \
    && rm -rf /var/cache/apk/* \
    && apk autoremove \
    && ln -snf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime && echo Asia/Kolkata > /etc/timezone




# Runtime stage
FROM python:3.11-alpine

ENV PATH="/reports_wheels/scripts:/py/bin:$PATH"

COPY --from=builder /venv /venv


CMD ["./scripts/py_run.sh"]
