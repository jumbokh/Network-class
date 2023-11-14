### Enable SSH
```
sudo systemctl enable ssh
sudo systemctl start ssh
sudo systemctl status ssh
```
### add user
```
sudo useradd username -m -d /home/username
sudo passwd username
# add user to /etc/sudoers
```
### add search path
* export PATH=.:$PATH
* nano ~/.bashrc
* echo 'export PATH=.:$PATH' >> ~/.bashrc
* source .bashrc
### add nameserver
* sudo nano /etc/resolv.conf
     * nameserver 8.8.8.8
     * nameserver 168.95.1.1
### dig mail server
* dig 8.8.8.8 mx
### trace
* dig +trace csu.edu.tw
