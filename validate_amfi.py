import pandas as pd

fund_master = pd.read_csv("01_fund_master.csv")
nav_history = pd.read_csv("02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Total codes in fund_master:", len(master_codes))
print("Total codes in nav_history:", len(nav_codes))
print("Missing codes:", len(missing_codes))
print(missing_codes)