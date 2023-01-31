```
kali@kali:~$ sudo apt update
kali@kali:~$
kali@kali:~$ sudo apt install -y docker.io
kali@kali:~$
kali@kali:~$ sudo systemctl enable docker --now
kali@kali:~$
kali@kali:~$ sudo groupadd docker
kali@kali:~$ sudo usermod -aG docker $USER
kali@kali:~$ docker
kali@kali:~$
```
* check plateform: $ dpkg-architecture -q DEB_BUILD_ARCH
* clean dangling <none>:<none> : $ sudo docker rmi $(sudo docker images -f "dangling=true" -q)
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
```
sudo python -m pip install --upgrade pip
git clone https://github.com/fr4nc1stein/osint-framework osif
cd osif
docker-compose up -d
docker exec -ti osif bash
./osif
```
#### pentdocks
* https://github.com/diwsec/pentdocks
```
web application pentesting tools for docker
```
#### fsociety -- A Modular Penetration Testing Framework
* https://github.com/fsociety-team/fsociety
```
Install
pip install fsociety
Update
pip install --upgrade fsociety
Usage
usage: fsociety [-h] [-i] [-s]

A Penetration Testing Framework

optional arguments:
  -h, --help     show this help message and exit
  -i, --info     gets fsociety info
  -s, --suggest  suggest a tool
Docker
docker pull fsocietyteam/fsociety
docker run -it fsocietyteam/fsociety fsociety
Developing
git clone https://github.com/fsociety-team/fsociety.git
pip install -e ".[dev]"
```
#### RED_HAWK build
* git clone https://github.com/Tuhinshubhra/RED_HAWK
* cd RED_HAWK
* sudo docker build -t myred_hawk . --no-cache
#### Running
* sudo docker run -it myred_hawk
#### second run 
* sudo docker ps -a
```
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS                      PORTS     NAMES
6566f37bdf3b   myred_hawk      "docker-php-entrypoi…"   38 minutes ago   Exited (0) 20 minutes ago             trusting_shannon
```
* sudo docker start 6566f37bdf3b
* sudo docker attach 6566f37bdf3b
(directory input web site url -- without http/https)
##
#### save and push to docker.hub
* sudo docker save myred_hawk > myred_hawk.tar
#### https://hub.docker.com/
* sudo docker login
* sudo docker tag myred_hawk jumbokh/myred_hawk
* sudo push jumbokh/myred_hawk
