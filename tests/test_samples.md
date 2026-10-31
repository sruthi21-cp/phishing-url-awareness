# Test Results

Python version used: Python 3.11.9
Operating system: Windows
Date: 2026-10-31

| # | Input | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `https://www.example.com/login` | No listed warning signs found.<br>This does NOT prove safety. | No listed warning signs found.<br>This does NOT prove safety. | PASS |
| 2 | `http://192.0.2.10/account` | - IP address warning.<br>- HTTP warning. | Warnings detected:<br>- Uses an IP address instead of a familiar domain.<br>- Uses HTTP. HTTPS alone does not prove trust.<br>REVIEW CAREFULLY: 2 warning sign(s) found. | PASS |
| 3 | `http://example.com@sample.invalid/login` | - @ symbol warning.<br>- HTTP warning. | Warnings detected:<br>- Contains an '@' symbol, which may be used to mislead or obscure the destination.<br>- Uses HTTP. HTTPS alone does not prove trust.<br>REVIEW CAREFULLY: 2 warning sign(s) found. | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | - Many hostname segments/subdomains warning. | Warnings detected:<br>- Contains 5 or more hostname segments (multiple subdomains).<br>REVIEW CAREFULLY: 1 warning sign(s) found. | PASS |
| 5 | `https://xn--example.invalid/` | - Punycode-style hostname warning. | Warnings detected:<br>- Hostname contains Punycode ('xn--'), which may indicate an IDN homograph attack.<br>REVIEW CAREFULLY: 1 warning sign(s) found. | PASS |

## Test Notes

- **What was learned from testing**: Static lexical analysis reliably surfaces structural deception techniques—such as raw IPv4 hostnames, unencrypted HTTP transport, Punycode IDN homographs, and userinfo-based destination obscuration—entirely offline without connecting to suspicious hosts.
- **What surprised you**: The effectiveness of the `@` delimiter in masking actual destinations: to an untrained user, `http://example.com@sample.invalid/login` resembles a trusted domain, whereas standard URL parsers route traffic strictly to `sample.invalid`.
- **Why no warning signs does not guarantee safety**: Absence of structural anomalies does not prove legitimacy; adversaries routinely host sophisticated credential-harvesting kits on newly registered domains or compromised infrastructure utilizing valid HTTPS certificates and normal URL lengths.
