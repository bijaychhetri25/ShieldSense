# Week 4 Meeting Preparation

**Student:** Jaskaran Singh
**Role:** Data & Labelling Lead
**Date:** 24 September 2026
**Meeting:** Thursday on-campus, 2:15–3:00 pm
**Checkpoint 1:** continue / narrow / redirect

## One Artefact Produced This Week

Three linked artefacts, all committed to GitHub:

1. Risk Taxonomy v2.0 — refined Low / Medium / High definitions with edge cases, hard negatives and decision tree.
2. Labelling Protocol v1.0 — steps, edge cases, adjudication, inter-rater agreement plan.
3. Consistency Check Log — Batch 1 — 50 messages checked, 10 ambiguous cases flagged, patterns documented.

Plus the dataset file started (200 messages) and the data card draft.

**Evidence:** `risk-taxonomy.md`, `labelling-protocol.md`, `consistency-check-batch1.md`, `shieldsense-dataset.csv`, `data-card.md`

## One Decision Required

Held-out test set split ratio.

- Option A: 80/20
- Option B: 70/30
- Option C: Stratified split by risk category (my preference)

I lean towards Option C because it guarantees the test set reflects the real distribution of Low, Medium and High risk messages. I also want to confirm Cohen's kappa as the primary agreement metric with percentage agreement as secondary.

## One Evidence Item — Logbook

- Hours this week: 12
- Cumulative: 47
- Activities: taxonomy refinement, consistency check on 50 messages, dataset labelling, data card draft, GitHub commits, sharing taxonomy and dataset structure with the Model Lead
- Evidence reference: GitHub commits under my own account; logbook

## Checkpoint 1 — Honest Assessment

- Taxonomy and protocol are strong and ready.
- Dataset is progressing; 200 messages done, target met.
- Consistency check done on first batch; useful patterns found.
- Test set not yet locked — waiting on split ratio decision.
- Recommendation: Continue, with narrowing on the split decision. No redirect needed.

## Blockers

- Split ratio decision needed to lock test set by Friday.
- GitHub is now active — all four of us are committing.

## Next Week (Week 5)

- Complete dataset (150–250 messages) — done at 200
- Lock held-out test set
- Finalise data card
- Run 30 double-labelled messages for inter-rater agreement
- Support Model Lead and Interface Lead with examples