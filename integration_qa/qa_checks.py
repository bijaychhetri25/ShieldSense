import sys
from pathlib import Path

# Allow the script to import the ShieldSense model from the project root
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from model_evaluation.rules_baseline import classify_message


# --------------------------------------------------
# ShieldSense QA Checks
# Student: Bijay Bahadur Chhetri
# Role: Integration, Documentation & QA Lead
# --------------------------------------------------

TEST_CASES = [
    {
        "id": "TC07",
        "description": "Password request should be HIGH",
        "message": "Send me your password now",
        "expected": "HIGH",
    },
    {
        "id": "TC08",
        "description": "Blocked bank account + transfer should be HIGH",
        "message": "Your bank account has been blocked, transfer now",
        "expected": "HIGH",
    },
    {
        "id": "TC09",
        "description": "Urgency-only message should be HIGH",
        "message": "URGENT! Act now, limited time!",
        "expected": "HIGH",
    },
    {
        "id": "TC10",
        "description": "Shopping message should be LOW",
        "message": "Going shopping later?",
        "expected": "LOW",
    },
]


def run_qa_tests():
    passed = 0
    failed = 0

    print("=" * 60)
    print("ShieldSense QA Test Results")
    print("=" * 60)

    for test in TEST_CASES:
        result = classify_message(test["message"])

        actual = result["risk"]
        score = result["score"]
        reasons = result["reasons"]

        status = "PASS" if actual == test["expected"] else "FAIL"

        if status == "PASS":
            passed += 1
        else:
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
    print("=" * 60)

    if failed == 0:
        print("All supervisor feedback test cases passed.")
    else:
        print("Some QA tests failed. Record these failures for review.")


if __name__ == "__main__":
    run_qa_tests()