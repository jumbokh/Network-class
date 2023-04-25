### [nmap command](https://hack543.com/nmap-tutorial/)
* nmap -A 192.168.1.1   #全面掃描
* nmap 192.168.1.1-200  # 掃描指定段
```
-sP      Ping掃描
-P0      無Ping掃描, 用於防火牆禁止 Ping 掃描
-PS      TCP SYN Ping掃描
-PA      TCP ACK Ping掃描
-PU      UDP Ping掃描
-PE;-PP;-PM      ICMP Ping Types掃描
-PR      ARP Ping掃描
-n       禁止DNS反向解析
-R       反向解析域名
--system-dns    使用系統域名解析器
-sL      列表掃描
-6       掃描 IPv6 地址
--traceroute 路由跟蹤
-PY      SCTP INIT Ping 掃描
```
* nmap -sP 192.168.1.1/24
* nmap -p0 --packet-trace scanme.nmap.org
* nmap -PS -v 192.168.1.1
* nmap -PS80,100-200 -v 192.168.1.1
* nmap -PA -v 192.168.1.1
* nmap -PA -PS 192.168.1.1
* nmap --traceroute -v kali.org
* nmap -T4 192.168.1.1
* nmap -sT --script vuln 192.168.1.100
* sudo time nmap -T4 -sT -p T:1-65535 192.168.0.1
* sudo time nmap -T4 -sS -p T:1-65535 192.168.0.1
#### 列舉開啟服務的詳細版本
* sudo  nmap -sV -T4 192.168.0.1
#### 確認目標網段內有哪些機器活著
* sudo nmap -T4 -sn 192.168.1.0/24 
#### 掃描 1-65535 Port
* sudo  nmap -T4 -sT -p 1-65535 192.168.0.1
#### 限定是 TCP Port
* sudo nmap -T4 -sT -p T:1-65535 192.168.0.1
####  不 Ping Probes 直接掃描
```
# 主機前端的防火牆直接拒絕回應 TCP Port 80 與 443 的 SYN 封包，就會得到上面訊息的回應
Starting Nmap 7.01 ( https://nmap.org ) at 2021-04-25 10:45 CST
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 2.00 seconds
```
* sudo nmap -T4 -Pn 192.168.0.1 
#### 防火牆保護下的通訊埠掃描
```
白名單防火牆規則
防火牆僅用白名單方式，開放 TCP Port 3306、3389，預設阻擋其他的Port 。
所以也一併阻擋了 Nmap 向 TCP Port 80, Port 443 發送的主機存活刺探封包。
必須得加上 -Pn 參數進行掃描。
```
#### 猜測檢測目標的作業系統版本
* sudo nmap -T4 -sT -O 192.168.0.1
#### 整合
* sudo  nmap -T4 -sT -p 1-65535 -r -sC -sV 192.168.0.1
#### [nmap script](https://www.tecmint.com/use-nmap-script-engine-nse-scripts-in-linux/)
##
#### 資訊蒐集
* sudo nmap --script ip-geolocation-* www.0day.co
* sudo nmap --script whois-domain.nse www.0day.co     # whois
* sudo nmap --script whois-domain.nse --script-args whois.whodb=nofollow www.0day.co
* sudo nmap -sn --script whois -v -iL host.txt
* sudo nmap --script dns-brute kali.org
* sudo nmap -p 445 154.213.16.101 --script membase-http-info        # 檢索系統資訊
##
#### 蒐集 E-mail
* sudo nmap --script http-email-harvest 0day
##
#### IP 反查
* sudo nmap -sn --script hostmap-ip2hosts 0day
####
1. 找一台未修補 ms17-010 的 Windows 7 做為攻擊目標
* scan w script: https://nmap.org/nsedoc/scripts/smb-os-discovery.html
* sudo nmap --script smb-os-discovery.nse -d -p445 10.8.8.24
2. metasploit : msfconsole
    * official site: https://www.metasploit.com/
```
msf6 > use auxiliary/scanner/smb/smb_ms17_010
msf6 auxiliary(scanner/smb/smb_ms17_010) > show options

Module options (auxiliary/scanner/smb/smb_ms17_010):

   Name         Current Setting      Required  Description
   ----         ---------------      --------  -----------
   CHECK_ARCH   true                 no        Check for architecture on vulner
                                               able hosts
   CHECK_DOPU   true                 no        Check for DOUBLEPULSAR on vulner
                                               able hosts
   CHECK_PIPE   false                no        Check for named pipe on vulnerab
                                               le hosts
   NAMED_PIPES  /opt/metasploit-fra  yes       List of named pipes to check
                mework/embedded/fra
                mework/data/wordlis
                ts/named_pipes.txt
   RHOSTS                            yes       The target host(s), see https://
                                               github.com/rapid7/metasploit-fra
                                               mework/wiki/Using-Metasploit
   RPORT        445                  yes       The SMB service port (TCP)
   SMBDomain    .                    no        The Windows domain to use for au
                                               thentication
   SMBPass                           no        The password for the specified u
                                               sername
   SMBUser                           no        The username to authenticate as
   THREADS      1                    yes       The number of concurrent threads
                                                (max one per host)


View the full module info with the info, or info -d command.

msf6 auxiliary(scanner/smb/smb_ms17_010) > set RHOSTS 10.8.8.24
msf6 auxiliary(scanner/smb/smb_ms17_010) > exploit
```
##
### nmap script install
```
$ sudo locate *.nse
locate where your nmap scripts are located on your system
    for *nix system it might be  ~/.nmap/scripts/ or $NMAPDIR
    for Mac it might be /usr/local/Cellar/nmap/<version>/share/nmap/scripts/
    for Windows it might be C:\Program Files (x86)\Nmap\scripts
copy the provided script (vulners.nse) into that directory
run *nmap --script-updatedb* to update the nmap script DB 
```
```
cd /usr/share/nmap/scripts/
sudo git clone https://github.com/vulnersCom/nmap-vulners.git
sudo nmap -sV --script nmap-vulners/ <target IP>
```
* sudo nmap 192.168.1.121 --script=ftp-anon -p 21
```
* jumbo@raspberrypi:~/notebooks $ sudo nmap 192.168.1.121 --script=ftp-anon -p 21
Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-02 14:58 CST
Nmap scan report for 192.168.1.121
Host is up (0.00064s latency).

PORT   STATE SERVICE
21/tcp open  ftp
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
MAC Address: 08:00:27:33:DD:95 (Oracle VirtualBox virtual NIC)

Nmap done: 1 IP address (1 host up) scanned in 2.09 seconds
jumbo@raspberrypi:~/notebooks $ 
```
##
#### 靶機測試
* https://www.cnblogs.com/ayoung/p/15186328.html
