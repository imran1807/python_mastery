import pandas as pd
import seaborn as sns
import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Study_Hours": [2, 4, 5, 3, 7, 6, 8, 5],
    "Marks": [55, 65, 72, 60, 85, 78, 92, 75],
    "City": [
        "Delhi", "Mumbai", "Delhi", "Chennai",
        "Mumbai", "Delhi", "Chennai", "Mumbai"
    ]
})
"""

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks",
    hue="City"
)

plt.title("Study Hours vs Marks by City")
plt.show()
sns.histplot(
    data=df,
    x="Marks",
    bins=5
)

plt.title("Distribution of Marks")
plt.show()
sns.histplot(
    data=df,
    x="Marks",
    hue="City",
    bins=5
)

plt.title("Marks Distribution by City")
plt.show()
sns.boxplot(
    data=df,
    x="City",
    y="Marks"
    hue="City"
)

plt.title("Marks Distribution by City")
plt.show()

sns.countplot(
    data=df,
    x="City"
)
plt.title("Count of Students by City")
plt.show() 
sns.barplot(
    data=df,
    x="City",
    y="Marks"
)
plt.title("Average Marks by City")
plt.show()

corr=df.corr(numeric_only=True)
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.show()"""
sns.pairplot(
    data=df,
    hue="City",
)
plt.show()
    