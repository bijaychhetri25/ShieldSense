
# ShieldSense - Duplicate-Safe Model Evaluation
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead

import csv
from pathlib import Path
from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "data_labelling" / "shieldsense-dataset.csv"

unique_messages = {}

with open(DATASET, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        message = row["message"].strip()
        label = row["label"].strip().upper()

        if not message or label not in {"LOW", "MEDIUM", "HIGH"}:
            continue

        key = " ".join(message.lower().split())

        if key not in unique_messages:
            unique_messages[key] = {
                "message": message,
                "labels": set()
            }

        unique_messages[key]["labels"].add(label)

# Exclude conflicting labels from evaluation.
conflicts = [
    item for item in unique_messages.values()
    if len(item["labels"]) > 1
]

clean_records = [
    item for item in unique_messages.values()
    if len(item["labels"]) == 1
]

messages = [item["message"] for item in clean_records]
labels = [next(iter(item["labels"])) for item in clean_records]

print("ShieldSense - Duplicate-Safe Evaluation")
print("=======================================")
print("Unique message groups:", len(unique_messages))
print("Conflicting-label groups:", len(conflicts))
print("Usable unique messages:", len(messages))
print("Label distribution:", dict(Counter(labels)))

if conflicts:
    print("\nWARNING: Conflicting labels require team review.")
    for item in conflicts:
        print(item["message"], "->", sorted(item["labels"]))

if len(set(labels)) < 3:
    raise ValueError("All three risk categories are required.")

# Split unique messages, preventing exact duplicates
# from appearing in both training and testing.
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

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
print("Macro F1:", round(
    f1_score(y_test, predictions, average="macro"), 4
))

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
print("\nNOTE: Preliminary duplicate-safe development evaluation.")
print("Final results require verified labels and a locked test set.")
