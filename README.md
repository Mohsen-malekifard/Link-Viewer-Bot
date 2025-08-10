# Python URL Status Checker

A simple Python script that continuously checks the status of a given URL every **1 second** and displays the HTTP status code along with the response time.

---

## Features
- Sends HTTP GET requests to a specified URL.
- Prints HTTP status code and response time.
- Runs in an infinite loop with a **1-second delay** between checks.
- Custom `User-Agent` for request identification.

---

## Requirements
- Python 3.6 or higher
- `requests` library

---

## Installation
1. Clone this repository or download the script.
2. Install the required dependency:
```bash
pip install requests

---

Usage

1. Open the script and replace:


url = "https://example.com"

with your desired link.

---

2. Run the script:

python check_url.py


---
The script will output something like:

[14:32:01] https://example.com - 200 - 0.123s
[14:32:02] https://example.com - 200 - 0.115s
[14:32:03] https://example.com - 200 - 0.119s

