# Week 6 Meeting Preparation

**Student:** Jaskaran Singh
**Role:** Data & Labelling Lead
**Date:** 8 October 2026
**Meeting:** Thursday on-campus, 2:15–3:00 pm
**Meeting type:** Week 6 — Evaluation and accessibility week. Presentation rehearsal.

## One Artefact Produced This Week

Three linked deliverables, committed to the repo under my own account:

1. **Leakage check script (`leakage_check.py`)** — proves no test message appears in the training set.
2. **Leakage check report (`leakage-check-report.md`)** — documents the PASS result.
3. **Held-out test set lock confirmed** — the test set remains locked after the leakage check.

Also committed:
- `dataset-gaps-wk5.md` — error-case-driven gap filling documentation
- `inter-rater-agreement-report.md` — kappa = 0.832 (almost perfect)
- Updated `data-card.md` v1.0
- `week5-prep.md` — completed and pushed today

**Evidence:** Latest commits on `main` branch under `jaskaran0710`.

## One Decision Required

Confirm the held-out test set split ratio (stratified 80/20) that I locked this week, and confirm the inter-rater agreement metric (Cohen's kappa primary, percentage agreement secondary). If the ratio should change, I will regenerate the split and re-run the leakage check tonight.

## One Evidence Item — Logbook

- **Hours this week:** 6 so far (Week 6: 5–9 Oct) — will reach 12 by Friday
- **Cumulative:** ~71
- **Activities:** leakage check script and report, test set lock confirmation, week5-prep.md finalised, week6-prep.md prepared
- **Evidence reference:** GitHub commit history; `data_labelling/` folder

## Progress Against My Role

- Taxonomy v2 committed
- Labelling protocol v1.0 committed
- Dataset: 202 messages, balanced across all three classes (~33% each)
- Held-out test set: locked, and confirmed leakage-free
- Inter-rater agreement: kappa = 0.832 (almost perfect), 89.5% agreement
- All five Python scripts committed (create, dedupe, split, verify, agreement) plus leakage_check.py
- Source code and dataset both under my own GitHub account

## Blockers

None. Dataset and test set are complete. Ready for the AT2 Progress Presentation rehearsal.

## Next Week (Week 7)

- **Progress Presentation (Task 2, 30%)** — present my role and contribution in a mock job interview format
- Continue supporting Kapil's held-out evaluation
- Prepare the AT3 Final Report structure for my section

## Presentation Rehearsal Notes

For the AT2 rehearsal this week, my section will cover:

1. **Role ownership** — what a Data & Labelling Lead actually does
2. **Deliverables shipped** — taxonomy, protocol, 202-message dataset, locked test set, kappa = 0.832
3. **Key decision I made** — rebalanced the dataset from 18% Medium to 33% Medium, after identifying Kapil's Week 4 model failures were both on Medium-risk messages
4. **Complexity** — the trade-off between synthetic data realism and the hard boundaries (no real messages)
5. **What I would do differently** — commit weekly from Week 1 instead of retroactively