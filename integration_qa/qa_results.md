# ShieldSense QA Results

**Student:** Bijay Bahadur Chhetri  
**Role:** Integration, Documentation & QA Lead

## Week 5 QA Testing

The current rules-based baseline was tested against the supervisor feedback
test cases.

| Test ID | Test Case | Expected | Actual | Result |
|---|---|---|---|---|
| TC07 | Password request | HIGH | HIGH | PASS |
| TC08 | Bank account blocked + transfer | HIGH | HIGH | PASS |
| TC09 | Urgency-only message | HIGH | HIGH | PASS |
| TC10 | Shopping message / word-boundary check | LOW | LOW | PASS |

## QA Summary

- Tests executed: 4
- Passed: 4
- Failed: 0
- Pass rate: 100%

All four supervisor feedback test cases passed against the current
rules-based baseline.

### Test Outcome Summary

- **TC07 – Password request:** HIGH → HIGH — PASS
- **TC08 – Blocked bank account + transfer:** HIGH → HIGH — PASS
- **TC09 – Urgency-only message:** HIGH → HIGH — PASS
- **TC10 – Shopping message / word-boundary check:** LOW → LOW — PASS

The QA testing confirms that the current baseline produces the expected
risk levels for these four test cases.

## Integration QA Notes

The Streamlit interface was also tested locally with the current
rules-based baseline.

The interface successfully:

- accepts an SMS or chat message as input;
- runs the message through the classification logic;
- displays the risk level;
- displays the risk score;
- displays the reasons for the classification;
- presents Low, Medium and High risk states using Green, Amber and Red
  visual cues;
- provides a technical result section for QA/debugging information.

## Current QA Status

**Status: PASS**

The supervisor feedback test cases and the current local interface
workflow have been checked. The machine-learning model has since been integrated with the interface and tested using selected normal and suspicious messages. Further QA is still required to cover additional risk levels, empty-input validation, accessibility and false-positive or false-negative cases.
## Week 6 Extended Rules-Based QA

The rules-based classifier was tested with seven test cases covering password requests, blocked bank accounts, urgency-only messages, normal shopping messages, a payment-related message, empty input, and a long normal message.

| Test ID | Test Description | Expected | Actual | Result |
|---|---|---|---|---|
| TC07 | Password request | HIGH | HIGH | PASS |
| TC08 | Blocked bank account + transfer | HIGH | HIGH | PASS |
| TC09 | Urgency-only message | HIGH | HIGH | PASS |
| TC10 | Shopping message / word-boundary check | LOW | LOW | PASS |
| TC11 | Medium-risk payment message | MEDIUM | MEDIUM | PASS |
| TC12 | Empty message | LOW | LOW | PASS |
| TC13 | Long normal message | LOW | LOW | PASS |

### Extended QA Summary

- Tests executed: 7
- Passed: 7
- Failed: 0
- Pass rate: 100%

These results apply only to the seven selected rules-based test cases. Empty input was classified as LOW by the classifier; further verification is needed to determine whether the interface should instead display an input-validation message.

## Week 7 Integrated Application QA

The integrated ShieldSense Streamlit application was manually tested using both the Rules-Based Baseline and Machine Learning modes. Two messages were tested with each model: a normal meeting message and a suspicious bank message.

| Test ID | Model | Test message | Expected | Actual | Result |
|---|---|---|---|---|---|
| INT01 | Rules-Based Baseline | Normal meeting message | LOW | LOW | PASS |
| INT02 | Machine Learning | Normal meeting message | LOW | LOW | PASS |
| INT03 | Rules-Based Baseline | Suspicious bank message | HIGH | HIGH (score: 9) | PASS |
| INT04 | Machine Learning | Suspicious bank message | HIGH | HIGH (confidence: 59.19%) | PASS |

### Integrated QA Summary

- Integrated application tests executed: 4
- Passed: 4
- Failed: 0
- Pass rate: 100%

### Limitations

These tests confirm the expected outputs for the four selected messages only. They do not establish the overall accuracy of the machine-learning model. The confidence value is a model estimate, not a guarantee that a message is fraudulent or safe.

Further testing should cover medium-risk messages, empty input, unusual message formats, accessibility, and additional false-positive and false-negative cases.
### Empty-Input Validation Test

- **Test:** Submit an empty message through the Streamlit interface.
- **Expected result:** The application displays a warning and does not classify the empty input.
- **Actual result:** The application displays “Please enter a message before checking.”
- **Status:** PASS
- **Evidence:** Manual test of the running Streamlit application.
### Unusual Message Format Test

- **Test message:** “URGENT!!! Your account is blocked!!! Verify now!!!”
- **Rules-Based Baseline:** LOW RISK, risk score 1.
- **Machine Learning:** HIGH RISK, model confidence 77.44%.
- **Observation:** The two classification modes returned different risk levels for the same message.
- **Status:** Further investigation required.
- **Action:** Review the rules-based keyword detection and compare the results against the intended classification policy. Do not mark this as a confirmed defect until the expected result is established.
### Additional Rules-Based Classifier Retest

- **Test message:** “URGENT!!! Your account is blocked!!! Verify now!!!”
- **Previous result:** LOW RISK, score 1.
- **Updated result:** HIGH RISK, score 3.
- **Reason:** The threat keyword list was updated to recognise the phrase “account is blocked”.
- **Retest result:** The message now returns HIGH RISK with urgency and threat/account-warning indicators.
- **Formal QA suite:** TC07–TC13 — 7 passed, 0 failed.
- **Status:** Retest successful for the documented scenarios.
- **Note:** The classifier change still requires coordination with the Model & Evaluation Lead before it is committed to the shared repository.
### Keyboard Accessibility Check

- **Test:** Navigate through the ShieldSense interface using the keyboard.
- **Expected result:** Users can reach and activate the message input, classification mode selector and Check Message button using the keyboard.
- **Initial observation:** The Check Message button was not highlighted during keyboard navigation in Safari.
- **Corrective action:** Enabled Safari's setting to highlight each item on a webpage when using Tab.
- **Retest result:** The Check Message button became highlighted and was successfully activated using Enter.
- **Status:** PASS after browser setting adjustment.
- **Note:** This test confirms keyboard operation in the tested Safari configuration. Further accessibility checks are still required.

### Risk Label and Colour Accessibility Check

- **Purpose:** Check whether users can identify the risk level without relying on colour alone.
- **HIGH-risk test:** The interface displayed “HIGH RISK” with a red indicator.
- **MEDIUM-risk test:** The interface displayed “MEDIUM RISK” with an amber indicator.
- **LOW-risk test:** The interface displayed “LOW RISK” with a green indicator.
- **Result:** All three tested risk levels included a text label as well as a colour indicator.
- **Status:** PASS for text-based risk labels in the tested scenarios.
- **Limitation:** This check does not confirm colour contrast compliance, screen-reader compatibility or full WCAG 2.2 AA compliance.

### Visual Contrast Check

- **Test:** Visually inspect the risk labels and explanatory text in the ShieldSense interface.
- **Observation:** All text appeared easy to read during the visual inspection.
- **Result:** No obvious readability issue was observed in this check.
- **Status:** Visual inspection completed.
- **Limitation:** Formal colour-contrast ratios have not been measured, so WCAG contrast compliance has not been confirmed.

### Screen-Reader Accessibility Check

- **Test:** Navigate through the ShieldSense interface using macOS VoiceOver in Safari.
- **Expected result:** VoiceOver should announce interface controls clearly.
- **Actual result:** VoiceOver was activated successfully and announced the control names during keyboard navigation.
- **Status:** PASS for the controls tested.

### Risk Label and Colour Accessibility Check

- **Test:** Check whether risk levels are displayed using both text labels and colours.
- **Expected result:** LOW, MEDIUM and HIGH risk levels should be identifiable by text as well as colour.
- **Actual result:** The application displays risk labels such as HIGH RISK in red, with the risk level also shown as HIGH.
- **Status:** PASS for text-label visibility.
- **Limitation:** Formal colour-contrast ratios have not been measured, so WCAG 2.2 AA contrast compliance has not been confirmed.