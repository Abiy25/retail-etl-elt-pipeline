
def transform_records(valid_records):
    """Calculate sales values for valid transactions."""

    transformed_records = []

    for row in valid_records:

        # Convert numeric CSV values from strings to numbers.
        quantity = int(row["quantity"])
        unit_price = float(row["unit_price"])
        discount = float(row["discount"])

        # Calculate gross and net sales.
        gross_sales = quantity * unit_price
        net_sales = gross_sales - discount

        # Create a transformed record.
        transformed_row = {
            "transaction_id": row["transaction_id"],
            "transaction_date": row["transaction_date"],
            "customer_id": row["customer_id"],
            "product_id": int(row["product_id"]),
            "quantity": quantity,
            "unit_price": unit_price,
            "discount": discount,
            "gross_sales": gross_sales,
            "net_sales": net_sales,
            "payment_method": row["payment_method"],
            "store_id": row["store_id"]
        }

        transformed_records.append(transformed_row)

    return transformed_records
