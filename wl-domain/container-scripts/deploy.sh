#!/bin/bash

# DEPLOYMENT
# This assumes WARS are set as env var while starting container
# example: WARS="wta.war webtt.war"

for WAR in $WARS
do
echo "ATTEMPTING TO UNDEPLOY $WAR ..."
wlst /u01/oracle/undeploy.py ${WAR//\.war/}

echo "DEPLOYING $WAR ..."
wlst /u01/oracle/deploy.py $WAR ${WAR//\.war/}
done


