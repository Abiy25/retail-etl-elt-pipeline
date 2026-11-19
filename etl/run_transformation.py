
from .ingestion import extract_csv
from .validation import validate_records
from .transformation import transform_records


def main():
    print("Starting ETL transformation...")

    # Step 1: Extract.
    rows = extract_csv()

    # Step 2: Validate.
    valid_records, invalid_records = validate_records(rows)

    # Step 3: Transform.
    transformed_records = transform_records(valid_records)

    print(f"Extracted records: {len(rows)}")
    print(f"Valid records: {len(valid_records)}")
    print(f"Rejected records: {len(invalid_records)}")
    print(f"Transformed records: {len(transformed_records)}")

    if transformed_records:
        print("\nFirst transformed record:")
        print(transformed_records[0])

    print("\nETL transformation completed successfully.")


if __name__ == "__main__":
    main()
