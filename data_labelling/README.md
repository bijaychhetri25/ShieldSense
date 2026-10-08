# Data & Labelling — ShieldSense

**Role Owner:** Jaskaran Singh (S00391717)
**Role:** Data & Labelling Lead

## What This Folder Contains

**Documentation:**
- `risk-taxonomy.md` — Low / Medium / High risk definitions with examples
- `labelling-protocol.md` — steps, edge cases, adjudication, agreement plan
- `data-card.md` — dataset documentation (v1.0)
- `test-set-plan.md` — held-out test set plan
- `test-set-lock.md` — lock note and reasoning
- `consistency-check-batch1.md` — first batch consistency check
- `dataset-gaps-wk5.md` — error-case-driven gap filling
- `inter-rater-agreement-report.md` — kappa = 0.832
- `leakage-check-report.md` — Week 6 leakage check (PASS)
- `scam-patterns-notes.md` — background research

**Source code:**
- `create_dataset.py`
- `dedupe_dataset.py`
- `split_dataset.py`
- `verify_dataset.py`
- `inter_rater_agreement.py`
- `leakage_check.py`

**Data:**
- `shieldsense-dataset.csv` — 202 balanced messages
- `training-set.csv` — 162 messages
- `test-set.csv` — 40 messages (locked)
- `double-labelled.csv` — 30 messages labelled by all four team members

**Weekly meeting prep:**
- `week1-prep.md` through `week6-prep.md`

## Status (Week 6)

- Taxonomy v2 finalised
- Labelling protocol v1.0 finalised
- Dataset: 202 messages, balanced across Low / Medium / High (33% each)
- Hard negatives: 108
- All verifier checks pass (labels, duplicates, length, PII, balance, hard negatives)
- Held-out test set locked (stratified 80/20, 162 train / 40 test)
- Leakage check passed — 0 overlap between training and test sets
- Inter-rater agreement: average Cohen's kappa = 0.832 (Almost perfect), 89.5% agreement
- Six Python scripts committed: create, dedupe, split, verify, agreement, leakage
- Ready for AT2 Progress Presentation (Week 7)