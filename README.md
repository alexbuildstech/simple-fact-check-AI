# Simple Fact-Check AI

Simple Fact-Check AI is a full-stack web application that provides instant, AI-powered fact-checking.  
Users can enter any claim, and the system leverages the **Google Gemini model** with web search capabilities to deliver a concise verdict:

- ✅ **True**  
- ❌ **False**  
- ⚠️ **Partially True**  
- ❓ **Unverifiable**  

Each verdict comes with a detailed explanation.

<img width="1919" height="987" alt="FactCheck-AI-Verify-Claims-Instantly" src="https://github.com/user-attachments/assets/8fba1f4f-9b3e-4c56-aed4-a8c2c39c920d" />

---

## ✨ Key Features

- **AI-Powered Analysis** – Utilizes the Google Gemini model to analyze claims.  
- **Live Web Search** – Finds real-time, credible evidence via Google Search.  
- **Clear Verdicts** – Classifies claims into **True, False, Partially True, Unverified**.  
- **Detailed Explanations** – Provides context, not just "yes/no".  
- **Modern UI** – Built with Tailwind CSS, responsive and intuitive.  
- **Easy to Deploy** – Flask backend + simple frontend (HTML + JS).  

---

## ⚙️ How It Works

The app follows a **client-server architecture**:

1. **Frontend (`index.html`)**  
   - User enters a claim in the textarea and clicks **Fact Check**.  
   - Built with **HTML, Tailwind CSS, and vanilla JavaScript**.  
   - Sends claim to backend via `POST`.  

2. **Backend (`backend.py`)**  
   - Flask server receives the claim.  

3. **Gemini API**  
   - Claim is forwarded to the **Google Gemini API**.  
   - Model is instructed to act as a fact-checker using **web search**.  

4. **Response**  
   - Gemini returns a verdict + explanation.  
   - Other APIs can be swapped for faster results.  

5. **Display**  
   - Verdict, badge, explanation, and confidence score are shown in the UI.  

---

## 🚀 Getting Started

Follow these instructions to run locally.  

### 📌 Prerequisites

- Python **3.7+**  
- `pip` (Python package installer)  
- Google Gemini API Key (get one from **Google AI Studio**)  

---

### 🔧 Installation & Setup

1. **Clone the Repository**


```
git clone https://github.com/your-username/simple-fact-check-AI.git
cd simple-fact-check-AI
```
2. **Set Up the Backend**
 Create a requirements.txt file:
```
Flask
Flask-Cors
google-generativeai
```
3. **Configure Your API Key (Important!)**

⚠️ Do NOT hardcode your API key into backend.py.
Instead, load it from an environment variable:
```
import os
API_KEY = os.getenv("GEMINI_API_KEY")
```

**Set the key in your environment (Linux/macOS):**
```
export GEMINI_API_KEY="your_api_key_here"
```

**On Windows (PowerShell):**
```
setx GEMINI_API_KEY "your_api_key_here"
```
**▶️ Running the App**

Start the backend server:
```
python backend.py
```
for Linux:
```
python3 backend.py
```


Then open index.html in your browser to use the app.
Here are a few examples:
<img width="1919" height="1381" alt="image" src="https://github.com/user-attachments/assets/d74ca82a-e4de-4317-94d5-8683f155d735" />
<img width="1919" height="1332" alt="image" src="https://github.com/user-attachments/assets/0e157a08-0517-4b3c-8a99-6e8b6a30213c" />
<img width="1919" height="1272" alt="image" src="https://github.com/user-attachments/assets/ff7771ba-1e2d-4ac4-aaad-19cfd7fec4a2" />


