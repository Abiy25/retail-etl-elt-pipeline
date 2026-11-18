
from .ingestion import extract_csv


def main():
    print("Starting CSV extraction...")

    rows = extract_csv()

    print(f"Successfully extracted {len(rows)} records.")

    if rows:
        print("\nCSV columns:")
        print(list(rows[0].keys()))

        print("\nFirst record:")
        print(rows[0])

    print("\nCSV extraction completed successfully.")


if __name__ == "__main__":
    main()
