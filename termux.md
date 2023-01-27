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
