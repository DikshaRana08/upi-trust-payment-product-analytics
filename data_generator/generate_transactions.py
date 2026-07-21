# ==========================================
# TrustPay UPI Product Analytics
# Generate Transactions Dataset
# ==========================================

import numpy as np
import pandas as pd
from pathlib import Path

print("======================================")
print("Generating Transactions Dataset...")
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
banks = pd.read_csv(dataset_folder / "banks.csv")
merchants = pd.read_csv(dataset_folder / "merchants.csv")
sessions = pd.read_csv(dataset_folder / "sessions.csv")

# ---------------------------------
# Configuration
# ---------------------------------

NUM_TRANSACTIONS = 100000

statuses = ["SUCCESS", "FAILED", "PENDING"]
status_probabilities = [0.94, 0.05, 0.01]

failure_reasons = [
    "Bank Server Down",
    "Insufficient Balance",
    "UPI Timeout",
    "Incorrect UPI PIN",
    "Daily Limit Exceeded",
    "Beneficiary Bank Offline"
]

# ---------------------------------
# Generate Transactions
# ---------------------------------

rng = np.random.default_rng(42)

user_ids = users["user_id"].to_numpy()
merchant_ids = merchants["merchant_id"].to_numpy()
bank_ids = banks["bank_id"].to_numpy()
session_ids = sessions["session_id"].to_numpy()

transaction_statuses = rng.choice(statuses, size=NUM_TRANSACTIONS, p=status_probabilities)
failed_mask = transaction_statuses == "FAILED"

failure_reasons_generated = np.full(NUM_TRANSACTIONS, "", dtype=object)
failure_reasons_generated[failed_mask] = rng.choice(
    failure_reasons,
    size=int(failed_mask.sum()),
)

transaction_amounts = np.round(rng.uniform(20, 15000, size=NUM_TRANSACTIONS), 2)
payment_types = rng.choice(["P2P", "Merchant", "Bill Payment"], size=NUM_TRANSACTIONS)
payment_methods = rng.choice(["QR", "UPI ID", "Mobile Number"], size=NUM_TRANSACTIONS)

transactions_df = pd.DataFrame({
    "transaction_id": [f"T{i:07d}" for i in range(1, NUM_TRANSACTIONS + 1)],
    "session_id": rng.choice(session_ids, size=NUM_TRANSACTIONS),
    "user_id": rng.choice(user_ids, size=NUM_TRANSACTIONS),
    "merchant_id": rng.choice(merchant_ids, size=NUM_TRANSACTIONS),
    "bank_id": rng.choice(bank_ids, size=NUM_TRANSACTIONS),
    "transaction_amount": transaction_amounts,
    "transaction_status": transaction_statuses,
    "failure_reason": failure_reasons_generated,
    "payment_type": payment_types,
    "payment_method": payment_methods,
})

print("\nFirst 5 Transactions\n")

print(transactions_df.head())

# ---------------------------------
# Save CSV
# ---------------------------------

output_file = dataset_folder / "transactions.csv"

transactions_df.to_csv(output_file, index=False)

# ---------------------------------
# Summary
# ---------------------------------

print("\n======================================")
print("Transactions Dataset Created Successfully!")
print("File Saved At :")
print(output_file)
print("Total Transactions :", len(transactions_df))
print("======================================")