
# ShieldSense - Machine Learning Predictor
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead

import csv
from pathlib import Path
from functools import lru_cache

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data_labelling" / "shieldsense-dataset.csv"


@lru_cache(maxsize=1)
def load_model():
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

    if not messages:
        raise ValueError("No valid messages found in dataset.")

    # Use the same development training split as train_classifier.py.
    # The development test messages are excluded from training.
    X_train, _, y_train, _ = train_test_split(
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
    return model


def predict_message(message):
    if not message or not message.strip():
        raise ValueError("Please enter a message.")

    model = load_model()

    risk = str(model.predict([message])[0])

    probabilities = model.predict_proba([message])[0]
    confidence = float(max(probabilities))

    return {
        "risk": risk,
        "confidence": round(confidence * 100, 2),
        "model": "TF-IDF + Logistic Regression",
    }
