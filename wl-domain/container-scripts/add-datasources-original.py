
execfile('/u01/oracle/commonfuncs.py')

#connectToAdmin()
#editMode()
#domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/webtt-domain')
#readDomain(domainhome)

cd('/')
cmo.createJDBCSystemResource('JDBC Data Source-0')

cd('/JDBCSystemResources/JDBC Data Source-0/JDBCResource/JDBC Data Source-0')
cmo.setName('JDBC Data Source-0')

cd('/JDBCSystemResources/JDBC Data Source-0/JDBCResource/JDBC Data Source-0/JDBCDataSourceParams/JDBC Data Source-0')
set('JNDINames',jarray.array([String('ngcsDatasource_52')], String))

cd('/JDBCSystemResources/JDBC Data Source-0/JDBCResource/JDBC Data Source-0/JDBCDriverParams/JDBC Data Source-0')
cmo.setUrl('jdbc:oracle:thin:@//192.57.138.32:7041/EWEBTT2')
cmo.setDriverName('oracle.jdbc.replay.OracleDataSourceImpl')
setEncrypted('Password', 'Password_1530701536833', '/u01/oracle/secrets/Script1530701463339Config', '/u01/oracle/secrets/Script1530701463339Secret')

cd('/JDBCSystemResources/JDBC Data Source-0/JDBCResource/JDBC Data Source-0/JDBCConnectionPoolParams/JDBC Data Source-0')
cmo.setTestTableName('SQL ISVALID\r\n\r\n')

cd('/JDBCSystemResources/JDBC Data Source-0/JDBCResource/JDBC Data Source-0/JDBCDriverParams/JDBC Data Source-0/Properties/JDBC Data Source-0')
cmo.createProperty('user')

cd('/JDBCSystemResources/JDBC Data Source-0/JDBCResource/JDBC Data Source-0/JDBCDriverParams/JDBC Data Source-0/Properties/JDBC Data Source-0/Properties/user')
cmo.setValue('ngcs_cn')

cd('/JDBCSystemResources/JDBC Data Source-0/JDBCResource/JDBC Data Source-0/JDBCDataSourceParams/JDBC Data Source-0')
cmo.setGlobalTransactionsProtocol('OnePhaseCommit')

cd('/JDBCSystemResources/JDBC Data Source-0')
set('Targets',jarray.array([ObjectName('com.bea:Name=webtt_cluster,Type=Cluster')], ObjectName))

#saveActivate()

closeDomain()

#

editMode()

cd('/')
cmo.createJDBCSystemResource('JDBC Data Source-1')

cd('/JDBCSystemResources/JDBC Data Source-1/JDBCResource/JDBC Data Source-1')
cmo.setName('JDBC Data Source-1')

cd('/JDBCSystemResources/JDBC Data Source-1/JDBCResource/JDBC Data Source-1/JDBCDataSourceParams/JDBC Data Source-1')
set('JNDINames',jarray.array([String('acsDatasource')], String))

cd('/JDBCSystemResources/JDBC Data Source-1/JDBCResource/JDBC Data Source-1/JDBCDriverParams/JDBC Data Source-1')
cmo.setUrl('jdbc:oracle:thin:@//ukwtselux103.elabs.svcs.entsvcs.net:7040/A1EFFONL')
cmo.setDriverName('oracle.jdbc.replay.OracleDataSourceImpl')
setEncrypted('Password', 'Password_1530701642706', '/u01/oracle/secrets/Script1530701558941Config', '/u01/oracle/secrets/Script1530701558941Secret')

cd('/JDBCSystemResources/JDBC Data Source-1/JDBCResource/JDBC Data Source-1/JDBCConnectionPoolParams/JDBC Data Source-1')
cmo.setTestTableName('SQL ISVALID\r\n\r\n')

cd('/JDBCSystemResources/JDBC Data Source-1/JDBCResource/JDBC Data Source-1/JDBCDriverParams/JDBC Data Source-1/Properties/JDBC Data Source-1')
cmo.createProperty('user')

cd('/JDBCSystemResources/JDBC Data Source-1/JDBCResource/JDBC Data Source-1/JDBCDriverParams/JDBC Data Source-1/Properties/JDBC Data Source-1/Properties/user')
cmo.setValue('acs_user')

cd('/JDBCSystemResources/JDBC Data Source-1/JDBCResource/JDBC Data Source-1/JDBCDataSourceParams/JDBC Data Source-1')
cmo.setGlobalTransactionsProtocol('OnePhaseCommit')

cd('/JDBCSystemResources/JDBC Data Source-1')
set('Targets',jarray.array([ObjectName('com.bea:Name=webtt_cluster,Type=Cluster')], ObjectName))

saveActivate()
disconnect()

