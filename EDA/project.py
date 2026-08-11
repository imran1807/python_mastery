import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F", "G", "G"],
    "Age": [20, 21, np.nan, 22, 20, 23, 21, 21],
    "Study_Hours": [2, 4, 6, 3, 8, 5, 20, 20],
    "Marks": [55, 65, 75, 60, 88, np.nan, 150, 150],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai",
             "Mumbai", "Delhi", "Chennai", "Chennai"]
})
"""
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
"""
print(df.isna().sum())
print(df.duplicated().sum())

print(df[df.duplicated(keep=False)].sort_values(by=list(df.columns)))
print(df[df.isna().any(axis=1)].sort_values(by=list(df.columns)))
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
df=df.drop_duplicates()

print(df["Marks"].describe())
print(df["Age"].describe())
print("Study Hours Q1:", df["Study_Hours"].quantile(0.25))
print("Study Hours Q3:", df["Study_Hours"].quantile(0.75))
"""
study_iqr = (
    df["Study_Hours"].quantile(0.75)
    - df["Study_Hours"].quantile(0.25)
)

print("Study Hours IQR:", study_iqr)


print("Marks Q1:", df["Marks"].quantile(0.25))
print("Marks Q3:", df["Marks"].quantile(0.75))

marks_iqr = (
    df["Marks"].quantile(0.75)
    - df["Marks"].quantile(0.25)
)
print("Marks IQR:", marks_iqr)
"""
df.loc[df["Marks"] > 100, "Marks"] = np.nan
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
df=df[df["Study_Hours"]<=12.5]
print(df)
print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

print("\nSummary:")
print(df.describe())

print("Average Marks:", df["Marks"].mean())

print("Average Study Hours:", df["Study_Hours"].mean())

print("\nAverage Marks by City:")
print(df.groupby("City")["Marks"].mean())

print("\nCorrelation:")
print(df["Study_Hours"].corr(df["Marks"]))

plt.hist(df["Marks"], bins=5)
plt.xlabel("Marks")
plt.ylabel("students")
plt.title("Distribution of student")
plt.show()

plt.boxplot(df["Marks"])
plt.ylabel("Marks")
plt.title("Marks distribution")
plt.show()

plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

city_avg=df.groupby("City")["Marks"].mean()
city_avg.plot(kind="bar")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.title("Average Marks by City")
plt.show()