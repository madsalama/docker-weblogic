#!/bin/bash

# assign notification -> watch 
# activate diagnostic module
# start JMX Listener

docker exec -it webtt_admin bash -c '
. .bashrc;
wlst /u01/oracle/assign-notification.py
CLASSPATH=$CLASSPATH:/u01/oracle/
javac /u01/oracle/JMXWatchNotificationListener.java
nohup java JMXWatchNotificationListener > JMXWatchNotificationListener.log &
PID=$!
echo "kill $PID" > ~/stop_listener.sh
chmod u+x ~/stop_listener.sh
sleep 5s
'
# sync admin configuration
# docker exec -it webtt_admin bash -c '. .bashrc; ADMIN_URL="t3://webtt-admin:7001" && /u01/oracle/user_projects/domains/webtt_domain/bin/stopWebLogic.sh'
# ./clear-admin.sh
# docker cp ~/config.xml webtt_admin:/u01/oracle/user_projects/domains/webtt_domain/config/config.xml
# docker exec -it webtt_admin bash -c '. .bashrc; /u01/oracle/user_projects/domains/webtt_domain/bin/startWebLogic.sh'
