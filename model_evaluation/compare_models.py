
# ShieldSense - Final Locked Test Set Model Comparison
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead
#
# Compares the rules-based baseline and TF-IDF + Logistic
# Regression on the SAME locked 40-message test set.
# Do not tune either model using these results.

import csv
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    classification_report
)

from rules_baseline import classify_message

ROOT = Path(__file__).resolve().parent.parent
TRAIN_PATH = ROOT / "data_labelling" / "training-set.csv"
TEST_PATH = ROOT / "data_labelling" / "test-set.csv"

RISK_LABELS = ["LOW", "MEDIUM", "HIGH"]


def load_dataset(path):
    messages = []
    labels = []

    with open(path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            message = row["message"].strip()
            label = row["label"].strip().upper()

            if not message or label not in RISK_LABELS:
                raise ValueError(
                    f"Invalid message or label in {path.name}: {row}"
                )

            messages.append(message)
            labels.append(label)

    return messages, labels


# Load Jaskaran's approved training and locked test sets
X_train, y_train = load_dataset(TRAIN_PATH)
X_test, y_test = load_dataset(TEST_PATH)

# Verify no exact message overlap after basic normalisation
train_messages = {m.strip().lower() for m in X_train}
test_messages = {m.strip().lower() for m in X_test}

overlap = train_messages.intersection(test_messages)

if overlap:
    raise ValueError(
        f"Data leakage detected: {len(overlap)} overlapping messages."
    )

print("SHIELDSENSE - FINAL HELD-OUT MODEL COMPARISON")
print("=" * 65)
print("Training messages:", len(X_train))
print("Locked test messages:", len(X_test))
print("Training/test overlap:", len(overlap))


# Model 1: Existing rules-based baseline
baseline_predictions = [
    classify_message(message)["risk"]
    for message in X_test
]


# Model 2: Original TF-IDF + Logistic Regression
# Keep the same configuration as final_model_evaluation.py
ml_model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ))
])

# Train only on the 162 training messages
ml_model.fit(X_train, y_train)

# Predict only on the locked test messages
ml_predictions = ml_model.predict(X_test)


def evaluate(name, predictions):
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test,
        predictions,
        labels=RISK_LABELS,
        average="macro",
        zero_division=0
    )

    accuracy = accuracy_score(y_test, predictions)

    print(f"\n{name}")
    print("-" * 65)
    print(f"Accuracy:        {accuracy:.2%}")
    print(f"Macro Precision: {precision:.2%}")
    print(f"Macro Recall:    {recall:.2%}")
    print(f"Macro F1-score:  {f1:.2%}")

    print("\nClassification Report:")
    print(classification_report(
        y_test,
        predictions,
        labels=RISK_LABELS,
        zero_division=0
    ))

    print("Confusion Matrix:")
    print("Rows = Actual, Columns = Predicted")
    print("Order:", RISK_LABELS)
    print(confusion_matrix(
        y_test,
        predictions,
        labels=RISK_LABELS
    ))

    high_total = sum(label == "HIGH" for label in y_test)
    high_correct = sum(
        actual == "HIGH" and predicted == "HIGH"
        for actual, predicted in zip(y_test, predictions)
    )

    high_recall = (
        high_correct / high_total if high_total else 0
    )

    print(
        f"\nHIGH-risk detection: "
        f"{high_correct}/{high_total}"
    )
    print(f"HIGH-risk recall: {high_recall:.2%}")

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

    return accuracy, precision, recall, f1, high_recall


baseline_results = evaluate(
    "RULES-BASED BASELINE",
    baseline_predictions
)

ml_results = evaluate(
    "TF-IDF + LOGISTIC REGRESSION",
    ml_predictions
)


print("\nFINAL LOCKED TEST COMPARISON TABLE")
print("=" * 90)

print(
    f"{'Model':<30}"
    f"{'Accuracy':>12}"
    f"{'Macro F1':>12}"
    f"{'HIGH Recall':>15}"
)

for name, results in [
    ("Rules-Based Baseline", baseline_results),
    ("TF-IDF + Logistic Regression", ml_results)
]:
    accuracy, precision, recall, f1, high_recall = results

    print(
        f"{name:<30}"
        f"{accuracy:>12.2%}"
        f"{f1:>12.2%}"
        f"{high_recall:>15.2%}"
    )


print("\nIMPORTANT NOTES")
print("-" * 65)
print("Both models were evaluated on the same locked test set.")
print("The ML model was trained only on training-set.csv.")
print("No model tuning was performed using the locked test set.")
print("Earlier comparison results used a different development split.")
print("Those preliminary figures are not final held-out results.")
print("These results apply to a small synthetic dataset.")
print("ShieldSense is a prototype, not a deployable safety system.")
