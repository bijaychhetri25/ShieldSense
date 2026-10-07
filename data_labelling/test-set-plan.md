# Held-Out Test Set Plan

**Author:** Jaskaran Singh
**Date:** 24 September 2026
**Status:** Awaiting client ruling on split ratio

## Options

- Option A: 80/20 split (approx. 160 train / 40 test)
- Option B: 70/30 split (approx. 140 train / 60 test)
- Option C: Stratified split by risk category (recommended)

## Recommendation

Stratified split (Option C) to guarantee each risk band is proportionally represented in both training and test sets. This is better for honest evaluation and matches the client's expectation of a professional-grade comparison table.

## Lock Procedure

1. Client approves split ratio
2. Test set extracted from the full dataset
3. Test set saved as `test-set.csv` (separate file)
4. Training set saved as `training-set.csv`
5. Test set never opened again until Week 6 evaluation
6. Leakage check run in Week 6