#!/bin/bash

# clearAS.sh | Clear AdminServer's NodeManager Directories in ADMIN CONTAINER
# AUTHOR: Mahmoud Salama

docker exec -it webtt_admin bash -c '
echo "Clearing ${DOMAIN_HOME}/servers/AdminServer/tmp"
rm -rf ${DOMAIN_HOME}/servers/AdminServer/tmp/*
echo "Clearing ${DOMAIN_HOME}/servers/AdminServer/cache"
rm -rf ${DOMAIN_HOME}/servers/AdminServer/cache/*
echo "Clearing ${DOMAIN_HOME}/servers/AdminServer/data"
rm -rf ${DOMAIN_HOME}/servers/AdminServer/data/*
echo "Clearing ${DOMAIN_HOME}/servers/AdminServer/stage"
rm -rf ${DOMAIN_HOME}/servers/AdminServer/stage/*
'
