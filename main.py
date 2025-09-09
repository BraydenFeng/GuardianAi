import dataloader
import ai
from dataloader import results
from fastapi import FastAPI
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore, auth
from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet

load_dotenv()
fernet_key = os.getenv("FERNET_KEY")
app = FastAPI()
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
cipher = Fernet(fernet_key)

class User(BaseModel):
    username: str
    password: str
    email: str
    discord_token: str
    discord_username: str

@app.post("/create-user")
def create_user(request: User):
    processed_token = cipher.encrypt(request.discord_token.encode())
    user = auth.create_user(
        email = request.email,
        password = request.password,
        display_name = request.username
        )   
    user_data = {
        "username": request.username,
        "email": request.email,
        "discord_token": processed_token,
        "discord_username": request.discord_username
    }
    db.collection("users").add(user_data)
    return "success"

@app.post("/process-data")
def process_data():
    results = dataloader.results()
    return results

