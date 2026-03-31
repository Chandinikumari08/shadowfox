import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

print("=== SPAM DETECTION PROJECT ===")

# Load dataset
data = pd.read_csv("spam.csv")

# Preprocessing (convert to lowercase)
data['text'] = data['text'].str.lower()

# Features and labels
X = data['text']
y = data['label']

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

print("\nModel Trained Successfully\n")

# Predict on test data
y_pred = model.predict(X_test)

# Show accuracy
print("=== MODEL EVALUATION ===")
print("Accuracy:", accuracy_score(y_test, y_pred))

# Show classification report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Test with sample messages
print("\n=== SAMPLE PREDICTIONS ===")

messages = [
    "Win money now",
    "Hello friend",
    "Free offer just for you",
    "Good morning"
]

for msg in messages:
    vec = vectorizer.transform([msg.lower()])
    result = model.predict(vec)
    print(f"{msg} --> {result[0]}")

print("\n=== PROGRAM COMPLETED ===")