```
Nuclei使用零误报的定制模板向目标发送请求，同时可以对主机进行批量快速扫描。Nuclei提供TCP、DNS、HTTP、FILE等各类协议的扫描，
通过强大且灵活的模板，可以使用Nuclei模拟各种安全检查。
```
* install: go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
* use: nuclei -h
* reference: https://github.com/projectdiscovery/nuclei/blob/main/README_CN.md
* official site: https://nuclei.projectdiscovery.io/nuclei/get-started/
* template download: https://github.com/projectdiscovery/nuclei-templates
### 應用 [docs](https://www.geeksforgeeks.org/nuclei-fast-and-customizable-vulnerability-scanner/?fbclid=IwAR1d5hyicSdEou4V5JzlpisOEXPyeIDqcXTToBTws3O6amRIYtYcQ-z_v1E)
* cd nuclei-templates
    * nuclei -u http://192.168.1.121:8180 -t technologies/nginx/nginx-version.yaml
    * nuclei -u http:192.168.1.121:8180 -t cves/ -t exposures/
    * nuclei -u http:192.168.1.121:8180 -exclude-templates exposed-panels/ -exclude-templates technologies/
    * nuclei -u http:192.168.1.121:8180 -t cves/ -etags xss
    * nuclei -l target_urls.txt -t cves/
    * nuclei -u http:192.168.1.121:8180 -t cves/ - evclude-templates cves/2020/
    * nuclei -u http:192.168.1.121:8180 -exclude-templates exposed-panels/ -exclude-templates technologies/
    * nuclei -u https://facebook.com -t cves/ -etags xss
    * nuclei -u geeksforgeeks.org -t cves/ -etags sqli.rce
### 參考
* https://www.geeksforgeeks.org/nuclei-fast-and-customizable-vulnerability-scanner/?fbclid=IwAR2R0hliaHmGLcMS5qZ4548Sb8YnSpN-VoXUgfOH-PmE_CLTNZMPsn0xmIg
* Howto install golang on raspberry pi: https://www.jeremymorgan.com/tutorials/raspberry-pi/install-go-raspberry-pi/
* golang download page: https://go.dev/dl/
