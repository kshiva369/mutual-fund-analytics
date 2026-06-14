import pandas as pd
import sqlite3

# Create SQLite database
conn = sqlite3.connect("bluestock_mf.db")

# Load cleaned files
nav = pd.read_csv("data/processed/nav_history_clean.csv")
trans = pd.read_csv("data/processed/investor_transactions_clean.csv")
perf = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Load into SQLite
nav.to_sql("nav_history", conn, if_exists="replace", index=False)
trans.to_sql("investor_transactions", conn, if_exists="replace", index=False)
perf.to_sql("scheme_performance", conn, if_exists="replace", index=False)

conn.close()

print("Database Loaded Successfully")
print("NAV Rows:", len(nav))
print("Transactions Rows:", len(trans))
print("Performance Rows:", len(perf))