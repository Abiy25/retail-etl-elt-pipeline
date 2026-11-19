from .ingestion import extract_csv
from .validation import validate_records
from .transformation import transform_records
from .loading import load_records


def main():
    print("Starting ETL loading process...")

    # Step 1: Extract.
    rows = extract_csv()

    # Step 2: Validate.
    valid_records, invalid_records = validate_records(rows)

    # Step 3: Transform.
    transformed_records = transform_records(valid_records)

    # Step 4: Load into SQLite.
    record_count = load_records(transformed_records)

    print(f"Extracted records: {len(rows)}")
    print(f"Valid records: {len(valid_records)}")
    print(f"Rejected records: {len(invalid_records)}")
    print(f"Transformed records: {len(transformed_records)}")
    print(f"Records stored in database: {record_count}")

    print("\nETL loading process completed successfully.")


if __name__ == "__main__":
    main()