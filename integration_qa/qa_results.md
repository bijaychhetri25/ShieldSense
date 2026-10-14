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