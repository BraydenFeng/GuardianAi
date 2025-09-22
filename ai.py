from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from dependencies import db, cipher, dataloader
from google.cloud.firestore_v1 import ArrayUnion
from services import process_user_data

id2label = {0: "Not Predatory", 1: "Predatory"}
label2id = {"Not Predatory": 0, "Predatory": 1}
model = AutoModelForSequenceClassification.from_pretrained("model")
tokenizer = AutoTokenizer.from_pretrained("model")

def call_model(uid: str):
    dangerous_messages = []
    data = process_user_data(db, cipher, dataloader, uid)
    model.eval()
    with torch.no_grad():
        for channel in data:
            for message in channel:
                tokenized_text = tokenizer(message['content'], padding=True, truncation=True, return_tensors="pt")
                predictions = model(input_ids=tokenized_text['input_ids'], attention_mask=tokenized_text['attention_mask'])
                predicted_class = predictions.logits.argmax(dim=1).item()
                label = id2label[predicted_class]
                if label == "Predatory":
                    dangerous_messages.append(message)
    db.collection("users").document(uid).collection("messages").document("dangerous-messages").set({
        "dangerous_messages": ArrayUnion(dangerous_messages)
        }, merge=True)
    return "Success!"

