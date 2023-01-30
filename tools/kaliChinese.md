### [Kali 中文化](https://hack543.com/kali-linux-2021-tradictional-chinese-env/)
#### locales
* sudo dpkg-reconfigure locales
```
1. 往下找到: "zh_TW.UTF-8 UTF-8"
2. 確定
```
#### kali Linux 中文環境 -- 中文字型 , 輸入法
```
sudo apt-get update
# 安裝文鼎中文明體與 Google Noto Sans CJK 字型
sudo apt install fonts-arphic-uming fonts-noto-cjk
# 安裝 fcitx5 中文輸入框架、新酷音輸入法 (New Chewing) 與桌面環境輸入法設定工具 (im-config)
sudo apt install fcitx5 fcitx5-chewing im-config 
### 指定 Kali Linux 視窗字型為文鼎中文明體
```
![setting](https://github.com/jumbokh/Network-class/blob/main/images/kali-setting-manager-shortcut.jpg)
#### (1) 開啟 Kali Linux 選單，並點擊右下角的 Setting Manager 圖示
#### (2) 點擊「Appearance」，選擇第 3 個 Tab 「Fonts」
#### (3) 點擊 「Default Font」中間的字型條，並選擇使用文鼎中文明體字型 (AR PL UMing TW MBE Light)，Size 選擇 12。
##
### 設定 fcitx5 輸入法
#### (1). 開啟終端機，執行 im-config 指令。點擊 「OK」 鈕繼續。
#### (2). 下一步，選擇「Yes」，覆蓋原本的輸入法設定。
#### (3). 下一步，選擇「fcitx5」輸入法，點擊「OK」按鈕。
#### (4). 視窗顯示輸入法設定結果，點擊「OK」按鈕。
#### (5). 設定完畢輸入法，需要重新啟動 Xsession，請登出 (Logout) 再登入。
