import argparse
from parsers.csv_parser import parse_csv_file
from tabulate import tabulate

def generate_table_report(data):
    if data:
        print(f"Keys in the first row: {data[0].keys()}")

    # Формируем таблицу с 5 колонками
    table = [
        (
            row['department'],
            row['name'],
            row['hours_worked'],
            row['rate'],
            f"${float(row['hours_worked']) * float(row['rate']):,.2f}"
        )
        for row in data
    ]

    return tabulate(
        table,
        headers=["Department", "Name", "Hours", "Rate", "Payout"],
        tablefmt="grid"
    )

def main():
    parser = argparse.ArgumentParser(description="Employee report generator")
    parser.add_argument("files", nargs="+", help="Paths to CSV files")
    parser.add_argument("--report", required=True, help="Report type (e.g., payout)")
    args = parser.parse_args()

    data = []
    for file in args.files:
        data.extend(parse_csv_file(file))

    if args.report == "payout":
        print(generate_table_report(data))
    else:
        print(f"Unknown report type: {args.report}")

if __name__ == "__main__":
    main()
