"""
create_dataset.py

Regenerates the ShieldSense synthetic scam-message dataset from
message pools. Run this if the dataset needs to be rebuilt.

Author: Jaskaran Singh (S00391717)
Role: Data & Labelling Lead
Date: 8 October 2026

Usage:
    python create_dataset.py

Output:
    shieldsense-dataset.csv — 202 balanced messages

Notes:
    - This script reads from the existing CSV if it is present, so it
      acts as a validator + reorganiser rather than a generator.
    - The messages themselves are curated manually; this script ensures
      the CSV is well-formed and correctly labelled.
"""

import csv
from pathlib import Path
from collections import Counter


FIELD_NAMES = [
    "id", "message", "label", "labeller",
    "date_labelled", "hard_negative", "notes"
]

VALID_LABELS = {"Low", "Medium", "High"}


def load_existing(path):
    """Load existing dataset if present."""
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate(rows):
    """Basic validation before writing."""
    issues = []
    for i, row in enumerate(rows, start=1):
        if row["label"] not in VALID_LABELS:
            issues.append(f"Row {i}: invalid label {row['label']}")
        if not row["message"].strip():
            issues.append(f"Row {i}: empty message")
    return issues


def write_csv(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in FIELD_NAMES})


def main():
    here = Path(__file__).parent
    path = here / "shieldsense-dataset.csv"

    rows = load_existing(path)
    if not rows:
        print(f"No existing dataset found at {path}")
        print("Nothing to do.")
        return

    issues = validate(rows)
    if issues:
        print(f"{len(issues)} validation issues:")
        for issue in issues:
            print(f"  - {issue}")
        return

    # Reassign IDs to be sequential
    for i, row in enumerate(rows, start=1):
        row["id"] = i

    write_csv(rows, path)

    print(f"Wrote {len(rows)} messages to {path.name}")
    counts = Counter(r["label"] for r in rows)
    for label in ["Low", "Medium", "High"]:
        pct = counts[label] / len(rows) * 100
        print(f"  {label}: {counts[label]} ({pct:.1f}%)")
    hn = sum(1 for r in rows if r["hard_negative"].upper() == "TRUE")
    print(f"  Hard negatives: {hn}")


if __name__ == "__main__":
    main()