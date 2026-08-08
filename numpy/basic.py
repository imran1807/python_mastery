import numpy as np
"""print(np.__version__)
arr=np.arange(10)
print(arr)"""
"""
arr = np.arange(1, 7)

new_arr = arr.reshape(2, 3)

print(new_arr)

a = np.array([
    [1],
    [2],
    [3]
])

b = np.array([10, 20, 30])

print(a + b)

np.random.seed(0)

print(np.random.randn(2, 3)"""
scores = np.array([
    [60, 70, 80],
    [80, 90, 100],
    [40, 50, 60]
])
print(scores.shape)
print(scores.mean(axis=0))
print(scores.mean(axis=1))
print(scores.max(axis=1))