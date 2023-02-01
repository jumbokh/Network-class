#### Fuzz Faster U Fool (ffuf)
* [Fuzz](https://blog.deurainfosec.com/how-to-find-zero-day-vulnerabilities-with-fuzz-faster-u-fool-ffuf-detailed-free-fuzzing-tool-tutorial/?fbclid=IwAR0rRDuhLo3sUxVhg9nIB3fdDxcrGwc9jS_CALc6-rQohoLDL1YAnl0gYLo)
#### INSTALLATION
1. golang
2. go install github.com/ffuf/ffuf@latest
3. apt install ffuf
#### use
1. Download dict.txt: https://github.com/steveklabnik/password-cracker/blob/master/dictionary.txt
2. 	ffuf -u http://testphp.vulnweb.com/FUZZ/ -w ./dictionary.txt
