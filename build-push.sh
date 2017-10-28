#!/bin/bash

docker-compose build
docker push damiano7pixel/pykafkaproducersample 
docker push damiano7pixel/pykafkaconsumerrsample
