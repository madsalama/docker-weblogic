# weblogic-docker

### Install Docker via RPM:

- Package: docker-ce-18.03.1.ce-1.el7.centos.x84-64.rpm (On CentOS 7) 
- Command: ``` $ rpm -ivh path/to/rpm-package.rpm ```
- Download and install dependencies:
    -	container-selinux >= 2.9	
        - policycoreutils-python
        - audit-libs-python >= 2.1.3-4
        - checkpolicy
        - libapol.so.4()(64bit) 	#  replaced by setools-libs (ignored)
        - libapol.so.4(VERS_4.0)(64bit)	# replaced by setools-libs (ignored)
        - libqpol.so.1()(64bit)		# replaced by setools-libs (ignored)
        - libqpol.so.1.VERS_1.2)(64bit) 	# replaced by setools-libs (ignored)
        - libqpol.so.1(VERS_1.4)(64bit)	# replaced by setools-libs (ignored)
        - libsemanage-python >= 2.5-9
        - python-IPy
        - setools-libs >=3.3.8-2
    -	libcgroup
    -	pigz

- Enable Docker Daemon:
```
$ systemctl enable dockerd        # tag it to it always start after OS boot
$ systemctl start dockerd         # start it now if down
```

### Install WebLogic on Docker:
- Make sure all required packages exist in their respective directory:
  - oraclelinux-slim-7/oraclelinux-7-slim-rootfs.tar.xz
  - jre-8u171/server-jre-8u171-linux-x64.tar.gz
  - weblogic-12.1.3/fmw_12.1.3.0.0_wls.jar

- For deployments, war file is expected to be copied from container-scripts/*.war; change that inside deploy.py in the future to wherever the war is delivered. 
- For experiments, use the convenience script ```rebuild.sh``` to destroy/recreate needed containers/images if you made a change in an image, but modify as needed. 
- It's imperative that you understand and customize these files as needed:
  - weblogic-12.1.3/Dockerfile
  - wl-domain/Dockerfile
  - wl-deployment/Dockerfile
  - container-scripts/
      - add-server.py
      - create_deployServer.sh
      - deploy.py
 - You should set below to be able to restart after OS reboot. (power failure) 


### Build pre-requisite images:
```
$ docker build -t oracle/oraclelinux/slim-7 oraclelinux-slim-7
$ docker build -t oracle/serverjre:8 jre-8u171
$ docker build -t oracle/weblogic:12.1.3 weblogic-12.1.3
$ docker build -t wl-domain --build-arg ADMIN_PASSWORD=<define> wl-domain
$ docker build -t webtt-deployment wl-deployment
```

### Run Admin/Managed with auto-deploy/auto-start:

```
$ docker run -d --name wlsadmin --hostname wlsadmin -p 7001:7001 webtt-deployment
$ docker run -d --name wlsmanaged --link wlsadmin:wlsadmin -p 7002:7002 webtt-deployment createServer.sh
$ docker contanier ls 

# Kill/Remove a container:
$ docker kill <container_id>
$ docker rm <container_id>

# List all containers (running/killed):
$ docker container ls -a 

# Restart killed containers (whose changes are not gone till you do a $ docker container rm)
$ docker start <container_id>
```
