#!/bin/bash

# DELIVERY_PATH=$1
# MS_NAME=$2
# WARS=$3

DELIVERY_PATH="wl-deployment/packages"
echo "DELIVERY_PATH=${DELIVERY_PATH}"

# Copy to the running ADMIN container...
docker cp "${DELIVERY_PATH}/." webtt_admin:/u01/oracle

# cp ${DELIVERY_PATH}/* wl-deployment/packages

# Rebuilding image (webtt_deployment)... New packages are permanent now if ADMIN STOPPED/RESTARTED!
# Since admin should start from same image (webtt_deployment) - Check rebuild.sh

echo "DESTROYING WEBTT CONTAINER/IMAGE..."

docker container kill webtt_MS3 
docker container rm webtt_MS3 

echo "REBUILDING WEBTT IMAGE... "

docker build -t webtt_deployment wl-deployment

echo "DEPLOYING/STARTING WEBTT..."

docker run -d --name webtt_MS3 --link webtt_admin:webtt_admin -e MS_NAME="webtt_MS3" -e MS_PORT="7004" -e WARS='ted.war'\
 -e CLUSTER_NAME="webtt_cluster" -p 7004:7004 webtt_deployment create_deployServer.sh

docker logs -f webtt_MS3

