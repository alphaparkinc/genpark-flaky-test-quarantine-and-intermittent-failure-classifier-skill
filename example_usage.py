"""Example usage for Flaky Test Classifier."""
from client import FlakyTestClassifier

if __name__ == "__main__":
    runs = [{"status": "PASS"}, {"status": "FAIL"}, {"status": "PASS"}]
    res = FlakyTestClassifier.analyze_test_history("test_billing_webhook", runs)
    print("Is Flaky:", res["is_flaky"], "Action:", res["recommended_action"])
