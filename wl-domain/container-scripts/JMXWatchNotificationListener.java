/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import javax.management.NotificationListener;
import javax.management.MBeanServerConnection;
import javax.management.ObjectName;

import javax.management.Notification;
import javax.management.remote.JMXServiceURL;
import javax.management.remote.JMXConnectorFactory;
import javax.management.remote.JMXConnector;
import javax.naming.Context;
import java.util.Hashtable;

import weblogic.management.mbeanservers.runtime.RuntimeServiceMBean;
import weblogic.diagnostics.watch.WatchNotification;
import weblogic.diagnostics.watch.JMXWatchNotification;

import org.python.core.PyString;
import org.python.util.InteractiveInterpreter;
import weblogic.management.scripting.utils.WLSTInterpreter;
import java.io.IOException;
import java.io.OutputStream;

public class JMXWatchNotificationListener implements NotificationListener {

  private MBeanServerConnection rmbs = null;
  private String notifName = "server-unavailable";
  private int notifCount = 0;
  
  private String serverName = "AdminServer";
  private String hostName   = "localhost";
  private int    port       = 7001;
  private String user       = "weblogic";
  private String password   = "weblogic1";

  public JMXWatchNotificationListener(String args[]) throws Exception {
    int size = (args != null ? args.length : 0);
    for (int i=0; i < size; i++) {
      String arg = args[i];
      if (arg.equals("-server")) {
        serverName = args[++i];
      } else if (arg.equals("-host")) {
        hostName = args[++i];
      } else if (arg.equals("-port")) {
        port = Integer.parseInt(args[++i]);
      } else if (arg.equals("-user")) {
        user = args[++i];
      } else if (arg.equals("-password")) {
        password = args[++i];
      }
    }    
  }

  private void register() throws Exception {
    rmbs = getRuntimeMBeanServerConnection();
    addNotificationHandler();
  }
  
  private MBeanServerConnection getRuntimeMBeanServerConnection()
    throws Exception {    

    String JNDI = "/jndi/";

    JMXServiceURL serviceURL;
    serviceURL =
      new JMXServiceURL("t3", hostName, port,
                        JNDI + RuntimeServiceMBean.MBEANSERVER_JNDI_NAME);

    System.out.println("URL=" + serviceURL);

    Hashtable h = new Hashtable();
    h.put(Context.SECURITY_PRINCIPAL,user);
    h.put(Context.SECURITY_CREDENTIALS,password);
    h.put(JMXConnectorFactory.PROTOCOL_PROVIDER_PACKAGES,
          "weblogic.management.remote");
    JMXConnector connector = JMXConnectorFactory.connect(serviceURL,h);
    return connector.getMBeanServerConnection();
  }
  
  private void addNotificationHandler() throws Exception {

    /*
     * The JMX Watch notification listener registers with a Runtime MBean
     * that matches the name of the corresponding watch bean.
     * Each watch has its own Runtime MBean instance.
     */    

    ObjectName oname = 
      new ObjectName(
          "com.bea:ServerRuntime=" + serverName + ",Name=" +  
          JMXWatchNotification.GLOBAL_JMX_NOTIFICATION_PRODUCER_NAME + 
          ",Type=WLDFWatchJMXNotificationRuntime," +
          "WLDFWatchNotificationRuntime=WatchNotification," +
          "WLDFRuntime=WLDFRuntime"
          );
     System.out.println("Adding notification handler for: " +
       oname.getCanonicalName());
    rmbs.addNotificationListener(oname, this, null, null);
  }
 
public static class NullOutputStream extends OutputStream
  {
    @Override public void write(int b) throws IOException {}
    @Override public void write(byte[] b) throws IOException {}
    @Override public void write(byte[] b, int off, int len) throws IOException { }
  }
 
private void removeServer(String servername)  {
  
InteractiveInterpreter interpreter = new WLSTInterpreter();
interpreter.setOut(new NullOutputStream());

// exec(): no-result commands

// remove server
interpreter.exec("connect('weblogic', 'weblogic1', 'localhost:7001')");
interpreter.exec("edit()");
interpreter.exec("startEdit()");
interpreter.exec("cd('/')");
interpreter.exec("cd('/Servers/"+servername+"')");
interpreter.exec("cmo.setCluster(None)");
interpreter.exec("cmo.setMachine(None)");
interpreter.exec("editService.getConfigurationManager().removeReferencesToBean(getMBean('/Servers/"+servername+"'))");
interpreter.exec("cd('/')");
interpreter.exec("cmo.destroyServer(getMBean('/Servers/"+servername+"'))");

// remove associated machine
interpreter.exec("editService.getConfigurationManager().removeReferencesToBean(getMBean('/Machines/Machine-" + servername + "'))");
interpreter.exec("cd('/')");
interpreter.exec("cmo.destroyMachine(getMBean('/Machines/Machine-" + servername + "'))");

interpreter.exec("activate()");

// eval(): result commands
// PyString result = (PyString)interpreter.eval("ls()");

System.out.println( "UNAVAILABLE SERVER " + servername + " REMOVED...");

}

private String[] getServerNames(String servernames){

 String str = servernames.replaceAll(" = ", "=");
 String[] data = str.split(" ");
 String _temp = "";

 for (int i = 0; i < data.length; i++){

  if ( data[i].contains("SHUTDOWN") || data[i].contains("UNKNOWN") ) {

  String _str = data[i].replaceAll(",Type=ServerLifeCycleRuntime//State=SHUTDOWN", "");
  String __str = _str.replaceAll(",Type=ServerLifeCycleRuntime//State=UNKNOWN", "");
  String ___str  = __str.replaceAll("com.bea:Name=", "");
  _temp = _temp + " " +  ___str;

  }
 }

String[] servers = _temp.split(" ");
return servers;

}
  
  /**
   * Handle JMX notification
   */
  public void handleNotification(Notification notif, Object handback) {
    synchronized (this) {
      try {
        if (notif instanceof JMXWatchNotification) {
          WatchNotification wNotif =
                ((JMXWatchNotification)notif).getExtendedInfo();
          notifCount++;

	String servernames[] = this.getServerNames(wNotif.getWatchDataToString());
	
	// for servername in $servernames
	for (int i=1; i < servernames.length; i++){
	        System.out.println("REMOVING " + servernames[i] + " ...");	
	        this.removeServer(servernames[i]);
	}

        }
      } catch (Throwable x) {
        System.out.println("Exception occurred processing JMX watch                   notification: " + notifName +"\n" + x);
        x.printStackTrace();
      }
    }
  }

  public static void  main(String[] args) {
    try {
      JMXWatchNotificationListener listener =
              new JMXWatchNotificationListener(args);
      listener.register();
      // Sleep waiting for notifications
      Thread.sleep(Long.MAX_VALUE);
    } catch (Throwable e) {
      e.printStackTrace();
    } // end of try-catch 
  } // end of main()
}
