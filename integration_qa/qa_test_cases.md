
# ShieldSense QA Test Cases

## Purpose

These test cases are designed to check that ShieldSense correctly processes messages, produces the expected risk classification, and displays the result correctly in the user interface.

## Test Cases

| Test ID | Test Description | Expected Result | Status |
|---|---|---|---|
| TC01 | Enter a low-risk message | System displays Low risk and Green cue | Pending |
| TC02 | Enter a medium-risk message | System displays Medium risk and Amber cue | Pending |
| TC03 | Enter a high-risk message | System displays High risk and Red cue | Pending |
| TC04 | Submit an empty message | System displays an appropriate validation message | Pending |
| TC05 | Submit a normal non-scam message | System provides a risk classification | Pending |
| TC06 | Submit a message containing scam indicators | System identifies the appropriate risk level | Pending |
| TC07 | Compare model output with interface output | Interface result matches model result | Pending |
| TC08 | Check risk explanation | Plain-language explanation is displayed correctly | Pending |
| TC09 | Enter a long message | System processes the message without unexpected failure | Pending |
| TC10 | Test all three risk levels | Correct Green, Amber or Red cue is displayed | Pending |

## QA Objective

The purpose of these tests is to verify that the ShieldSense components work together correctly and that the risk classification produced by the detection component is accurately displayed by the interface.

Testing will be performed when the model and interface components are available for integration.

## Supervisor Feedback Test Cases

These test cases were added based on the supervisor's Week 4 feedback and will be used to verify the rules-based baseline after integration.

| Test ID | Test Description | Input Message | Expected Result |
|---|---|---|---|
| TC07 | Password request | "Send me your password now" | HIGH |
| TC08 | Blocked bank account and transfer request | "Your bank account has been blocked, transfer now" | HIGH |
| TC09 | Urgency-only message | "URGENT! Act now, limited time!" | HIGH |
| TC10 | Word-boundary check | "Going shopping later?" | LOW |

### QA Purpose

- TC07 checks that a direct password request is treated as a high-risk message.
- TC08 checks that a blocked-account and transfer combination is detected as high risk.
- TC09 checks that the urgency-only message returns HIGH, consistent with the confirmed rules-based baseline QA result.
- TC10 checks that the word "pin" is not incorrectly detected inside another word such as "shopping".
