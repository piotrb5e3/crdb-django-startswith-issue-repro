#!/usr/bin/env bash

docker build -t "crdb-startswith-issue-repro:latest" .

trap "docker-compose down" EXIT

docker-compose run main python manage.py test