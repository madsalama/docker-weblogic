execfile('/u01/oracle/commonfuncs.py')
connectToAdmin()
editMode()

cd('/WLDFSystemResources/Module-0/WLDFResource/Module-0/WatchNotification/WatchNotification/Watches/server-status')
set('Notifications',jarray.array([ObjectName('com.bea:Name=server-unavailable,Type=weblogic.diagnostics.descriptor.WLDFJMXNotificationBean,Parent=[webtt_domain]/WLDFSystemResources[Module-0],Path=WLDFResource[Module-0]/WatchNotification[WatchNotification]/JMXNotifications[server-unavailable]')], ObjectName))

saveActivate()

serverRuntime()
cd ('/WLDFRuntime/WLDFRuntime/WLDFControlRuntime/AdminServer/SystemResourceControls/Module-0')
cmo.setEnabled(true)

exit()
