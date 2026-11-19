import sqlite3

from .config import DATABASE_FILE


def load_records(records):
    """Load transformed sales records into the SQLite database."""

    # Make sure the database directory exists.
    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Connect to the SQLite database.
    connection = sqlite3.connect(DATABASE_FILE)

    try:
        with connection:

            # Create the sales table if it does not already exist.
            connection.execute("""
                CREATE TABLE IF NOT EXISTS sales (
                    transaction_id TEXT PRIMARY KEY,
                    transaction_date TEXT NOT NULL,
                    customer_id TEXT NOT NULL,
                    product_id INTEGER NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_price REAL NOT NULL,
                    discount REAL NOT NULL,
                    gross_sales REAL NOT NULL,
                    net_sales REAL NOT NULL,
                    payment_method TEXT NOT NULL,
                    store_id TEXT NOT NULL
                )
            """)

            # Clear previous records to prevent duplicates when rerunning.
            connection.execute("DELETE FROM sales")

            # Insert the transformed records.
            connection.executemany("""
                INSERT INTO sales (
                    transaction_id,
                    transaction_date,
                    customer_id,
                    product_id,
                    quantity,
                    unit_price,
                    discount,
                    gross_sales,
                    net_sales,
                    payment_method,
                    store_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, [
                (
                    row["transaction_id"],
                    row["transaction_date"],
                    row["customer_id"],
                    row["product_id"],
                    row["quantity"],
                    row["unit_price"],
                    row["discount"],
                    row["gross_sales"],
                    row["net_sales"],
                    row["payment_method"],
                    row["store_id"]
                )
                for row in records
            ])

            # Count the records currently stored in the table.
            result = connection.execute(
                "SELECT COUNT(*) FROM sales"
            )

            record_count = result.fetchone()[0]

        return record_count

    finally:
        connection.close()