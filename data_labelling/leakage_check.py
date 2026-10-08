"""
leakage_check.py

Verifies that no message from the held-out test set appears in the
training set. This is the leakage check required in Week 6.

Author: Jaskaran Singh (S00391717)
Role: Data & Labelling Lead
Date: 8 October 2026

Usage:
    python leakage_check.py

Reads:
    training-set.csv — the training data
    test-set.csv     — the held-out test data

Outputs:
    A leakage report printed to the terminal.
    Exit code 0 if no leakage, exit code 1 if leakage detected.
"""

import csv
import sys
from pathlib import Path


def load_messages(path):
    """Load all messages from a CSV file, lowercased and stripped."""
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [row["message"].strip().lower() for row in rows]


def main():
    here = Path(__file__).parent
    train_path = here / "training-set.csv"
    test_path = here / "test-set.csv"

    if not train_path.exists() or not test_path.exists():
        print("ERROR: training-set.csv or test-set.csv is missing.")
        sys.exit(1)

    train = load_messages(train_path)
    test = load_messages(test_path)

    print(f"Training set: {len(train)} messages")
    print(f"Test set:     {len(test)} messages")
    print()

    # Check overlap
    train_set = set(train)
    test_set = set(test)
    overlap = train_set & test_set

    if overlap:
        print(f"LEAKAGE DETECTED: {len(overlap)} test messages appear in training.")
        print()
        print("Leaking messages:")
        for msg in overlap:
            print(f"  - {msg[:80]}")
        print()
        print("Result: FAIL")
        sys.exit(1)
    else:
        print("No overlap between training and test sets.")
        print()
        print("Result: PASS — no leakage detected.")
        sys.exit(0)


if __name__ == "__main__":
    main()