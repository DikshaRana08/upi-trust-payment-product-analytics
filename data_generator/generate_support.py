# ==========================================
# TrustPay UPI Product Analytics
# Generate Support Tickets Dataset
# ==========================================

import random
import pandas as pd
from pathlib import Path

print("======================================")
print("Generating Support Tickets Dataset...")
print("======================================")

# ---------------------------------
# Project Folder
# ---------------------------------

project_folder = Path(__file__).resolve().parent.parent

dataset_folder = project_folder / "datasets"

# ---------------------------------
# Read Transactions
# ---------------------------------

transactions = pd.read_csv(dataset_folder / "transactions.csv")

# ---------------------------------
# Configuration
# ---------------------------------

NUM_TICKETS = 3000

issues = [
    "Payment Failed",
    "Money Debited Not Credited",
    "Refund Pending",
    "UPI PIN Issue",
    "Bank Server Error",
    "Merchant Complaint",
    "Transaction Pending",
    "Duplicate Debit"
]

status_list = [
    "Resolved",
    "Resolved",
    "Resolved",
    "Resolved",
    "In Progress",
    "Open"
]

# ---------------------------------
# Generate Tickets
# ---------------------------------

tickets = []

for i in range(1, NUM_TICKETS + 1):

    txn = transactions.sample(1).iloc[0]

    resolution_time = random.randint(5, 1440)

    tickets.append({

        "ticket_id": f"SP{i:06d}",

        "transaction_id": txn["transaction_id"],

        "user_id": txn["user_id"],

        "issue_type": random.choice(issues),

        "ticket_status": random.choice(status_list),

        "resolution_time_minutes": resolution_time,

        "customer_rating": random.randint(1,5)

    })

# ---------------------------------
# DataFrame
# ---------------------------------

tickets_df = pd.DataFrame(tickets)

print("\nFirst 5 Support Tickets\n")

print(tickets_df.head())

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = dataset_folder / "support_tickets.csv"

tickets_df.to_csv(output_file, index=False)

# ---------------------------------
# Summary
# ---------------------------------

print("\n======================================")
print("Support Tickets Dataset Created Successfully!")
print("File Saved At :")
print(output_file)
print("Total Tickets :", len(tickets_df))
print("======================================")