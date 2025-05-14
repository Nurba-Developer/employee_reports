from reports.payout import PayoutReport
import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_payout_report_generation():
    data = [
        {"name": "Alice", "department": "Marketing", "hours_worked": 160, "rate": 50},
        {"name": "Bob", "department": "Design", "hours_worked": 150, "rate": 40},
    ]
    report = PayoutReport(data)
    result = json.loads(report.generate())

    assert result[0]["name"] == "Alice"
    assert result[0]["payout"] == 8000
    assert result[1]["payout"] == 6000
