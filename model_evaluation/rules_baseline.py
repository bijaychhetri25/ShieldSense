
import re


# ShieldSense - Rules-Based Baseline
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead
#
# Initial rules-based baseline for scam-message screening.
# Rules are being refined based on testing, dataset evidence,
# team input and supervisor feedback.


# -----------------------------
# 1. Scam indicator keywords
# -----------------------------

URGENCY_WORDS = [
    "urgent",
    "immediately",
    "act now",
    "limited time"
]

FINANCIAL_WORDS = [
    "payment",
    "bank account",
    "transfer",
    "pay now"
]

SENSITIVE_INFO_WORDS = [
    "password",
    "pin",
    "card details",
    "bank details"
]

PRIZE_WORDS = [
    "winner",
    "prize",
    "claim reward",
    "congratulations"
]

THREAT_WORDS = [
    "account suspended",
    "account has been suspended",
    "account is suspended",
    "account blocked",
    "account has been blocked",
    "account is blocked",
    "account locked",
    "account has been locked",
    "account is locked",
    "final warning"
]


# -----------------------------
# 2. Detection functions
# -----------------------------

def contains_keyword(message, keywords):
    """
    Check for keywords using word boundaries.
    This prevents partial matches such as
    'pin' being detected inside 'shopping'.
    """
    message = message.lower()

    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

        if re.search(pattern, message):
            return True

    return False


def count_keywords(message, keywords):
    """
    Count how many listed keywords or phrases
    occur in the message.
    """
    message = message.lower()
    count = 0

    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

        if re.search(pattern, message):
            count += 1

    return count


def contains_url(message):
    """Check whether the message contains a URL."""
    url_pattern = r"https?://\S+|www\.\S+"
    return bool(re.search(url_pattern, message.lower()))


# -----------------------------
# 3. Rules-based classifier
# -----------------------------

def classify_message(message):

    score = 0
    reasons = []

    # Count separate urgency indicators
    urgency_count = count_keywords(message, URGENCY_WORDS)

    if urgency_count > 0:
        score += urgency_count
        reasons.append(
            f"Urgency language detected ({urgency_count} indicator(s))"
        )

    # Financial/payment language
    if contains_keyword(message, FINANCIAL_WORDS):
        score += 2
        reasons.append("Financial/payment language detected")

    # Requests for sensitive information
    if contains_keyword(message, SENSITIVE_INFO_WORDS):
        score += 3
        reasons.append("Request for sensitive information detected")

    # URLs
    if contains_url(message):
        score += 2
        reasons.append("URL detected")

    # Prize/reward language
    if contains_keyword(message, PRIZE_WORDS):
        score += 2
        reasons.append("Prize/reward language detected")

    # Threat or account-warning language
    if contains_keyword(message, THREAT_WORDS):
        score += 2
        reasons.append("Threat or account-warning language detected")

    # Risk classification thresholds
    if score >= 3:
        risk = "HIGH"

    elif score >= 2:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    return {
        "message": message,
        "score": score,
        "risk": risk,
        "reasons": reasons
    }


# -----------------------------
# 4. Test messages
# -----------------------------

if __name__ == "__main__":

    test_messages = [
        "Hi, are we still meeting at 4pm today?",
        "Your payment is overdue. Please check your account.",
        "Congratulations! You have won a prize.",

        "URGENT! Your account has been suspended. "
        "Verify your password immediately at http://example.com",

        # Checks that 'pin' does not match inside 'shopping'
        "Going shopping later?",

        # Additional risk-classification test cases
        "Send me your password now",
        "Your bank account has been blocked, transfer now",
        "URGENT! Act now, limited time!",

        # Additional account-warning variations
        "URGENT!!! Your account is blocked!!! Verify now!!!"
    ]

    for message in test_messages:

        result = classify_message(message)

        print("\n-----------------------------------")
        print("Message:", result["message"])
        print("Score:", result["score"])
        print("Risk:", result["risk"])
        print("Reasons:", result["reasons"])
