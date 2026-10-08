
# ShieldSense - Preliminary Model Comparison
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead

import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    classification_report
)

from rules_baseline import classify_message

ROOT = Path(__file__).resolve().parent.parent
DATASET = ROOT / "data_labelling" / "shieldsense-dataset.csv"

messages = []
labels = []

with open(DATASET, newline="", encoding="utf-8-sig") as file:
    for row in csv.DictReader(file):
        message = row["message"].strip()
        label = row["label"].strip().upper()

        if message and label in {"LOW", "MEDIUM", "HIGH"}:
            messages.append(message)
            labels.append(label)

# Same preliminary development split for both models
X_train, X_test, y_train, y_test = train_test_split(
    messages,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)

# Model 1: Rules-based baseline
baseline_predictions = [
    classify_message(message)["risk"]
    for message in X_test
]

# Model 2: TF-IDF + Logistic Regression
ml_model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ))
])

ml_model.fit(X_train, y_train)
ml_predictions = ml_model.predict(X_test)

risk_labels = ["LOW", "MEDIUM", "HIGH"]


def evaluate(name, predictions):
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test,
        predictions,
        labels=risk_labels,
        average="macro",
        zero_division=0
    )

    accuracy = accuracy_score(y_test, predictions)

    print(f"\n{name}")
    print("-" * 50)
    print(f"Accuracy:        {accuracy:.2%}")
    print(f"Macro Precision: {precision:.2%}")
    print(f"Macro Recall:    {recall:.2%}")
    print(f"Macro F1-score:  {f1:.2%}")

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        predictions,
        labels=risk_labels,
        zero_division=0
    ))

    print("Confusion Matrix:")
    print("Rows = Actual, Columns = Predicted")
    print("Order:", risk_labels)
    print(confusion_matrix(
        y_test,
        predictions,
        labels=risk_labels
    ))

    errors = [
        (message, actual, predicted)
        for message, actual, predicted
        in zip(X_test, y_test, predictions)
        if actual != predicted
    ]

    print(f"\nMisclassified messages: {len(errors)}")

    for message, actual, predicted in errors:
        print(f"\nMessage: {message}")
        print(f"Expected: {actual}")
        print(f"Predicted: {predicted}")

    return accuracy, precision, recall, f1


print("SHIELDSENSE - PRELIMINARY MODEL COMPARISON")
print("=" * 50)
print("Dataset messages:", len(messages))
print("Training messages:", len(X_train))
print("Testing messages:", len(X_test))

baseline_results = evaluate(
    "RULES-BASED BASELINE",
    baseline_predictions
)

ml_results = evaluate(
    "TF-IDF + LOGISTIC REGRESSION",
    ml_predictions
)

print("\nFINAL COMPARISON TABLE")
print("=" * 75)
print(
    f"{'Model':<28}"
    f"{'Accuracy':>10}"
    f"{'Precision':>12}"
    f"{'Recall':>10}"
    f"{'F1':>10}"
)

for name, results in [
    ("Rules-Based Baseline", baseline_results),
    ("TF-IDF + Logistic Regression", ml_results)
]:
    print(
        f"{name:<28}"
        + "".join(f"{value:>10.2%}" for value in results)
    )

print("\nNOTE: These are preliminary development results.")
print("The dataset labels and held-out test set require final verification.")
