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
workflow have been checked. Further QA will be performed when the
machine-learning model is integrated with the interface.