# Retail ETL & ELT Pipeline

## Project Overview

This is a data engineering project that demonstrates two approaches to data processing: ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform).

The project uses Python, SQLite, and SQL to process retail sales and inventory data from CSV files.

## Technologies Used

- Python
- SQLite
- SQL
- CSV

## Project Objectives

1. Build an ETL pipeline using Python.
2. Build an ELT pipeline using Python and SQL.
3. Clean and validate raw data.
4. Store data in SQLite databases.
5. Generate simple summaries using SQL.
6. Understand the differences between ETL and ELT.

## Project Structure

- `data/` – Contains the CSV datasets.
- `etl/` – Contains the Python files for the ETL pipeline.
- `elt/` – Contains the Python and SQL files for the ELT pipeline.
- `database/` – Stores the SQLite databases.

## How to Run

Run the ETL pipeline:

```bash
python -m etl.run_loading
```

Run the ELT pipeline:

```bash
python -m elt.run_elt
```

## Results

**ETL Pipeline**
- Extracted: 36 records
- Valid records: 31
- Rejected records: 5
- Loaded into database: 31 records

**ELT Pipeline**
- Extracted: 19 records
- Raw records loaded: 19
- Clean records: 12
- Rejected records: 7
- Inventory summary rows: 8

## Author

Abiy Abebe

GitHub: [Abiy25](https://github.com/Abiy25)