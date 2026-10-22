import csv

with open("double-labelled.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

labellers = ["Jaskaran", "Kapil", "Alisha", "Bijay"]
disagreements = []

for row in rows:
    labels = [row[l] for l in labellers]
    if len(set(labels)) > 1:
        disagreements.append(row)

total = len(rows)
count = len(disagreements)
pct = (count / total) * 100

print(f"Rows with disagreement: {count} of {total} ({pct:.1f}%)")
print("\nDisagreement rows:")
for row in disagreements:
    print(f"  id={row['id']}: {row['message'][:70]}")
    print(f"     Labels: J={row['Jaskaran']}, K={row['Kapil']}, A={row['Alisha']}, B={row['Bijay']}")
    print()