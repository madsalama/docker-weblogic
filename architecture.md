```
	# 2/7/2018 : 6/7/2018
	# AUTOMATED DOMAIN-LEVEL SETUP...
        # COMMON-LIBRARIES (@CLUSTER)
        # DATASOURCES (@CLUSTER)
        # MAIL-SESSIONS(@CLUSTER)
        # UN-HARDWIRED SERVER PARAMETERS (MS_NAME/PORT/WAR/CLUSTER)

	# CREATED INDIVIDUAL DEPLOYMENT SCRIPTS (APP/MS)...
	# CREATED GENERIC DEPLOYMENT SCRIPT
	# HANDLE RESTART KILLED/STOPPED SERVER CONTAINER (UNKNOWN/SHUTDOWN)...

	# EXCEPTION HANDLING FOR CASES...
        # MACHINE ALREADY EXISTS
        # MANAGED SERVER ALREADY EXISTS
        # APPLICATION EXISTS (UNDEPLOY/RE-DEPLOY)
```

```
# Docker pauses running container while committing:
	$ docker commit <CONTAINER_ID> <NEW_IMAGE_NAME>
	$ docker commit webtt-deployment webtt-deployment-modified
# If I attempt to spawn a new container from the same image a container is running from,
docker will pause running containers while the new one is starting...
```

```
# Pass war name with server creation - only one deployment script needed (deploy.py)

# In run command argument: WARS="wta.war webtt.war"
# In createServer.sh:

for WAR in WARS
do
wlst deploy.py $WAR ${WAR/\.war/}
done

# In deploy.py:
import sys
apppkg=sys.argv[0]
appname=sys.argv[1]


# DEV_MS1: (WEBTT, WTA)
  # creates server/deploys (webtt, wta)
  --name='wlsmanaged_ms1' -p 7002:7002 -e MS_PORT=7002 -e WARS="wta.war webtt.war" -e MS_NAME='MS1' createServer.sh

# DEV_MS2: (TED)
  --name='WEBTT_MS2' -p 7003:7003 -e MS_PORT=7003 -e WARS="ted.war" -e MS_NAME='MS2' createServer.sh
```
