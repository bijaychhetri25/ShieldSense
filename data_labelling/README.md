# Data & Labelling — ShieldSense

**Role Owner:** Jaskaran Singh (S00391717)
**Role:** Data & Labelling Lead

## What This Folder Contains

This folder holds all artefacts owned by the Data & Labelling Lead:

- `risk-taxonomy.md` — Low / Medium / High risk definitions with examples
- `labelling-protocol.md` — steps, edge cases, adjudication, agreement plan
- `consistency-check-batch1.md` — first batch consistency check
- `data-card.md` — dataset documentation
- `shieldsense-dataset.csv` — the 150–250 verified synthetic messages
- `test-set-plan.md` — held-out test set plan
- `week1-prep.md` through `week4-prep.md` — weekly meeting prep
- `scam-patterns-notes.md` — background research

## Status (Week 5)

- Taxonomy v2 finalised
- Labelling protocol v1.0 finalised
- Dataset: 202 messages, balanced across Low / Medium / High (33% each)
- Hard negatives: 108
- All verifier checks pass (labels, duplicates, length, PII, balance, hard negatives)
- Held-out test set locked (stratified 80/20, 162 train / 40 test)
- Inter-rater agreement: average Cohen's kappa = 0.832 (Almost perfect), 89.5% agreement
- Five Python scripts committed: create, dedupe, split, verify, agreement
- Ready for Week 6 leakage check