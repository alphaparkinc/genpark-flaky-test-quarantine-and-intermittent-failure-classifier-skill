"""Flaky Test Quarantine & Intermittent Failure Classifier.
100% Python Standard Library.
"""

class FlakyTestClassifier:
    """Tracks test run history and latency variance to detect intermittent non-deterministic flakes."""

    @staticmethod
    def analyze_test_history(test_name: str, runs: list) -> dict:
        total = len(runs)
        if total == 0:
            return {"test_name": test_name, "is_flaky": False, "pass_rate": 1.0}

        passes = sum(1 for r in runs if r.get("status") == "PASS")
        failures = total - passes
        pass_rate = passes / float(total)

        is_flaky = (failures > 0 and passes > 0)
        action = "QUARANTINE_TEST" if is_flaky else ("INVESTIGATE_PERMANENT_FAILURE" if pass_rate == 0.0 else "HEALTHY")

        return {
            "test_name": test_name,
            "total_runs": total,
            "pass_rate": round(pass_rate, 3),
            "is_flaky": is_flaky,
            "recommended_action": action
        }
