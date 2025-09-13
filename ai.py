from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch

model_path = "model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
id2label = {
    0: "Coercion and Manipulation",
    1: "Deception",
    2: "Explicit Solicitation",
    3: "Grooming",
    4: "Not predatory"
}

text = "What music do you like to listen to? Just curious!"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=-1).item()

print("Predicted label:", id2label[predicted_class])
