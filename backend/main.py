# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from app.agent import interpret_message
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class Message(BaseModel):
#     text: str

# @app.post("/chat")
# def chat(msg: Message):
#     response = interpret_message(msg.text)
#     return {"response": response}

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.agent import interpret_message
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: Message):
    print("📨 Incoming message:", msg.text)
    response = interpret_message(msg.text)
    print("🤖 Bot response:", response)
    return {"response": response}

