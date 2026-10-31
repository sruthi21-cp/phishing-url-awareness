"""
Phishing URL Awareness Checker
Cybersecurity Internship Mini Project
Compliant with EWB Cybersecurity Mini Project Workbook - Phase 2 Improved Application

Author: Senior Python Developer & Project Architect
Python Version: 3.10+
Dependencies: Python Standard Library Only (re, urllib.parse)
"""

import re
from urllib.parse import urlparse


def inspect_url(raw_url: str) -> list[str]:
    """
    Inspect a raw URL string using lexical and structural heuristics.

    Args:
        raw_url: The URL string entered by the user.

    Returns:
        A list of detected warning strings or error/notice messages.
    """
    findings: list[str] = []

    # 1. Clean input and handle empty submission
    cleaned_url = raw_url.strip()
    if not cleaned_url:
        return ["No URL entered."]

    # 2. Add default scheme if none is provided
    if "://" not in cleaned_url:
        cleaned_url = "http://" + cleaned_url

    # 3. Safely parse URL with ValueError exception handling
    try:
        parsed = urlparse(cleaned_url)
    except ValueError as err:
        return [f"Error: Malformed URL entered ({err}). Please enter a valid URL."]

    # 4. Extract and normalize lowercase hostname, handling None safely
    hostname = (parsed.hostname or "").lower()
    if not hostname:
        findings.append("Notice: URL does not contain a valid hostname.")

    # --- SIX FOUNDATIONAL DETECTION CHECKS ---

    # Check 1: @ Symbol Detection
    if "@" in cleaned_url:
        findings.append(
            "Contains an '@' symbol, which may be used to mislead or obscure the destination."
        )

    # Check 2: Long URL Detection (> 100 characters)
    if len(cleaned_url) > 100:
        findings.append("URL exceeds 100 characters in length.")

    # Check 3: IP Address Detection (IPv4-style: digits.digits.digits.digits)
    if hostname and re.match(r"^\d+\.\d+\.\d+\.\d+$", hostname):
        findings.append("Uses an IP address instead of a familiar domain.")

    # Check 4: Subdomain Detection (5 or more hostname segments)
    if hostname:
        segments = hostname.split(".")
        if len(segments) >= 5:
            findings.append(
                "Contains 5 or more hostname segments (multiple subdomains)."
            )

    # Check 5: Punycode Detection ("xn--")
    if hostname and "xn--" in hostname:
        findings.append(
            "Hostname contains Punycode ('xn--'), which may indicate an IDN homograph attack."
        )

    # Check 6: HTTP Detection
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    return findings


def has_warnings(findings: list[str]) -> bool:
    """
    Identify whether actual warning signs exist and display the summary.

    Filters out informational/error notices, counts genuine warning signs,
    and displays either the warning count or the cautious safety reminder.

    Args:
        findings: The findings list returned by inspect_url().

    Returns:
        bool: True if actual warning signs exist, False otherwise.
    """
    warning_signs = [
        item
        for item in findings
        if not item.startswith("Error:")
        and not item.startswith("Notice:")
        and not item.startswith("Info:")
        and item != "No URL entered."
    ]
    count = len(warning_signs)

    if count > 0:
        print("\nREVIEW CAREFULLY:")
        print(f"{count} warning sign(s) found.")
        return True
    else:
        print("\nNo listed warning signs found.")
        print("This does NOT prove safety.")
        return False


def main() -> None:
    """Main CLI entry point allowing continuous inspection of multiple URLs."""
    print("=" * 65)
    print("             PHISHING URL AWARENESS CHECKER")
    print("=" * 65)
    print("Notice: This program analyzes URL text using lexical and structural")
    print("heuristics. It operates offline and never connects to or visits URLs.")
    print("-" * 65)
    print("Type 'q', 'quit', or 'exit' at the prompt to end the session.")
    print("=" * 65)

    while True:
        try:
            user_input = input("\nEnter a URL to check: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting Phishing URL Awareness Checker. Goodbye!")
            break

        cleaned_input = user_input.strip()

        # Handle session termination
        if cleaned_input.lower() in ("q", "quit", "exit"):
            print("\nThank you for using the Phishing URL Awareness Checker.")
            print("Exiting application. Stay safe online! Goodbye!")
            break

        # Handle empty input without crashing
        if not cleaned_input:
            print("No URL entered. Please enter a valid URL.")
            continue

        findings = inspect_url(cleaned_input)

        # Handle malformed URL or fatal parsing errors
        errors = [f for f in findings if f.startswith("Error:")]
        if errors:
            print("\n--- Detection Results ---")
            for err in errors:
                print(err)
            print("-" * 65)
            continue

        # Extract genuine warning signs
        warning_signs = [
            item
            for item in findings
            if not item.startswith("Notice:")
            and not item.startswith("Info:")
            and not item.startswith("Error:")
        ]

        print("\n--- Detection Results ---")
        if warning_signs:
            print("Warnings detected:")
            for warning in warning_signs:
                print(f"- {warning}")

        # Display review summary via helper function
        has_warnings(findings)

        print("-" * 65)
        print("Cybersecurity Reminder: Always verify the sender, check domain")
        print("spelling carefully, and never enter sensitive information into")
        print("unexpected or unverified web addresses.")
        print("-" * 65)


if __name__ == "__main__":
    main()
