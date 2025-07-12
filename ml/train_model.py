import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from ml.utils import pipe_tokenizer
import pickle
import os


# Load dataset
df = pd.read_csv('ml/symptoms.csv')
X = df['symptoms']
y = df['dosha']

vectorizer = CountVectorizer(tokenizer=pipe_tokenizer)
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("✅ Model Evaluation Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# ✅ Now this will work
with open('ml/dosha_model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)

print("\n✅ Model trained and saved successfully!")
