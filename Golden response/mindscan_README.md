# MindScan — Mental Wellness Screening & Mood Tracker

A full-stack mental wellness app using Flask, MongoDB, and a Random Forest ML model (DASS-21).

---

## 📁 Project Structure

```
mindscan/
├── app.py               ← Main Flask app (routes, ML, auth)
├── frontend.py          ← SPA HTML/CSS/JS served by Flask
├── requirements.txt     ← Python dependencies
├── .env.example         ← Copy to .env and set your values
├── .gitignore
├── ml_models/           ← Auto-created on first run (stores .pkl files)
└── README.md
```

---

## ✅ Prerequisites

- Python 3.9+
- MongoDB running locally on port 27017
  - Download: https://www.mongodb.com/try/download/community
  - Or use MongoDB Atlas (update MONGO_URI in .env)

---

## 🚀 Setup & Run

### 1. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
cp .env.example .env
# Edit .env if needed (defaults work for local dev)
```

### 4. Make sure MongoDB is running
```bash
# Windows (if installed as a service)
net start MongoDB

# Mac (with Homebrew)
brew services start mongodb-community
```

### 5. Run the app
```bash
python app.py
```

### 6. Open in browser
```
http://localhost:5000
```

---

## 🧠 ML Model

The model trains automatically on first run using 5000 synthetic DASS-21 samples.
Trained files are saved to `ml_models/` and reloaded on subsequent starts.

---

## 🔑 Features

- **Auth** — Signup / Login with bcrypt + JWT
- **DASS-21 Screening** — 21-question mental health questionnaire with ML-based severity prediction
- **Wellness Score** — Composite score (0–100) based on DASS subscales
- **Mood Journal** — Daily entries with emoji mood picker, tags, and search
- **Dashboard** — Mood trend chart (Chart.js), streak counter, wellness score
- **Resources** — Curated mental health links including India crisis helplines

---

## ⚠️ Disclaimer

This is a screening tool only — not a clinical diagnosis. Always consult a licensed mental health professional.
