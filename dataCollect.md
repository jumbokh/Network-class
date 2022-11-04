### From Domain name
```
nslookup kali.org
dig kali.org
dnsenum kali.org
whois kali.org
```
#### nslookup
* [如何使用 nslookup 指令查詢 DNS 紀錄？](https://kb.synology.com/zh-tw/DSM/tutorial/How_do_I_check_the_DNS_records_with_nslookup)
```
(env) jumbo@jumbo-nb:~/notebooks$ nslookup dns.hinet.net
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   dns.hinet.net
Address: 168.95.1.1
Name:   dns.hinet.net
Address: 168.95.192.1
Name:   dns.hinet.net
Address: 2001:b000:168::2
Name:   dns.hinet.net
Address: 2001:b000:168::1

(env) jumbo@jumbo-nb:~/notebooks$ nslookup www.google.com
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   www.google.com
Address: 172.217.163.36
Name:   www.google.com
Address: 2404:6800:4012:4::2004

(env) jumbo@jumbo-nb:~/notebooks$ 
```
#### dig
* [dig](https://charlie-c.me/post/dig/)
* [DNS 問題除錯 dig 指令使用教學與範例](https://officeguide.cc/dns-problem-dig-debug-tutorial-examples/)
