import dataloader
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