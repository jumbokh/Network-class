### [nmap command](https://hack543.com/nmap-tutorial/)
* nmap -T4 192.168.1.1
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
