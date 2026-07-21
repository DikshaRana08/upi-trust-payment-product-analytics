# ==========================================
# TrustPay UPI Product Analytics
# Generate Devices Dataset
# ==========================================

import random
import pandas as pd
from pathlib import Path

print("======================================")
print("Generating Devices Dataset...")
print("======================================")

# -----------------------------
# Sample Data
# -----------------------------

brands = {
    "Android": [
        "Samsung",
        "OnePlus",
        "Xiaomi",
        "Realme",
        "Vivo",
        "Oppo",
        "Motorola",
        "Nothing"
    ],
    "iOS": [
        "Apple"
    ]
}

android_models = [
    "Galaxy S23",
    "Galaxy A54",
    "Nord CE 3",
    "11T Pro",
    "Realme GT",
    "V29",
    "Reno 11",
    "Edge 50",
    "Phone 2"
]

ios_models = [
    "iPhone 13",
    "iPhone 14",
    "iPhone 15",
    "iPhone 16"
]

app_versions = [
    "5.1.8",
    "5.1.9",
    "5.2.0",
    "5.2.1",
    "5.2.2"
]

os_versions = [
    "Android 12",
    "Android 13",
    "Android 14",
    "iOS 16",
    "iOS 17",
    "iOS 18"
]

# -----------------------------
# Generate Devices
# -----------------------------

devices = []

for i in range(1, 5001):

    device_type = random.choice(["Android", "iOS"])

    if device_type == "Android":
        brand = random.choice(brands["Android"])
        model = random.choice(android_models)
    else:
        brand = "Apple"
        model = random.choice(ios_models)

    devices.append({

        "device_id": f"D{i:05d}",

        "device_type": device_type,

        "brand": brand,

        "model": model,

        "os_version": random.choice(os_versions),

        "app_version": random.choice(app_versions)

    })

# -----------------------------
# DataFrame
# -----------------------------

devices_df = pd.DataFrame(devices)

print("\nFirst 5 Devices\n")

print(devices_df.head())

# -----------------------------
# Create datasets folder
# -----------------------------

project_folder = Path(__file__).resolve().parent.parent

dataset_folder = project_folder / "datasets"

dataset_folder.mkdir(exist_ok=True)

# -----------------------------
# Save CSV
# -----------------------------

output_file = dataset_folder / "devices.csv"

devices_df.to_csv(output_file, index=False)

# -----------------------------
# Print Summary
# -----------------------------

print("\n======================================")
print("Devices Dataset Created Successfully!")
print("File Saved At :")
print(output_file)
print("Total Devices :", len(devices_df))
print("======================================")