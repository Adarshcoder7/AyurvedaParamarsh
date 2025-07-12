# ml/predict.py

import pickle
import os

# ✅ Add this tokenizer (MUST match training code!)
def pipe_tokenizer(text):
    return text.split('|')

# Load model and vectorizer
with open(os.path.join('ml', 'dosha_model.pkl'), 'rb') as f:
    model, vectorizer = pickle.load(f)

def predict_dosha(symptom_list):
    input_text = '|'.join(symptom_list)
    vec = vectorizer.transform([input_text])
    prediction = model.predict(vec)
    return prediction[0]

# Test run
if __name__ == "__main__":
    result = predict_dosha(['dry skin', 'anxiety', 'constipation'])
    print("Predicted Dosha:", result)
