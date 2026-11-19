from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_CSV_FILE = (
    PROJECT_ROOT / "data" / "elt_raw" / "inventory_movements.csv"
)

DATABASE_FILE = PROJECT_ROOT / "database" / "retail_elt.db"

SQL_FILE = PROJECT_ROOT / "elt" / "transform.sql"