import requests
from colorama import Fore, Style, init
import re
import argparse 
import os 
import json
from datetime import datetime

init(autoreset = True)

# ----------------------------
# ARGPARSE CONFIGURATION
# ----------------------------
parser = argparse.ArgumentParser(description="🛡️ Automated SQL Injection Scanner")

parser.add_argument("--url", required=True, help="Target URL (e.g. http://example.com/page.php?id=)")
parser.add_argument("--method", choices=["GET", "POST"], default="GET", help="HTTP method to use")
parser.add_argument("--payloads", default="payloads.txt", help="Path to payloads file")

args = parser.parse_args()

# Loading payloads
if not os.path.exists(args.payloads):
    print(Fore.RED + f"[!] Payloads file not found: {args.payloads}")
    exit()

with open(args.payloads, "r") as file:
    payloads = [line.strip() for line in file.readlines()]

# custom headers
headers = {
    "User-Agent": "Mozilla/5.0 (SQLi Scanner)"
}
results_data = {
    "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "target_url": args.url,
    "method": args.method,
    "vulnerabilities": [],
    "errors": []

}
# ----------------------------
# MAIN SCAN LOOP
# ----------------------------
print(Fore.CYAN + "\n Starting scan...\n")
with open("results.txt", "w") as log:
    for payload in payloads:
        try:
            if args.method == "GET":
                test_url = args.url + payload
                response = requests.get(test_url, headers=headers)
            elif args.method == "POST":
                # You'll need to customize 'username' and 'password' field names for real targets
                data = {
                    "username": payload,
                    "password": "test"
                }
                response = requests.post(args.url, data= data, headers=headers)
                test_url = f"{args.url} POST with {data}"
            else:
                print(Fore.RED + "[!] Invalid method. Choose GET or POST.")
                break
            title_match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE)
            page_title = title_match.group(1) if title_match else "No title found"

            text = response.text.lower()
            if any(x in text for x in ["welcome", "logged in", "you have an error", "syntax", "mysql", "sql"]):
                print(Fore.GREEN + "[!] Logging this to results.txt")
                print(Fore.GREEN + f"[VULNERABLE] {payload} -> {page_title}")
                log.write(f"[VULNERABLE] {payload} -> {test_url} -> {page_title}\n")

                results_data["vulnerabilities"].append({
                    "payload": payload,
                    "url": test_url,
                    "title": page_title
                })
            else:
                print(Fore.YELLOW + f"[NOT VULENRABEL] {payload} -> {test_url} -> {page_title}\n")
            # print(response.text[:500])
        except requests.exceptions.RequestException as e:
            print (Fore.RED + f"[ERROR]payload: {payload} -> {e}")
            results_data["errors"].append({
                "payload": payload,
                "error": str(e)
            })
json_report_file = f"sqli_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(json_report_file, "w") as json_file:
    json.dump(results_data, json_file, indent=4)

print(Fore.CYAN + f"\n[+] JSON report saved to {json_report_file}")
