# Week 5 Meeting Preparation

**Student:** Jaskaran Singh
**Role:** Data & Labelling Lead
**Date:** 8 October 2026
**Meeting:** Thursday on-campus, 2:15–3:00 pm

## One Artefact Produced This Week

Five linked deliverables, all committed to the repository under my own account (`jaskaran0710`):

1. **Data Card v1.0** — final version with distribution, limitations, and held-out test set section.
2. **Dataset Gap Filling Document** (`dataset-gaps-wk5.md`) — documents the error-case-driven gap filling. Kapil's Week 4 test showed two MEDIUM failures; I added 34 targeted Medium examples to fix the pattern the model was missing.
3. **Cleaned dataset (202 messages)** — removed 32 duplicates, rebalanced to 68 Low / 67 Medium / 67 High (all ~33%).
4. **Locked held-out test set** — stratified 80/20 (162 training / 40 test), with `test-set-lock.md` documenting reasoning and lock rules.
5. **Inter-rater agreement report** — 30 double-labelled messages, average Cohen's kappa = 0.832 (Almost perfect), 89.5% agreement.

Also committed: five Python scripts (`create_dataset.py`, `dedupe_dataset.py`, `split_dataset.py`, `verify_dataset.py`, `inter_rater_agreement.py`).

**Evidence:** All files in `data_labelling/` in the repo. Latest commit `95d91de`.

## One Decision Required

Confirm the held-out test set split ratio (stratified 80/20) that I locked this week. I made the decision to unblock Kapil for the Week 6 evaluation. If you would prefer a different ratio, I will regenerate the split and re-document.

I also want to confirm the agreement metric for the inter-rater report (Cohen's kappa as primary, percentage agreement as secondary).

## One Evidence Item — Logbook

- **Hours this week:** 12
- **Cumulative:** 71
- **Activities:** dataset gap filling from error cases, duplicate removal, rebalancing, test set lock, five Python scripts, data card update, inter-rater agreement report, weekly commits
- **Evidence reference:** GitHub commits under my own account; `data_labelling/` folder in repo

## Progress Against My Role

- Taxonomy v2 finalised and committed
- Labelling protocol v1.0 finalised and committed
- Dataset: 202 balanced messages (all ~33%)
- All verifier checks pass
- Held-out test set locked and delivered to Model Lead
- Inter-rater agreement: kappa = 0.832 (Almost perfect)
- Source code committed — supervisor's specific feedback addressed

## Blockers

None. The dataset is complete and the test set is locked. Ready for the Week 6 leakage check.

## Next Week (Week 6)

- Run leakage check between training and test sets
- Finalise inter-rater agreement report
- Rehearse AT2 Progress Presentation (Task 2, 30%) — present my role
- Support Kapil with any dataset findings from the held-out evaluation