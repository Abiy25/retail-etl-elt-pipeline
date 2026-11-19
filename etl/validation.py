
from datetime import datetime
from collections import Counter


def validate_records(rows):
    """Separate valid records from invalid records."""

    invalid_records = []
    valid_records = []

    # Count how many times each transaction ID appears.
    transaction_counts = Counter(
        row["transaction_id"] for row in rows
    )

    for row in rows:
        errors = []

        # Check for missing customer ID.
        if not row["customer_id"].strip():
            errors.append("Missing customer ID")

        # Check whether the transaction date is valid.
        try:
            datetime.strptime(
                row["transaction_date"], "%d-%m-%Y"
            )
        except ValueError:
            errors.append("Invalid transaction date")

        # Check that quantity is a positive number.
        try:
            quantity = int(row["quantity"])

            if quantity <= 0:
                errors.append("Quantity must be positive")

        except ValueError:
            errors.append("Invalid quantity")

        # Check for duplicate transaction IDs.
        if transaction_counts[row["transaction_id"]] > 1:
            errors.append("Duplicate transaction ID")

        # Separate valid and invalid records.
        if errors:
            invalid_records.append({
                "record": row,
                "errors": errors
            })
        else:
            valid_records.append(row)

    return valid_records, invalid_records