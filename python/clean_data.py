import pandas as pd

df = pd.read_csv("../dataset/sales_raw.csv")

print("Raw data:")
print(df)

# Cleaning
df = df.dropna()          # hapus data kosong
df = df.drop_duplicates()

print("\nClean data:")
print(df)

df.to_csv("../dataset/sales_clean.csv", index=False)