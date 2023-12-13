FROM python:3.10-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN apk add bash

EXPOSE 8000

