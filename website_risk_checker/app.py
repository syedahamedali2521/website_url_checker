import streamlit as st
import validators
import requests
import whois
from datetime import datetime
from urllib.parse import urlparse

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Neon Website Risk Checker",
    page_icon="🌐",
    layout="wide"
)

# ----------------------------
# DARK THEME + ANIMATED CURSOR CSS
# ----------------------------
st.markdown("""
    <style>
        /* Global Dark Background */
        .stApp, .main, html, body, .block-container {
            background-color: #000000 !important;
            color: #ffffff !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #0d0d0d !important;
        }

        /* Input box */
        .stTextInput > div > div > input {
            background-color: #111 !important;
            color: #0aff9d !important;
            border: 1px solid #0aff9d !important;
            border-radius: 10px;
        }

        /* Button */
        .stButton>button {
            background-color: #0aff9d !important;
            color: black !important;
            border-radius: 8px;
            border: none;
            font-weight: bold;
        }

        .stButton>button:hover {
            background-color: #11ffaa !important;
            color: black !important;
        }

        /* Neon Title */
        .neon-title {
            font-size: 40px;
            color: #0aff9d;
            text-shadow: 0px 0px 20px #0aff9d;
            font-weight: bold;
        }

        /* Risk Score Circle */
        .score-circle {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            border: 6px solid #0aff9d;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 42px;
            font-weight: bold;
            margin: auto;
            color: #0aff9d;
            text-shadow: 0px 0px 15px #0aff9d;
        }

        /* Animated Neon Cursor */
        body {
            cursor: none;
        }

        .cursor {
            width: 20px;
            height: 20px;
            border: 3px solid #0aff9d;
            border-radius: 50%;
            position: fixed;
            transform: translate(-50%, -50%);
            pointer-events: none;
            animation: pulse 0.2s infinite alternate;
            z-index: 9999;
        }

        @keyframes pulse {
            from { transform: translate(-50%, -50%) scale(1); }
            to   { transform: translate(-50%, -50%) scale(1.3); }
        }
    </style>

    <div class="cursor" id="cursor"></div>

    <script>
        const cursor = document.getElementById("cursor");
        document.addEventListener("mousemove", (e) => {
            cursor.style.left = e.pageX + "px";
            cursor.style.top = e.pageY + "px";
        });
    </script>
""", unsafe_allow_html=True)


# ----------------------------
# UTILITY FUNCTIONS
# ----------------------------
def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url

def check_ssl(url):
    try:
        response = requests.get(url, timeout=5)
        return response.url.startswith("https")
    except:
        return False

def check_domain_age(domain):
    try:
        info = whois.whois(domain)
        if isinstance(info.creation_date, list):
            creation_date = info.creation_date[0]
        else:
            creation_date = info.creation_date

        age_days = (datetime.now() - creation_date).days
        return age_days
    except:
        return 0

def check_risky_keywords(url):
    risky = ["verify", "update", "login", "secure", "account", "bank", "confirm"]
    return any(word in url.lower() for word in risky)

def analyze_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    ssl_ok = check_ssl(url)
    age_days = check_domain_age(domain)
    risky_words = check_risky_keywords(url)

    score = 100
    score -= 20 if not ssl_ok else 0
    score -= 30 if age_days < 90 else 0
    score -= 40 if risky_words else 0

    if score < 0: 
        score = 0

    if score > 70:
        status = "SAFE"
    elif score > 40:
        status = "NEUTRAL"
    else:
        status = "RISKY"

    return score, status, ssl_ok, age_days, risky_words


# ----------------------------
# UI LAYOUT
# ----------------------------
st.sidebar.title("Integrations")
st.sidebar.write("""
Enhance detection with APIs:

- VirusTotal  
- Google Safe Browsing  
- URLhaus  

Add API keys to extend the scanner.
""")

st.markdown('<p class="neon-title">🌐 Website Risk Checker (Neon Dark Edition)</p>', unsafe_allow_html=True)

url_input = st.text_input("Enter URL:", placeholder="example.com")

if st.button("Analyze URL"):
    if not validators.url(normalize_url(url_input)):
        st.error("Invalid URL. Try again.")
    else:
        url = normalize_url(url_input)

        score, status, ssl_ok, age_days, risky_keywords = analyze_url(url)

        st.markdown(f"""
            <div class="score-circle">{score}</div>
        """, unsafe_allow_html=True)

        st.subheader(f"Risk Level: **{status}**")

        st.write("---")
        st.write("### 🔍 Detailed Breakdown")
        st.write(f"**SSL Secure:** {'Yes' if ssl_ok else 'No'}")
        st.write(f"**Domain Age:** {age_days} days old")
        st.write(f"**Suspicious Keywords:** {'Yes' if risky_keywords else 'No'}")
        st.write("---")

        st.success("Scan completed.")


    