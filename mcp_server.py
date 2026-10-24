"""MCP server for Flaky Test Classifier."""
import sys
import json
from client import FlakyTestClassifier

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "classify_flaky_test",
                "description": "Analyzes pass/fail execution history to identify and quarantine flaky tests",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "test_name": {"type": "string"},
                        "runs": {"type": "array"}
                    },
                    "required": ["test_name", "runs"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "classify_flaky_test":
            args = params.get("arguments", {})
            res = FlakyTestClassifier.analyze_test_history(
                args.get("test_name", "test"),
                args.get("runs", [])
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
