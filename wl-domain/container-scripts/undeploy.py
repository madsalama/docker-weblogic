# Copyright (c) 2018 Oracle and/or its affiliates. All rights reserved.
#
# WLST Offline for deploying an application under APP_NAME packaged in APP_PKG_FILE located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default
#
# author: Bruno Borges <bruno.borges@oracle.com>
# since: December, 2015
#
import os
import sys

execfile('/u01/oracle/commonfuncs.py')

# Deployment Information
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/dev-domain')
admin_name = os.environ.get('ADMIN_NAME', 'AdminServer')
managed_name = os.environ.get('MS_NAME', 'DEV_MS1')
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")

#appname    = os.environ.get('APP_NAME', 'WEBTT')
#apppkg     = os.environ.get('APP_PKG_FILE', 'webtt.war')
appdir     = os.environ.get('APP_PKG_LOCATION', '/u01/oracle')

appname=sys.argv[1]

# JSF LIBRARY
#connectToAdmin()
#progress_lib= undeploy(appName='jsf')
#progress_lib.printStatus()
#disconnect()


# UNDEPLOY APPLICATION... 
connectToAdmin()
try:
    progress_managed = undeploy(appName=appname)
except:
    print('UNDEPLOY: APPLICATION NOT FOUND...')
    disconnect()
    exit()

progress_managed.printStatus()
disconnect()

exit()
