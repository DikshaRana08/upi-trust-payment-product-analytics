# ==========================================
# TrustPay UPI Product Analytics
# Import users.csv into MySQL
# ==========================================

import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

print("======================================")
print("Importing Users Dataset into MySQL...")
print("======================================")

# -----------------------------------------
# Read CSV File
# -----------------------------------------

project_folder = Path(__file__).resolve().parent.parent
csv_path = project_folder / "datasets" / "users.csv"

users_df = pd.read_csv(csv_path)

print("\nCSV Loaded Successfully!")
print("Total Users :", len(users_df))
print(users_df.head())

# -----------------------------------------
# Database Connection
# -----------------------------------------

username = os.getenv("MYSQL_USER", "root")
password = os.getenv("MYSQL_PASSWORD", "dik2007@")
host = os.getenv("MYSQL_HOST", "localhost")
port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DATABASE", "trustpay_upi")
sqlite_path = project_folder / "datasets" / "trustpay_upi.sqlite"

engine = None
backend = "mysql"

try:
    mysql_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("Connected to MySQL successfully.")
except Exception:
    print("MySQL is not available. Using SQLite local database instead.")
    backend = "sqlite"
    engine = create_engine(f"sqlite:///{sqlite_path}")

# -----------------------------------------
# Import into Database
# -----------------------------------------

chunk_size = 100
users_df.to_sql(
    name="users",
    con=engine,
    if_exists="replace",
    index=False,
    method="multi",
    chunksize=chunk_size
)

# -----------------------------------------
# Success Message
# -----------------------------------------

print("\n======================================")
print("Users Imported Successfully!")
print("Rows Imported :", len(users_df))
print("Database Backend :", backend)
print("Database Path :", sqlite_path if backend == "sqlite" else f"mysql://{host}:{port}/{database}")
print("======================================")