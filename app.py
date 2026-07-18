import streamlit as st
from google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM_PROMPT = "You are a witty pirate captain. You answer every question accurately and helpfully, but always in pirate speak, with nautical metaphors where you can fit them."

st.title("🏴‍☠️ Ask the Captain")

# Keep chat history across interactions on the page
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])

# Input box at the bottom
question = st.chat_input("Ask something...")

if question:
    st.session_state.messages.append({"role": "user", "text": question})
    with st.chat_message("user"):
        st.write(question)

    contents = [
        types.Content(role=m["role"] if m["role"] == "user" else "model", parts=[types.Part(text=m["text"])])
        for m in st.session_state.messages
    ]

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    )

    st.session_state.messages.append({"role": "model", "text": response.text})
    with st.chat_message("assistant"):
        st.write(response.text)