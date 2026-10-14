# ShieldSense

ShieldSense is a proof-of-concept application designed to analyse short SMS or chat messages for possible scam indicators and classify them as Low, Medium, or High risk.

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

The application uses Streamlit for the web interface and scikit-learn for machine-learning predictions. Install the dependencies before running the application.

## Installation

Clone the repository:

```bash
git clone https://github.com/bijaychhetri25/ShieldSense.git
cd ShieldSense
### Install dependencies

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

### Run the application

Start the ShieldSense web application:

```bash
python3 -m streamlit run interface_accessibility/app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

### Run quality assurance tests

From the project root, run:

```bash
python3 integration_qa/qa_checks.py
```

Review the test results in the terminal.