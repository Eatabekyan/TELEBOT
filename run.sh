#!/bin/bash

docker build . -t telegram_bot --build-arg TOKEN=$1
docker-compose up