import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# NAV History Cleaning
nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv("data/processed/nav_history_clean.csv", index=False)

print("NAV History Cleaned Successfully")
print("Rows:", len(nav))

# investor transactions ceaning -------------

# Investor Transactions Cleaning

trans = pd.read_csv("data/raw/08_investor_transactions.csv")

# Fix date format
trans["transaction_date"] = pd.to_datetime(trans["transaction_date"])

# Standardize transaction types
trans["transaction_type"] = trans["transaction_type"].str.strip().str.upper()

# Keep only valid amounts
trans = trans[trans["amount_inr"] > 0]

# Check KYC status values
print("\nKYC Status Values:")
print(trans["kyc_status"].unique())

# Save cleaned file
trans.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions Cleaned Successfully")


# schema performance clening --------------------------

# Scheme Performance Cleaning

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
perf["return_1yr_pct"] = pd.to_numeric(perf["return_1yr_pct"], errors="coerce")
perf["return_3yr_pct"] = pd.to_numeric(perf["return_3yr_pct"], errors="coerce")
perf["return_5yr_pct"] = pd.to_numeric(perf["return_5yr_pct"], errors="coerce")

# Convert expense ratio
perf["expense_ratio_pct"] = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

# Flag anomalies
anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(len(anomalies))

# Save anomalies if any
anomalies.to_csv(
    "data/processed/expense_ratio_anomalies.csv",
    index=False
)

# Save cleaned file
perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance Cleaned Successfully")