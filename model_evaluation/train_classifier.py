
# ShieldSense - TF-IDF + Logistic Regression Classifier
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead
# Week 5 - Preliminary Model Development

import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# Locate Jaskaran's dataset
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data_labelling" / "shieldsense-dataset.csv"

messages = []
labels = []

with open(DATASET_PATH, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        message = row["message"].strip()
        label = row["label"].strip().upper()

        if message and label in {"LOW", "MEDIUM", "HIGH"}:
            messages.append(message)
            labels.append(label)

print("ShieldSense - Preliminary ML Evaluation")
print("=======================================")
print("Total valid messages:", len(messages))

# Development split only - NOT the final locked test set
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

# TF-IDF converts text into numerical features.
# Logistic Regression learns to classify the risk level.
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ))
])

model.fit(X_train, y_train)
predictions = model.predict(X_test)

risk_labels = ["LOW", "MEDIUM", "HIGH"]

print("\nTraining messages:", len(X_train))
print("Testing messages:", len(X_test))

print("\nAccuracy:", round(accuracy_score(y_test, predictions), 4))

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    labels=risk_labels,
    zero_division=0
))

print("\nConfusion Matrix:")
print("Rows = Actual, Columns = Predicted")
print("Order:", risk_labels)
print(confusion_matrix(
    y_test,
    predictions,
    labels=risk_labels
))

print("\nMisclassified Messages:")
errors = 0

for message, actual, predicted in zip(X_test, y_test, predictions):
    if actual != predicted:
        errors += 1
        print("\nMessage:", message)
        print("Expected:", actual)
        print("Predicted:", predicted)

print("\nTotal misclassified:", errors)
print("\nNOTE: Preliminary development results only.")
print("Final evaluation requires the verified, locked test set.")
