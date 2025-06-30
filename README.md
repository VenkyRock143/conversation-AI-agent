# Conversational AI for Booking Appointments

### ✅ Features
- Conversational chatbot built with FastAPI, Streamlit, and LangGraph-like logic
- Understands natural language like "Book tomorrow at 3 PM"
- Checks your Google Calendar availability
- Books the appointment if the time is free

### 🚀 Getting Started
1. Clone or download the project
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Add your Google credentials to a `.env` file (see `.env.example`)
4. Run backend:
```bash
uvicorn app.main:app --reload
```
5. Run frontend:
```bash
streamlit run frontend.py
```

### 📌 Notes
- Ensure you’ve enabled the Google Calendar API in your Google Developer Console
- Use your client ID, client secret, and authorized redirect URIs
- On first run, browser will open to authenticate Google account

### 🏁 Example Queries
- "Book tomorrow at 3 PM"
- "Do you have time this Friday?"
- "Schedule something next Monday at 10 AM"

---
