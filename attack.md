### QRLJACKER - QRLJACKING EXPLOITATION FRAMEWORK
```
QRLJACKER - QRLJACKING EXPLOITATION FRAMEWORK
QRLJacker is a highly customizable exploitation framework to demonstrate "QRLJacking Attack Vector" to show how it is easy to hijack services that depend on QR Code as an authentication and login method, Mainly it aims to raise the security awareness regarding all the services using the QR Code as a main way to login users to different services!
👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻. #WHATSAPPHACKING
PREREQUISITES BEFORE INSTALLING:
1.Linux or MacOS. (Not working on windows)
2.Python 3.7+
Installing instructions:
❗Note: Don't install QRLJacker and Firefox as root in a regular user's session because it's not supported by Firefox which would give error on running modules in framework.❗
Important note: If you have multiple python version, use python3.7 command instead of python3 in the following steps and use python3.7 -m pip instead of pip, pip3 or even python3 -m pip because that's the reason of 95% of the issues opened here. I think people often skip the important parts 😄
1.Update Firefox browser to the latest version
2. Install the latest geckodriver from https://github.com/mozilla/geckodriver/releases and extract the file then do :
chmod +x geckodriver
sudo mv -f geckodriver /usr/local/share/geckodriver
sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver
sudo ln -s /usr/local/share/geckodriver /usr/bin/geckodriver
3. Clone the repo with git clone https://github.com/OWASP/QRLJacking
then do  cd QRLJacking/QRLJacker
4. Install all the requirements with pip install -r requirements.txt
5. Now you can run the framework with python3 QrlJacker.py --help
TESTED ON )
Ubuntu 18.04 Bionic Beaver
Kali Linux 2018.x and up
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```