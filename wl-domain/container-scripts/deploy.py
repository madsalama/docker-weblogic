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

apppkg=sys.argv[1]
appname=sys.argv[2]


# DEPLOY APP 
connectToAdmin()
progress_managed= deploy(appName=appname,path=appdir + '/' + apppkg, targets=managed_name)
progress_managed.printStatus()
startApplication(appname)
disconnect()

exit()
