#### output for command:
* nuclei -l target_urls.txt -include-tags iot,misc,fuzz
* target_urls.txt: 
```
192.168.1.121:8180
192.168.1.121
192.168.1.121:8009
```
#### output message
```

                     __     _
   ____  __  _______/ /__  (_)
  / __ \/ / / / ___/ / _ \/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\__,_/\___/_/\___/_/   v2.8.8

                projectdiscovery.io

[INF] Using Nuclei Engine 2.8.8 (latest)
[INF] Using Nuclei Templates 9.3.6 (latest)
[INF] Templates added in last update: 30
[INF] Templates loaded for scan: 4892
[INF] Targets loaded for scan: 3
[INF] Running httpx on input host
[INF] Found 2 URL from httpx
[INF] Templates clustered: 958 (Reduced 2640 Requests)
[apache-detect] [http] [info] http://192.168.1.121 [Apache/2.2.8 (Ubuntu) DAV/2]
[php-detect] [http] [info] http://192.168.1.121 [5.2.4]
[tech-detect:php] [http] [info] http://192.168.1.121
[apache-detect] [http] [info] http://192.168.1.121:8180 [Apache-Coyote/1.1]
[vnc-service-detect] [network] [info] 192.168.1.121:5900 [RFB 003.003]
[vnc-service-detect] [network] [info] 192.168.1.121:5900 [RFB 003.003]
[vnc-service-detect] [network] [info] 192.168.1.121:5900 [RFB 003.003]
[INF] Using Interactsh Server: oast.pro
[tomcat-default-login] [http] [high] http://192.168.1.121:8180/manager/html [username="tomcat",password="tomcat"]
[openssh-detect] [network] [info] 192.168.1.121:22 [SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
]
[pgsql-detect] [network] [info] 192.168.1.121:5432
[openssh-detect] [network] [info] 192.168.1.121:22 [SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
]
[openssh-detect] [network] [info] 192.168.1.121:22 [SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
]
[esmtp-detect] [network] [info] 192.168.1.121:25
[esmtp-detect] [network] [info] 192.168.1.121:25
[esmtp-detect] [network] [info] 192.168.1.121:25
[CVE-2012-1823] [http] [critical] http://192.168.1.121/index.php?-d+allow_url_include%3don+-d+auto_prepend_file%3dphp%3a//input
[phpinfo-files] [http] [low] http://192.168.1.121/phpinfo.php
[samba-detect] [network] [info] 192.168.1.121:139
[tomcat-detect] [http] [info] http://192.168.1.121:8180
[samba-detect] [network] [info] 192.168.1.121:139
[samba-detect] [network] [info] 192.168.1.121:139
[vsftpd-backdoor] [network] [critical] 192.168.1.121:21
[vsftpd-backdoor] [network] [critical] 192.168.1.121:21
[vsftpd-backdoor] [network] [critical] 192.168.1.121:21
[favicon-detect:apache-tomcat] [http] [info] http://192.168.1.121:8180/favicon.ico
[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] http://192.168.1.121
[http-missing-security-headers:access-control-allow-credentials] [http] [info] http://192.168.1.121
[http-missing-security-headers:access-control-allow-methods] [http] [info] http://192.168.1.121
[http-missing-security-headers:x-frame-options] [http] [info] http://192.168.1.121
[http-missing-security-headers:cross-origin-resource-policy] [http] [info] http://192.168.1.121
[http-missing-security-headers:access-control-max-age] [http] [info] http://192.168.1.121
[http-missing-security-headers:x-content-type-options] [http] [info] http://192.168.1.121
[http-missing-security-headers:referrer-policy] [http] [info] http://192.168.1.121
[http-missing-security-headers:clear-site-data] [http] [info] http://192.168.1.121
[http-missing-security-headers:access-control-allow-headers] [http] [info] http://192.168.1.121
[http-missing-security-headers:cross-origin-opener-policy] [http] [info] http://192.168.1.121
[http-missing-security-headers:access-control-allow-origin] [http] [info] http://192.168.1.121
[http-missing-security-headers:access-control-expose-headers] [http] [info] http://192.168.1.121
[http-missing-security-headers:strict-transport-security] [http] [info] http://192.168.1.121
[http-missing-security-headers:content-security-policy] [http] [info] http://192.168.1.121
[http-missing-security-headers:permissions-policy] [http] [info] http://192.168.1.121
[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] http://192.168.1.121
[http-missing-security-headers:x-frame-options] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:access-control-allow-origin] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:content-security-policy] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:access-control-max-age] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:permissions-policy] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:cross-origin-resource-policy] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:access-control-allow-credentials] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:access-control-allow-headers] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:strict-transport-security] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:x-content-type-options] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:referrer-policy] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:clear-site-data] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:cross-origin-opener-policy] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:access-control-expose-headers] [http] [info] http://192.168.1.121:8180
[http-missing-security-headers:access-control-allow-methods] [http] [info] http://192.168.1.121:8180
[old-copyright] [http] [info] http://192.168.1.121:8180 [&copy; 1999]
[waf-detect:apachegeneric] [http] [info] http://192.168.1.121/
[waf-detect:ats] [http] [info] http://192.168.1.121:8180/
[waf-detect:apachegeneric] [http] [info] http://192.168.1.121:8180/
[CVE-2020-1938] [network] [critical] 192.168.1.121:8009
[CVE-2020-1938] [network] [critical] 192.168.1.121:8009
[CVE-2020-1938] [network] [critical] 192.168.1.121:8009
[public-tomcat-manager] [http] [info] http://192.168.1.121:8180/manager/html
[public-tomcat-manager] [http] [info] http://192.168.1.121:8180/host-manager/html
[HTTP-TRACE:trace-request] [http] [info] http://192.168.1.121
[phpmyadmin-panel] [http] [info] http://192.168.1.121/phpMyAdmin/
[smtp-service-detect] [network] [info] 192.168.1.121:25
[smtp-service-detect] [network] [info] 192.168.1.121:25
[smtp-service-detect] [network] [info] 192.168.1.121:25
[ftp-anonymous-login] [network] [medium] 192.168.1.121:21
[ftp-anonymous-login] [network] [medium] 192.168.1.121:21
[ftp-anonymous-login] [network] [medium] 192.168.1.121:21
```
