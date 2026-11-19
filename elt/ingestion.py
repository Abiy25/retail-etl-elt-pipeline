import csv

from .config import RAW_CSV_FILE


def extract_inventory():
    """Extract inventory records from the CSV file."""

    with open(
        RAW_CSV_FILE,
        mode="r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)
        records = list(reader)

    return records