# Scam and Phishing Message Patterns — Background Research

**Author:** Jaskaran Singh
**Date:** 4 September 2026
**Purpose:** Background reading for the ShieldSense project, Week 1.

## Sources Reviewed

1. ACCC Scamwatch — "Top scams of 2025"
2. ACMA — "Avoiding SMS and phone scams"
3. Australian Cyber Security Centre — "Phishing and scam messages"
4. Australian Banking Association — "Scam awareness guidance"
5. eSafety Commissioner — "How to spot a scam message"

## Common Patterns Observed

### Urgency cues
- "Act now", "Immediately", "Final notice", "Within 24 hours"
- "Your account will be suspended"

### Requests for personal information
- Bank details, passwords, PINs, tax file number
- "Verify your identity", "Confirm your details"

### Suspicious links
- Shortened URLs (bit.ly, tinyurl)
- Lookalike domains (commbank-secure.com)
- Links that do not match the claimed sender

### Impersonation
- Banks, Australia Post, Telstra, myGov, ATO
- Generic greetings ("Dear customer") instead of the person's name

### Too-good-to-be-true offers
- Prize winnings, free iPhones, pre-approved loans
- "You have been selected"

## Hard Negatives Noticed

Legitimate service notifications often use language similar to scams:
- "Your parcel could not be delivered"
- "Your account has a new login"
- "Your bill is overdue"

These must be included in the dataset to prevent the model from learning "urgent = scam".

## Notes for the Taxonomy

The taxonomy should classify by intent, not just language. A legitimate bank message using urgent language is not a scam, but it follows the same pattern. This is why hard negatives matter.