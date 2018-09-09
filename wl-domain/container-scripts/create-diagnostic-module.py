
# DIAGNOSTIC SYSTEM MODULE
cd('/')
create('Module-0','WLDFSystemResource')

cd('/WLDFSystemResource/Module-0/WLDFResource/Module-0')
create('Harvester','Harvester')
create('WatchNotification','WatchNotification')

cd('/WLDFSystemResource/Module-0/WLDFResource/Module-0/Harvester/NO_NAME_0')
set('SamplePeriod',10000)
set('Enabled','true')

# JMX-NOTIFICATION
cd('/WLDFSystemResource/Module-0/WLDFResource/Module-0/WatchNotification/NO_NAME_0')
set('Enabled','true')
set('LogWatchSeverity','Error')
set('Severity','Error')

create('server-unavailable','JMXNotification')
create('server-status','Watch')

cd('JMXNotification/server-unavailable')
set('Enabled','true')
set('NotificationType','weblogic.diagnostics.watch.defaultNotificationType')

# WATCH
cd('../../Watch/server-status')
set('RuleType','Harvester')
set('Enabled','true')
set('RuleExpression','(${DomainRuntime//[weblogic.management.runtime.ServerLifeCycleRuntimeMBean]//State} = \'UNKNOWN\') OR (${DomainRuntime//[weblogic.management.runtime.ServerLifeCycleRuntimeMBean]//State} = \'SHUTDOWN\')')
#set('Notification','server-unavailable')
set('AlarmType','None')

