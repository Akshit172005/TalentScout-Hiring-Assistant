import json
import streamlit as st
import re
from textblob import TextBlob
from llm_handler import get_response

st.set_page_config(page_title="TalentScout Hiring Assistant")
st.title("TalentScout Hiring Assistant 🤖")

# -----------------------------
# Session State Initialization
# -----------------------------

if "stage" not in st.session_state:
    st.session_state.stage = "greeting"

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Display Previous Chat
# -----------------------------

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------
# Greeting Stage
# -----------------------------

if st.session_state.stage == "greeting":
    greeting_message = (
        "Hello! Welcome to TalentScout.\n\n"
        "I will guide you through a short initial screening process.\n\n"
        "To begin, may I know your full name?"
    )
    st.session_state.chat_history.append(
        {"role": "assistant", "content": greeting_message}
    )
    st.session_state.stage = "name"
    st.rerun()

# -----------------------------
# Sentiment Analysis Function
# -----------------------------

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"

# -----------------------------
# User Input Section
# -----------------------------

user_input = st.chat_input("Type your response here...")

if user_input:

    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": "Thank you for your time. Our recruitment team will contact you soon."
        })
        st.session_state.stage = "completed"
        st.rerun()

    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Run sentiment analysis on meaningful responses
    if st.session_state.stage in ["experience", "position", "tech_stack"]:
        sentiment = analyze_sentiment(user_input)
        st.session_state.candidate_data["sentiment"] = sentiment

    # -----------------------------
    # Stage Handling
    # -----------------------------

    if st.session_state.stage == "name":

        if any(char.isdigit() for char in user_input):
            reply = "Your name should not contain numbers. Please enter a valid full name."
        else:
            st.session_state.candidate_data["name"] = user_input
            st.session_state.stage = "email"
            reply = "Thank you. Please provide your email address."

    elif st.session_state.stage == "email":

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if re.match(email_pattern, user_input):
            st.session_state.candidate_data["email"] = user_input
            st.session_state.stage = "phone"
            reply = "Email noted. Please provide your 10-digit phone number."
        else:
            reply = "That doesn't seem to be a valid email address. Please enter a valid email."

    elif st.session_state.stage == "phone":

        if user_input.isdigit() and len(user_input) == 10:
            st.session_state.candidate_data["phone"] = user_input
            st.session_state.stage = "experience"
            reply = "Thank you. How many years of experience do you have?"
        else:
            reply = "Please enter a valid 10-digit phone number."

    elif st.session_state.stage == "experience":

        if user_input.isdigit():
            st.session_state.candidate_data["experience"] = user_input
            st.session_state.stage = "position"
            reply = "Which position are you interested in applying for?"
        else:
            reply = "Please enter your experience as a number."

    elif st.session_state.stage == "position":

        st.session_state.candidate_data["position"] = user_input
        st.session_state.stage = "location"
        reply = "Please share your current location."

    elif st.session_state.stage == "location":

        st.session_state.candidate_data["location"] = user_input
        st.session_state.stage = "tech_stack"
        reply = "Please list your tech stack separated by commas."

    elif st.session_state.stage == "tech_stack":

        if "," not in user_input:
            reply = "Please list multiple technologies separated by commas."
        else:
            st.session_state.candidate_data["tech_stack"] = user_input

            tech_prompt = f"""
You are a strict technical interviewer.

The candidate has the following tech stack:
{user_input}

Generate exactly 3 technical interview questions per technology.
Format strictly as:

Technology: <Technology Name>
1.
2.
3.
"""

            questions = get_response([
                {"role": "system", "content": tech_prompt}
            ])

            try:
                with open("candidates_data.json", "a") as f:
                    json.dump(st.session_state.candidate_data, f)
                    f.write("\n")
            except:
                pass

            reply = (
                questions +
                "\n\nCandidate Sentiment Detected: "
                + st.session_state.candidate_data.get("sentiment", "Neutral") +
                "\n\nThank you for completing the screening. Our team will contact you soon."
            )

            st.session_state.stage = "completed"

    elif st.session_state.stage == "completed":
        reply = "This session has already been completed."

    else:
        reply = (
        "I'm here to conduct your initial screening for the applied position.\n\n"
        "Please provide the requested information so we can continue the process."
    )

    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.rerun()
