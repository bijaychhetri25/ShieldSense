# ShieldSense QA Results

**Student:** Bijay Bahadur Chhetri  
**Role:** Integration, Documentation & QA Lead

## Week 5 QA Testing

The current rules-based baseline was tested against the supervisor feedback test cases.

| Test ID | Test Case | Expected | Actual | Result |
|---|---|---|---|---|
| TC07 | Password request | HIGH | HIGH | PASS |
| TC08 | Bank account blocked + transfer | HIGH | HIGH | PASS |
| TC09 | Urgency-only message | LOW | HIGH | FAIL |
| TC10 | Shopping message / word-boundary check | LOW | LOW | PASS |

## QA Summary

- Tests executed: 4
- Passed: 3
- Failed: 1
- Pass rate: 75%

## Issue Identified

### TC09 – Urgency-only message

**Test message:**

> "URGENT! Act now, limited time!"

**Expected result:** LOW

**Actual result:** HIGH

The current rules-based classifier detects three urgency indicators:

- urgent
- act now
- limited time

This produces a score of 3. The current classifier assigns HIGH risk to scores of 3 or above.

## QA Finding

The urgency-only case does not match the expected supervisor requirement.

The issue has been recorded for review by the Model & Evaluation Lead.

No changes were made to the Model & Evaluation Lead's source code as part of this QA test.

## Successful Checks

**TC07 – Password request**

The password request was correctly classified as HIGH.

**TC08 – Blocked bank account + transfer**

The blocked bank account and transfer message was correctly classified as HIGH.

**TC10 – Word-boundary check**

The message "Going shopping later?" was correctly classified as LOW. The test confirms that "pin" is not incorrectly detected inside the word "shopping".

## Next Action

The failed TC09 result should be reviewed by the Model & Evaluation Lead.

After any model change, the QA tests should be executed again to confirm whether the issue has been resolved.