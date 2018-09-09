
# DATASOURCE 1

cd('/')
create('JDBC Data Source-0', 'JDBCSystemResource')

cd('JDBCSystemResource/JDBC Data Source-0/JdbcResource/JDBC Data Source-0')
create('myJdbcDriverParams','JDBCDriverParams')

cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','oracle.jdbc.replay.OracleDataSourceImpl')
set('URL','jdbc:oracle:thin:@//192.57.138.32:7041/EWEBTT2')
set('PasswordEncrypted', 'ngcs')

create('myProps','Properties')
cd('Properties/NO_NAME_0')

create('user', 'Property')
cd('Property/user')

cmo.setValue('ngcs_cn')

cd('/JDBCSystemResource/JDBC Data Source-0/JdbcResource/JDBC Data Source-0')
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String('ngcsDatasource_52'))

cd('/JDBCSystemResource/JDBC Data Source-0/JdbcResource/JDBC Data Source-0')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL ISVALID\r\n\r\n')

# DATASOURCE 2

cd('/')
create('JDBC Data Source-1', 'JDBCSystemResource')

cd('JDBCSystemResource/JDBC Data Source-1/JdbcResource/JDBC Data Source-1')
create('myJdbcDriverParams','JDBCDriverParams')

cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','oracle.jdbc.replay.OracleDataSourceImpl')
set('URL','jdbc:oracle:thin:@//ukwtselux103.elabs.svcs.entsvcs.net:7040/A1EFFONL')
set('PasswordEncrypted', 'au')

create('myProps','Properties')
cd('Properties/NO_NAME_0')

create('user', 'Property')
cd('Property/user')

cmo.setValue('acs_user')

cd('/JDBCSystemResource/JDBC Data Source-1/JdbcResource/JDBC Data Source-1')
create('myJdbcDataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String('acsDatasource'))

cd('/JDBCSystemResource/JDBC Data Source-1/JdbcResource/JDBC Data Source-1')
create('myJdbcConnectionPoolParams','JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL ISVALID\r\n\r\n')

