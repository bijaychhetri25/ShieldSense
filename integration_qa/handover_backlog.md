# ShieldSense Handover Backlog

**Project:** ShieldSense  
**Student:** Bijay Bahadur Chhetri  
**Role:** Integration, Documentation & QA Lead  
**Purpose:** Record outstanding improvements and recommendations for future development.

## 1. Current Project Status

ShieldSense is a proof-of-concept application that analyses SMS and chat messages for possible scam indicators. It provides Low, Medium and High risk classifications using a rules-based baseline and a machine-learning classifier through a Streamlit interface.

The documented rules-based QA script completed seven tests with seven passes and zero failures. Four selected integrated application tests also produced their expected classifications.

These results apply only to the tested scenarios and do not establish the overall accuracy of the application.

## 2. Future Work and Improvements

| ID | Priority | Task | Reason | Suggested Action |
|---|---|---|---|---|
| HW01 | High | Expand machine-learning QA | Only a small number of messages have been tested through the interface. | Test additional Low, Medium and High risk examples and record actual results. |
| HW02 | High | Improve empty-input handling | The rules-based classifier currently returns LOW for an empty message. | Verify the interface behaviour and consider displaying a validation message instead. |
| HW03 | High | Evaluate false positives and false negatives | Incorrect classifications could mislead users. | Review misclassified examples using the held-out evaluation data. |
| HW04 | Medium | Expand unusual-message testing | Unusual formats may affect classification. | Test long messages, punctuation, spelling variations, URLs and mixed-case text. |
| HW05 | Medium | Complete accessibility verification | Accessible design is important for a scam-awareness application. | Check keyboard navigation, contrast, readable wording and risk cues that do not rely on colour alone. |
| HW06 | Medium | Improve model explanations | Machine-learning predictions may not provide detailed reasons for a classification. | Investigate ways to present understandable explanations while avoiding unsupported claims. |
| HW07 | Medium | Maintain project documentation | Future contributors need clear setup and operating instructions. | Keep the README, requirements and testing instructions aligned with the current application. |
| HW08 | Low | Expand the dataset | A broader dataset may help test more message patterns. | Review dataset coverage and add appropriately labelled examples with documented provenance. |

## 3. Known Limitations

- ShieldSense is a proof-of-concept, not a guarantee that a message is safe or fraudulent.
- The current QA results cover selected test cases only.
- Machine-learning confidence is an estimate and should not be interpreted as a guarantee of correctness.
- New scam techniques and unusual message patterns may not be recognised.
- Accessibility and broader edge-case testing require further verification.

## 4. Handover Recommendations

1. Run the application using the installation and run instructions in the main README.
2. Review the dataset documentation and model evaluation results before making claims about accuracy.
3. Run the QA tests and review the latest recorded outcomes.
4. Review unresolved items in this backlog before adding new features.
5. Record any fixes, retest the affected scenarios and update the defect log.
6. Keep future changes in version control and document important releases.

## 5. Handover Status

This backlog records recommended future work. Items should be marked complete only after the work has been performed and verified. The project team should review priorities and assign owners before implementation.

**Prepared by:** Bijay Bahadur Chhetri  
**Role:** Integration, Documentation & QA Lead