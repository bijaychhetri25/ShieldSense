# Label Consistency Check Log — Batch 1

**Author:** Jaskaran Singh — Data & Labelling Lead
**Date:** 23 September 2026
**Batch:** First 50 messages

## 1. Summary

- Messages checked: 50
- Labelled by: Jaskaran Singh
- Cross-checked against: Labelling Protocol v1.0
- Date of check: 23 September 2026

## 2. Ambiguous Cases Flagged

| # | Message | Initial label | Issue | Final label |
|---|---|---|---|---|
| 1 | "Your parcel is waiting. Click here." | Medium | Could be legitimate or scam; shortened link | Medium (flagged) |
| 2 | "Hi, it's Sarah from work." | Low | Unknown number | Low |
| 3 | "Your account has a new login." | Medium | Matches scam pattern but could be legitimate | Medium |
| 4 | "Final notice: unpaid toll. Pay now." | High | Clear scam pattern | High |
| 5 | "Your Telstra bill is ready. View it in the app." | Low | Legitimate but urgent tone | Low (hard negative) |
| 6 | "You have won a $500 gift card. Claim here." | High | Too-good-to-be-true + link | High |
| 7 | "Reminder: dentist appointment tomorrow." | Low | Familiar context | Low |
| 8 | "Your ATO refund is ready. Log in to myGov." | Medium | Legitimate but matches scam wording | Medium (hard negative) |
| 9 | "URGENT: Your account will be closed." | High | Threat + urgency | High |
| 10 | "Can you send me the report by 5pm?" | Low | Work context | Low |

## 3. Patterns Noticed

- Legitimate service notifications often use urgent language, which makes them look riskier than they are.
- Shortened links are a strong indicator but not always present in scams.
- Messages from unknown numbers with no context are hard to label and often need review.
- Too-good-to-be-true offers almost always indicate High risk.

## 4. Actions Taken

- Added "flag for review" category to the protocol for ambiguous cases.
- Noted that shortened links should raise the risk level by one band.
- Added at least 5 hard negatives to the dataset from this batch.
- Flagged two messages for a second opinion before finalising.

## 5. Next Steps

- Complete consistency check on the remaining messages.
- Run the 30 double-labelled messages for inter-rater agreement.
- Finalise the data card with these findings.