#!/bin/bash

# AUTHOR: MAHMOUD SALAMA
# deploy_generic.sh | AUTOMATED DEPLOYMENT
# deploy_generic.sh "<DELIVERY_PATH>" <MS_NAME> "<WARS>"
# deploy_generic.sh "wl-deployment/packages" webtt_MS1 "webtt.war ted.war"

function show {
echo '
deploy_generic.sh | AUTOMATED DEPLOYMENT
deploy_generic.sh "<DELIVERY_PATH>" <MS_NAME> "<WARS>"
deploy_generic.sh "wl-deployment/packages" webtt_MS1 "webtt.war ted.war"
'
}

show
exit

# DELIVERY_PATH=$1
# MS_NAME=$2
# WARS=$3

DELIVERY_PATH="wl-deployment/packages"
echo "DELIVERY_PATH=${DELIVERY_PATH}"

# Copy to the running ADMIN container...
docker cp "${DELIVERY_PATH}/." webtt_admin:/u01/oracle

# Rebuilding image (webtt_deployment)... New packages will be permanent now if -> ADMIN STOPPED/RESTARTED!
# Since admin should start from same image (webtt_deployment) - Check rebuild.sh

echo "DESTROYING WEBTT CONTAINER/IMAGE..."

docker container kill webtt_MS1 
docker container rm webtt_MS1 

echo "REBUILDING WEBTT IMAGE... "
docker build -t webtt_deployment wl-deployment

# DEPLOY/START MANAGED
echo "DEPLOYING/STARTING WEBTT..."

docker run -d --name webtt_MS1 --link webtt_admin:webtt_admin -e MS_NAME="webtt_MS1" -e MS_PORT="7010" -e WARS='webtt.war ted.war'\
 -e CLUSTER_NAME="webtt_cluster" -p 7010:7010 webtt_deployment create_deployServer.sh

docker logs -f webtt_MS1

