# Held-Out Test Set Lock Note

**Author:** Jaskaran Singh — Data & Labelling Lead
**Date:** 8 October 2026
**Status:** LOCKED

## 1. Decision

The ShieldSense dataset has been split into:

- `training-set.csv` — 162 messages (used for model development)
- `test-set.csv` — 40 messages (held out, locked)

Split method: **stratified 80/20 by risk label**, with a fixed random seed (42) for reproducibility.

## 2. Rationale

- **Stratified:** Each risk band (Low, Medium, High) is proportionally represented in both sets.
- **80/20:** A standard split ratio that gives 40 messages for evaluation — enough for honest metric calculation on a small dataset.
- **Fixed seed:** Ensures the split can be reproduced exactly if the script is re-run.
- **Balanced:** Every class sits at ~33% of the dataset after deduplication and rebalancing. Test set has 14 Low, 13 Medium, 13 High. No class is under-represented.

## 3. Lock Rules

The test set is now locked. It must not be:

- Used for training
- Used for tuning thresholds
- Used to select model hyperparameters
- Opened by anyone except at Week 6 held-out evaluation

Any change to the test set requires Dr Bekhit's written approval.

The lock is verified by:

- Git commit history showing no changes to `test-set.csv` after 8 October
- Leakage check in Week 6 confirming no test messages appear in the training set

## 4. Contingency

If Dr Bekhit rules on a different split ratio, this lock will be revised and the test set regenerated. The reasoning will be documented and committed.

## 5. Sign-off

Jaskaran Singh — Data & Labelling Lead — 6 October 2026