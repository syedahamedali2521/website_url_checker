# 🌐 Website Risk Checker (Streamlit App)

A cyber-styled Streamlit application that analyzes any website and generates a **risk score** based on multiple security factors including SSL validity, domain age, suspicious keywords, headers, and external scripts.  
The app uses a **dark neon-green UI** with animations and a custom glowing mouse cursor for a modern, interactive feel.

---

## 🚀 Features
- ✔️ URL validation & normalization  
- ✔️ SSL certificate check (validity + expiry time)  
- ✔️ WHOIS domain age lookup  
- ✔️ Suspicious keyword detection (phishing indicators)  
- ✔️ External script count (potential malicious injections)  
- ✔️ HTTP header inspection  
- ✔️ Animated neon UI with custom pointer  
- ✔️ Final risk score (0–100) with category: **SAFE | NEUTRAL | RISKY**

---

## 🖥️ Live Interface
Modern dark cyber theme with:
- Neon glow effects  
- Animated cursor  
- Smooth fade-in transitions  
- Circular risk score gauge  

---

## 📦 Installation

### 1️⃣ Clone the project
```bash
git clone https://github.com/your-username/website-risk-checker.git
cd website-risk-checker
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

---

## 🧪 Test URLs (Safe but "Risky-looking")
Here are some URLs you can test safely:

```
https://www.eicar.org/download/eicar.com.txt
http://secure-login-update.com
http://verynewdomain1234567.xyz
http://xj29dk1az.com
http://example.com/login?verify=true
```

---

## 🧠 How Risk is Calculated
The app assigns points based on:
- URL validity  
- SSL status  
- Domain age  
- Server headers  
- Script count  
- Presence of suspicious words (login, bank, verify, update, secure, etc.)

Final score → Category:
- **70–100 = SAFE**
- **40–69 = NEUTRAL**
- **0–39 = RISKY**

---

## 🔧 Optional Integrations (Coming Soon)
You can extend this app using:
- VirusTotal API  
- Google Safe Browsing API  
- URLhaus Threat Feed  
- Machine-Learning URL Risk Model  

(Add API keys in code to enable these services.)

---

## 🎨 UI Theme
- Pure black background  
- Neon green highlights  
- Glowing text + buttons  
- Animated cyber pointer  
- Soft glassmorphism panels  

---

## 📄 License
This project is free to modify and extend.

---

## ❤️ Contributing
Feel free to submit PRs for:
- UI improvements  
- More threat intelligence integrations  
- ML-based risk scoring  

---

## 📬 Contact
For help or customization requests, reach out anytime!

