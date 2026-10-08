"""
verify_dataset.py

Validates the ShieldSense synthetic dataset for quality and consistency.

Author: Jaskaran Singh (S00391717)
Role: Data & Labelling Lead
Date: 8 October 2026

Usage:
    python verify_dataset.py
"""

import csv
import re
from pathlib import Path
from collections import Counter


VALID_LABELS = {"Low", "Medium", "High"}
MAX_LENGTH = 160
PHONE_PATTERN = re.compile(r"\b(?:\+?61|0)[2-478](?:[ -]?\d){8}\b")
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")


def load_dataset(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_labels(rows):
    issues = []
    for row in rows:
        if row["label"] not in VALID_LABELS:
            issues.append(f"Row {row['id']}: invalid label '{row['label']}'")
    return issues


def check_duplicates(rows):
    seen = {}
    issues = []
    for row in rows:
        msg = row["message"].strip().lower()
        if msg in seen:
            issues.append(f"Row {row['id']}: duplicate of row {seen[msg]}")
        else:
            seen[msg] = row["id"]
    return issues


def check_length(rows):
    issues = []
    for row in rows:
        if len(row["message"]) > MAX_LENGTH:
            issues.append(f"Row {row['id']}: {len(row['message'])} chars (> {MAX_LENGTH})")
    return issues


def check_pii(rows):
    issues = []
    for row in rows:
        if PHONE_PATTERN.search(row["message"]):
            issues.append(f"Row {row['id']}: contains a phone number")
        if EMAIL_PATTERN.search(row["message"]):
            issues.append(f"Row {row['id']}: contains an email address")
    return issues


def check_balance(rows):
    counts = Counter(r["label"] for r in rows)
    total = sum(counts.values())
    issues = []
    for label in VALID_LABELS:
        pct = counts[label] / total * 100
        if pct < 20 or pct > 50:
            issues.append(f"Label '{label}' is {pct:.1f}% of dataset (expected 20-50%)")
    return issues


def check_hard_negatives(rows):
    issues = []
    for row in rows:
        flag = row["hard_negative"].strip().upper()
        if flag not in ("TRUE", "FALSE"):
            issues.append(f"Row {row['id']}: hard_negative='{row['hard_negative']}' (expected TRUE or FALSE)")
    return issues


def main():
    path = Path(__file__).parent / "shieldsense-dataset.csv"
    rows = load_dataset(path)

    print(f"Loaded {len(rows)} messages from {path.name}")
    print()

    all_checks = [
        ("Labels", check_labels),
        ("Duplicates", check_duplicates),
        ("Message length", check_length),
        ("PII (phone/email)", check_pii),
        ("Class balance", check_balance),
        ("Hard negative flags", check_hard_negatives),
    ]

    total_issues = 0
    for name, func in all_checks:
        issues = func(rows)
        status = "PASS" if not issues else f"FAIL ({len(issues)} issues)"
        print(f"[{status}] {name}")
        for issue in issues:
            print(f"    - {issue}")
        total_issues += len(issues)

    print()
    if total_issues == 0:
        print("All checks passed. Dataset is ready for use.")
    else:
        print(f"{total_issues} issues found. Fix before handover.")

    print()
    print("Distribution:")
    counts = Counter(r["label"] for r in rows)
    for label in ["Low", "Medium", "High"]:
        pct = counts[label] / len(rows) * 100
        print(f"  {label}: {counts[label]} ({pct:.1f}%)")
    hn = sum(1 for r in rows if r["hard_negative"].upper() == "TRUE")
    print(f"  Hard negatives: {hn}")


if __name__ == "__main__":
    main()