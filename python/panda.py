import pandas as pd
df = pd.read_csv("Sales_raw.csv")

# Preview data
print(df.head())

# Clean and transform
df["SaleID"] = pd.to_numeric(df["SaleID"], errors="coerce")
df["Date"] = df["Date"].str.strip().str.lower()

# Filter rows
df = df[df["SaleID"] > 0]

# Add new column
df["Total"] = df["SaleID"]
print(df.head())