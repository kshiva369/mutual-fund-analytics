import pandas as pd
import os

folder_path = "."

for file in os.listdir(folder_path):

    if file.endswith(".csv"):

        print("\n" + "="*60)
        print("FILE:", file)

        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())