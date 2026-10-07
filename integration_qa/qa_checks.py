import sys
from pathlib import Path

# Add the ShieldSense project root to Python's path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from model_evaluation.rules_baseline import classify_message


# ShieldSense - Integration & QA Checks
# Student: Bijay Bahadur Chhetri
# Role: Integration, Documentation & QA Lead


TEST_CASES = [
    {
        "id": "TC07",
        "description": "Password request should be HIGH",
        "message": "Send me your password now",
        "expected": "HIGH"
    },
    {
        "id": "TC08",
        "description": "Blocked bank account + transfer should be HIGH",
        "message": "Your bank account has been blocked, transfer now",
        "expected": "HIGH"
    },
    {
        "id": "TC09",
        "description": "Urgency-only message should be LOW",
        "message": "URGENT! Act now, limited time!",
        "expected": "LOW"
    },
    {
        "id": "TC10",
        "description": "Shopping message should be LOW",
        "message": "Going shopping later?",
        "expected": "LOW"
    }
]


def run_qa_tests():
    print("ShieldSense - Integration & QA Checks")
    print("=" * 60)

    passed = 0
    failed = 0

    for test in TEST_CASES:

        result = classify_message(test["message"])

        actual = result["risk"]
        score = result["score"]
        reasons = result["reasons"]

        if actual == test["expected"]:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1

        print("\n" + "-" * 60)
        print(f"{test['id']}: {test['description']}")
        print(f"Message:  {test['message']}")
        print(f"Expected: {test['expected']}")
        print(f"Actual:   {actual}")
        print(f"Score:    {score}")
        print(f"Reasons:  {reasons}")
        print(f"Status:   {status}")

    print("\n" + "=" * 60)
    print(f"QA SUMMARY: {passed} passed, {failed} failed")

    if failed == 0:
        print("All QA tests passed.")
    else:
        print("Some QA tests failed. Record these failures for review.")


if __name__ == "__main__":
    run_qa_tests()