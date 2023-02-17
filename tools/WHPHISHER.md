##
* https://github.com/WhBeatZ/WhPhisher.git
```
WHPHISHER
The best tool for phishing with the most famous pages updated.
Tested on:
Termux, Kali Linux and debian
Steps
To make this tool less likely to fail, it is advised to install the latest version of Termux, and the Termux API.
How to install --
pkg install bash
pkg install git
git clone https://github.com/WhBeatZ/WhPhisher.git
cd WhPhisher
chmod +x *
bash requisitoswh.sh
Solution if the link is not generated or does not work (2 solutions)
- - - Solution 1 - - -
Open new session
cd NgrokWh
chmod +x ngrokwh.sh
./ngrokwh.sh
and
ngrok http 8080
Solution 2 - - -
Steps:
We open a new session
cd
pkg install openssh -y
ssh -R 80:localhost:8080 nokey@localhost.run
```
