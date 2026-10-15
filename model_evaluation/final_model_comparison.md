# ShieldSense – Final Model Comparison and Error Analysis

**Student:** Kapil Thapa Magar  
**Role:** Model & Evaluation Lead  
**Supervisor:** Dr Mahmoud Bekhit  
**Date:** 15 October 2026

## 1. Purpose

This report compares the performance of the ShieldSense rules-based baseline and the TF-IDF + Logistic Regression classifier.

Both models were evaluated on the same 40-message locked test dataset prepared by Jaskaran Singh.

The purpose was to identify which model performs better at classifying LOW, MEDIUM and HIGH scam-risk messages.

## 2. Evaluation Method

The evaluation used:

- `training-set.csv` – 162 training messages
- `test-set.csv` – 40 locked test messages
- `rules_baseline.py` – existing keyword-based detection model
- `compare_models.py` – model comparison script

The machine-learning classifier was trained using only the training dataset.

The rules-based baseline and machine-learning classifier were evaluated using the same locked test messages.

The leakage check confirmed zero exact message overlap after basic text normalisation.

No model tuning was performed using the locked test set.

## 3. Final Model Comparison

| Metric | Rules-Based Baseline | TF-IDF + Logistic Regression |
|---|---:|---:|
| Accuracy | 40.00% | 85.00% |
| Macro Precision | 57.58% | 86.19% |
| Macro Recall | 38.64% | 85.16% |
| Macro F1-score | 30.22% | 85.07% |
| HIGH-risk Recall | 7.69% | 92.31% |
| Correct HIGH-risk Predictions | 1/13 | 12/13 |
| Total Incorrect Predictions | 24 | 6 |

The machine-learning classifier achieved higher accuracy, macro F1-score and HIGH-risk recall than the rules-based baseline.

## 4. Main Finding

The most important difference was HIGH-risk detection.

The rules-based baseline correctly identified only 1 of 13 HIGH-risk messages, missing the other 12.

The machine-learning classifier correctly identified 12 of 13 HIGH-risk messages.

The rules-based baseline relies on predefined keywords and patterns. Some suspicious messages do not contain the specific keywords required to trigger a HIGH-risk classification.

For example:

**Message:** "Your account is flagged. Verify now."

- Actual label: HIGH
- Rules-based prediction: LOW

The machine-learning model learns statistical patterns from labelled training messages rather than relying only on fixed keyword rules.

These results support the use of machine learning for this prototype, while also showing the safety limitations of the baseline.

## 5. Machine Learning Error Analysis

The machine-learning model incorrectly classified six messages in the locked test set.

| Message | Actual | Predicted | Possible Explanation |
|---|---|---|---|
| Your account has been verified. | LOW | HIGH | Account-related wording may resemble suspicious training examples |
| Please confirm your booking for Saturday. | LOW | MEDIUM | The word "confirm" may be associated with verification requests |
| Your account is being verified. | MEDIUM | HIGH | Verification wording may resemble high-risk account warnings |
| Your account is pending verification. | MEDIUM | HIGH | Account verification language may resemble suspicious requests |
| Your Centrelink payment is ready. Log in to myGov. | LOW | MEDIUM | Government and payment terminology may resemble scam messages |
| Congratulations, you've won a holiday! Claim now. | HIGH | MEDIUM | Prize-related wording was not classified at the expected HIGH level |

These are possible explanations based on the wording of the messages. They are not verified feature-attribution results.

The errors show that the model sometimes struggles to distinguish legitimate notifications from suspicious messages with similar language.

One HIGH-risk message was incorrectly classified as MEDIUM. This is particularly important because a screening application should minimise missed HIGH-risk messages.

## 6. Preliminary and Final Results

The earlier `compare_models.py` used a new random training and testing split from the complete dataset.

This approach was intended for preliminary development comparison. It was not a valid independent held-out evaluation because the full dataset included messages later assigned to the locked test set.

Therefore, the earlier preliminary comparison must not be presented as the final result.

The corrected comparison uses Jaskaran's separate training and locked test datasets.

**The final comparison results in Section 3 replace the earlier preliminary comparison for reporting purposes.**

The preliminary comparison remains part of the project's development history but is not directly comparable because the dataset and evaluation procedure differed.

## 7. Limitations

- The locked test dataset contains only 40 messages.
- The messages are synthetic and may not represent real-world scam patterns.
- The rules-based baseline missed 12 of 13 HIGH-risk messages.
- The machine-learning model incorrectly classified six messages.
- The model's performance on real-world messages is unknown.
- Confidence percentages are not guarantees of correctness.

ShieldSense remains a proof-of-concept application and should not be treated as a reliable real-world scam detection service.

## 8. Conclusion

The final evaluation shows that the TF-IDF + Logistic Regression classifier performed substantially better than the rules-based baseline on the locked synthetic test dataset.

The classifier achieved 85.00% accuracy and 85.07% macro F1-score, compared with 40.00% accuracy and 30.22% macro F1-score for the baseline.

The most important finding was HIGH-risk recall, where machine learning achieved 92.31%, compared with 7.69% for the baseline.

This provides measurable evidence supporting the machine-learning approach in ShieldSense, while highlighting the need for further real-world evaluation before deployment.

## 9. Evidence

- `model_evaluation/compare_models.py`
- `model_evaluation/final_model_evaluation.py`
- `model_evaluation/rules_baseline.py`
- `data_labelling/training-set.csv`
- `data_labelling/test-set.csv`
- `data_labelling/test-set-lock.md`
- `data_labelling/leakage-check-report.md`

**Note:** The supervisor previously reported a baseline macro F1-score of 30.27%. The current repository code produced 30.22%. This small discrepancy requires reconciliation if the comparison is reproduced using a different baseline revision.