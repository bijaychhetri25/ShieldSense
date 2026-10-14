# ShieldSense Technical Handover Report

**Student:** Bijay Bahadur Chhetri  
**Role:** Integration, Documentation & QA Lead  
**Project:** ShieldSense — Scam-Message Screening Application  
**Release Tag:** v0.7.0

## 1. Project Overview

ShieldSense is a proof-of-concept application designed to screen SMS and chat messages for potential scam risks. It classifies messages as LOW, MEDIUM or HIGH risk and provides information intended to help users understand potentially suspicious messages.

The application provides two classification modes: a rules-based baseline and a machine-learning classifier. The Streamlit interface uses Green, Amber and Red risk cues.

ShieldSense is a screening aid, not a guarantee that a message is safe or fraudulent.

## 2. Integration and Application

The Streamlit interface is located in `interface_accessibility/app.py`. It connects to the rules-based classifier and machine-learning predictor.

The application was tested locally using selected normal and suspicious messages. Four selected integrated application scenarios produced their expected classifications.

The rules-based classifier was locally updated to recognise additional account-warning phrases, including "account is suspended", "account is blocked" and "account is locked". The change improved classification for the tested wording variations. Coordination with the Model & Evaluation Lead is still required before the change is committed and pushed to the shared repository.

These changes improve handling of the tested wording variations but do not establish overall scam-detection accuracy.

## 3. Quality Assurance Results

The documented rules-based baseline QA script completed seven test cases, with seven passing and zero failing.

The tests covered password requests, blocked bank accounts with transfer language, urgency-only messages, normal shopping messages, subscription payment failures, empty input passed directly to the classifier, and a long normal message.

Four selected integrated application scenarios were also tested across the rules-based and machine-learning modes. All four produced their expected classifications.

These results apply only to the tested scenarios. They do not establish the overall accuracy or reliability of the application.

## 4. Accessibility Verification

The following manual checks were performed:

- **Keyboard navigation:** The Check Message button was reachable and usable with the keyboard after enabling Safari's setting to highlight each item on a webpage with Tab.
- **Risk labels:** Risk levels were displayed using text labels as well as colour cues.
- **Visual readability:** Text was visually inspected and appeared easy to read.
- **VoiceOver:** VoiceOver announced control names during the controls tested in Safari.

These were basic manual checks. Formal colour-contrast ratios have not been measured, and full WCAG 2.2 AA compliance has not been confirmed.

## 5. Outstanding Testing

The following areas remain open for further verification:

- Additional machine-learning test scenarios.
- Empty-input validation through the Streamlit interface.
- More medium-risk, long-message, punctuation and unusual-format scenarios.
- False-positive and false-negative classifications using held-out evaluation data.
- Formal colour-contrast measurements.
- Broader keyboard and screen-reader testing.
- Further verification of explanations and risk information for users with different accessibility needs.

## 6. Repository and Setup

The project repository is:

https://github.com/bijaychhetri25/ShieldSense

Install the project dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the application from the project root:

```bash
python3 -m streamlit run interface_accessibility/app.py
```

Run the rules-based QA checks:

```bash
python3 integration_qa/qa_checks.py
```

Open the local application URL displayed in the terminal.

## 7. Documentation and Handover

The repository includes:

- `README.md` — Main project overview and setup instructions.
- `integration_qa/README.md` — Integration and QA instructions.
- `integration_qa/qa_test_cases.md` — Documented QA test cases.
- `integration_qa/qa_results.md` — Recorded QA results and accessibility checks.
- `integration_qa/defect_log.md` — Recorded issues and their status.
- `integration_qa/handover_backlog.md` — Outstanding improvements and future recommendations.
- `docs/TECHNICAL_HANDOVER_REPORT.md` — Technical implementation, QA status and handover information.

Future contributors should review the test results, defect log and handover backlog before making changes. Any fixes should be retested and documented.

## 8. Release Status

The Git tag `v0.7.0` was created and pushed to the remote repository to mark the Week 7 feature-freeze milestone.

This tag records the committed repository state at that milestone. It does not indicate that all outstanding testing or final handover activities have been completed.

## 9. Final Status

The documented rules-based QA suite has seven passing tests and zero failures. Four selected integrated application scenarios also produced their expected classifications.

The project documentation has been updated, and the latest README and QA documentation changes have been pushed to GitHub. Further machine-learning testing, formal colour-contrast verification and final review of project deliverables remain outstanding before the project can be considered fully handed over.