# ==========================================
# TrustPay UPI Product Analytics
# Generate Sessions Dataset
# ==========================================

import random
import pandas as pd
from pathlib import Path

print("======================================")
print("Generating Sessions Dataset...")
print("======================================")

# ---------------------------------
# Project Folder
# ---------------------------------

project_folder = Path(__file__).resolve().parent.parent

dataset_folder = project_folder / "datasets"

# ---------------------------------
# Read Existing Datasets
# ---------------------------------

users = pd.read_csv(dataset_folder / "users.csv")

devices = pd.read_csv(dataset_folder / "devices.csv")

calendar = pd.read_csv(dataset_folder / "calendar.csv")

# ---------------------------------
# Generate Sessions
# ---------------------------------

sessions = []

NUM_SESSIONS = 50000

for i in range(1, NUM_SESSIONS + 1):

    user = users.sample(1).iloc[0]

    device = devices.sample(1).iloc[0]

    day = calendar.sample(1).iloc[0]

    sessions.append({

        "session_id": f"S{i:07d}",

        "user_id": user["user_id"],

        "device_id": device["device_id"],

        "session_date": day["date"],

        "hour": random.randint(0,23),

        "session_duration_minutes": random.randint(1,45),

        "screens_viewed": random.randint(1,20),

        "transactions_attempted": random.randint(0,5)

    })

# ---------------------------------
# DataFrame
# ---------------------------------

sessions_df = pd.DataFrame(sessions)

print("\nFirst 5 Sessions\n")

print(sessions_df.head())

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = dataset_folder / "sessions.csv"

sessions_df.to_csv(output_file,index=False)

# ---------------------------------
# Summary
# ---------------------------------

print("\n======================================")
print("Sessions Dataset Created Successfully!")
print("File Saved At :")
print(output_file)
print("Total Sessions :",len(sessions_df))
print("======================================")