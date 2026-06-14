import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav = pd.read_csv("data/processed/nav_history_clean.csv")
trans = pd.read_csv("data/processed/investor_transactions_clean.csv")
perf = pd.read_csv("data/processed/scheme_performance_clean.csv")

# Load into SQLite
nav.to_sql("nav_history", engine, if_exists="replace", index=False)
trans.to_sql("investor_transactions", engine, if_exists="replace", index=False)
perf.to_sql("scheme_performance", engine, if_exists="replace", index=False)

print("Database Loaded Successfully")
print("NAV Rows:", len(nav))
print("Transactions Rows:", len(trans))
print("Performance Rows:", len(perf))