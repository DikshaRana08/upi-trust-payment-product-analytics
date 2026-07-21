# ==========================================
# TrustPay UPI Product Analytics
# Generate Calendar Dataset
# ==========================================

import pandas as pd
from pathlib import Path

print("======================================")
print("Generating Calendar Dataset...")
print("======================================")

# -----------------------------
# Generate Calendar
# -----------------------------

calendar_df = pd.DataFrame({

    "date": pd.date_range(
        start="2025-01-01",
        end="2025-12-31",
        freq="D"
    )

})

# -----------------------------
# Calendar Attributes
# -----------------------------

calendar_df["year"] = calendar_df["date"].dt.year

calendar_df["month"] = calendar_df["date"].dt.month

calendar_df["month_name"] = calendar_df["date"].dt.month_name()

calendar_df["quarter"] = calendar_df["date"].dt.quarter

calendar_df["week"] = calendar_df["date"].dt.isocalendar().week

calendar_df["day"] = calendar_df["date"].dt.day

calendar_df["day_name"] = calendar_df["date"].dt.day_name()

calendar_df["is_weekend"] = calendar_df["day_name"].isin([
    "Saturday",
    "Sunday"
])

# -----------------------------
# Preview
# -----------------------------

print("\nFirst 5 Dates\n")

print(calendar_df.head())

# -----------------------------
# Save CSV
# -----------------------------

project_folder = Path(__file__).resolve().parent.parent

dataset_folder = project_folder / "datasets"

dataset_folder.mkdir(exist_ok=True)

output_file = dataset_folder / "calendar.csv"

calendar_df.to_csv(output_file, index=False)

# -----------------------------
# Summary
# -----------------------------

print("\n======================================")
print("Calendar Dataset Created Successfully!")
print("File Saved At :")
print(output_file)
print("Total Days :", len(calendar_df))
print("======================================")