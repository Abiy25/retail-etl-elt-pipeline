import sqlite3

from .config import DATABASE_FILE, SQL_FILE
from .ingestion import extract_inventory
from .load_raw import load_raw_records


def main():
    print("Starting inventory ELT pipeline...")

    # Step 1: Extract.
    records = extract_inventory()

    print(f"Extracted records: {len(records)}")

    # Step 2: Load raw data.
    raw_count = load_raw_records(records)

    print(f"Raw records loaded: {raw_count}")

    # Step 3: Transform using SQL.
    connection = sqlite3.connect(DATABASE_FILE)

    try:
        with open(SQL_FILE, encoding="utf-8") as file:
            sql_script = file.read()

        connection.executescript(sql_script)

        clean_count = connection.execute(
            "SELECT COUNT(*) FROM clean_inventory_movements"
        ).fetchone()[0]

        rejected_count = connection.execute(
            "SELECT COUNT(*) FROM rejected_inventory_movements"
        ).fetchone()[0]

        summary_count = connection.execute(
            "SELECT COUNT(*) FROM inventory_summary"
        ).fetchone()[0]

        print(f"Clean records: {clean_count}")
        print(f"Rejected records: {rejected_count}")
        print(f"Inventory summary rows: {summary_count}")

        print("\nInventory ELT pipeline completed successfully.")

    finally:
        connection.close()


if __name__ == "__main__":
    main()