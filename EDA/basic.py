import pandas as pd
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": [20, 21, 22, 20, 23, 21, 24, 22],
    "Study_Hours": [2, 4, 5, 3, 7, 6, 8, 5],
    "Marks": [55, 65, 72, 60, 85, 78, 92, 75],
    "City": [
        "Delhi", "Mumbai", "Delhi", "Chennai",
        "Mumbai", "Delhi", "Chennai", "Mumbai"
    ]
})
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df.isna().sum())
print(df.duplicated().sum())
"""
print("corelation between study hours")
print(df["Study_Hours"].corr(df["Marks"]))
print("\nCorrelation matrix:")
print(df.corr(numeric_only=True))
plt.scatter(df["Study_Hours"],df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
plt.hist(df["Marks"], bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")

plt.show()
plt.boxplot(df["Marks"])

plt.ylabel("Marks")
plt.title("Marks Distribution")

plt.show()"""
df["City"].value_counts().plot(kind="bar")

plt.xlabel("City")
plt.ylabel("Number of Students")
plt.title("Students by City")

plt.show()
city_avg = df.groupby("City")["Marks"].mean()

print(city_avg)

city_avg.plot(kind="bar")

plt.xlabel("City")
plt.ylabel("Average Marks")
plt.title("Average Marks by City")

plt.show()
months=["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales=[100, 150, 200, 250, 300, 350]
plt.plot(months, sales, marker="o", linestyle="-", color="b")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()
import numpy as np
import matplotlib.pyplot as plt

corr = df.corr(numeric_only=True)

plt.imshow(corr)

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(
            j, i,
            f"{corr.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Correlation Heatmap")
plt.show()