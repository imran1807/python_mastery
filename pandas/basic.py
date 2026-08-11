import pandas as pd

"""marks = pd.Series([80, 90, 70, 85])

print(marks)
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22]
})
print(df)
print(df.shape)
df.info()
df.describe()"""
df=pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age":  [20, 21, 27],
    "city": ["X", "Y", "Z"],
    "sale": [100, 200, 300],
    "category": ["A", "B", "C"]
})
ages = df[df['Age'] > 25]
print(ages)