import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": [" Alice ", "Bob", "Charlie", "Bob"],
    "Age": [20, 21, np.nan, 21],
    "Marks": ["85", "90", "unknown", "90"],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai"]
})
"""
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
"""
print(df.info())
print(df.isna().sum())
df["Name"] = df["Name"].str.strip()  # Remove leading/trailing whitespace
print(df["Name"])
df["marks"] = pd.to_numeric(df["Marks"], errors='coerce')  # Convert to numeric, set errors to NaN
print(df["marks"])
df["marks"] = df["marks"].fillna(df["marks"].mean())  # Fill NaN with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())  # Fill NaN with mean
print(df.info())
