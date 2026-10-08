# Leakage Check Report — Week 6

**Author:** Jaskaran Singh — Data & Labelling Lead
**Date:** 8 October 2026
**Status:** PASS

## 1. Purpose

This report verifies that no message from the held-out test set appears in the training set. If test messages leaked into training, the model would have already seen the "unseen" data and the held-out evaluation would be meaningless.

## 2. Method

- Loaded `training-set.csv` (162 messages)
- Loaded `test-set.csv` (40 messages)
- Normalised both sets by lowercasing and stripping whitespace
- Computed the intersection of the two message sets
- If the intersection is non-empty, leakage is present

Script: `leakage_check.py`

## 3. Result

| Check | Result |
|---|---|
| Training set size | 162 messages |
| Test set size | 40 messages |
| Overlap | 0 messages |
| Leakage detected | No |
| **Result** | **PASS** |

The training and test sets are disjoint. No test message appears in the training set.

## 4. Interpretation

The held-out test set is clean. Any evaluation results produced by the Model & Evaluation Lead on `test-set.csv` reflect the model's performance on messages it has not seen during training. The evaluation is therefore valid.

## 5. Follow-up

- The test set remains locked (see `test-set-lock.md`)
- No changes to `test-set.csv` are permitted after this check without supervisor approval
- If the model is retrained, this check must be repeated

## 6. Evidence

- `training-set.csv`
- `test-set.csv`
- `leakage_check.py`
- This report

## 7. Sign-off

Jaskaran Singh — Data & Labelling Lead — 8 October 2026