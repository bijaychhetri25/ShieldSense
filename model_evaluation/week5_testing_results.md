# ShieldSense – Week 5 Model Testing and Evaluation Report

**Student:** Kapil Thapa Magar  
**Role:** Model & Evaluation Lead  
**Project:** ShieldSense – Accessible Scam-Message Screening  
**Supervisor:** Dr Mahmoud Bekhit

## 1. Testing Objective

The purpose of testing was to verify the functionality of the rules-based baseline, evaluate the preliminary machine-learning classifier, and confirm successful integration with the Streamlit user interface.

## 2. Rules-Based Baseline Testing

Four automated test cases were executed using `baseline_tests.py`.

| Test Case | Expected | Actual | Result |
|---|---|---|---|
| Normal shopping message | LOW | LOW | PASS |
| Password request | HIGH | HIGH | PASS |
| Blocked bank account warning | HIGH | HIGH | PASS |
| Urgent limited-time message | HIGH | HIGH | PASS |

**Results:** 4 tests passed, 0 failed.

The baseline correctly classified all four predefined test messages.

## 3. Preliminary Machine Learning Evaluation

The preliminary classifier uses:

- TF-IDF text vectorisation with unigrams and bigrams
- Logistic Regression with balanced class weights
- Stratified training and testing splits
- LOW, MEDIUM and HIGH risk categories

The original dataset contained 200 labelled messages. Duplicate-message analysis identified 168 unique messages.

A duplicate-safe development evaluation was performed using 134 training messages and 34 testing messages.

**Results:**

- Accuracy: 76.47%
- Macro F1-score: 67.86%
- LOW recall: 100%
- MEDIUM recall: approximately 29%
- HIGH recall: approximately 77%

These results are preliminary development metrics, not final independent test results.

## 4. Application Integration Testing

The classifier was integrated into the Streamlit interface, allowing users to select either the rules-based baseline or the machine-learning model.

| Test Message | Expected Risk | Actual Risk | Result |
|---|---|---|---|
| Urgent bank account warning | HIGH | HIGH | PASS |
| Meeting arrangement | LOW | LOW | PASS |
| Subscription payment failure | MEDIUM | LOW | FAIL |
| Account verification request | MEDIUM | HIGH | FAIL |

**Results:** 2 of 4 illustrative manual test cases passed.

The interface successfully displayed model predictions. However, MEDIUM-risk messages were not consistently classified correctly.

## 5. Technical Verification

The following checks were completed:

- All four baseline automated tests passed.
- Python syntax compilation completed without errors.
- The Streamlit application launched successfully.
- Both detection model options were available.
- The machine-learning model returned predictions through the interface.
- The Git working tree was confirmed clean before this documentation update.

## 6. Identified Limitations

The preliminary machine-learning model has difficulty identifying MEDIUM-risk messages. The dataset is relatively small and contains synthetic examples, limiting the conclusions that can be drawn about performance on real-world scam messages.

Model confidence percentages should not be interpreted as guarantees of correctness.

The application remains a prototype and should not be relied upon as a definitive scam detection system.

## 7. Remaining Work

- Obtain the verified and locked test dataset from the Data & Labelling Lead.
- Complete independent final evaluation without using the locked test set for model tuning.
- Record final accuracy, precision, recall, macro F1-score and confusion matrix.
- Coordinate integration and quality assurance with the team.
- Prepare the final demonstration and presentation.

## 8. Conclusion

ShieldSense has a functioning rules-based baseline and an integrated preliminary machine-learning classifier. Initial testing confirms that the application can process messages and display risk predictions.

Further evaluation is required, particularly for MEDIUM-risk classification, before making stronger claims about the model's effectiveness.