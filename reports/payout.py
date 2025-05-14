import json
from reports.base import Report

class PayoutReport(Report):
    def generate(self):
        result = []
        for item in self.data:
            payout = item["hours_worked"] * item["rate"]
            result.append({
                "name": item["name"],
                "department": item["department"],
                "payout": round(payout, 2)
            })
        return json.dumps(result, indent=4)
