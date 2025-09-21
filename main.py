from dependencies import *
import ai

class User(BaseModel):
    username: str
    password: str
    email: str
    discord_token: str
    discord_username: str

class Uid(BaseModel):
    uid: str

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

@app.post("/call-model")
def call_model(uid: Uid):
    return (ai.call_model(uid.uid))