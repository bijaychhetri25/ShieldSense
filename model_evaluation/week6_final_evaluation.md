# ShieldSense – Week 6 Final Model Evaluation Report

**Student:** Kapil Thapa Magar  
**Role:** Model & Evaluation Lead  
**Project:** ShieldSense – Accessible Scam-Message Screening  
**Supervisor:** Dr Mahmoud Bekhit  
**Date:** 13 October 2026

## 1. Introduction

This report presents the final held-out evaluation of the ShieldSense machine-learning classifier.

The purpose was to measure how well the model identifies LOW, MEDIUM and HIGH scam-risk messages using a separate test dataset.

## 2. Dataset

The dataset was prepared by Jaskaran Singh, the Data & Labelling Lead.

- Training dataset: 162 messages
- Locked test dataset: 40 messages
- Risk categories: LOW, MEDIUM and HIGH

The test dataset was locked and kept separate from model development.

The dataset leakage report recorded no overlapping messages between the training and testing datasets after basic text normalisation.

## 3. Machine Learning Model

The classifier uses:

- TF-IDF text vectorisation with unigrams and bigrams
- Logistic Regression
- Balanced class weights
- Random state of 42
- Maximum of 1,000 iterations

The model was trained using only `training-set.csv` and evaluated using `test-set.csv`.

The locked test data was not used for model training or hyperparameter tuning.

## 4. Final Evaluation Results

| Evaluation Metric | Result |
|---|---|
| Accuracy | 85.00% |
| Macro F1-score | 85.07% |
| Correct predictions | 34 out of 40 |
| Incorrect predictions | 6 out of 40 |
| Training/test message overlap | 0 |

### Performance by Risk Category

| Risk Level | Precision | Recall | F1-score | Test Messages |
|---|---|---|---|---|
| LOW | 1.00 | 0.79 | 0.88 | 14 |
| MEDIUM | 0.79 | 0.85 | 0.81 | 13 |
| HIGH | 0.80 | 0.92 | 0.86 | 13 |

The model correctly classified 34 out of 40 test messages.

HIGH-risk recall was approximately 92%, meaning the model correctly identified 12 of the 13 HIGH-risk messages.

MEDIUM-risk recall was approximately 85%, which was better than in the earlier preliminary development evaluation.

## 5. Confusion Matrix

The confusion matrix shows the actual and predicted risk levels.

| Actual / Predicted | LOW | MEDIUM | HIGH |
|---|---:|---:|---:|
| LOW | 11 | 2 | 1 |
| MEDIUM | 0 | 11 | 2 |
| HIGH | 0 | 1 | 12 |

The model correctly predicted 11 LOW-risk, 11 MEDIUM-risk and 12 HIGH-risk messages.

One HIGH-risk message was classified as MEDIUM, while two MEDIUM-risk messages were classified as HIGH.

## 6. Model Limitations

Although the results are promising, the model has several limitations:

- The dataset is relatively small.
- The messages are synthetic rather than a representative sample of real-world scams.
- Six test messages were incorrectly classified.
- Some LOW-risk messages were classified as MEDIUM or HIGH.
- Performance may change when tested on different or real-world messages.

The model should be considered a prototype, not a fully reliable scam detection system.

The final test results must not be used to tune the model.

## 7. Conclusion

The final held-out evaluation was completed successfully.

The TF-IDF and Logistic Regression classifier achieved 85.00% accuracy and 85.07% macro F1-score on 40 locked test messages.

These results demonstrate promising performance on the prepared dataset, including improved MEDIUM-risk classification compared with the earlier development evaluation.

Further testing with larger, independently verified real-world datasets would be needed before practical deployment.

## 8. Evidence

The following files support this evaluation:

- `model_evaluation/final_model_evaluation.py`
- `data_labelling/training-set.csv`
- `data_labelling/test-set.csv`
- `data_labelling/test-set-lock.md`
- `data_labelling/leakage-check-report.md`
- `Week6_Final_Model_Evaluation.png` (screenshot saved locally)

All numerical results were calculated using Python and scikit-learn.