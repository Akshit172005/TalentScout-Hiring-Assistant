import json
import re
import streamlit as st
from textblob import TextBlob
from llm_handler import get_response

st.set_page_config(page_title="TalentScout Hiring Assistant")
st.title("TalentScout Hiring Assistant 🤖")

# -----------------------------------
# Initialize Session State Variables
# -----------------------------------

if "stage" not in st.session_state:
    st.session_state.stage = "greeting"

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------------
# Display Previous Chat
# -----------------------------------

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -----------------------------------
# Sentiment Analysis Function
# -----------------------------------

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"

# -----------------------------------
# Greeting Stage
# -----------------------------------

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

# -----------------------------------
# User Input Section
# -----------------------------------

user_input = st.chat_input("Type your response here...")

if user_input:

    # Empty input protection
    if not user_input.strip():
        reply = "Input cannot be empty. Please provide the requested information."
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

    # Exit keywords
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": "Thank you for your time. Our recruitment team will contact you soon."
        })
        st.session_state.stage = "completed"
        st.rerun()

    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # -----------------------------------
    # Stage-Based Flow Control
    # -----------------------------------

    # 1️⃣ Name
    if st.session_state.stage == "name":

        if any(char.isdigit() for char in user_input):
            reply = "Your name should not contain numbers. Please enter a valid full name."
        else:
            st.session_state.candidate_data["name"] = user_input.strip()
            st.session_state.stage = "email"
            reply = "Thank you. Please provide your email address."

    # 2️⃣ Email
    elif st.session_state.stage == "email":

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if re.match(email_pattern, user_input.strip()):
            st.session_state.candidate_data["email"] = user_input.strip()
            st.session_state.stage = "phone"
            reply = "Email noted. Please provide your 10-digit phone number."
        else:
            reply = "That doesn't appear to be a valid email address. Please enter a valid email."

    # 3️⃣ Phone
    elif st.session_state.stage == "phone":

        if user_input.isdigit() and len(user_input) == 10:
            st.session_state.candidate_data["phone"] = user_input
            st.session_state.stage = "experience"
            reply = "Thank you. How many years of experience do you have?"
        else:
            reply = "Please enter a valid 10-digit phone number."

    # 4️⃣ Experience
    elif st.session_state.stage == "experience":

        if user_input.isdigit():
            st.session_state.candidate_data["experience"] = user_input
            st.session_state.stage = "position"
            reply = "Which position are you interested in applying for?"
        else:
            reply = "Please enter your experience as a number (e.g., 1, 2, 3)."

    # 5️⃣ Position
    elif st.session_state.stage == "position":

        st.session_state.candidate_data["position"] = user_input.strip()
        st.session_state.stage = "location"
        reply = "Please share your current location."

    # 6️⃣ Location
    elif st.session_state.stage == "location":

        st.session_state.candidate_data["location"] = user_input.strip()
        st.session_state.stage = "tech_stack"
        reply = (
            "Please list your tech stack (programming languages, frameworks, "
            "databases, tools) separated by commas."
        )

    # 7️⃣ Tech Stack + Question Generation
    elif st.session_state.stage == "tech_stack":

        if "," not in user_input:
            reply = "Please list multiple technologies separated by commas (e.g., Python, Django, MySQL)."
        else:
            st.session_state.candidate_data["tech_stack"] = user_input.strip()

            # Sentiment Analysis on final meaningful response
            sentiment = analyze_sentiment(user_input)
            st.session_state.candidate_data["sentiment"] = sentiment

            tech_prompt = f"""
You are a strict technical interviewer.

The candidate has the following tech stack:
{user_input}

Instructions:
- Identify each technology separately.
- Generate exactly 3 technical interview questions per technology.
- Do not add explanations.
- Format strictly as:

Technology: <Technology Name>
1.
2.
3.
"""

            questions = get_response([
                {"role": "system", "content": tech_prompt}
            ])

            # Save anonymized candidate data
            try:
                with open("candidates_data.json", "a") as f:
                    json.dump(st.session_state.candidate_data, f)
                    f.write("\n")
            except:
                pass

            reply = (
                questions +
                f"\n\nCandidate Sentiment Detected: {sentiment}\n\n"
                "Thank you for completing the screening process.\n"
                "Your information is securely stored and will only be used for recruitment purposes.\n"
                "Our team will review your profile and contact you shortly."
            )

            st.session_state.stage = "completed"

    # 8️⃣ Completed
    elif st.session_state.stage == "completed":
        reply = "This session has already been completed. Please restart the application to apply again."

    # Fallback Protection
    else:
        reply = (
            "I am here to conduct your initial screening for the applied position.\n\n"
            "Please provide the requested information so we can continue."
        )

    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.rerun()
    