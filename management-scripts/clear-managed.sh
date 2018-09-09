#!/bin/bash

# clearMS.sh | Clear Managed Server's NodeManager Directories in ADMIN CONTAINER
# AUTHOR: Mahmoud Salama

MS_NAME=$1

docker exec -it webtt-admin bash -c '
echo "Clearing ${DOMAIN_HOME}/servers/'$MS_NAME'/tmp"
rm -rf ${DOMAIN_HOME}/servers/'$MS_NAME'/tmp/*
echo "Clearing ${DOMAIN_HOME}/servers/'$MS_NAME'/cache"
rm -rf ${DOMAIN_HOME}/servers/'$MS_NAME'/cache/*
echo "Clearing ${DOMAIN_HOME}/servers/'$MS_NAME'/data"
rm -rf ${DOMAIN_HOME}/servers/'$MS_NAME'/data/*
echo "Clearing ${DOMAIN_HOME}/servers/'$MS_NAME'/stage"
rm -rf ${DOMAIN_HOME}/servers/'$MS_NAME'/stage/*
'
