# ShieldSense Labelling Protocol v1.0

**Author:** Jaskaran Singh — Data & Labelling Lead
**Date:** 17 September 2026
**Status:** Ready for team use

## 1. Purpose

This protocol ensures all four labellers apply the same rules when assigning Low, Medium or High risk to each message. It exists so that our labels are consistent, reproducible, and defensible.

## 2. Labelling Steps

1. Read the message once without analysing it.
2. Check for three key indicators:
   - Urgency (e.g., "immediately", "final notice", "act now")
   - Request for personal information, payment, or credentials
   - Sender unfamiliarity (unknown number, generic greeting)
3. Apply the decision tree from the taxonomy:
   - No indicators → Low
   - One or two indicators → Medium
   - Request + urgency/threat/link, or all three → High
4. If unsure, mark as "flag for review" and bring it to the group.
5. Record your label in the dataset file with your initials and the date.

## 3. Edge Cases

- Legitimate service notifications that use urgent language: Label as Medium unless they ask for payment or personal information, in which case High.
- Messages from unknown numbers with no content: Label as Low but flag for review.
- Messages with shortened links: Raise the risk level by one band (Low → Medium, Medium → High).
- Messages that mix personal and commercial content: Label based on the dominant intent.

## 4. Adjudication Process

1. If two labellers disagree, the message goes to a third labeller.
2. If the third labeller agrees with one of the first two, that label is final.
3. If all three disagree, the message goes to the Data & Labelling Lead for a final ruling.
4. All disagreements and resolutions are logged in the agreement report.

## 5. Inter-Rater Agreement

- 30 messages will be double-labelled.
- Agreement will be measured using Cohen's kappa (primary) and percentage agreement (secondary).
- Target: kappa ≥ 0.61 (substantial agreement).
- If agreement falls below 0.61, the protocol is reviewed and labellers are retrained.

## 6. Hard Negatives

At least 20 messages in the dataset must be hard negatives — legitimate messages that look risky.

## 7. Labeller Training Record

| Labeller | Date trained | Protocol version | Signature |
|---|---|---|---|
| Jaskaran Singh | 17 Sep 2026 | 1.0 | J.S. |
| Kapil Thapa Magar | 17 Sep 2026 | 1.0 | |
| Alisha | 17 Sep 2026 | 1.0 | |
| Bijay Bahadur Chhetri | 17 Sep 2026 | 1.0 | |

## 8. Version History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 17 Sep 2026 | Initial protocol | Jaskaran |