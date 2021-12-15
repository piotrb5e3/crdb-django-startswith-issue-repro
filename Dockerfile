# syntax=docker/dockerfile:1

FROM python:3.8.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .