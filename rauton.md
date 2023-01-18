### rauton: 蟲賞金偵查工具
```
Rauton:-- Bug Bounty Recon Tool.
Features;-
1. Take Screenshots from subdomains via @sensepost/gowitness
2. Get title and headers from subdomains via @sensepost/gowitness
3. General info about company and CIDRs
4. Network scan via @nmap/nmap
5. HTTP scan via @nmap/nmap
6. Collecting and separating archives urls via @tomnomnom/unfurl, @tomnomnom/gf, @lc/gau, @tomnomnom/waybackurls
7. Templated-based vulnerability scan with @projectdiscovery/nuclei
8. Directory fuzzing with @maurosoria/dirsearch
9. SSL scan with @rbsec/sslscan
10. Get all host IPs from subdomains
Installation :
Clone the repository with git clone https://github.com/Huntinex/rauton
Run installation file ./install.sh
Edit the script CONFIG section and enter your dirsearch_wordlist_path .
Usage :
For single domains use :
./rauton.sh -single apple.com
# or (default mode is single)
./rauton.sh apple.com
And for wildcard domains use :
./rauton.sh -wild apple.com
Note:- This tool is only for educational purpose. We are not responsible for any misuse or illegal activities.
```