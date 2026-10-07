# ShieldSense - Baseline Tests
# Student: Kapil Thapa Magar
# Role: Model & Evaluation Lead
#
# Tests added following Week 3 supervisor feedback.

from rules_baseline import classify_message


test_cases = [
    {
        "message": "Going shopping later?",
        "expected": "LOW"
    },
    {
        "message": "Send me your password now",
        "expected": "HIGH"
    },
    {
        "message": "Your bank account has been blocked, transfer now",
        "expected": "HIGH"
    },
    {
        "message": "URGENT! Act now, limited time!",
        "expected": "HIGH"
    }
]


passed = 0
failed = 0


print("\nShieldSense Rules-Based Baseline Tests")
print("======================================")


for test in test_cases:

    result = classify_message(test["message"])

    actual = result["risk"]
    expected = test["expected"]

    if actual == expected:
        status = "PASS"
        passed += 1
    else:
        status = "FAIL"
        failed += 1

    print("\n-----------------------------------")
    print("Message:", test["message"])
    print("Expected:", expected)
    print("Actual:", actual)
    print("Score:", result["score"])
    print("Reasons:", result["reasons"])
    print("Result:", status)


print("\n======================================")
print("Test Summary")
print("Passed:", passed)
print("Failed:", failed)
print("Total:", len(test_cases))