
# ShieldSense - Final Held-Out Model Evaluation
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead

import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
TRAIN_PATH = PROJECT_ROOT / "data_labelling" / "training-set.csv"
TEST_PATH = PROJECT_ROOT / "data_labelling" / "test-set.csv"

LABELS = ["LOW", "MEDIUM", "HIGH"]


def load_dataset(path):
    messages = []
    labels = []

    with open(path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            message = row["message"].strip()
            label = row["label"].strip().upper()

            if not message or label not in LABELS:
                raise ValueError(f"Invalid row in {path.name}: {row}")

            messages.append(message)
            labels.append(label)

    return messages, labels


# Load separate training and locked testing datasets
X_train, y_train = load_dataset(TRAIN_PATH)
X_test, y_test = load_dataset(TEST_PATH)

# Check that no exact messages overlap after normalisation
train_messages = {m.strip().lower() for m in X_train}
test_messages = {m.strip().lower() for m in X_test}

if train_messages & test_messages:
    raise ValueError("Data leakage detected! Evaluation stopped.")

# Keep the original model settings
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ))
])

# Train ONLY on the training set
model.fit(X_train, y_train)

# Evaluate ONLY on the locked test set
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
macro_f1 = f1_score(
    y_test, predictions, labels=LABELS, average="macro", zero_division=0
)

print("\nShieldSense - Final Held-Out Evaluation")
print("======================================")
print("Training messages:", len(X_train))
print("Locked test messages:", len(X_test))
print("Training/test overlap: 0")
print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Macro F1-score: {macro_f1 * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    labels=LABELS,
    zero_division=0
))

print("Confusion Matrix:")
print("Label order:", LABELS)
print(confusion_matrix(y_test, predictions, labels=LABELS))

print("\nFinal evaluation completed.")
print("Do not tune the model using these test results.")
