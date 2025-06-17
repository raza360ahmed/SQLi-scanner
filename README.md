
# 🛡️ SQLi Scanner - Automated SQL Injection Detection Tool

A Python-based lightweight scanner to identify SQL Injection vulnerabilities in web applications using **GET** or **POST** requests. Designed for learning, testing, and demo purposes — ideal for bug bounty practice, local testing (like DVWA/bWAPP), or cybersecurity portfolios.

---

## 🔧 Features

- ✅ Accepts dynamic target URLs via CLI
- ✅ Supports both **GET** and **POST** methods
- ✅ Injects multiple SQL payloads from `payloads.txt`
- ✅ Detects possible injection by keyword-based response analysis
- ✅ Extracts `<title>` from responses for better context
- ✅ Colorized terminal output using `colorama`
- ✅ Logs vulnerable payloads to a `results.txt` file
- ✅ Generates structured **JSON report** with timestamp
- ✅ CLI flags via `argparse` for flexibility

---

## 🚀 How to Use

### 🔹 1. Install Requirements

```bash
pip install requests colorama
🔹 2. Run the Scanner

python scanner.py --url "http://target.com/page.php?id=" --method GET --payloads payloads.txt
✅ Replace the URL with your own
✅ Use POST if scanning login forms

⚙️ Command-Line Flags
Flag	Description
--url	Target URL (required)
--method	GET or POST (default: GET)
--payloads	Path to payloads file (default: payloads.txt)

📂 Output
✅ results.txt — Plain-text log of successful payloads

✅ sqli_report_YYYYMMDD_HHSS.json — Full scan summary

🧪 Example Use (with DVWA)
python scanner.py --url "http://localhost/dvwa/vulnerabilities/sqli/?id=" --method GET --payloads payloads.txt

📁 File Structure
SQLi-Scanner/
├── scanner.py         # Main script
├── payloads.txt       # SQL payloads
└── README.md          # This file

⚠️ Legal Disclaimer
This tool is intended for educational and authorized testing only.
Do NOT use on websites you don't own or have explicit permission to test.

🙌 Credits
Made by raza360ahmed
Inspired by hands-on cybersecurity learning 💻🔐
