# Integration, Documentation & QA

This folder contains the integration, quality assurance and documentation work for ShieldSense.

## Responsibilities

- Maintain the project repository structure.
- Support integration between the dataset, model and user interface.
- Prepare integration and QA test cases.
- Check that model outputs are correctly displayed by the interface.
- Maintain project documentation.
- Support final project testing and project handover.

## Integration & QA Lead

**Bijay Bahadur Chhetri**

The Integration, Documentation & QA Lead is responsible for checking that the components developed by the team work together correctly and that the application meets the agreed requirements.

## Running QA Tests

From the project root, run:

```bash id="hm04la"
python3 integration_qa/qa_checks.py
```

The documented rules-based QA suite contains seven test cases. The latest recorded result was seven passed and zero failed.

These results apply only to the scenarios tested and do not establish the overall accuracy of the application.

## QA Documentation

- `qa_test_cases.md` – Documents the test cases.
- `qa_results.md` – Records test outcomes and accessibility checks.
- `defect_log.md` – Records identified issues and their status.
- `handover_backlog.md` – Lists outstanding improvements and future recommendations.

## Known Limitations

- Additional machine-learning and edge-case testing is recommended.
- Formal colour-contrast ratios have not been measured.
- Full accessibility compliance has not been confirmed.
- Classification results are not a guarantee that a message is safe or fraudulent.