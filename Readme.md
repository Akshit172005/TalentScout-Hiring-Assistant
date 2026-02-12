\# TalentScout Hiring Assistant 🤖



\## Project Overview



TalentScout Hiring Assistant is an AI-powered chatbot built using Streamlit and a Large Language Model (LLM).  

It simulates an initial screening interview process for a fictional recruitment agency called "TalentScout."



The chatbot collects essential candidate information and generates technical interview questions based on the candidate's declared tech stack.



This project demonstrates:

\- Prompt engineering

\- Context-aware conversation handling

\- LLM integration

\- Structured input validation

\- Simulated backend data storage



---



\## Features



\- Structured stage-based conversation flow

\- Input validation (email, phone number, experience)

\- Tech stack declaration and parsing

\- Automatic generation of 3 technical questions per technology

\- Context-aware interaction using session state

\- Fallback mechanism for invalid input

\- Simulated data storage using JSON

\- Privacy-aware messaging

\- Clean and intuitive Streamlit UI



---



\## Technologies Used



\- Python

\- Streamlit (Frontend UI)

\- Groq LLM API (Llama 3.1 model)

\- JSON (Simulated backend storage)

\- Regular Expressions (Input validation)



---



\## Architecture Overview



The system is divided into the following components:



1\. \*\*Streamlit UI (app.py)\*\*

&nbsp;  - Handles user interaction

&nbsp;  - Maintains session state

&nbsp;  - Controls conversation stages



2\. \*\*LLM Handler (llm\_handler.py)\*\*

&nbsp;  - Connects to Groq API

&nbsp;  - Sends structured prompts

&nbsp;  - Returns generated responses



3\. \*\*Prompt Strategy\*\*

&nbsp;  - Separate structured prompts for:

&nbsp;    - Information gathering

&nbsp;    - Technical question generation

&nbsp;  - Strict formatting rules enforced during question generation



4\. \*\*Simulated Data Storage\*\*

&nbsp;  - Candidate data is stored locally in `candidates\_data.json`

&nbsp;  - No external database is used



---



\## Conversation Flow



The chatbot follows a strict stage-based structure:



1\. Greeting

2\. Name collection

3\. Email validation

4\. Phone validation

5\. Experience collection

6\. Desired position

7\. Location

8\. Tech stack declaration

9\. Technical question generation

10\. Completion message



This ensures:

\- Controlled flow

\- Context awareness

\- No deviation from hiring purpose



---



\## Prompt Engineering Strategy



Two types of prompts are used:



\### 1. Screening Prompt

Guides the conversation and ensures the chatbot collects required information step by step.



\### 2. Technical Interview Prompt

A strict instruction-based prompt that:

\- Identifies technologies separately

\- Generates exactly 3 questions per technology

\- Avoids explanations

\- Enforces structured formatting



This prevents hallucination and ensures relevant technical depth.



---



\## Data Handling \& Privacy



\- Candidate information is stored locally in a JSON file.

\- No external database or cloud storage is used.

\- Data is not shared with any third party.

\- The chatbot explicitly informs the user that data is used only for recruitment purposes.

\- Sensitive data handling is simulated following basic privacy awareness principles aligned with GDPR guidelines.



---



\## Installation Instructions



1\. Clone the repository:



