# ShieldSense

ShieldSense is a proof-of-concept application designed to analyse short SMS or chat messages for possible scam indicators and classify them as Low, Medium, or High risk.

The application provides a Streamlit web interface with a rules-based baseline and a machine-learning classifier. Results are not a guarantee that a message is safe or fraudulent.

## Project Structure

- `data_labelling/` – Dataset preparation, risk taxonomy and labelling work.
- `model_evaluation/` – Scam detection baseline, machine-learning model and evaluation.
- `interface_accessibility/` – User interface and accessibility work.
- `integration_qa/` – Integration, quality assurance and testing.
- `docs/` – Project documentation, research and supporting evidence.
- `WEEK4_ROLES.md` – Team roles and responsibilities.

## Requirements

- Python 3.x
- Git

The application uses Streamlit for the web interface and scikit-learn for machine-learning predictions.

## Installation

Clone the repository:

```bash
git clone https://github.com/bijaychhetri25/ShieldSense.git
cd ShieldSense
```

## Install Dependencies

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

## Run the Application

From the project root, run:

```bash
python3 -m streamlit run interface_accessibility/app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Run Quality Assurance Tests

From the project root, run:

```bash
python3 integration_qa/qa_checks.py
```

Review the test results in the terminal. The documented rules-based QA suite has seven test cases. Results apply only to the scenarios tested.

## Limitations

- ShieldSense is a proof-of-concept and cannot guarantee whether a message is safe or fraudulent.
- Scam-detection results may be incorrect.
- Machine-learning confidence should not be interpreted as a guarantee of correctness.
- New scam techniques and unusual message patterns may not be recognised.
- Further model evaluation, edge-case testing and accessibility verification are required.
- Formal colour-contrast ratios have not been measured, so WCAG 2.2 AA contrast compliance has not been confirmed.