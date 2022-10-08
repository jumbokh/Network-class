# Network-class
###

### 電腦網路概論 [ppt](https://github.com/jumbokh/Network-class/blob/main/class.7z)
#### 網路概論與ISO七層
#### [Packet Tracer安裝與簡單操作](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/doc/CiscoPacketTracer.pdf)
* [packet tracer下載](https://www.netacad.com/courses/packet-tracer)
### 參考網站
* [澎湖人自由軟體交流CCNA實作講義](http://www.phcno1.net/modules/tad_book3/index.php?op=list_docs&tbsn=21)
* [Packet Tracer 思科模拟器入门教程 之一 初识Packet Tracer](https://blog.csdn.net/gengkui9897/article/details/85107429)
* [Packet Tracer 思科模擬器入門教程 之二 交換機的基本配置與管理](https://www.itread01.com/content/1546225748.html)
* [CSDN-Packet Tracer 思科模拟器入门教程 之二 交换机的基本配置与管理](https://blog.csdn.net/gengkui9897/article/details/85109962?utm_medium=distribute.pc_relevant.none-task-blog-blogcommendfrommachinelearnpai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-blogcommendfrommachinelearnpai2-1.channel_param)
* [CSDN-Packet Tracer 思科模拟器入门教程 之三 交换机的Telnet远程登陆配置](https://blog.csdn.net/gengkui9897/article/details/85141157)
##
* [Lab 1](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab1.pkt)
    * switch+2pc config
* [Lab 2](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab2.pkt)
* [Lab 2-2](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab-2-1-2.pkt)
* [Lab 2-3](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab-2-1-3.pkt)
    * 參考: http://www.phcno1.net/modules/tad_book3/html_all.php?tbsn=21
    * 1-4 ~ 1-9  設定 CISCO1841 Router
* ![lab2](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab2.png)
* [Lab 3](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab3.pkt)
    * 參考 http://www.phcno1.net/modules/tad_book3/page.php?tbdsn=517
    * 設定路由, 使得 192.168.100.2 可以 ping 192.168.10.3 的電腦
* [Lab 3-1](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab3-1.pkt)
* [Lab 4a](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab4a.pkt)
    * http://www.phcno1.net/modules/tad_book3/html_all.php?tbsn=21
    * 1-11 動態路由設定
    * 2-1 Switch的STP協定
* [Lab 4b](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab4b.pkt)
* [Lab 4c](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab4c.pkt)
* [Lab 5](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab5.pkt)
    * 1. 在二台Switch都執行RSTP
    * 2. 一個port只能允許一台電腦
    * 參考 http://www.phcno1.net/modules/tad_book3/html_all.php?tbsn=21
* [Lab 6](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab6.pkt)
    * 2-3 switch的基本設定
    * port , vlan
* [Lab 7](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab7.pkt)
    * switch trunk 2-5-1
* [Lab 7-1](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab7-1.pkt)
* [Lab 8](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab8-1.pkt)
<pre>
3-1 LAB-1
1)在工作區中新增一台CISCO1842的Router及一台PC
2)使用PC透過Console連接到Router進行設定，設定如下：

2-1)Hostname：Taipei
2-2)enable secret：54321
2-3)telnet password：12345
2-4)Fastethernet ip：192.168.10.1/24
2-5)將telnet密碼加密

3-2 LAB-1
請看下圖，在Packer Tracer中完成，設定好：

1)CISCO 2811的Fastethernet 0/0與Fastethernet 0/1的IP
2)做好PC0與PC1的網路相關設定
3)測試PC0是否能正確ping到PC1
</pre>
* [Lab 8-2](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab8-2.pkt)
* [路由器設定](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab-router/readme.md)
* [RIPv2+EIGRP]()    
    * http://ccnatiy.blogspot.com/2015/01/ripv2eigrp.html
* Lab1. 新增硬體
* Lab2. 設定PC
* Lab3. 增加模組至設備中
* Lab4. 設定路由
##
#### 交換機的基本配置與管理
* Lab5. Switch 的 STP設置
* Lab6. Switch Trunk

#### 路由器
* 設定路由與動態路由
* 動態路由RIPv2
* 子網路切割
* 路由協定 EIGRP 設定

#### 整合實驗
* Lab9. 實驗一
* Lab10. 實驗二

#### Linux系統概論
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
* DNS 伺服器：
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

#### 遠端控制
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
