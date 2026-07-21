# ==========================================
# TrustPay UPI Product Analytics
# Generate Users Dataset
# ==========================================

import random
import pandas as pd
from pathlib import Path
from config import *

print("======================================")
print("Generating Users Dataset...")
print("======================================")

# -----------------------------
# Sample Data
# -----------------------------

first_names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun",
    "Diya", "Ananya", "Aisha", "Riya", "Priya",
    "Rahul", "Aman", "Karan", "Neha", "Sneha"
]

last_names = [
    "Sharma", "Verma", "Patel", "Singh", "Gupta",
    "Kumar", "Reddy", "Nair", "Joshi", "Mehta"
]

banks = [
    "SBI",
    "HDFC",
    "ICICI",
    "Axis",
    "PNB",
    "Kotak"
]

# -----------------------------
# Generate Users
# -----------------------------

users = []

for i in range(1, NUM_USERS + 1):

    users.append({

        "user_id": f"U{i:06d}",

        "first_name": random.choice(first_names),

        "last_name": random.choice(last_names),

        "age": random.randint(18, 60),

        "gender": random.choice(["Male", "Female"]),

        "city": random.choice(CITIES),

        "device_type": random.choice(DEVICE_TYPES),

        "bank": random.choice(banks),

        "kyc_status": random.choice([
            "Completed",
            "Completed",
            "Completed",
            "Pending"
        ]),

        "registration_year": random.choice([
            2023,
            2024,
            2025,
            2026
        ])

    })

# -----------------------------
# Convert to DataFrame
# -----------------------------

users_df = pd.DataFrame(users)

print("\nFirst 5 Users\n")

print(users_df.head())

# -----------------------------
# Create datasets folder
# -----------------------------

project_folder = Path(__file__).resolve().parent.parent

dataset_folder = project_folder / "datasets"

dataset_folder.mkdir(exist_ok=True)

# -----------------------------
# Save CSV
# -----------------------------

output_file = dataset_folder / "users.csv"

users_df.to_csv(output_file, index=False)

# -----------------------------
# Print Summary
# -----------------------------

print("\n======================================")
print("Users Dataset Created Successfully!")
print("File Saved At :")
print(output_file)
print("Total Users :", len(users_df))
print("======================================")