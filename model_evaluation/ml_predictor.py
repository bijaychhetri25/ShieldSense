
# ShieldSense - Machine Learning Predictor
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead
# Week 6 - Final Training Dataset Integration

import csv
from pathlib import Path
from functools import lru_cache

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Locate the project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Use Jaskaran's final training dataset
# The locked test set is NOT used for training
DATASET_PATH = PROJECT_ROOT / "data_labelling" / "training-set.csv"


@lru_cache(maxsize=1)
def load_model():
    messages = []
    labels = []

    # Load training messages
    with open(DATASET_PATH, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            message = row["message"].strip()
            label = row["label"].strip().upper()

            if message and label in {"LOW", "MEDIUM", "HIGH"}:
                messages.append(message)
                labels.append(label)

    if not messages:
        raise ValueError("No valid messages found in training dataset.")

    # Final TF-IDF + Logistic Regression model
    # Same configuration as final_model_evaluation.py
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        ))
    ])

    # Train using ONLY the final training dataset
    model.fit(messages, labels)

    return model


def predict_message(message):
    if not message or not message.strip():
        raise ValueError("Please enter a message.")

    model = load_model()

    # Predict scam risk
    risk = str(model.predict([message])[0])

    # Calculate prediction confidence
    probabilities = model.predict_proba([message])[0]
    confidence = float(max(probabilities))

    return {
        "risk": risk,
        "confidence": round(confidence * 100, 2),
        "model": "TF-IDF + Logistic Regression",
    }
