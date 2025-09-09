import dataloader
import ai
from dataloader import results
from fastapi import FastAPI
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore, auth

app = FastAPI()
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class User(BaseModel):
    username: str
    password: str
    email: str

@app.post("/create-user")
def create_user(request: User):
    user = auth.create_user(
        email = request.email,
        password = request.password,
        display_name = request.username
        )   
    user_data = {
        "username": request.username,
        "email": request.email
    }
    db.collection("users").add(user_data)
    return "success"

@app.post("/process-data")
def process_data()
    #TODO integrate data