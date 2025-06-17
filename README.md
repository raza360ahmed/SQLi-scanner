# 🔍 SQLi Scanner (Python)

An automated SQL Injection vulnerability scanner written in Python.

## 📦 Features
- Supports GET and POST scanning
- CLI interface using argparse
- HTML title extraction
- Colorized terminal output
- Logs to `.txt` and `.json`
- User-agent header support

## 🚀 Usage

```bash
python sqli_scanner.py --url "http://localhost/dvwa/vulnerabilities/sqli/?id=" --method GET
python sqli_scanner.py --url "http://localhost/dvwa/login.php" --method POST
