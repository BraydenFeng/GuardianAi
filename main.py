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
    user = auth.get_user_by_email(request.email)
    user_data = {
        "username": request.username,
        "email": request.email,
        "discord_token": processed_token,
        "discord_username": request.discord_username
    }
    db.collection("users").document(user.uid).set(user_data)
    return "success"

@app.post("/call-model")
def call_model(uid: Uid):
    return (ai.call_model(uid.uid))

@app.get("/read-dangerous")
def read_dangerous(uid: str):
    messages = db.collection("users").document(uid).collection("messages").document("dangerous-messages").get()
    if messages.exists:
        return messages.to_dict()
    else:
        return "No dangerous messages!"
    
@app.get("/get-user-info")
def get_info(uid: str):
    user_info = db.collection("users").document(uid).get()
    if user_info.exists:
        return user_info.to_dict()
    else:
        return "No user info!"
    
@app.delete("/delete-user")
def delete_user(uid: Uid):
    try:
        auth.delete_user(uid.uid)
    except auth.UserNotFoundError:
        return {"error": "User not found in Auth"}

    user_ref = db.collection("users").document(uid.uid)
    messages = user_ref.collection("messages").stream()
    for msg in messages:
        msg.reference.delete()
    user_ref.delete()

    return {"status": "success"}