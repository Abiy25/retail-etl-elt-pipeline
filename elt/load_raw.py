import sqlite3

from .config import DATABASE_FILE


def load_raw_records(records):
    """Load original inventory records into SQLite."""

    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_FILE)

    try:
        with connection:

            connection.execute("""
                CREATE TABLE IF NOT EXISTS raw_inventory_movements (
                    source_row INTEGER,
                    movement_id TEXT,
                    movement_date TEXT,
                    product_id TEXT,
                    product_name TEXT,
                    category TEXT,
                    supplier_id TEXT,
                    warehouse_id TEXT,
                    movement_type TEXT,
                    quantity TEXT,
                    unit_cost TEXT,
                    reference_number TEXT
                )
            """)

            connection.execute(
                "DELETE FROM raw_inventory_movements"
            )

            connection.executemany("""
                INSERT INTO raw_inventory_movements VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """, [
                (
                    index,
                    row["movement_id"],
                    row["movement_date"],
                    row["product_id"],
                    row["product_name"],
                    row["category"],
                    row["supplier_id"],
                    row["warehouse_id"],
                    row["movement_type"],
                    row["quantity"],
                    row["unit_cost"],
                    row["reference_number"]
                )
                for index, row in enumerate(records, start=1)
            ])

        return len(records)

    finally:
        connection.close()