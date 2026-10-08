"""
inter_rater_agreement.py

Calculates inter-rater agreement for the ShieldSense dataset.

Author: Jaskaran Singh (S00391717)
Role: Data & Labelling Lead
Date: 8 October 2026

Usage:
    python inter_rater_agreement.py

Reads:
    double-labelled.csv — 30 messages labelled by all 4 labellers

Outputs:
    Cohen's kappa for each pair of labellers
    Percentage agreement for each pair
    Overall average
"""

import csv
from itertools import combinations
from pathlib import Path
from collections import Counter


def cohens_kappa(labels_a, labels_b):
    """
    Compute Cohen's kappa between two lists of labels.
    kappa = (po - pe) / (1 - pe)
    """
    assert len(labels_a) == len(labels_b)
    n = len(labels_a)

    po = sum(1 for a, b in zip(labels_a, labels_b) if a == b) / n

    counts_a = Counter(labels_a)
    counts_b = Counter(labels_b)
    pe = sum(
        (counts_a[k] / n) * (counts_b[k] / n)
        for k in set(list(counts_a) + list(counts_b))
    )

    if pe == 1:
        return 1.0
    return (po - pe) / (1 - pe)


def interpret(kappa):
    """Landis & Koch interpretation."""
    if kappa < 0:
        return "Poor"
    if kappa < 0.21:
        return "Slight"
    if kappa < 0.41:
        return "Fair"
    if kappa < 0.61:
        return "Moderate"
    if kappa < 0.81:
        return "Substantial"
    return "Almost perfect"


def main():
    here = Path(__file__).parent
    path = here / "double-labelled.csv"

    if not path.exists():
        print(f"No file found at {path}")
        print("Create double-labelled.csv with columns: id, message, Jaskaran, Kapil, Alisha, Bijay")
        return

    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    labellers = ["Jaskaran", "Kapil", "Alisha", "Bijay"]
    print(f"Loaded {len(rows)} double-labelled messages")
    print()

    print("Pairwise agreement:")
    print(f"{'Pair':<25} {'% agree':>8} {'kappa':>8}  Interpretation")
    print("-" * 65)

    kappas = []
    for a, b in combinations(labellers, 2):
        labels_a = [r[a] for r in rows]
        labels_b = [r[b] for r in rows]

        n = len(rows)
        agree = sum(1 for x, y in zip(labels_a, labels_b) if x == y)
        pct = agree / n * 100

        k = cohens_kappa(labels_a, labels_b)
        kappas.append(k)

        print(f"{a} <-> {b:<15} {pct:>7.1f}% {k:>8.3f}  {interpret(k)}")

    print()
    avg = sum(kappas) / len(kappas)
    print(f"Average kappa: {avg:.3f}")
    print(f"Target: >= 0.61 (substantial agreement)")
    status = "PASS" if avg >= 0.61 else "FAIL"
    print(f"Status: {status}")


if __name__ == "__main__":
    main()