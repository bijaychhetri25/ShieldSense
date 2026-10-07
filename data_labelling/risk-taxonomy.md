# Risk Taxonomy v2.0

**Author:** Jaskaran Singh — Data & Labelling Lead
**Date:** 17 September 2026
**Status:** Approved for dataset labelling

## 1. Purpose

This document defines what "Low", "Medium" and "High" risk mean for ShieldSense. Every label in the dataset must be traceable back to these definitions. If a message does not fit, the taxonomy is amended — not the message.

## 2. Low Risk

**Definition:** A message that shows no clear signs of scam or phishing intent. It may be a normal personal message, a routine service notification, or a legitimate marketing message from a known sender. There is no request for personal information, payment, or urgent action.

**Indicators:**
- Familiar sender or known service
- No link, or a link to a well-known domain
- No request for personal information or payment
- No urgency or threat
- Normal conversational tone

**Example 1:** "Hey, are we still meeting at 3pm tomorrow?"
**Example 2:** "Your Woolworths order has been delivered. Thanks for shopping with us."
**Example 3:** "Reminder: your appointment at ACU Health Clinic is on Tuesday at 10am."

**Edge case:** A message from an unknown number saying only "Hi" with no context. Label as Low because there is no scam signal, but flag for review if the same number sends repeated messages.

## 3. Medium Risk

**Definition:** A message that contains one or two mild scam indicators, such as urgency, an unfamiliar sender, or a request to click a link, but does not clearly ask for personal information or money. It might be legitimate, but the pattern matches known scam templates.

**Indicators:**
- One or two of: urgency, unfamiliar sender, shortened link, generic greeting
- No direct request for payment or personal details
- Wording matches known scam patterns
- Could plausibly be legitimate

**Example 1:** "Your package could not be delivered. Please reschedule here: [shortened link]"
**Example 2:** "Your account has a new login. If this wasn't you, contact us."
**Example 3:** "Congratulations! You have been selected for a survey. Click here to participate."

**Edge case:** A legitimate Australia Post message that uses the same phrasing as a known scam. Label as Medium because the pattern matches a scam template, even if the sender is real. This is a hard negative and must be included in the dataset.

## 4. High Risk

**Definition:** A message that clearly asks for personal information, payment, or urgent action, and contains multiple scam indicators such as a shortened link, a threat, or an unfamiliar sender. The intent is clearly to deceive.

**Indicators:**
- Two or more of: urgency, threat, unfamiliar sender, shortened link, request for payment, request for personal details
- Clear ask for money, passwords, bank details, or identity documents
- Threat of account suspension, legal action, or loss
- Too-good-to-be-true offers

**Example 1:** "Your bank account will be suspended. Verify your details immediately: [link]"
**Example 2:** "You have won $5,000. Send your bank details to claim."
**Example 3:** "Final notice: unpaid toll. Pay now or face legal action: [link]"

**Edge case:** A message from a legitimate bank that uses urgent language. Label as High because the pattern matches a known phishing template, even if the sender is real. This is a hard negative and must be included in the dataset.

## 5. Hard Negatives (Legitimate Messages That Look Risky)

These must be included in the dataset to prevent the model from learning "urgent = scam" too simplistically.

- "Your Telstra bill is ready. View it in the app."
- "Your parcel is at the post office. Bring ID to collect."
- "Your appointment at [clinic] is confirmed for Tuesday."
- "Your ATO refund has been processed. Log in to myGov to view."
- "Your electricity bill is overdue. Please pay by Friday."

## 6. Decision Tree
Is there a request for payment or personal information?
├── YES → Is there also urgency, a threat, or a shortened link?
│ ├── YES → HIGH RISK
│ └── NO → MEDIUM RISK
└── NO → Are there one or two mild scam indicators?
├── YES → MEDIUM RISK
└── NO → LOW RISK

## 7. Version History

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 10 Sep 2026 | Initial draft, 6 categories | Jaskaran |
| 2.0 | 17 Sep 2026 | Collapsed to 3 categories; added hard negatives and decision tree | Jaskaran |