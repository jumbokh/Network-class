### 軟體下載
* https://www.netacad.com/portal/resources/packet-tracer
##
### 參考網站
* [澎湖人自由軟體交流CCNA實作講義](http://www.phcno1.net/modules/tad_book3/index.php?op=list_docs&tbsn=21)
* [Packet Tracer 思科模拟器入门教程 之一 初识Packet Tracer](https://blog.csdn.net/gengkui9897/article/details/85107429)
* [Packet Tracer 思科模擬器入門教程 之二 交換機的基本配置與管理](https://www.itread01.com/content/1546225748.html)
* [CSDN-Packet Tracer 思科模拟器入门教程 之二 交换机的基本配置与管理](https://blog.csdn.net/gengkui9897/article/details/85109962?utm_medium=distribute.pc_relevant.none-task-blog-blogcommendfrommachinelearnpai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-blogcommendfrommachinelearnpai2-1.channel_param)
* [CSDN-Packet Tracer 思科模拟器入门教程 之三 交换机的Telnet远程登陆配置](https://blog.csdn.net/gengkui9897/article/details/85141157)
##
### 作業
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
    * 1-11 動態路由設定
    * 2-1 Switch的STP協定
* [Lab 4b](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab4b.pkt)
* [Lab 4c](https://github.com/jumbokh/class1091/blob/master/cisco-lab/lab/lab4c.pkt)
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
pc0:192.168.10.1 接switchf0/1   vlan50
pc1:192.168.10.2 接switchf0/2   vlan50
pc3:192.168.10.3 接switchf0/3   vlan60
pc4:192.168.10.4 接switchf0/4   vlan60
測試pc1   ping    pc2 and pc3
```
##
#### vlan-2 setup
```
pc0~pc3:192.168.10.1~192.168.10.4
pc4~pc7:192.168.10.5~192.168.10.8
vlan10:pc0、pc1、pc4、pc5
vlan20:pc2、pc3、pc6、pc7
Giga1/1設為trunk
```
##
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
