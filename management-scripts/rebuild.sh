#!/bin/bash

docker container kill webtt_MS1 webtt_MS2 webtt_MS3 webtt_admin
docker container rm webtt_MS1 webtt_MS2 webtt_MS3 webtt_admin	

docker image rm webtt_domain
docker image rm webtt_deployment

docker build -t webtt_domain --build-arg ADMIN_PASSWORD=weblogic1 wl-domain	
docker build -t webtt_deployment wl-deployment

./1.restart-admin.sh

