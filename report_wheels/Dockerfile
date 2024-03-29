# Build stage
FROM python:3.11-alpine as builder


WORKDIR /reports_wheels

COPY ./requirements.txt /reports_wheels/requirements.txt

RUN apk update \
    && apk upgrade \
    && apk add --no-cache git build-base linux-headers \
    && python3 -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install --no-cache --no-cache-dir -r /reports_wheels/requirements.txt  \
    && chmod -R 777 /reports_wheels \
    && apk del git build-base linux-headers \
    && rm -rf /var/cache/apk/* 



# Runtime stage
FROM python:3.11-alpine

WORKDIR /reports_wheels

COPY --from=builder /py /py

COPY . /reports_wheels

LABEL maintainer='ahmed'

ENV PYTHONUNBUFFERED 1


ENV PATH="/reports_wheels/scripts:/py/bin:$PATH"


CMD ["./scripts/py_run.sh"]
