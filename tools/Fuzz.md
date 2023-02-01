#### Fuzz Faster U Fool (ffuf)
* [Fuzz](https://blog.deurainfosec.com/how-to-find-zero-day-vulnerabilities-with-fuzz-faster-u-fool-ffuf-detailed-free-fuzzing-tool-tutorial/?fbclid=IwAR0rRDuhLo3sUxVhg9nIB3fdDxcrGwc9jS_CALc6-rQohoLDL1YAnl0gYLo)
#### INSTALLATION
1. golang
2. go install github.com/ffuf/ffuf@latest
3. apt install ffuf
#### use
1. Download dict.txt: https://github.com/steveklabnik/password-cracker/blob/master/dictionary.txt
2. 	ffuf -u http://testphp.vulnweb.com/FUZZ/ -w ./dictionary.txt
#### output
```
root@raspberrypi:~# ffuf -u http://192.168.1.121/FUZZ -w ./dict.txt -e .php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.1.121/FUZZ
 :: Wordlist         : FUZZ: ./dict.txt
 :: Extensions       : .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

index                   [Status: 200, Size: 891, Words: 237, Lines: 30]
index.php               [Status: 200, Size: 891, Words: 237, Lines: 30]
test                    [Status: 301, Size: 318, Words: 21, Lines: 10]
:: Progress: [90804/90804] :: Job [1/1] :: 3783 req/sec :: Duration: [0:00:24] :: Errors: 0 ::
root@raspberrypi:~# 
```
### Target directory
* ![FUZZ](https://github.com/jumbokh/Network-class/blob/main/images/FUZZ.JPG)
