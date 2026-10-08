"""
split_dataset.py

Splits the ShieldSense dataset into a training set and a held-out test set
using a stratified 80/20 split.

Author: Jaskaran Singh (S00391717)
Role: Data & Labelling Lead
Date: 8 October 2026

Usage:
    python split_dataset.py

Inputs:
    shieldsense-dataset.csv — 200 labelled messages

Outputs:
    training-set.csv — 160 messages for model training
    test-set.csv     — 40 messages for held-out evaluation
"""

import csv
import random
from pathlib import Path
from collections import defaultdict

random.seed(42)  # fixed seed for reproducibility

TEST_RATIO = 0.20  # 20% held out


def load_dataset(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def stratified_split(rows, test_ratio):
    """
    Split rows into training and test sets, stratified by label
    so each class is proportionally represented.
    """
    by_label = defaultdict(list)
    for row in rows:
        by_label[row["label"]].append(row)

    train, test = [], []
    for label, group in by_label.items():
        random.shuffle(group)
        n_test = max(1, round(len(group) * test_ratio))
        test.extend(group[:n_test])
        train.extend(group[n_test:])

    random.shuffle(train)
    random.shuffle(test)
    return train, test


def write_csv(rows, path):
    fieldnames = [
        "id", "message", "label", "labeller",
        "date_labelled", "hard_negative", "notes"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def main():
    here = Path(__file__).parent
    rows = load_dataset(here / "shieldsense-dataset.csv")
    print(f"Loaded {len(rows)} messages")

    train, test = stratified_split(rows, TEST_RATIO)

    write_csv(train, here / "training-set.csv")
    write_csv(test, here / "test-set.csv")

    print(f"Wrote {len(train)} messages to training-set.csv")
    print(f"Wrote {len(test)} messages to test-set.csv")

    for name, group in [("Training", train), ("Test", test)]:
        print(f"\n{name} set distribution:")
        for label in ["Low", "Medium", "High"]:
            n = sum(1 for r in group if r["label"] == label)
            pct = n / len(group) * 100
            print(f"  {label}: {n} ({pct:.1f}%)")


if __name__ == "__main__":
    main()