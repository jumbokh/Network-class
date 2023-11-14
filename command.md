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
