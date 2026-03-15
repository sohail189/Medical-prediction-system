import streamlit as st
from google import genai
import joblib
import pandas as pd
import os
from dotenv import load_dotenv

# ── Load API Key ──────────────────────────────────────────────
load_dotenv(r"C:/Users/Sohail/Desktop/health chatbot1/src/.env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("Gemini API key missing. Please add it in the .env file.")
    st.stop()

# ── Initialize Gemini Client ──────────────────────────────────
client = genai.Client(api_key=GEMINI_API_KEY)

# ── Load ML Model ─────────────────────────────────────────────
model = joblib.load(r"C:\Users\Sohail\Downloads\my_model.pkl")

# ── Page Setup ────────────────────────────────────────────────
st.title("Heart Disease Detection System")
st.caption("Ask about heart disease or type 'predict:' to get a prediction.")

# ── Session State ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I can answer questions about heart disease or predict risk. How can I help you?"
        }
    ]

# ── Display Chat History ──────────────────────────────────────
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ── Chat Input ────────────────────────────────────────────────
if prompt := st.chat_input("Ask something or type: predict: age=55, chol=240, trestbps=130"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # ── Prediction Mode ───────────────────────────────────────
    if prompt.lower().startswith("predict:"):
        try:
            data  = prompt.replace("predict:", "").strip()
            items = data.split(",")
            input_dict = {
                k.strip(): float(v)
                for k, v in (item.split("=") for item in items)
            }
            df         = pd.DataFrame([input_dict])
            prediction = model.predict(df)[0]

            if prediction == 1:
                msg = " High risk of heart disease detected. Please consult a doctor."
            else:
                msg = " Low risk of heart disease. Keep maintaining a healthy lifestyle!"

        except Exception as e:
            msg = (
                " Invalid format. Please use:\n\n"
                "`predict: age=55, chol=240, trestbps=130`\n\n"
                f"Error: {e}"
            )

    # ── Gemini Chat Mode ──────────────────────────────────────
    else:
        try:
            # Build conversation history as a single string for context
            history = ""
            for m in st.session_state.messages[:-1]:  # exclude latest user msg
                role    = "User" if m["role"] == "user" else "Assistant"
                history += f"{role}: {m['content']}\n"

            full_prompt = (
                "You are a helpful medical assistant specialized in heart disease. "
                "Answer clearly and recommend consulting a doctor for serious concerns.\n\n"
                f"{history}"
                f"User: {prompt}\n"
                "Assistant:"
            )

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=full_prompt
            )
            msg = response.text

        except Exception as e:
            msg = f" Gemini API error: {e}"

    # ── Display & Save Response ───────────────────────────────
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)