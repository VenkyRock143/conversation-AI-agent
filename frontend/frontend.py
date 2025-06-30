

import streamlit as st
import requests

st.set_page_config(page_title="Conversational AI", layout="centered")
st.title("🤖 Conversational AI Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Say something like 'Book tomorrow at 3PM'")

if user_input:
    st.session_state.messages.append({"user": user_input})
    try:
        response = requests.post("http://localhost:8000/chat", json={"text": user_input})
        if response.status_code == 200:
            bot_reply = response.json().get("response", "⚠️ Unexpected reply from bot.")
        else:
            bot_reply = f"⚠️ Server Error: {response.status_code}"
    except Exception as e:
        bot_reply = f"❌ Failed to connect to backend: {str(e)}"
    st.session_state.messages.append({"bot": bot_reply})

for msg in st.session_state.messages:
    if "user" in msg:
        st.markdown(f"👤 You: {msg['user']}")
    else:
        st.markdown(f"🤖 Bot: {msg['bot']}")