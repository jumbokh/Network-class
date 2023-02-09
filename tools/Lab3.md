#### Attack kali.org
#### osif check host
```
osif > use host_enum/dns_host                                                                                                                                                       
osif host_enum(dns_host) > set DOMAIN kali.org                                                                                                                                      
[+] DOMAIN => kali.org
osif host_enum(dns_host) > run                                                                                                                                                      

 Analyzing 'kali.org'...

 kali.org,50.116.58.136
urania.kali.org,51.161.119.11
polyhymnia.kali.org,54.39.103.103
hestia.kali.org,192.99.150.26
hera.kali.org,192.99.45.140
download.kali.org,104.18.5.159
discord.kali.org,104.18.5.159
hebe.kali.org,192.99.200.113
image.kali.org,104.18.5.159
nike.kali.org,104.18.5.159
melpomene.kali.org,54.39.52.157
mnemosyne.kali.org,45.33.88.48
terpsichore.kali.org,54.39.49.227
hecate.kali.org,176.31.228.102
pkg.kali.org,192.124.249.9
buildd-arm.kali.org,192.124.249.170
poseidon.kali.org,158.69.125.93
hyperion.kali.org,172.104.26.143
clio.kali.org,172.104.29.198
leto.kali.org,45.33.83.49
redirector.kali.org,104.18.4.159
janitor.kali.org,192.124.249.67
atlas.kali.org,54.39.17.132
docs.kali.org,104.18.4.159
ja.docs.kali.org,104.18.5.159
id.docs.kali.org,104.18.5.159
de.docs.kali.org,104.18.5.159
he.docs.kali.org,104.18.5.159
nl.docs.kali.org,104.18.4.159
cn.docs.kali.org,104.18.4.159
en.docs.kali.org,104.18.5.159
r.docs.kali.org,104.18.4.159
ar.docs.kali.org,104.18.4.159
br.docs.kali.org,104.18.4.159
fr.docs.kali.org,104.18.5.159
tr.docs.kali.org,104.18.4.159
es.docs.kali.org,104.18.4.159
it.docs.kali.org,104.18.5.159
ru.docs.kali.org,104.18.5.159
www.docs.kali.org,104.18.4.159
downloads.kali.org,104.18.4.159
images.kali.org,104.18.4.159
cdimages.kali.org,104.18.4.159
bugs.kali.org,192.124.249.169
iris.kali.org,45.79.132.233
lachesis.kali.org,23.92.17.15
tools.kali.org,104.18.5.159
forums.kali.org,192.124.249.12
cronos.kali.org,192.124.249.29
atropos.kali.org,51.79.80.98
eratos.kali.org,149.56.16.175
epimetheus.kali.org,104.18.4.159
coeus.kali.org,140.211.167.78
zeus.kali.org,144.217.77.182
crius.kali.org,140.211.167.88
dionysus.kali.org,144.217.75.200
status.kali.org,192.124.249.56
get.kali.org,104.18.5.159
git.kali.org,104.18.4.159
autopkgtest.kali.org,192.124.249.38
www.kali.org,104.18.5.159
osif host_enum(dns_host) >
```
#### try the download : 104.18.4.159
```
jumbo@raspberrypi:~/notebooks $ sudo nmap -T4 -Pn -O 104.18.4.159
Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-09 11:20 CST
Nmap scan report for 104.18.4.159
Host is up (0.014s latency).
Not shown: 996 filtered ports
PORT     STATE SERVICE
80/tcp   open  http
443/tcp  open  https
8080/tcp open  http-proxy
8443/tcp open  https-alt
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|PBX
Running (JUST GUESSING): Linux 4.X (87%), Vodavi embedded (86%), FreeBSD 11.X (86%)
OS CPE: cpe:/o:linux:linux_kernel:4.10 cpe:/h:vodavi:xts-ip cpe:/o:freebsd:freebsd:11.0
Aggressive OS guesses: Linux 4.10 (87%), Vodavi XTS-IP PBX (86%), FreeBSD 11.0-RELEASE (86%), FreeBSD 11.0-STABLE (86%)
No exact OS matches for host (test conditions non-ideal).

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.14 seconds
jumbo@raspberrypi:~/notebooks $
```
