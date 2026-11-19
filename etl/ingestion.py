
import csv

from .config import RAW_FILE


def extract_csv(path=RAW_FILE):
    
    #Read a CSV file and return its records as dictionaries.
    with open(path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        rows = list(reader)

    return rows