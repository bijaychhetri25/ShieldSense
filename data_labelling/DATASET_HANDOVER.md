# ShieldSense Dataset Handover

## Handover From

Bijay Bahadur Chhetri  
Integration, Documentation & QA Lead

## Handover To

Jaskaran Singh  
Data & Labelling Lead

## Dataset Status

### Historical Dataset

File: `data/shieldsense_messages.csv`

The earlier dataset-generation workflow contained 180 synthetic messages, balanced across Red, Amber and Green risk levels, with 60 messages per level.

The historical dataset was checked for duplicate and empty messages. The recorded checks reported 180 unique messages, zero duplicates and zero empty messages.

**Status: Retired.** The earlier dataset and its generation and verification scripts under `src/` have been removed from the current working tree. Their earlier versions remain available in Git history.

### Current Authoritative Dataset

File: `data_labelling/shieldsense-dataset.csv`

The current dataset contains 202 labelled messages and is maintained by the Data & Labelling Lead.

The current model workflow uses:

- `data_labelling/training-set.csv` — 162 training messages.
- `data_labelling/test-set.csv` — 40 locked test messages.

The locked test set must remain unchanged unless the supervisor authorises a change.

## Current Dataset Workflow

The current dataset workflow is maintained in `data_labelling/` and includes:

- `create_dataset.py` — creates the current dataset.
- `dedupe_dataset.py` — checks and removes duplicate messages.
- `split_dataset.py` — creates the training and test splits.
- `verify_dataset.py` — validates the dataset.
- `leakage_check.py` — checks for overlap between training and test data.

Other supporting scripts and documentation in `data_labelling/` remain part of the project.

## Historical Hard Negatives

The earlier dataset included synthetic legitimate-style examples intended to make testing more challenging, including:

- Bank statements
- Payment confirmations
- Delivery tracking
- Parcel updates
- ACU student notifications
- ACU tuition payment receipts
- Banking account information
- Scheduled payments

These examples were intended to support review and labelling against the agreed risk taxonomy. This historical description does not establish that every example was transferred into the current dataset.

## Handover Responsibilities

The Data & Labelling Lead is responsible for:

1. Reviewing messages against the agreed risk taxonomy.
2. Checking label consistency.
3. Completing required corrections.
4. Maintaining the current dataset and labelling documentation.
5. Maintaining the training and locked test sets according to the agreed evaluation process.

## QA and Limitations

The historical dataset's recorded checks reported no duplicate or empty messages and balanced risk levels.

The current dataset and evaluation workflow must be assessed using their own verification and leakage-check results. Historical checks do not establish that the current dataset passes every check.

The current model evaluation uses the separate training and locked test files. The test set must not be used for model tuning.

## Handover Status

The earlier 180-message dataset workflow has been retired from the current working tree. `data_labelling/shieldsense-dataset.csv` is the current authoritative dataset.

The original dataset files and scripts remain recoverable through Git history.