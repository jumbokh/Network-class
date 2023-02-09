### Find the vulnerable host
#### [docs](https://docs.metasploit.com/docs/pentesting/active-directory/ad-certificates/attacking-ad-cs-esc-vulnerabilities.html)
* msfconsole
* use auxiliary/gather/ldap_esc_vulnerable_cert_finder
* set DOMAIN ee.nkust.edu.tw
* set USERNAME normal
* set PASSWORD normaluser
* set RHOSTS 140.127.114.5
* options
```
msf6 auxiliary(gather/ldap_esc_vulnerable_cert_finder) > options

Module options (auxiliary/gather/ldap_esc_vulnerable_cert_finder):

   Name                  Current Setting  Required  Description
   ----                  ---------------  --------  -----------
   BASE_DN                                no        LDAP base DN if you already have it
   DOMAIN                ee.nkust.edu.tw  no        The domain to authenticate to
   PASSWORD              normaluser       no        The password to authenticate with
   REPORT_NONENROLLABLE  false            yes       Report nonenrollable certificate templates
   RHOSTS                140.127.114.5    yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT                 389              yes       The target port
   SSL                   false            no        Enable SSL on the LDAP connection
   USERNAME                               no        The username to authenticate with


View the full module info with the info, or info -d command.
```
* run
