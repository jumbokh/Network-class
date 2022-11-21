### check netowrk device 1st
* ls /sys/class/net
### check wireless device status
* sudo nmcli -i wlan0
```
# if show dev is unmanaged, do following command
sudo systemctl stop NetworkManager
sudo systemctl disable NetworkManager
```
* iwconfig
* sudo ifconfig wlan0 up
* sudo iwlist wlan0 scan | grep ESSID
* sudo wpa_passphrase <Your-ESSID> <Your-passphrase> | sudo tee /etc/wpa_supplicant/wpa_supplicant.conf
* sudo wpa_supplicant -c /etc/wpa_supplicant/wpa_supplicant.conf -i wlan0
```
# open a new terminal, check iwconfig
# to see if wlan0 is assoicate with ESSID ap
# than type Ctrl-C from the other terminal
```
# Execute wlan0 connection at background
* sudo wpa_supplicant -B -c /etc/wpa_supplicant/wpa_supplicant.conf -i wlan0
* sudo dhclient wlan0
* sudo ifconfig
