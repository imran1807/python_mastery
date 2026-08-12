import pandas as pd
import seaborn as sns
import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt


df = pd.DataFrame({
    "Department": [
        "CSE", "CSE", "ECE", "ECE",
        "EEE", "EEE", "CSE", "ECE"
    ],
    "Study_Hours": [5, 7, 4, 6, 3, 5, 8, 7],
    "Marks": [70, 85, 60, 78, 55, 68, 92, 80]
})
sns.countplot(
    data=df,
    x="Department",
    hue="Department"
)
plt.title("Marks Distribution by Department")
plt.show()

sns.barplot(
    data=df,
    x="Department",
    y="Marks",
    errorbar=None
)
plt.title("Average Marks by Department")
plt.show()

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks",
    hue="Department"
)
plt.title("Study Hours vs Marks by Department")
plt.show()

corr=df.corr(numeric_only=True)
sns.heatmap(
    data=corr,
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix")
plt.show()