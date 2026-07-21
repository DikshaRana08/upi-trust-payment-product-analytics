# ==========================================
# TrustPay UPI Product Analytics
# Configuration File
# ==========================================

# -----------------------------
# Dataset Sizes
# -----------------------------
NUM_USERS = 10000
NUM_SESSIONS = 50000
NUM_TRANSACTIONS = 100000
NUM_SUPPORT_TICKETS = 3000

# -----------------------------
# Transaction Status Distribution
# -----------------------------
SUCCESS_RATE = 0.94
FAILURE_RATE = 0.05
PENDING_RATE = 0.01

# -----------------------------
# Cities
# -----------------------------
CITIES = [
    "Delhi",
    "Mumbai",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Pune",
    "Ahmedabad",
    "Jaipur",
    "Lucknow"
]

# -----------------------------
# Device Types
# -----------------------------
DEVICE_TYPES = [
    "Android",
    "iOS"
]

# -----------------------------
# Payment Types
# -----------------------------
PAYMENT_TYPES = [
    "P2P",
    "Merchant",
    "Bill Payment"
]

# -----------------------------
# Payment Methods
# -----------------------------
PAYMENT_METHODS = [
    "UPI QR",
    "UPI ID",
    "Mobile Number"
]

# -----------------------------
# App Versions
# -----------------------------
APP_VERSIONS = [
    "5.1.8",
    "5.1.9",
    "5.2.0",
    "5.2.1",
    "5.2.2"
]

# -----------------------------
# Peak Hours
# -----------------------------
PEAK_HOURS = [
    18,
    19,
    20,
    21
]

# -----------------------------
# Print Configuration
# (Temporary - remove later)
# -----------------------------
print("========== CONFIG LOADED ==========")
print("Users:", NUM_USERS)
print("Sessions:", NUM_SESSIONS)
print("Transactions:", NUM_TRANSACTIONS)
print("Support Tickets:", NUM_SUPPORT_TICKETS)
print("Success Rate:", SUCCESS_RATE)
print("Failure Rate:", FAILURE_RATE)
print("Pending Rate:", PENDING_RATE)
print("===================================")