# Dataset Gap Filling — Week 5

**Author:** Jaskaran Singh — Data & Labelling Lead
**Date:** 8 October 2026
**Purpose:** Document dataset gaps identified from model error cases and the targeted examples added to fix them.

## 1. Why This Document Exists

In Week 4 the Model & Evaluation Lead (Kapil) ran the first classifier against the rules baseline and reported its results. Some messages were misclassified. As Data & Labelling Lead, my job is to use those errors to identify gaps in the dataset — the dataset should expose the model to harder cases, not just easy ones.

## 2. Error Cases Observed in Week 4

Kapil's preliminary test on four messages produced two failures:

| Test message | Expected | Actual | Result |
|---|---|---|---|
| Urgent bank account warning | HIGH | HIGH | Pass |
| Meeting at 3pm | LOW | LOW | Pass |
| Subscription payment failed | MEDIUM | LOW | **Fail** |
| Account pending verification | MEDIUM | HIGH | **Fail** |

Both failures were on **Medium-risk** messages. The model did not have enough Medium examples to learn the boundary between Low and Medium, and between Medium and High.

This matched the placement plan's own warning:

> "120 Red / 20 Amber / 60 Green won't work. Twenty Amber means ~4 in the test set, so any metric is noise. Balance the classes."

## 3. Dataset Gaps Identified

Based on the errors, four gaps were identified:

### Gap 1 — Medium was under-represented

Before Week 5: 36 Medium messages (18% of the dataset). This was the smallest class and produced noisy test results.

**Action:** Added 34 additional Medium messages with the pattern "urgent tone but no direct request for money or credentials" — exactly the pattern the model was missing.

### Gap 2 — Short, ambiguous messages

Real scams often use very short messages. The dataset had too few of these.

**Added examples:**
- "Confirm your identity."
- "Verify now."
- "Urgent action required."
- "Click to secure your account."
- "You have 24 hours."

### Gap 3 — Government-service tone hard negatives

Legitimate messages from ATO, Centrelink, Medicare, and myGov use formal, urgent-sounding language. The model needed to see these labelled correctly.

**Added examples:**
- "Your myGov account has a new sign-in. If this wasn't you, log in to review."
- "Your Centrelink payment is scheduled for Tuesday."
- "Your Medicare card has been renewed. It will arrive by post."

### Gap 4 — Mixed personal + commercial

Edge cases where the tone is conversational but the ask is risky.

**Added examples:**
- "Mum, can you send me your bank details? I lost my card."
- "Hi, it's your boss. Can you send me the password for the shared drive?"

## 4. Duplicate Removal

When I ran `verify_dataset.py` after adding the new messages, 32 duplicate rows were detected. These were removed by `dedupe_dataset.py`, keeping the first occurrence of each message.

## 5. Distribution After Gap Filling

| Label | Before Week 5 | After Week 5 | % of total |
|---|---|---|---|
| Low | 71 | 68 | 33.7% |
| Medium | 36 | 67 | 33.2% |
| High | 56 | 67 | 33.2% |
| **Total** | **163** | **202** | **100%** |
| Hard negatives | 55 | 108 | — |

Every class now sits at ~33% of the dataset. No class is under-represented. The supervisor's balance requirement is satisfied.

## 6. Verification

All checks pass in `verify_dataset.py`:
- Labels valid
- No duplicates
- No messages over 160 characters
- No real phone numbers or email addresses
- Class balance within 20–50%
- Hard negative flags valid

## 7. Summary of Actions Taken

- Reviewed Kapil's Week 4 error cases
- Identified four dataset gaps
- Added 34 Medium messages, plus 5 short ambiguous, 3 government-tone hard negatives, 2 mixed-personal, and 3 casual legit messages
- Removed 32 duplicates
- Rebalanced to 202 messages (all ~33%)
- Re-locked the held-out test set (stratified 80/20, 162/40)
- Updated the data card to v1.0
- Committed all changes to the repository

## 8. Next Steps

- Support Kapil's retraining on the new balanced training set
- Run the leakage check in Week 6
- Finalise the inter-rater agreement report