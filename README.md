## git clone SSL error for vpn :
### git config --global http.sslBackend openssl
## [sploitscan](https://github.com/xaitax/SploitScan)
## [期末報告](https://github.com/jumbokh/Network-class/blob/main/Final.md)
## [payload](https://docs.rapid7.com/metasploit/working-with-payloads/)
* [Tutoring](https://github.com/xalgord/Massive-Web-Application-Penetration-Testing-Bug-Bounty-Notes)
* [DVWA target](https://ithelp.ithome.com.tw/articles/10207050)
* [OSIF install](https://osif.laet4x.com/installation)
### ubuntu install OSIF tools
```
sudo apt-get install python3-chardet
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
pip install faust-cchardet
pip3 install cython
pip3 install cchardet aiodns
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
pip3 install twint
sudo apt-get -y install python3-async-timeout
pip install aiodns
pip install async-timeout
pip install --upgrade aiohttp
pip install --upgrade aiohttp_socks
```
#### wordlist: https://github.com/kkrypt0nn/wordlists
####  aircrack-ng -w /usr/share/wordlists/rockyou.txt /root/桌面-1.cap
#### 課綱
* w1. 網路概論 -- Packet Tracer安裝與簡單操作
* w2. CCNA 實作 交換機設定
* w3. 228和平紀念日
* w4. CCNA 實作 路由與 VLAN
* w5. Kali Linux on oracle virtualbox, 安裝與網路設定
```
1.進入 正修訊息網, 選擇圖書資訊->圖資雲教室->第一次使用, 需下載用戶端程式->桌面雲-程式AI雲
2. 下載安裝 virtualbox
3. 開啟檔案總管, 啟用網路與共享
4. 複製本地端下載中的 kali 及 metasploit 的 vm 至 雲端的文件, 並解開
   kali的使用者及密碼:  kali/kali
   meta的使用者及密碼: msfadmin/msfadmin
5. 開啟 virtualbox, 新增虛擬機
6. kali 的網路 及 metasploit 的網路設定為:僅限主機介面卡+virtualbox host-only Ethernet Adapter
7. 開啟 kali, 打開終端機, 輸入:
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install kali-linux-everything
$ sudo reboot
假設 kali 的 ip: 192.168.56.102, meta 的 ip: 192.168.56.101
從 kali ping meta:
$ sudo ping 192.168.56.101
```
## 靶機
* [VM](https://www.vulnhub.com/)
* [本地架設攻防](https://feifei.tw/qcon-003-how-to-set-up-a-cybersecurity-lab-locally/)
* [Target](https://github.com/jumbokh/Network-class/blob/main/target.md)
##
## 資訊收集
* [kali](https://blog.51cto.com/u_15309736/5471646)
##
### [軟路由](https://cloud.tencent.com/developer/article/1850766)
![kali](https://github.com/jumbokh/Network-class/blob/main/images/kali.PNG)
### [Install Metasploit on Kali Linux using Terminal](https://www.fosslinux.com/48112/install-metasploit-kali-linux.htm)
* sudo apt install metasploit-framework
```
Starting the Kali PostgreSQL service
If PostgreSQL isn’t running, use the following command to run it:
```
* sudo /etc/init.d/postgresql start 
* sudo /etc/init.d/postgresql status 
```
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb> msfinstall && chmod 755 && msfinstall && ./msfinstall

$ sudo msfdb init
```
* msfconsole -q
* [metasploit use reference](https://github.com/jumbokh/Network-class/blob/main/tools/metasploitable.md)
* [metasploit-cve-search](https://github.com/ferdinandmudjialim/metasploit-cve-search/tree/main)
* [cve_list.txt](https://github.com/jumbokh/Network-class/blob/main/cve_list.txt)
* w6. 網路安全滲透測試的相關理論和工具, 滲透測試報告的編寫
    * [網站漏洞掃描 Acunetix Web Vulnerability Scanner](https://ithelp.ithome.com.tw/articles/10008411)
    * [如何编写一份专业的渗透测试报告](https://www.anquanke.com/post/id/215031)
    * [如何寫好一份滲透測試報告](https://read01.com/zh-tw/4nnzay4.html#.ZBh0XXZByUk)
    * [某單位網站弱點掃描報告](https://github.com/jumbokh/Network-class/blob/main/refers/%E6%9F%90%E5%96%AE%E4%BD%8D%E7%B6%B2%E7%AB%99%E6%8E%83%E6%8F%8F%E5%A0%B1%E5%91%8A.pdf)
    * [public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports)
    * [渗透测试报告](https://www.doc88.com/tag/%E3%80%90%E7%B2%BE%E5%93%81%E3%80%91%E9%9F%B6%E5%85%B3%E7%A7%BB%E5%8A%A8%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A111206)
* w7. 資訊蒐集 -- whois, nslookup, dig, nmap
    * [Data collect](https://github.com/jumbokh/Network-class/blob/main/tools/dataCollect.md)
    * [nmap](https://github.com/jumbokh/Network-class/blob/main/tools/nmap.md)
    * [WiFi Crack](https://github.com/jumbokh/Network-class/blob/main/pentest/wificrack.md)
    * [DNS 問題除錯 dig 指令使用教學與範例](https://officeguide.cc/dns-problem-dig-debug-tutorial-examples/)
* w8. 兒童節
* w9. 期中考
* w10. NMAP + scripts 進行漏洞掃描 + Metasploit 系統漏洞分析
    * [SSH Pentesting Guide](https://community.turgensec.com/ssh-hacking-guide/?fbclid=IwAR2qItiPOu3CD689o6qoECpEjTZq2Vp4tyL0NQMnERpmoes8XVbWo_ZrzyY)
    * [Lab1:nmap attack](https://github.com/jumbokh/Network-class/blob/main/tools/Lab1.md)
    * [nmap + vulscan](https://github.com/jumbokh/Network-class/blob/main/pentest/HackingTools.md)
    * [vuln scan](https://github.com/jumbokh/Network-class/blob/main/pentest/Vuln-Map.md)
* w11. 靶機建立 (Metasploitable ), 以Docker建立工具環境
    * [Metasploitable](https://github.com/jumbokh/Network-class/blob/main/tools/metasploitable.md)
    * [Lab4: Metasploit Framework](https://github.com/jumbokh/Network-class/blob/main/refers/lab4-instruction.pdf)
    * [參考: Pentest lab - Metasploitable 2](https://chousensha.github.io/blog/2014/06/03/pentest-lab-metasploitable-2/)
* w12. osif 漏洞掃描, metasploit-framework 漏洞文件
    * [Lab2](https://github.com/jumbokh/Network-class/blob/main/tools/Lab2.md)
    * [Lab7: Wireless Exploitation & Defense](https://github.com/jumbokh/Network-class/blob/main/refers/lab7-instruction.pdf)
* w13. terminux + Nethunter on Android system
    * [Youtube](https://www.youtube.com/watch?v=KxOGyuGq0Ts)
    * [wifite]()
    * [termux](https://github.com/jumbokh/Network-class/blob/main/tools/termux.md)
* w14. USB rubber ducky 介紹
    * [Top10 OSINT](https://seon.io/resources/comparisons/osint-software-tools/)
    * [Nessus Download](https://www.tenable.com/downloads/nessus?loginAttempted=true)
    * [Nessus install](https://linux.how2shout.com/how-to-install-configure-nessus-on-ubuntu-20-04/)
    * [pentest](https://github.com/jumbokh/Network-class/blob/main/pentest/pentest.md)
    * [Bad USB key](https://github.com/jumbokh/Network-class/blob/main/pentest/badUSB.md)
    * [Attiny85 Bootloader](https://github.com/Jasdoge/Attiny85-Bootloader-Tutorial)
    * [pico keyboard micropython](https://www.hackster.io/TomoDesigns/the-super-easy-pico-keyboard-989e7d)
    * [Fix error Downloading](https://www.linuxndroid.com/2022/12/not-downloading-how-to-fix-digistump.html)
    * [Attiny85 Install 1](https://learn.sparkfun.com/tutorials/how-to-install-an-attiny-bootloader-with-virtual-usb)
    * [Attiny85 Install QA](https://bbs.pigoo.com/thread-67527-1-1.html)
    * [Attiny85教學](https://jimirobot.tw/arduino-tutorial-attiny-attiny85-usb/)
    * [Attiny85 project](http://highlowtech.org/?p=1695)
    * json:
        * http://drazzy.com/package_drazzy.com_index.json
        * http://digistump.com/package_digistump_index.json
    * RGB DHT11 project:
        * [ref. url](https://www.instructables.com/Temperature-Humidity-Monitoring-Using-Digispark-US/)
        * [arduino code](https://github.com/jumbokh/Network-class/blob/main/source/rgb_dht11_digispark_.ino)
        * [DHT.zip](https://github.com/jumbokh/Network-class/blob/main/source/DHT.zip)
* w15. 期末考
* 練習
    * [Lab Attack](https://github.com/jumbokh/Network-class/blob/main/tools/Lab-attack.md)
    * [Lab-metasploit](https://github.com/jumbokh/Network-class/blob/main/tools/Lab-metasploit.md)
    * [Lab1 : nmap](https://github.com/jumbokh/Network-class/blob/main/tools/Lab1.md)
    * [Lab2 : Find the vulnerable host](https://github.com/jumbokh/Network-class/blob/main/tools/Lab2.md)
    * [Lab3 : osif check host](https://github.com/jumbokh/Network-class/blob/main/tools/Lab3.md)
    * [Lab4-Metasploit](https://github.com/jumbokh/Network-class/blob/main/tools/Lab4-Metasploit.md)
##
* docker run --name container-name -it tleemcjr/metasploitable2:latest sh -c "/bin/services.sh && bash"
* ![jobs](https://github.com/jumbokh/Network-class/blob/main/images/Jobs.jpg)
# Network-class
### [Network Basic](https://github.com/jumbokh/Network-class/blob/main/tools/Network-Basic.md)
### 電腦網路概論 [ppt](https://github.com/jumbokh/Network-class/blob/main/tools/class.7z)
* [資安這條路─系統化學習滲透測試](https://ithelp.ithome.com.tw/users/20108446/ironman/4492)
#### [kali Linux 中文設定](https://github.com/jumbokh/Network-class/blob/main/tools/kaliChinese.md)
#### [Kali Linux基礎](https://tw511.com/a/01/33439.html)
#### [tryHackMe](https://tryhackme.com/dashboard)
#### [Honeypot Or Not?](https://honeyscore.shodan.io/?fbclid=IwAR34JUm-wj8BBMi1eEEF_rLk8VfA2Ut7OJpAh6j0eIhSLrJVCz-M3NU7KUQ)
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
#### [Linux for Beginner](https://github.com/jumbokh/Network-class/blob/main/refers/Linux%20For%20Beginners%20Including%20commandline.pdf)
#### [kali vm 安裝](https://ithelp.ithome.com.tw/articles/10298620)
* login: kali password: kali
* 打開 terminal
* sudo apt-get update
* sudo apt-get upgrade
* sudo apt-get install kali-linux-everything
##
#### [打造 Kali Linux 2021 中文桌面環境(字型、中文輸入法)](https://hack543.com/kali-linux-2021-tradictional-chinese-env/)
#### [Kali linux images](https://www.kali.org/get-kali/)
#### [install kali on Android system none rooted](https://www.youtube.com/watch?v=KxOGyuGq0Ts&t=1s)
#### [Android手機安裝Kali Linux步驟](https://github.com/jumbokh/Network-class/blob/main/refers/Android%20Kali%20NetHunter%20Install%20-%20v3.pdf)
* [termux/termux-app](https://github.com/termux/termux-app)
#### [Install Kali Linux on Raspberry Pi 4](https://linuxhint.com/install_kali_linux_raspberry_pi_4/)
* [Raspberry pi image](https://kali.download/arm-images/kali-2022.3/kali-linux-2022.3-raspberry-pi-arm64.img.xz)
#### [如何成為駭客 – 基礎學習篇](https://hack543.com/how-to-become-a-hacker-basic-learning/)
#### [9個常見的 Nmap通訊埠掃描境](https://hack543.com/nmap-tutorial/)
#### [Kali 滲透測試第一章](https://wooyun.js.org/drops/Kali%20Linux%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E5%AE%9E%E6%88%98%20%20%E7%AC%AC%E4%B8%80%E7%AB%A0.html)
#### [資訊蒐集](https://ithelp.ithome.com.tw/articles/10268608)
#### [CyberSecurity](https://github.com/NafisiAslH/KnowledgeSharing)
#### [Blockchain Security](https://github.com/NafisiAslH/KnowledgeSharing/tree/main/BlockchainSecurity)
```
nslookup
dig
dnsenum
whois
fierce
```
![DNS](https://github.com/jumbokh/Network-class/blob/main/images/PfvqEUM.png)
##
### [nmap](https://github.com/jumbokh/Network-class/blob/main/tools/nmap.md)
### Dracnmap
```
Dracnmap is an open source program which is using to exploit the network and gathering information with nmap help. Nmap command comes with lots of options that can make the utility more robust and difficult to follow for new users. Hence Dracnmap is designed to perform fast scaning with the utilizing script engine of nmap and nmap can perform various automatic scanning techniques with the advanced commands.
Getting Started
git clone https://github.com/Screetsec/Dracnmap.git
cd Dracnmap
chmod +x Dracnmap.sh 
sudo ./Dracnmap.sh or sudo su ./Dracnmap.sh 
Requirements
A linux operating system. We recommend Kali Linux 2 or Kali 2016.1 rolling / Cyborg / Parrot / Dracos / BackTrack / Backbox / and another operating system ( linux )
Must install nmap
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```
#### [install python2.7](https://github.com/jumbokh/Network-class/blob/main/tools/installpy2.md)
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
### THECHOICE TOOL
```
THECHOICE TOOL All in one tools
installation commands in termux.
Installation Commands
apt update && apt upgrade
pkg install git -y
git clone https://github.com/8L4NK/thechoice
cd thechoice
chmod +x thechoice
bash thechoice
NOW ENJOY AND USE THE TOOL... 🫡
Note:- This tool is only for educational purposes. We are not responsible for any misuse or illegal activities.
```
##
### Lazymux
* git clone https://github.com/Gameye98/Lazymux
```
Lazymux is a tool installer that is specially made for termux user which provides a lot of tool mainly used tools in termux and its easy to use, Lazymux install any of the given tools provided by it from itself with just one click, and its often get updated.
FEATURE
Tool Installation
Install Single Tool
lzmx > set_install 1
Install Multi Tool
lzmx > set_install 1 2 3 4
Install All Tool
lzmx > set_install @
Default Dir Install On lazymux.conf replace symbol ~ with directory you want
Example: lazymux.conf
HOME = /sdcard
Requirements
• Python 3.x
Installation and Using Lazymux
apt install python git
git clone https://github.com/Gameye98/Lazymux
cd Lazymux
python lazymux.py
ENJOY 🫡 Sharing is caring
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```
### RED_HAWK -- All in one tool for Information Gathering and Vulnerability Scanning
* https://github.com/Tuhinshubhra/RED_HAWK
```
Installation:
Run The Tool and Type fix This will Install All Required Modules.
For The Bloggers View To Work Properly you have to configure RED HAWK with moz.com's api keys for that follow the following steps:
How To Configure RED HAWK with moz.com for Bloggers View Scan

Create an account in moz follow this link : https://moz.com/community/join
After successful account creation and completing the verification you need to generate the API Keys
You can get your API Keys here: https://moz.com/products/mozscape/access
Get your AccessID and SecretKey and replace the $accessID and $secretKey variable's value in the config.php file
All set, now you can enjoy the bloggers view.
Usage:
git clone https://github.com/Tuhinshubhra/RED_HAWK
cd RED_HAWK
php rhawk.php
Use the "help" command to see the command list or type in the domain name you want to scan (without Http:// OR Https://).
Select whether The Site Runs On HTTPS or not.
Select the type of scan you want to perform
Leave the rest to the scanner
List of CMS Supported
RED HAWK's CMS Detector currently is able to detect the following CMSs (Content Management Systems) in case the website is using some other CMS, Detector will return could not detect.

WordPress
Joomla
Drupal
Magento
```
##
```
Brutal
Brutal is a toolkit to quickly create various payload,powershell attack , virus attack and launch listener for a Human Interface Device
Getting Started
git clone https://github.com/Screetsec/Brutal.git
cd Brutal
chmod +x Brutal.sh
sudo ./Brutal.sh or sudo su ./Brutal.sh
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```
### Fatrat -- exploiting tool
* [fatRat](https://github.com/jumbokh/Network-class/blob/main/tools/FatRar.md)
### Brutesploit
```
Brutesploit
BruteSploit is a collection of method for automated Generate, Bruteforce and Manipulation wordlist with interactive shell. That can be used during a penetration test to enumerate and can be used in CTF for manipulation,combine,transform and permutation some words or file text 😛 i wrote this just for fun and learn how create interactive shell is work
Getting Started
git clone https://github.com/Screetsec/Brutesploit.git
cd Brutesploit
chmod +x Brutesploit 
sudo ./Brutesploit or sudo su ./Brutesploit 
A linux operating system. We recommend :
Kali Linux 2 or Kali 2016.1 rolling
Cyborg
Parrot
BackTrack
Backbox
```
### Metasploit on Termux
```
Metasploit on Termux
Last complete installation method! 
apt-get update -y
apt-get upgrade -y
# use pkg install python
apt install python python2 -y
pip install lolcat
git clone https://github.com/h4ck3r0/Metasploit-termux
cd $HOME
cd Metasploit-termux
chmod +x *
bash metasploit.sh
```
### Facebook-BruteForce Tool
```
Facebook-BruteForce Tool
Install Requirements "On Linux"
$ git clone https://github.com/IAmBlackHacker/Facebook-BruteForce
$  cd Facebook-BruteForce
$ python3 -m pip install requests bs4
$  python3 -m pip install mechanize
$ python3 fb.py or python fb2.py
```
### TorBot:-- Dark Web OSINT Tool.
```
TorBot:-- Dark Web OSINT Tool.
Features:-
1. Onion Crawler (.onion). (Completed)
2. Returns Page title and address with a short description of the site. (Partially Completed)
3. Save links to the database. (PR to be reviewed)
4. Get emails from the site. (Completed)
5. Save crawl info to JSON file. (Completed)
6. Crawl custom domains. (Completed)
7. Check if the link is live. (Completed)
8. Built-in Updater. (Completed)
9. TorBot GUI (In progress)
10. Social Media integration. (not Started)
11. Build a visual tree of link relationships that can be quickly viewed or saved to an image file (Completed)
#Download #Link:-
https://github.com/DedSecInside/TorBot
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```
### [sqlmap](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-zh-CN.md)
```
python sqlmap.py -u "http://testphp.vulnweb.com/listproducts.php?cat=1" --batch --banner
```
* ![sqlmap](https://github.com/jumbokh/Network-class/blob/main/images/sqlmap1.JPG)
* ![sqlmap1](https://github.com/jumbokh/Network-class/blob/main/images/sqlmap2.JPG)
### RouterSploit - Exploitation Framework for Embedded Devices that can run in Termux
```
RouterSploit - Exploitation Framework for Embedded Devices that can run in Termux
It consists of various modules that aid penetration testing operations:
1) exploits - modules that take advantage of identified vulnerabilities
2) creds - modules designed to test credentials against network services…… 顯示更多
RouterSploit - 可在 Termux 中運行的嵌入式裝置開發框架
它由各種輔助滲透測試操作的模組組組成:
1) 剝削 - 利用認定脆弱性的模組
2) creds - 旨在測試憑證對抗網路服務的模組
3) 掃描器 - 檢查目標是否容易受到任何剝削的模組
4)有效載荷 - 負責為各種架構和注射點產生有效載荷的模組
5) 通用 - 執行通用攻擊的模組
使用有效載載模組,我能夠在自己測試的路由器上識別弱的webconsole管理員密碼。
https://github.com/threat9/routersploit
```
### [DarkArmy tools](https://github.com/jumbokh/Network-class/blob/main/tools/DarkArmy.md)
### WEBSCRAPE
```
TERMUX INSTALLATION GUIDE 
pkg update -y 
pkg upgrade -y 
pkg install git 
git clone https://github.com/3xploitGuy/webscrape.git
cd webscrape 
webscrape
chmod +x webscrape.sh 
webscrape 
bash webscrape.sh
You must have use https://....
INSTALLING AND REQUIREMENTS
Linux or Unix-based system
~ ❯❯❯ git clone https://github.com/3xploitGuy/webscrape.git
~ ❯❯❯ cd webscrape
~/webscrape ❯❯❯ chmod +x webscrape.sh
~/webscrape ❯❯❯ ./webscrape.sh
SHARING IS CARING
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```
* ![webscrape](https://github.com/jumbokh/Network-class/blob/main/images/168756.jpg)
### [Lazymux](https://github.com/jumbokh/Network-class/blob/main/tools/Lazymux.md)
### [Rauton:-- Bug Bounty Recon Tool.](https://github.com/jumbokh/Network-class/blob/main/pentest/rauton.md)
### [Vegile - Ghost In The Shell](https://github.com/jumbokh/Network-class/blob/main/tools/Vegile.md)
### [Crassus Windows privilege escalation discovery tool](https://github.com/vullabs/Crassus?fbclid=IwAR2J_u-oqZ9GJw4fc8jH5zmjR9M028wsx98LMo-9KUnyFSI9EhgtbO6bD-A)
### [bad USB](https://github.com/jumbokh/Network-class/blob/main/pentest/badUSB.md)
### shells : A script for generating common revshells fast and easy.
```
git clone https://github.com/4ndr34z/shells
cd shells
./install.sh
```
### [LFIMap -- Local file inclusion discovery and exploitation tool](https://github.com/jumbokh/Network-class/blob/main/tools/LFIMap.md)
### dBmonster :-- Track WiFi Devices With Their Received Signal Strength. 
```
Features:-
1. Listing WiFi interfaces
2. Track & scan on 2.4GHz
3. Track & scan on 5GHz
4. Scanning for AP
5. Scanning for STA
6. Beep when a device found
Download Link:-
https://github.com/90N45-d3v/dBmonster
Sharing is Caring
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```
### [WiFi Crack](https://github.com/jumbokh/Network-class/blob/main/pentest/wificrack.md)
### [osint-framework](https://github.com/fr4nc1stein/osint-framework)
### [DDOS](https://github.com/jumbokh/Network-class/blob/main/pentest/DDOS.md)
#### [安裝並使用virtualenv虛擬環境](https://medium.com/@scofield44165/ubuntu-20-04%E4%B8%AD%E5%AE%89%E8%A3%9D%E4%B8%A6%E4%BD%BF%E7%94%A8virtualenv%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83-install-and-use-virtualenv-in-ubuntu-20-04-7849091ea8e0)
#### [在 Kali Linux 上使用 virtualenv 執行 Python 2 撰寫的 exploit 程式](https://hack543.com/kali-linux-virtualenv-python2-exploit/)
* [靶機metasploitable 2 virtualbox download](https://sourceforge.net/projects/metasploitable/)
#### Linux系統概論 [大学霸 Kali Linux 安全渗透教程](https://wizardforcel.gitbooks.io/daxueba-kali-linux-tutorial/content/)
* Virtualbox與Kali Linux
* 安裝設定與套件管理
* 檔案與目錄操作
* 排程工作
* 壓縮與解壓縮
* Internet連線網路設定
* [pdf : Linux Bible 9th-ed](https://drive.google.com/file/d/1Qp4Qrs8kgditW_SrAk5X9gyzPEUI6J4o/view?usp=sharing)
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
* DNS 伺服器：[DNS](https://github.com/jumbokh/Network-class/blob/main/tools/DNS.md)
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
* [滲透實驗網站](https://www.vulnmachines.com/?fbclid=IwAR3KL2xf8_mTqsrlbLC6CQaihpuPYhQwjmOmxyK0AbH_LKtuaM7uYwh8i_g)
#### Docker
* [How to Create a Docker Image From a Container](https://www.dataset.com/blog/create-docker-image/)
* [靶機 metaploitable](https://drive.google.com/file/d/1Pz14NMxzjTKIP2jFX0xhR7nEfCe7QSoN/view?usp=sharing)
* [弱點架設](https://github.com/jumbokh/VulApps)
#### 參考
### [FB Zeroday](https://www.facebook.com/ZeroDayExploitware)
```
Cyber-Bookmarks
A list of bookmarks I have used since I started my journey in cyber security 
Follow up: https://twitter.com/devmehedi101
                  https://www.youtube.com/@SecurityTalent
                  https://t.me/Securi3yTalent
https://x0rb3l.github.io/Cyber-Bookmarks/bookmarks.html
```
* password dictionary download: https://github.com/steveklabnik/password-cracker/blob/master/dictionary.txt
##
* [一个U盘黑掉你：HID攻击之TEENSY实战](https://bbs.kanxue.com/thread-191606.htm)
* [一个U盘黑掉你：TEENSY实战](https://maoxian.de/2014/07/1160.html)
* [一個U盤黑掉你：HID攻擊之TEENSY實戰](https://read01.com/nmegJz.html#.Y9tStXZByUk)
* [tvhelper](https://github.com/wukongdaily/tvhelper)
##
* [整合nmap & metasploit小試身手](https://ithelp.ithome.com.tw/articles/10225010)
* [top 500 hacking tool](https://github.com/shubhamg0sai/All_top_500_hacking_tool)
* [csc Cyber security Practice](https://cse.sustech.edu.cn/faculty/~zhangfw/18sp-csc4992/)
* [Hacking eBooks](https://github.com/C0MPL3XDEV/Hacking-Security-Ebooks)
