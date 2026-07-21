# ==========================================
# TrustPay UPI Product Analytics
# Import All CSV Files into MySQL
# ==========================================

import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

print("=" * 60)
print("CONNECTING TO DATABASE...")
print("=" * 60)

project_folder = Path(__file__).resolve().parent.parent
sqlite_path = project_folder / "datasets" / "trustpay_upi.sqlite"

username = os.getenv("MYSQL_USER", "root")
password = os.getenv("MYSQL_PASSWORD", "dik2007@")
host = os.getenv("MYSQL_HOST", "localhost")
port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DATABASE", "trustpay_upi")

backend = "mysql"
engine = None

try:
    mysql_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("✅ Connected to MySQL successfully!\n")
except Exception:
    backend = "sqlite"
    engine = create_engine(f"sqlite:///{sqlite_path}")
    print("MySQL is not available. Using SQLite local database instead.\n")

# ==========================================
# DATASETS
# ==========================================

datasets = [
    ("banks", project_folder / "datasets" / "banks.csv"),
    ("devices", project_folder / "datasets" / "devices.csv"),
    ("merchants", project_folder / "datasets" / "merchants.csv"),
    ("calendar", project_folder / "datasets" / "calendar.csv"),
    ("sessions", project_folder / "datasets" / "sessions.csv"),
    ("transactions", project_folder / "datasets" / "transactions.csv"),
    ("support_tickets", project_folder / "datasets" / "support_tickets.csv"),
]

# ==========================================
# IMPORT LOOP
# ==========================================

for table_name, file_path in datasets:
    print("=" * 60)
    print(f"Importing {table_name}...")
    print("=" * 60)

    df = pd.read_csv(file_path)

    if backend == "sqlite":
        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False,
            method="multi",
            chunksize=200,
        )
    else:
        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=200,
        )

    print(f"✅ {table_name} Imported Successfully")
    print(f"Rows Imported : {len(df)}\n")

print("=" * 60)
print("🎉 ALL DATA IMPORTED SUCCESSFULLY 🎉")
print(f"Database Backend : {backend}")
print(f"Database Path : {sqlite_path if backend == 'sqlite' else f'mysql://{host}:{port}/{database}' }")
print("=" * 60)