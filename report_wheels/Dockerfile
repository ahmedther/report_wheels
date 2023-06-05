# Build stage
FROM python:3.11-alpine as builder



RUN apk update \
    && apk upgrade \
    && apk add --no-cache git build-base linux-headers \
    && mkdir /temp_down \
    && git clone https://github.com/ahmedther/report_wheels.git /temp_down \
    && mv /temp_down/report_wheels* /reports_wheels \
    && rm -rf /temp_down \
    && python3 -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install --no-cache --no-cache-dir -r /reports_wheels/requirements.txt  \
    && chmod -R 777 /reports_wheels \
    && mkdir /var/log/uwsgi \
    && touch /var/log/uwsgi/reports_wheels.log  \ 
    && apk del git build-base linux-headers \
    && rm -rf /var/cache/apk/* 



# Runtime stage
FROM python:3.11-alpine

COPY --from=builder /py /py
COPY --from=builder /reports_wheels /reports_wheels
COPY --from=builder /var/log/uwsgi /var/log/uwsgi


LABEL maintainer='ahmed'

ENV PYTHONUNBUFFERED 1

WORKDIR /reports_wheels

ENV PATH="/reports_wheels/scripts:/py/bin:$PATH"


CMD ["./scripts/py_run.sh"]
