# TalentScout Hiring Assistant 🤖

## 📌 Project Overview

TalentScout Hiring Assistant is an AI-powered chatbot built using Streamlit and a Large Language Model (LLM).

It simulates an initial technical screening interview for a fictional recruitment agency named "TalentScout".

The chatbot:
- Collects essential candidate information
- Maintains conversation context
- Generates technical interview questions based on declared tech stack
- Performs basic sentiment analysis
- Handles conversation termination gracefully

---

## 🎯 Objective

This project demonstrates:

- Prompt Engineering
- Context-aware LLM interactions
- Controlled conversation flow
- Technical question generation
- Secure handling of candidate information
- Clean UI implementation using Streamlit

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq LLM API
- TextBlob (Sentiment Analysis)
- Regex (Validation)
- JSON (Simulated Data Storage)

---

## ⚙️ Features

### 1️⃣ Information Gathering
The chatbot collects:
- Full Name
- Email Address (validated)
- Phone Number (validated)
- Years of Experience
- Desired Position
- Current Location
- Tech Stack

### 2️⃣ Context Handling
Conversation flow is controlled using session-based stage management to ensure logical interaction.

### 3️⃣ Technical Question Generation
For each technology mentioned in the tech stack:
- Generates exactly 3 technical interview questions
- Ensures structured output format
- Avoids explanations or deviations

### 4️⃣ Sentiment Analysis (Bonus Feature)
Analyzes candidate responses using TextBlob and stores emotional tone as:
- Positive
- Neutral
- Negative

### 5️⃣ Data Privacy
- API keys stored in `.env`
- `.env` excluded using `.gitignore`
- Candidate data stored locally in `candidates_data.json` (simulated)

---

## 🧠 Prompt Engineering Strategy

Two types of prompts were designed:

### 1️⃣ System Prompt
Controls:
- Hiring assistant role
- Conversation flow
- Information boundaries
- Professional tone

### 2️⃣ Technical Generation Prompt
Strict formatting instructions:
- Exactly 3 questions per technology
- No explanations
- Structured output

This prevents hallucination and ensures consistent evaluation-style questions.

---

## 🚀 Installation Guide

### 1️⃣ Clone Repository
git clone https://github.com/Akshit172005/TalentScout-Hiring-Assistant.git

cd TalentScout-Hiring-Assistant


### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Dependencies

pip install -r requirements.txt


### 4️⃣ Create `.env` File

Add your Groq API key:

GROQ_API_KEY=your_api_key_here


### 5️⃣ Run Application

streamlit run app.py


---

## 🏗️ Architecture Overview

User → Streamlit UI → Stage Controller → LLM Handler → Groq API → Response → UI

Session State is used to:
- Maintain conversation flow
- Store candidate data
- Control transitions

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|------------|------------|
| Model hallucinating extra content | Strict prompt formatting rules |
| Losing conversation flow | Stage-based control system |
| API key exposure | .env + .gitignore |
| Secret push rejection | Clean Git history |
| Unstructured question output | Enforced formatting pattern |

---

## 📊 Evaluation Criteria Coverage

✔ Technical Implementation  
✔ Prompt Engineering  
✔ Context Handling  
✔ Data Validation  
✔ UI Experience  
✔ Sentiment Analysis (Bonus)  
✔ Clean Git Repository  
✔ Structured Documentation  

---

## 🎥 Demo

Live demo link (to be added after deployment)

Video walkthrough (to be added)

---

## 👨‍💻 Author

Akshit Gupta  
AI/ML Intern Applicant  