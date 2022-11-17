# Network-class
###

### 電腦網路概論 [ppt](https://github.com/jumbokh/Network-class/blob/main/class.7z)
#### 網路概論與ISO七層
* [MAC address Lookup manufacturer](https://macvendors.com/)
#### [Packet Tracer安裝與簡單操作](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/doc/CiscoPacketTracer.pdf)
* [packet tracer下載](https://www.netacad.com/courses/packet-tracer)
### 參考網站
* [澎湖人自由軟體交流CCNA實作講義](http://www.phcno1.net/modules/tad_book3/index.php?op=list_docs&tbsn=21)
* [Packet Tracer 思科模拟器入门教程 之一 初识Packet Tracer](https://blog.csdn.net/gengkui9897/article/details/85107429)
* [Packet Tracer 思科模擬器入門教程 之二 交換機的基本配置與管理](https://www.itread01.com/content/1546225748.html)
* [CSDN-Packet Tracer 思科模拟器入门教程 之二 交换机的基本配置与管理](https://blog.csdn.net/gengkui9897/article/details/85109962?utm_medium=distribute.pc_relevant.none-task-blog-blogcommendfrommachinelearnpai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-blogcommendfrommachinelearnpai2-1.channel_param)
* [CSDN-Packet Tracer 思科模拟器入门教程 之三 交换机的Telnet远程登陆配置](https://blog.csdn.net/gengkui9897/article/details/85141157)
##
### [Packet Tracer Lab](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/README.md)
![address](https://github.com/jumbokh/Network-class/blob/main/NetworkUniv.jpg)
##
* [資安這條路─系統化學習滲透測試](https://ithelp.ithome.com.tw/users/20108446/ironman/4492)
#### [kali Linux 中文設定](https://github.com/jumbokh/Network-class/blob/main/kaliChinese.md)
#### [Kali Linux基礎](https://tw511.com/a/01/33439.html)
```
一、Linux簡介
二、shell
三、SSH系統服務
四、vim編輯器
五、Linux常用命令
六、文字檔案編輯命令
七、檔案目錄管理命令
八、打包壓縮命令
九、搜尋命令
十、檔案管理許可權命令
```
#### [Kali linux images](https://www.kali.org/get-kali/)
#### [install kali on Android system non rooted](https://www.youtube.com/watch?v=KxOGyuGq0Ts&t=1s)
#### [Install Kali Linux on Raspberry Pi 4](https://linuxhint.com/install_kali_linux_raspberry_pi_4/)
* [Raspberry pi image](https://kali.download/arm-images/kali-2022.3/kali-linux-2022.3-raspberry-pi-arm64.img.xz)
#### [如何成為駭客 – 基礎學習篇](https://hack543.com/how-to-become-a-hacker-basic-learning/)
#### [9個常見的 Nmap通訊埠掃描境](https://hack543.com/nmap-tutorial/)
#### [Kali 滲透測試第一章](https://wooyun.js.org/drops/Kali%20Linux%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E5%AE%9E%E6%88%98%20%20%E7%AC%AC%E4%B8%80%E7%AB%A0.html)
#### [資訊蒐集](https://ithelp.ithome.com.tw/articles/10268608)
```
nslookup
dig
dnsenum
whois
fierce
```
![DNS](https://github.com/jumbokh/Network-class/blob/main/PfvqEUM.png)
##
### [nmap](https://github.com/jumbokh/Network-class/blob/main/nmap.md)
#### [install python2.7](https://github.com/jumbokh/Network-class/blob/main/installpy2.md)
#### 設定 python3 為 default python [參考](https://linuxconfig.org/change-default-python-version-on-raspbian-gnu-linuxl)
* Step 1. Add both (all) versions of python installed to the list of "alternatives" for the python binary.
<pre>
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 2
</pre>
* Step 2. Select desired version:
<pre>
sudo update-alternatives --config python
</pre>
##
### [WiFi Crack](https://github.com/jumbokh/Network-class/blob/main/wificrack.md)
#### [安裝並使用virtualenv虛擬環境](https://medium.com/@scofield44165/ubuntu-20-04%E4%B8%AD%E5%AE%89%E8%A3%9D%E4%B8%A6%E4%BD%BF%E7%94%A8virtualenv%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83-install-and-use-virtualenv-in-ubuntu-20-04-7849091ea8e0)
#### [在 Kali Linux 上使用 virtualenv 執行 Python 2 撰寫的 exploit 程式](https://hack543.com/kali-linux-virtualenv-python2-exploit/)
#### Linux系統概論 [大学霸 Kali Linux 安全渗透教程](https://wizardforcel.gitbooks.io/daxueba-kali-linux-tutorial/content/)
* Virtualbox與Kali Linux
* 安裝設定與套件管理
* 檔案與目錄操作
* 排程工作
* 壓縮與解壓縮
* Internet連線網路設定

#### Linux 使用者帳戶權限、群組權限
* 帳號與磁碟空間管理
* 檢視系統資訊
* 管理執行中的程序

#### Shell程式語言
* 建構Shell Script
* 輸出環境設定

#### 架設常用伺服器
* www 伺服器： Apache2
* ftp 伺服器：
* mail 伺服器：
* Samba 伺服器：
* DNS 伺服器：[DNS](https://github.com/jumbokh/Network-class/blob/main/DNS.md)
* DHCP 伺服器：
* NAT 伺服器：

#### 全網滲透
* 內網滲透測試基礎
* 內網資訊收集
* 隱藏通訊隧道技術
* 許可權提升分析及防禦
* 網域控制站安全
* 跨網域攻擊分析及防禦

#### 弱點掃描
* 被動掃描
* 主動掃描
* 程式漏洞分析
* 常見的專業掃描工具
* Web應用程式漏洞掃描

#### [遠端控制](https://github.com/jumbokh/PythonRAT)
* 開啟系統後門
* 生成被控端
* 啟動主控端
* 透過Web應用程式實現遠端控制

#### 滲透攻擊
* Metasploit基礎
* 對作業系統發起攻擊
* 對軟體發起攻擊
* 對用戶發起攻擊
* 利用瀏覽器外掛程式漏洞進行滲透攻擊
* 利用瀏覽器HTA檔案進行滲透攻擊
* 利用瀏覽器巨集病毒進行滲透攻擊
* 使用 Metasploit 對 Web應用的攻擊
