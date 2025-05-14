import os

POSSIBLE_RATE_FIELDS = {"hourly_rate", "rate", "salary"}

def parse_csv_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    if not lines:
        return []

    headers = [h.strip() for h in lines[0].split(",")]
    rate_field = next((h for h in headers if h in POSSIBLE_RATE_FIELDS), None)
    if not rate_field:
        raise ValueError(f"No rate field found in file: {file_path}")

    results = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        record = dict(zip(headers, values))
        record["hours_worked"] = float(record["hours_worked"])
        record["rate"] = float(record[rate_field])
        results.append({
            "name": record["name"],
            "department": record["department"],
            "hours_worked": record["hours_worked"],
            "rate": record["rate"],
        })
    return results
