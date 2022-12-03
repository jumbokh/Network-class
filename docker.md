```
kali@kali:~$ sudo apt update
kali@kali:~$
kali@kali:~$ sudo apt install -y docker.io
kali@kali:~$
kali@kali:~$ sudo systemctl enable docker --now
kali@kali:~$
kali@kali:~$ docker
kali@kali:~$
```
#### https://computingforgeeks.com/install-docker-and-docker-compose-on-kali-linux/
```
sudo apt update && sudo apt -y full-upgrade
sudo apt install curl gnupg2 apt-transport-https software-properties-common ca-certificates
sudo apt install docker-compose
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```
#### osint-framework
* https://github.com/fr4nc1stein/osint-framework
