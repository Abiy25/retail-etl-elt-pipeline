
from pathlib import Path

# Find the root directory of the project.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Location of the original CSV dataset.
RAW_FILE = PROJECT_ROOT / "data" / "raw" / "sales.csv"

# Location where cleaned data will eventually be saved.
PROCESSED_FILE = PROJECT_ROOT / "data" / "processed" / "sales_clean.csv"

# Location of our SQLite database.
DATABASE_FILE = PROJECT_ROOT / "database" / "retail.db"
