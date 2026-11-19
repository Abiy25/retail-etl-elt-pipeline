
from .ingestion import extract_csv
from .validation import validate_records


def main():
    print("Starting data validation...")

    rows = extract_csv()

    valid_records, invalid_records = validate_records(rows)

    print(f"Total extracted records: {len(rows)}")
    print(f"Valid records: {len(valid_records)}")
    print(f"Rejected records: {len(invalid_records)}")

    print("\nRejected record details:")

    for item in invalid_records:
        record = item["record"]
        errors = item["errors"]

        print(
            f"Transaction {record['transaction_id']}: "
            f"{', '.join(errors)}"
        )

    print("\nData validation completed successfully.")


if __name__ == "__main__":
    main()
