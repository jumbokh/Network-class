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
