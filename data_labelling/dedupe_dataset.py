"""
dedupe_dataset.py

Removes duplicate messages from shieldsense-dataset.csv,
keeping the first occurrence of each message.

Author: Jaskaran Singh (S00391717)
Role: Data & Labelling Lead
Date: 8 October 2026
"""

import csv
from pathlib import Path


def main():
    here = Path(__file__).parent
    path = here / "shieldsense-dataset.csv"

    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    seen = set()
    unique = []
    removed = []

    for row in rows:
        key = row["message"].strip().lower()
        if key in seen:
            removed.append(row)
        else:
            seen.add(key)
            unique.append(row)

    # Reassign sequential IDs
    for i, row in enumerate(unique, start=1):
        row["id"] = i

    fieldnames = [
        "id", "message", "label", "labeller",
        "date_labelled", "hard_negative", "notes"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in unique:
            writer.writerow({k: row.get(k, "") for k in fieldnames})

    print(f"Original: {len(rows)} rows")
    print(f"Removed:  {len(removed)} duplicates")
    print(f"Kept:     {len(unique)} unique messages")

    if removed:
        print("\nRemoved rows:")
        for row in removed:
            print(f"  id={row['id']}: {row['message'][:60]}")


if __name__ == "__main__":
    main()