# ShieldSense Technical Handover Report

## 1. Project Overview

ShieldSense is a proof-of-concept web application developed as part of the ITEC320 Work Integrated Learning (WIL) project. The application helps users identify potentially suspicious SMS and chat messages.

Users can enter a message into the Streamlit interface. The application evaluates the message and displays a risk classification:

- **LOW (Green):** The message has a low risk according to the current classifier.
- **MEDIUM (Amber):** The message contains indicators that require caution.
- **HIGH (Red):** The message contains indicators associated with a potentially suspicious message.

The application also provides an explanation of the classification to help users understand the result.

ShieldSense is an educational proof of concept and should not be treated as a guarantee that a message is safe or fraudulent.

## 2. Integration and Application

The Streamlit interface is located in `interface_accessibility/app.py`. It connects to the rules-based classifier and machine-learning predictor.

The application was tested locally using selected normal and suspicious messages. Four selected integrated application scenarios produced their expected classifications.

The rules-based classifier was updated to recognise additional account-warning phrases, including "account is suspended", "account is blocked" and "account is locked". The change was committed and pushed to GitHub in commit `1763dfa`.

The Model & Evaluation Lead should review the expected behaviour of these changes as part of ongoing evaluation. The changes improve handling of the tested wording variations but do not establish overall scam-detection accuracy.

## 3. Quality Assurance Results

The rules-based baseline QA script completed seven test cases, with seven passing and zero failing.

The tested cases included:

- **TC07:** Password-related request classified as HIGH.
- **TC08:** Blocked bank account and transfer request classified as HIGH.
- **TC09:** Urgency-only message classified as HIGH.
- **TC10:** Shopping message classified as LOW.
- **TC11:** Subscription payment failure classified as MEDIUM.
- **TC12:** Empty message passed directly to the classifier classified as LOW.
- **TC13:** Long normal message classified as LOW.

These results demonstrate that the tested scenarios produced the expected outputs. They do not represent a complete evaluation of the application's accuracy or performance.

The application was also tested manually with selected messages:

- "Your bank account has been blocked, transfer now" — HIGH.
- "Your subscription payment failed. Please review your account." — MEDIUM.
- "Going shopping later?" — LOW.

These manual checks support the expected behaviour for the selected examples only.

## 4. Accessibility Testing

Accessibility checks were carried out on the Streamlit interface.

### 4.1 Keyboard Navigation

Keyboard navigation was tested in Safari. The Check Message button could be highlighted and activated using the keyboard after enabling Safari's setting to highlight each item on a webpage with the Tab key.

This check passed under the tested browser configuration.

### 4.2 Risk Labels and Colour

The interface displays written LOW, MEDIUM and HIGH labels alongside green, amber and red visual cues.

The written labels help communicate the risk level without relying on colour alone. The tested labels were visually inspected.

### 4.3 Readability and Contrast

The text was visually inspected and appeared readable during the manual check. However, formal colour-contrast ratios have not been fully verified for all relevant text, backgrounds and interface components.

The current evidence is insufficient to confirm full WCAG 2.2 Level AA compliance.

### 4.4 Screen Reader Testing

VoiceOver was used to navigate the interface with Control + Option + Right Arrow. The controls tested were announced during navigation.

This was a limited manual check. Further testing is needed to verify all labels, results, explanations and error messages.

## 5. Tools and Technologies

The project uses the following tools and technologies:

- **Python:** Application and classifier implementation.
- **Streamlit:** Web interface.
- **Rules-based classifier:** Initial message risk assessment.
- **Machine-learning predictor:** Additional classification component requiring further evaluation.
- **Git and GitHub:** Version control and shared source code.
- **Jira:** Project planning, task allocation and sprint tracking.
- **VS Code:** Development and testing environment.

## 6. Repository Structure

The main project folders include:

- `interface_accessibility/` — Streamlit interface and accessibility-related work.
- `model_evaluation/` — Rules-based classifier and model evaluation work.
- `integration_qa/` — QA scripts, test cases, results and handover backlog.
- `docs/` — Technical documentation and handover report.
- `data/` — Project data resources.
- `data_labelling/` — Data labelling work.
- `src/` — Supporting source code.

The exact contents of these folders may change as development continues.

## 7. Setup and Running Instructions

### 7.1 Prerequisites

Python and the project's required packages must be installed before running the application.

### 7.2 Run the Application

Open the project folder in VS Code and run the following command in the terminal:

```bash
python3 -m streamlit run interface_accessibility/app.py
```

Streamlit should start the local application and provide a URL to open in a browser.

### 7.3 Run the Rules-Based QA Tests

From the project root, run:

```bash
python3 integration_qa/qa_checks.py
```

The documented test run completed seven test cases with seven passing and zero failing. Run the script again after future code changes to confirm the current result.

### 7.4 Run the Rules-Based Classifier Directly

To test the classifier independently, run:

```bash
python3 model_evaluation/rules_baseline.py
```

The available output depends on the examples included in the script.

## 8. Known Limitations

The current application has the following limitations:

1. **Limited test coverage:** Only selected scenarios have been tested.
2. **Machine-learning evaluation:** Broader evaluation of the machine-learning predictor is still required.
3. **False positives and false negatives:** Further testing is needed to identify messages that are incorrectly classified.
4. **Empty input:** The direct rules-based classifier returns LOW for an empty message. The interface should be checked to ensure that empty input is handled appropriately.
5. **Unusual messages:** Additional tests are needed for spelling mistakes, punctuation, long messages, URLs and mixed-case wording.
6. **Classification explanations:** The clarity and usefulness of explanations need further review.
7. **Accessibility:** Formal contrast measurements and broader keyboard and screen-reader testing remain incomplete.
8. **Detection accuracy:** The current test results do not establish overall scam-detection accuracy.

A LOW result does not guarantee that a message is legitimate. Users should remain cautious when a message requests personal information, payment or urgent action.

## 9. Outstanding Work and Recommendations

The following tasks are recommended for future development and handover:

| Priority | Task | Recommended action |
|---|---|---|
| High | Machine-learning QA | Expand testing across representative messages and document the results. |
| High | Empty-input handling | Verify interface validation and display a suitable message when no text is entered. |
| High | False-positive and false-negative testing | Evaluate performance using a held-out set of labelled messages. |
| Medium | Unusual-message testing | Test long messages, punctuation, spelling variations, URLs and mixed case. |
| Medium | Accessibility verification | Complete keyboard, contrast and screen-reader checks. |
| Medium | Model explanations | Review whether explanations are clear and consistent with the classification. |
| Medium | Documentation alignment | Keep the README, QA results and handover report consistent with the implementation. |
| Low | Dataset expansion | Add more representative messages and document their sources and labelling process. |

The team should update the relevant QA records and documentation when these tasks are completed.

## 10. Version Control and Handover

The project uses GitHub to share code and track changes.

The classifier update was committed and pushed in commit `1763dfa`. The handover report was subsequently updated to clarify the classifier status and document the testing results and remaining limitations.

The repository's `main` branch should be checked before further changes are made. Team members should review changes, run relevant tests and communicate updates through the agreed project workflow.

The following documents support the handover:

- `README.md` — Project overview, setup and running instructions.
- `integration_qa/README.md` — QA instructions.
- `integration_qa/qa_checks.py` — Rules-based baseline QA script.
- `integration_qa/qa_test_cases.md` — Test case documentation.
- `integration_qa/qa_results.md` — Recorded QA results.
- `integration_qa/handover_backlog.md` — Outstanding tasks and recommendations.
- `docs/TECHNICAL_HANDOVER_REPORT.md` — Technical handover summary.

## 11. Release and Final Status

The `v0.7.0` milestone represents a Week 7 feature-freeze milestone, not a final production release.

The current proof of concept has a working Streamlit interface, a rules-based classifier and documented results for selected QA scenarios. The baseline QA script passed all seven documented tests in the recorded run.

Further machine-learning evaluation, edge-case testing, empty-input validation and accessibility verification remain necessary.

**Overall status:** The application is suitable for continued development and demonstration as a proof of concept. It is not yet fully validated for production use, and full WCAG 2.2 Level AA compliance has not been confirmed.

---

**End of Technical Handover Report**