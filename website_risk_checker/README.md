# Website Risk Checker

A Streamlit-based web application that analyzes website URLs for potential security risks. It evaluates various factors such as SSL certificates, domain age, HTTP headers, external scripts, and suspicious keywords to assign a risk score and category (SAFE, NEUTRAL, or RISKY).

## Features

- URL normalization and validation
- SSL certificate checking (validity and expiry)
- WHOIS domain age analysis
- HTTP headers inspection
- External script counting
- Suspicious keyword detection
- Risk scoring (0-100) with visual score circle
- Detailed breakdown table of all checks
- Dark, modern UI with glass-like effects and neon accents
- Custom animated mouse pointer
- Sidebar with information on optional threat-intelligence integrations

## Installation

1. Clone or download this repository.
2. Navigate to the project directory:
   ```
   cd website_risk_checker
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app using the following command:

```
streamlit run app.py
```

This will start the application in your default web browser. Enter a website URL in the input field and click "Analyze URL" to perform the risk assessment.

## Dependencies

- streamlit
- validators
- requests
- python-whois

## Optional Threat-Intelligence Integrations

This app can be enhanced with additional threat-intelligence services for more comprehensive analysis:

- **VirusTotal**: Provides URL reputation scores and malware scan results. Requires an API key.
- **Google Safe Browsing**: Checks against Google's database of known malicious URLs. Requires an API key.
- **URLhaus**: Queries the Abuse.ch URLhaus database for phishing and malware URLs. Requires an API key.

To implement these integrations, obtain the necessary API keys from the respective services and modify the `app.py` file to include API calls and result processing.

## Notes

- The app performs basic checks and should not be considered a comprehensive security analysis tool.
- For production use, consider implementing rate limiting and caching to avoid overwhelming external services.
- Always exercise caution when visiting potentially risky websites, even if they score as SAFE in this tool.
