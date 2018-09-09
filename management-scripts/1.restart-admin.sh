#!/bin/bash

docker container kill webtt_admin
docker container rm webtt_admin

#docker run -d --name webtt_admin --hostname webtt-admin -p 7001:7001 -v wl-data webtt_deployment
docker run -d --name webtt_admin --hostname webtt-admin -p 7001:7001 webtt_deployment
docker logs -f webtt_admin
