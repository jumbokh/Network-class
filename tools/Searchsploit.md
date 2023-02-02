* https://ithelp.ithome.com.tw/articles/10223512
* https://www.exploit-db.com/searchsploit
##
#### Install
* sudo apt install snapd
* sudo reboot
* sudo snap install core
* sudo snap install searchsploit
* searchsploit -u
##
#### use
* Basic Search
    * kali@kali:~$ searchsploit afd windows local
* Title Searching
    * kali@kali:~$ searchsploit -t oracle windows
* Removing Unwanted Results
    * kali@kali:~$ searchsploit linux kernel 3.2 --exclude="(PoC)|/dos/"
* Piping Output (Alternative Method of Removing Unwanted Results)
    * kali@kali:~$ searchsploit XnView | grep -v '/dos/'
    * kali@kali:~$ searchsploit XnView | wc -l
* Colour Output
    * kali@kali:~$ searchsploit wordpress mail list
* Copy To Clipboard
    * kali@kali:~$ searchsploit -p 39446
