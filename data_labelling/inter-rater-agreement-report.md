# Inter-Rater Agreement Report

**Author:** Jaskaran Singh — Data & Labelling Lead
**Date:** 8 October 2026
**Status:** Final

## 1. Purpose

This report documents agreement between labellers on the ShieldSense dataset. It demonstrates that our labels are consistent, reproducible, and defensible — not one person's opinion.

## 2. Method

- **Sample:** 30 messages randomly selected from the dataset
- **Labellers:** All four team members — Jaskaran, Kapil, Alisha, Bijay
- **Process:** Each labeller independently assigned Low, Medium or High to all 30 messages using Labelling Protocol v1.0
- **Primary metric:** Cohen's kappa
- **Secondary metric:** Percentage agreement
- **Target:** kappa ≥ 0.61 (substantial agreement)

## 3. Results

### 3.1 Percentage agreement

| Labeller pair | Percentage agreement |
|---|---|
| Jaskaran ↔ Kapil | 93.3% |
| Jaskaran ↔ Alisha | 86.7% |
| Jaskaran ↔ Bijay | 90.0% |
| Kapil ↔ Alisha | 86.7% |
| Kapil ↔ Bijay | 96.7% |
| Alisha ↔ Bijay | 83.3% |
| **Average** | **89.5%** |

### 3.2 Cohen's kappa

| Labeller pair | Cohen's kappa | Interpretation |
|---|---|---|
| Jaskaran ↔ Kapil | 0.896 | Almost perfect |
| Jaskaran ↔ Alisha | 0.792 | Substantial |
| Jaskaran ↔ Bijay | 0.843 | Almost perfect |
| Kapil ↔ Alisha | 0.787 | Substantial |
| Kapil ↔ Bijay | 0.946 | Almost perfect |
| Alisha ↔ Bijay | 0.730 | Substantial |
| **Average** | **0.832** | **Almost perfect** |

Interpretation thresholds follow Landis & Koch (1977).

### 3.3 Interpretation

Average kappa of **0.832** falls in the "Almost perfect agreement" range (0.81–1.00). This substantially exceeds the target of 0.61 and confirms that the labelling protocol is working reliably across all four labellers.

Percentage agreement of **89.5%** supports this — the labellers agreed on nearly nine in ten messages.

## 4. Disagreements Observed

Disagreements occurred on 8 out of 30 messages (27%). These were resolved through the adjudication process defined in the protocol:

1. Two labellers disagree → message goes to a third labeller
2. If third agrees with one of them → that label is final
3. If all three disagree → Data & Labelling Lead makes the final ruling

Examples of disagreements:

| Message | Labels assigned | Resolution |
|---|---|---|
| "Your parcel is waiting. Click here." | Low, Medium, Medium, Low | Medium — shortened link raises band |
| "Your ATO refund is ready. Log in to myGov." | Low, Medium, Low, Medium | Medium — matches scam template (hard negative) |
| "Your account has been flagged. Verify now." | High, High, Medium, High | High — request + urgency |
| "Confirm your identity." | Medium, Medium, Low, Medium | Medium — request but no urgency |

## 5. Patterns in Disagreements

Three patterns were observed:

- **Short messages** were harder to label consistently — less context to apply the decision tree.
- **Government-service messages** were sometimes labelled Low by mistake when they should be Medium as hard negatives.
- **Urgency without a request** was sometimes labelled Medium instead of High.

## 6. Actions Taken

Based on the disagreements, the labelling protocol was clarified with two additional rules:

1. **Shortened links raise the risk band by one** (Low → Medium, Medium → High).
2. **Urgency with a vague threat is High**, even if there is no clear request.

These changes are documented in Labelling Protocol v1.0 section 3 (Edge Cases).

## 7. Conclusion

- Average Cohen's kappa: **0.832** (Almost perfect)
- Average percentage agreement: **89.5%**
- Both metrics exceed the target of kappa ≥ 0.61
- The labelling protocol is working reliably
- Disagreements have been documented and have led to protocol clarifications

The dataset is suitable for training and evaluation, and the labels are demonstrably consistent and reproducible.

## 8. Evidence

- `double-labelled.csv` — the 30 messages and 4 labellers' labels
- `inter_rater_agreement.py` — the script that calculates kappa
- Labelling Protocol v1.0 — the rules the labellers followed

## 9. Next Steps

- Apply the clarified protocol to remaining labelling work
- Re-run the agreement check if further messages are labelled
- Include this report as evidence in the AT2 Progress Presentation and AT3 Final Report