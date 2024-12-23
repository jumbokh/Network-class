### 註冊登錄 Cisco Academy
#### https://www.netacad.com/zh-hant/courses/packet-tracer
### 軟體下載
* https://www.netacad.com/portal/resources/packet-tracer
##
### 參考網站
* [澎湖人自由軟體交流CCNA實作講義](http://www.phcno1.net/modules/tad_book3/index.php?op=list_docs&tbsn=21)
* [Packet Tracer 思科模拟器入门教程 之一 初识Packet Tracer](https://blog.csdn.net/gengkui9897/article/details/85107429)
* [Packet Tracer 思科模擬器入門教程 之二 交換機的基本配置與管理](https://www.itread01.com/content/1546225748.html)
* [CSDN-Packet Tracer 思科模拟器入门教程 之二 交换机的基本配置与管理](https://blog.csdn.net/gengkui9897/article/details/85109962?utm_medium=distribute.pc_relevant.none-task-blog-blogcommendfrommachinelearnpai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-blogcommendfrommachinelearnpai2-1.channel_param)
* [CSDN-Packet Tracer 思科模拟器入门教程 之三 交换机的Telnet远程登陆配置](https://blog.csdn.net/gengkui9897/article/details/85141157)
* [蕭老師 個人網頁](http://www.csie.sju.edu.tw/cm/)
* [蕭老師講義](http://www.csie.sju.edu.tw/cm/course/list.htm)
* [Packet Tracer 思科模擬器入門教程 之十七 網路地址轉換NAT配置](https://www.796t.com/content/1546225513.html)
##
### 作業
![lab2-1](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/lab/images/Lab2-1.jpg)
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
```
Router0#ip route 192.168.100.0 255.255.255.0 192.168.50.3
指定192.168.100.0/24的封包往192.168.50.3這個ip送

Router1#ip route 192.168.10.0 255.255.255.0 192.168.50.2
指定192.168.10.0/24的封包往192.168.50.2這個ip送
```
![static Route](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/doc/staticRoutes.jpg)
* [Lab 3-1](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab3-1.pkt)
* [Lab 4a](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab4a.pkt)
    * http://www.phcno1.net/modules/tad_book3/html_all.php?tbsn=21
    * 1-11 動態路由設定 [動態路由學習筆記](https://jimylps.pixnet.net/blog/post/49099264-%E3%80%90cisco%E3%80%91%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E5%8B%95%E6%85%8B%E8%B7%AF%E7%94%B1%E5%8D%94%E8%AD%B0-rip)
    * 2-1 Switch的STP協定
* [Lab 4b](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab4b.pkt)
* [Lab 4c](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab4c.pkt)
* ![Lab4-1 spanning tree](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/lab/images/Lab4-1.jpg)
* ![spanning-tree sw](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/lab/images/Lab5-0.jpg)
* ![spanning-tree show](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/lab/images/Lab5-1.jpg)
* [Lab 5](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab5.pkt)
    * 1. 在二台Switch都執行RSTP
    * 2. 一個port只能允許一台電腦
    * 參考 http://www.phcno1.net/modules/tad_book3/html_all.php?tbsn=21
```
switch>en
switch#conf t
switch(config)# interface fastethernet0/1 ==>設定interface，也可以設定range
switch(config-if)# switchport mode access ==>將這個port設成access port
switch(config-if)# switchport port-security ==>啟用 port-security
switch(config-if)# switchport port-security maximum 1 ==>一個port只能允許一台電腦
switch(config-if)# switchport port-security violation shutdown ==>違反規定者即shutdown
switch(config-if)# switchport port-security mac-address sticky ==>自動學習mac，我們也可以看動輸入
```
* [Lab 6](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab6.pkt)
    * 2-3 switch的基本設定
    * port , vlan
![vlan group](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/lab/images/Lab6-1.jpg)
```
sw0(config)#int range fastethernet 0/10-20
sw0(config)# switch port access vlan 20
```
##
```
** Switch Trunk
* Sw0
    * pc0 - vlan 10 192.168.10.1
	* pc1 - vlan 20 192.168.10.2
* sw1
    * pc2 - vlan 10 192.168.10.3
	* pc3 - vlan 20 192.168.10.4
** vlan setup
sw0(config)# interface fastethernet 0/2
sw0(config)# switchport access vlan 20
** vlan range setup
sw0(config)#int range fastethernet 0/10-20
sw0(config)# switch port access vlan 20
** port Trunk
sw0(config)#int gigafastethernet 0/1 
sw0(config-if)#switchport mode trunk
```
##
#### vlan-1 setup
```
pc0:192.168.10.1 接switch1 f0/1   vlan50
pc1:192.168.10.2 接switch1 f0/2   vlan50
pc3:192.168.10.3 接switch2 f0/1   vlan60
pc4:192.168.10.4 接switch2 f0/2   vlan60
測試pc1   ping    pc2 and pc3
```
![vlan1](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/doc/vlan1.JPG)
##
#### vlan-2 setup
```
pc0~pc3:192.168.10.1~192.168.10.4
pc4~pc7:192.168.10.5~192.168.10.8
vlan10:pc0、pc1、pc4、pc5
vlan20:pc2、pc3、pc6、pc7
Giga1/1設為trunk
```
![vlan + port Trunk](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/doc/vlanPortTrunk.JPG)
##
* [Lab 7](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab7.pkt)
    * switch trunk 2-5-1
* [Lab 7-1](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab7-1.pkt)
* [Lab 8](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab8-1.pkt)
```
3-1 LAB-1
1)在工作區中新增一台CISCO1842的Router及一台PC
2)使用PC透過Console連接到Router進行設定，設定如下：

2-1)Hostname：Taipei
2-2)enable secret：54321
2-3)telnet password：12345
2-4)Fastethernet ip：192.168.10.1/24
2-5)將telnet密碼加密
```
![hw1](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/lab/images/hw1.JPG)
```
3-2 LAB-1
請看下圖，在Packer Tracer中完成，設定好：
```
![hw2](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/lab/images/hw2.JPG)
```
1)CISCO 2811的Fastethernet 0/0與Fastethernet 0/1的IP
2)做好PC0與PC1的網路相關設定
3)測試PC0是否能正確ping到PC1
```
* [Lab 8-2](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab8-2.pkt)
* [路由器設定](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab-router/readme.md)
* [RIPv2+EIGRP]()    
    * http://ccnatiy.blogspot.com/2015/01/ripv2eigrp.html
##
![NetMask](https://github.com/jumbokh/Network-class/blob/main/cisco-lab/doc/netmask.jpg)
* [網路與子網路遮罩](https://notes.andywu.tw/2018/ip%E7%AD%89%E7%B4%9A%E8%88%87%E5%AD%90%E7%B6%B2%E8%B7%AF%E9%81%AE%E7%BD%A9%E4%BB%8B%E7%B4%B9/)
