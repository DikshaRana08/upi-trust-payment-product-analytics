# ==========================================
# TrustPay UPI Product Analytics
# Generate Banks Dataset
# ==========================================

import pandas as pd
from pathlib import Path

print("======================================")
print("Generating Banks Dataset...")
print("======================================")

# -----------------------------
# Bank Data
# -----------------------------

banks = [

    [1, "State Bank of India", "SBI", "Public", "High"],
    [2, "HDFC Bank", "HDFC", "Private", "High"],
    [3, "ICICI Bank", "ICICI", "Private", "High"],
    [4, "Axis Bank", "AXIS", "Private", "Medium"],
    [5, "Punjab National Bank", "PNB", "Public", "Medium"],
    [6, "Bank of Baroda", "BOB", "Public", "High"],
    [7, "Canara Bank", "CANARA", "Public", "Medium"],
    [8, "Union Bank of India", "UNION", "Public", "Medium"],
    [9, "Kotak Mahindra Bank", "KOTAK", "Private", "High"],
    [10, "IndusInd Bank", "INDUSIND", "Private", "Medium"],
    [11, "IDFC FIRST Bank", "IDFC", "Private", "High"],
    [12, "Yes Bank", "YES", "Private", "Medium"],
    [13, "Federal Bank", "FEDERAL", "Private", "High"],
    [14, "AU Small Finance Bank", "AU", "Small Finance", "Medium"],
    [15, "Indian Bank", "INDIAN", "Public", "High"],
    [16, "UCO Bank", "UCO", "Public", "Medium"],
    [17, "Central Bank of India", "CENTRAL", "Public", "Medium"],
    [18, "South Indian Bank", "SIB", "Private", "Medium"],
    [19, "Karnataka Bank", "KBL", "Private", "Medium"],
    [20, "RBL Bank", "RBL", "Private", "Medium"]

]

# -----------------------------
# Create DataFrame
# -----------------------------

banks_df = pd.DataFrame(
    banks,
    columns=[
        "bank_id",
        "bank_name",
        "bank_code",
        "bank_type",
        "uptime_tier"
    ]
)

print("\nFirst 5 Banks\n")
print(banks_df.head())

# -----------------------------
# Create datasets folder
# -----------------------------

project_folder = Path(__file__).resolve().parent.parent

dataset_folder = project_folder / "datasets"

dataset_folder.mkdir(exist_ok=True)

# -----------------------------
# Save CSV
# -----------------------------

output_file = dataset_folder / "banks.csv"

banks_df.to_csv(output_file, index=False)

# -----------------------------
# Print Summary
# -----------------------------

print("\n======================================")
print("Banks Dataset Created Successfully!")
print("File Saved At :")
print(output_file)
print("Total Banks :", len(banks_df))
print("======================================")