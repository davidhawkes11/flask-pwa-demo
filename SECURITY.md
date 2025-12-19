## Security Policy
This document explains how to report security issues, what we support, and how we handle disclosures. It is intended as a teaching example you can drop into a repository and adapt for your own projects.

## Supported Versions
We provide security fixes and coordinated disclosure for the current stable release and the previous minor release. If you are running an older, unsupported version, please upgrade before reporting a vulnerability. When reporting, include the exact version and commit SHA.

## Reporting a Vulnerability
Report privately to: security@example.com. Do not open public issues for security vulnerabilities.

## What to include in your report

- Affected version and commit SHA.

- Steps to reproduce with minimal reproduction code or a proof of concept.

- Impact and attack surface (what an attacker can do).

- HTTP request/response traces if relevant (headers, body).

- Browser and environment details for client-side issues (browser, version, OS).

- Suggested mitigation if you have one.

- Contact preference and whether you want credit or anonymity.

PGP public key
Use the PGP key below to encrypt sensitive reports. Replace this placeholder with your real project key before publishing.

-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: OpenPGP

mQENBFuEXAMPLEBCADK1...REPLACE-WITH-YOUR-REAL-KEY...zQIDAQAB
-----END PGP PUBLIC KEY BLOCK-----

## Example encrypted report
Encrypt your message to the PGP key above. This is a placeholder showing the format only.

-----BEGIN PGP MESSAGE-----
Version: OpenPGP

hQGMA6EXAMPLEENCRYPTEDPAYLOAD...REDACTED...
-----END PGP MESSAGE-----


## Non‑sensitive reports
If the issue is not security sensitive (no secrets, no exploit code), you may open a public issue. 
Use the label security and do not include exploit code or sensitive data in the public issue.

## How We Respond
# Acknowledgement  
We will acknowledge receipt of a private report within 3 business days.

# Triage and remediation
We will triage and provide an initial remediation plan or timeline within 14 days.
For critical vulnerabilities we will prioritize fixes and coordinate an accelerated disclosure.

# Disclosure and advisory
We will coordinate public disclosure with the reporter. We aim to publish a fix and advisory within 90 days of confirmation, or sooner for critical issues. If we cannot meet this timeline we will provide status updates to the reporter.

# CVE and credit  
We will assign a CVE where appropriate and credit reporters in advisories unless they request anonymity.

## Scope and Safe Harbor
# In scope
Code in this repository and official images published by this project.
Configuration and deployment guidance maintained in this repo.

# Out of scope
Third‑party services, forks, or downstream deployments not maintained by this project.
Vulnerabilities in upstream dependencies should be reported to the dependency maintainers and to us if they affect this project directly.

# Safe harbor  
We will not pursue legal action against good‑faith security researchers who follow this policy. Do not publicly disclose vulnerabilities before we have had a chance to investigate and remediate.

### Content Security Policy
We enforce a strict Content Security Policy to reduce XSS and data exfiltration risk. 
If you are testing CSP bypasses, include the exact CSP header and request/response traces in your report.
- Baseline CSP directives used by the application
- default-src 'self'
- script-src 'self'
- style-src 'self'
- img-src 'self' data:
- connect-src 'self'

### What to include when reporting CSP bypasses

- Full HTTP request and response headers.
- Browser and version, including any extensions.
- Exact CSP header value observed.
- Minimal reproduction steps and PoC demonstrating bypass.
- Any console logs or network traces.

### Contact and Acknowledgements
## Contact  
first.last@example.com

# Acknowledgements  
We appreciate responsible disclosure. Reporters who follow this policy will be credited in advisories unless they request anonymity.

# Changes to this policy  
We may update this policy; the latest version is in the repository root. 
If you reported an issue under a previous policy, we will honor the terms that were in effect at the time of your report.
