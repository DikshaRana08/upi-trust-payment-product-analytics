# ==========================================
# TrustPay UPI Product Analytics
# Generate Merchants Dataset
# ==========================================

import random
import pandas as pd
from pathlib import Path

print("======================================")
print("Generating Merchants Dataset...")
print("======================================")

# -----------------------------
# Merchant Categories
# -----------------------------

merchant_categories = {

    "Food": [
        "Zomato",
        "Swiggy",
        "Dominos",
        "Pizza Hut",
        "Burger King"
    ],

    "E-Commerce": [
        "Amazon",
        "Flipkart",
        "Myntra",
        "Ajio",
        "Meesho"
    ],

    "Travel": [
        "IRCTC",
        "MakeMyTrip",
        "Goibibo",
        "Yatra",
        "RedBus"
    ],

    "Healthcare": [
        "Apollo Pharmacy",
        "1mg",
        "Netmeds",
        "Practo",
        "MedPlus"
    ],

    "Utilities": [
        "Electricity Board",
        "Water Board",
        "Gas Agency",
        "FASTag",
        "Broadband"
    ],

    "Entertainment": [
        "Netflix",
        "Spotify",
        "JioHotstar",
        "Sony LIV",
        "BookMyShow"
    ]

}

cities = [
    "Delhi",
    "Mumbai",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Lucknow"
]

# -----------------------------
# Generate Merchants
# -----------------------------

merchant_list = []

merchant_id = 1

for category, names in merchant_categories.items():

    for name in names:

        merchant_list.append({

            "merchant_id": f"M{merchant_id:04d}",

            "merchant_name": name,

            "category": category,

            "city": random.choice(cities),

            "verified": random.choice([
                "Yes",
                "Yes",
                "Yes",
                "No"
            ])

        })

        merchant_id += 1

# -----------------------------
# DataFrame
# -----------------------------

merchant_df = pd.DataFrame(merchant_list)

print("\nFirst 5 Merchants\n")

print(merchant_df.head())

# -----------------------------
# Create datasets folder
# -----------------------------

project_folder = Path(__file__).resolve().parent.parent

dataset_folder = project_folder / "datasets"

dataset_folder.mkdir(exist_ok=True)

# -----------------------------
# Save CSV
# -----------------------------

output_file = dataset_folder / "merchants.csv"

merchant_df.to_csv(output_file, index=False)

# -----------------------------
# Print Summary
# -----------------------------

print("\n======================================")
print("Merchants Dataset Created Successfully!")
print("File Saved At :")
print(output_file)
print("Total Merchants :", len(merchant_df))
print("======================================")