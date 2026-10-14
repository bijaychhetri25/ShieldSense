# ShieldSense Week 6 Defect Log

**Student:** Bijay Bahadur Chhetri  
**Role:** Integration, Documentation & QA Lead  
**Week:** Week 6

## Purpose

This defect log records issues and testing gaps identified during integration and quality assurance testing of the ShieldSense application. It tracks confirmed defects, outstanding testing requirements and actions needed before final handover.

## Defect List

| ID | Issue | Severity | Status | Action |
|---|---|---|---|---|
| D01 | No failures identified in the documented rules-based and integrated application QA tests. | None | Passed for tested cases | Continue broader testing before final handover. |
| D02 | Additional testing is required for unusual message formats, empty-input interface validation, accessibility and false-positive or false-negative cases. | Testing gap | Open | Complete further testing and record the actual results before final handover. |

## Defect Triage

- **High:** Issues affecting the correctness or core functionality of ShieldSense.
- **Medium:** Issues affecting usability, integration or quality.
- **Low:** Minor issues or improvements.
- **Testing gap:** A scenario that still needs verification. It is not automatically a confirmed software defect.

## Current QA Evidence

The rules-based baseline was tested using seven test cases, with seven passing and zero failing.

The integrated Streamlit application was also tested using four selected scenarios across the Rules-Based Baseline and Machine Learning modes. All four produced the expected risk classifications.

These results apply only to the selected test cases and do not establish the overall accuracy of the application or machine-learning model.

## Outstanding Testing

The following areas require further verification:

- Empty-input validation in the Streamlit interface.
- Unusual and long message formats.
- Additional medium-risk scenarios.
- Accessibility checks, including keyboard navigation, contrast and understandable risk messages.
- False-positive and false-negative classifications.
- Consistency between classifier results and the risk information displayed by the interface.

## Retesting

Any confirmed defect will be recorded with its severity, status and corrective action. After a fix is implemented, the affected test will be rerun and its actual result documented.

A defect will only be marked as resolved after successful retesting. Outstanding testing gaps will remain open until the relevant checks have been completed.

## Handover Status

The initial QA checks have passed for the documented scenarios. Broader testing and verification of the outstanding items above remain necessary before final handover.

The final handover record should include the completed QA results, unresolved limitations, release information and recommended future improvements.