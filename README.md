# Phishing URL Awareness Checker

An offline cybersecurity educational and heuristic analysis tool developed in accordance with the **EWB Cybersecurity Mini Project Workbook**.

---

## 1. Project Title

**Phishing URL Awareness Checker**  
*Cybersecurity Internship Mini Project — Static Lexical URL Heuristic Analyzer*

---

## 2. Project Overview

The **Phishing URL Awareness Checker** is a command-line interface (CLI) application built using standard Python. It is designed to evaluate suspicious web links and educate users on common deception techniques used by attackers. 

Unlike conventional browser extensions or web security tools that make live network calls, this application analyzes URLs **completely offline**. It inspects the text, structure, and lexical characteristics of a link without ever contacting the server or opening the page. This guarantees that inspecting potentially hazardous links is 100% safe.

---

## 3. Problem Statement

Phishing remains one of the most widespread attack vectors in cybersecurity. Malicious actors trick users into clicking misleading URLs that impersonate reputable organizations, banks, or online services to steal sensitive credentials and deliver malicious payloads. 

Many everyday internet users struggle to spot subtle URL manipulation techniques, such as embedded credentials (`@`), nested subdomains, Punycode homographs, or direct IP-based links. A lightweight, accessible, and offline tool is essential to educate users on these deceptive tactics and promote cybersecurity hygiene before any link is clicked.

---

## 4. Project Objectives

- **Promote Cybersecurity Awareness**: Help students, professionals, and home users recognize the structural hallmarks of phishing links.
- **Static Offline Heuristic Analysis**: Analyze links safely in memory without transmitting network packets or establishing web connections.
- **Zero Third-Party Dependency Overhead**: Deliver a self-contained security utility operating exclusively on standard library modules.
- **Provide Actionable Warnings**: Translate technical URL anomalies into easy-to-understand explanations accompanied by safety reminders.

---

## 5. Features

- **Interactive Continuous CLI**: Inspect multiple URLs in a single session without needing to restart the script.
- **Six Specialized Heuristic Checks**: Detects `@` symbols, excessive length, raw IPv4 addresses, deep subdomain nesting, Punycode encoding, and insecure HTTP transport.
- **Executive Review Summary**: Categorizes and quantifies identified risks with clear warning counts.
- **Malformed Input Resilience**: Catches invalid URL syntax (e.g., malformed IPv6 brackets) gracefully without crashing.
- **Safe & Offline**: Never visits, pings, fetches, or connects to target URLs.
- **Zero External Dependencies**: Runs out-of-the-box on standard Python 3.10 or newer.

---

## 6. Technologies Used

- **Programming Language**: Python 3.10+ (Verified on Python 3.11.9)
- **Built-In Standard Modules**:
  - `urllib.parse` (`urlparse`): Safely splits URLs into components (scheme, netloc, path, params, query, fragment).
  - `re`: Regular expressions for pattern-matching IPv4 addresses and format validation.
  - `sys`: Standard environment interaction.
- **External Dependencies**: None (Zero `pip` packages required).
- **Network / Database**: None. Operates completely in-memory.

---

## 7. Six URL Detection Mechanisms

The tool inspects input links against six foundational structural indicators:

1. **`@` Symbol Detection**  
   *How it works*: Scans the raw URL for the `@` character.  
   *Cybersecurity threat*: Under RFC 3986, content prior to `@` represents user credentials (userinfo), while browsers navigate exclusively to the host following `@`. Phishers exploit this to embed trusted brand names (e.g., `http://paypal.com@attacker-site.com`).
2. **Long URL Detection**  
   *How it works*: Flags URLs exceeding 100 characters in length.  
   *Cybersecurity threat*: Attackers pad URLs with lengthy query strings, base64 tokens, or fake folder paths to push the real domain out of the visible address bar on mobile devices and narrow windows.
3. **IP Address Detection**  
   *How it works*: Applies the regex pattern `^\d+\.\d+\.\d+\.\d+$` to the parsed hostname.  
   *Cybersecurity threat*: Legitimate public services almost universally use registered domain names. Attackers often deploy temporary phishing infrastructure directly on numeric IP addresses (e.g., `http://192.0.2.10/login`) to bypass domain-based reputation filters.
4. **Subdomain Segment Detection**  
   *How it works*: Splits the hostname by period (`.`) and flags domains with 5 or more segments.  
   *Cybersecurity threat*: Attackers stack subdomains (e.g., `login.secure.bank.com.update.attacker.net`) to confuse users into believing they are visiting an authentic site.
5. **Punycode Detection (`xn--`)**  
   *How it works*: Checks whether the hostname contains the string `xn--`.  
   *Cybersecurity threat*: Detects Internationalized Domain Names (IDNs) encoded in Punycode. Attackers use non-Latin homoglyphs (such as Cyrillic 'а' replacing Latin 'a') to spoof legitimate brands visually.
6. **HTTP Detection**  
   *How it works*: Checks if `parsed.scheme.lower() == "http"`.  
   *Cybersecurity threat*: Insecure plain-text HTTP allows network eavesdropping and data tampering. The tool flags HTTP while actively reminding users that *HTTPS alone does not prove a site is trustworthy*.

---

## 8. Project Folder Structure

```text
phishing-url-awareness/
│
├── phishing_checker.py       # Core application source code
├── README.md                 # Complete project documentation
├── requirements.txt          # Dependency specification (Standard library only)
│
├── tests/
│   └── test_samples.md       # Official test plan, execution matrix, and notes
│
└── screenshots/
    ├── sample_run.png        # Screenshot of interactive CLI session
    └── test_results.png      # Screenshot of verified test executions
```

---

## 9. Installation Requirements

1. **Python**: Python 3.10 or higher installed on your computer.
2. **Operating System**: Windows 10/11, Linux, or macOS.
3. **External Packages**: **None.** No packages need to be installed using `pip`.

To verify your Python installation, run in your terminal:

```powershell
python --version
```

---

## 10. How to Run the Application

Open Windows PowerShell, Command Prompt, or your preferred terminal, navigate to the project directory, and execute:

```powershell
python phishing_checker.py
```

### Navigating the Interface

- **Inspect a URL**: Type or paste any web address at the prompt and press `Enter`.
- **Continuous Session**: After reviewing the results, you can immediately enter another URL.
- **Empty Input**: Pressing `Enter` without text prompts you to enter a URL without terminating the program.
- **Exit Session**: Type `q`, `quit`, or `exit` and press `Enter` to end the session.

---

## 11. Example Input and Output

### Example 1: Phishing Indicator (IP Address + Insecure HTTP)

**Input**:
```text
http://192.0.2.10/account
```

**Output**:
```text
--- Detection Results ---
Warnings detected:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY:
2 warning sign(s) found.
-----------------------------------------------------------------
Cybersecurity Reminder: Always verify the sender, check domain
spelling carefully, and never enter sensitive information into
unexpected or unverified web addresses.
-----------------------------------------------------------------
```

### Example 2: Clean Baseline (No Warning Signs)

**Input**:
```text
https://www.example.com/login
```

**Output**:
```text
--- Detection Results ---

No listed warning signs found.
This does NOT prove safety.
-----------------------------------------------------------------
Cybersecurity Reminder: Always verify the sender, check domain
spelling carefully, and never enter sensitive information into
unexpected or unverified web addresses.
-----------------------------------------------------------------
```

### Example 3: Handling Malformed URL Input

**Input**:
```text
http://[bad
```

**Output**:
```text
--- Detection Results ---
Error: Malformed URL entered (Invalid IPv6 URL). Please enter a valid URL.
-----------------------------------------------------------------
```

---

## 12. Testing Results

The application was tested against the official test cases specified in **Section 08 of the EWB Cybersecurity Mini Project Workbook**. All tests passed with 100% compliance.

| # | Input URL | Expected Result | Actual Result | Status |
| :-: | :--- | :--- | :--- | :-: |
| **1** | `https://www.example.com/login` | No listed warning signs found.<br>This does NOT prove safety. | No listed warning signs found.<br>This does NOT prove safety. | **PASS** |
| **2** | `http://192.0.2.10/account` | - IP address warning.<br>- HTTP warning. | Warnings detected:<br>- Uses an IP address instead of a familiar domain.<br>- Uses HTTP. HTTPS alone does not prove trust.<br>REVIEW CAREFULLY: 2 warning sign(s) found. | **PASS** |
| **3** | `http://example.com@sample.invalid/login` | - @ symbol warning.<br>- HTTP warning. | Warnings detected:<br>- Contains an '@' symbol, which may be used to mislead or obscure the destination.<br>- Uses HTTP. HTTPS alone does not prove trust.<br>REVIEW CAREFULLY: 2 warning sign(s) found. | **PASS** |
| **4** | `https://a.b.c.d.e.example.invalid/path` | - Many hostname segments/subdomains warning. | Warnings detected:<br>- Contains 5 or more hostname segments (multiple subdomains).<br>REVIEW CAREFULLY: 1 warning sign(s) found. | **PASS** |
| **5** | `https://xn--example.invalid/` | - Punycode-style hostname warning. | Warnings detected:<br>- Hostname contains Punycode ('xn--'), which may indicate an IDN homograph attack.<br>REVIEW CAREFULLY: 1 warning sign(s) found. | **PASS** |

### Screenshot References

- **Interactive CLI Session**: See [`screenshots/sample_run.png`](screenshots/sample_run.png)
- **Verified Test Suite Outputs**: See [`screenshots/test_results.png`](screenshots/test_results.png)

---

## 13. Implemented Improvements

Building on the initial core specification, three application improvements were implemented:

1. **Improvement 1: Multiple URL Checking (`while True` Session Loop)**  
   Transformed the program from a one-off execution script into a continuous interactive console. Users can inspect multiple links consecutively and gracefully exit using `q`, `quit`, or `exit`.
2. **Improvement 2: Review Carefully Summary (`has_warnings()` Helper)**  
   Introduced a dedicated helper function that filters out informational parsing notices and calculates genuine security indicators, presenting a structured count (`REVIEW CAREFULLY: X warning sign(s) found`) or an explicit safety caution.
3. **Improvement 3: Malformed URL & Hostname Exception Handling**  
   Wrapped `urlparse()` in dedicated `try/except ValueError` exception handling, safely catching malformed inputs (such as improper IPv6 bracket formatting) and handling empty or missing hostnames without application crashes.

---

## 14. Project Limitations

While the tool is an effective educational utility, users must be aware of its technical boundaries:

- **Static Lexical Analysis Only**: It inspects URL string composition. It does not inspect HTML source code, JavaScript scripts, or form action destinations.
- **Zero Real-Time Intelligence**: Because it operates offline, it does not query live DNS records, WHOIS registration age, or threat intelligence feeds (e.g., Google Safe Browsing, VirusTotal).
- **Cannot Detect New Legitimate-Looking Domains**: Phishing sites hosted on newly registered, clean-looking domain names with valid HTTPS certificates will not trigger lexical warnings.
- **URL Shorteners**: Shortened URLs (e.g., `bit.ly`, `tinyurl.com`) hide the real destination address and cannot be unmasked without sending HTTP redirects.

---

## 15. Safety and Ethical Considerations

- **Strict Offline Safety**: The program **never visits, pings, fetches, or downloads from any URL**. This ensures complete immunity from drive-by downloads, tracking beacons, or server-side logging by malicious actors.
- **The Golden Rule of Phishing Awareness**: **Absence of warning signs does NOT prove that a URL is safe.** Attackers frequently register standard domains and enable free SSL certificates. Users must verify the sender, independently verify domains, and exercise caution.
- **Ethical Use**: Designed exclusively for cybersecurity awareness, education, and defense training.

---

## 16. Future Enhancements

Potential extensions for future iterations include:

- **Shannon Entropy Scoring**: Calculate character entropy to flag randomly generated or algorithmic domain names (DGAs).
- **Suspicious TLD Catalog**: Add an offline reference table of top-level domains frequently associated with spam or low-cost abuse (e.g., `.tk`, `.xyz`, `.top`).
- **Levenshtein Distance Typosquatting**: Implement string distance algorithms to detect brand impersonation (e.g., `goog1e.com` or `paypa1.com`).
- **Batch File Inspection**: Add CLI arguments to scan text or CSV files containing lists of links.

---

## 17. Author Details

- **Project**: Cybersecurity Internship Mini Project
- **Curriculum Compliance**: EWB Cybersecurity Mini Project Workbook
- **Role**: Python Developer & Cybersecurity Intern
- **Status**: Completed, Tested, and Verified
