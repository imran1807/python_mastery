1. Introduction

NumPy (Numerical Python) is a Python library used for efficient numerical computation.

import numpy as np

The main object in NumPy is the ndarray (N-dimensional array).

2. Creating Arrays
np.array([1, 2, 3])
np.zeros(5)
np.ones(5)
np.full(5, 10)
np.arange(1, 10)
np.linspace(0, 1, 5)
np.eye(3)
3. Array Attributes
arr.shape
arr.ndim
arr.size
arr.dtype

Example:

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
shape → (2, 3)
ndim  → 2
size  → 6
dtype → integer type
4. Indexing
1D
arr[0]
arr[-1]
2D
arr[row, column]

Example:

arr[1, 2]
5. Slicing
arr[start:stop]

The stop index is excluded.

For 2D arrays:

arr[row_start:row_stop, col_start:col_stop]

Examples:

arr[:, 1]     # all rows, column 1
arr[1, :]     # row 1, all columns
arr[::-1]     # reverse
arr[::2]      # every second element
6. Reshaping
arr.reshape(2, 3)

The total number of elements must remain unchanged.

Using -1:

arr.reshape(2, -1)

NumPy automatically calculates the missing dimension.

7. Flattening
arr.flatten()
arr.ravel()

flatten() creates a copy.

ravel() generally tries to return a view when possible.

8. Vectorization

Instead of:

[x * 2 for x in arr]

NumPy allows:

arr * 2

This avoids explicit Python loops and uses optimized low-level numerical code.

9. Broadcasting

NumPy can perform operations between compatible shapes.

arr = np.array([1, 2, 3])
arr + 10

Result:

[11 12 13]

A scalar is automatically applied to every element.

10. Aggregation

Important functions:

np.sum(arr)
np.mean(arr)
np.min(arr)
np.max(arr)
np.std(arr)
np.var(arr)
11. Axis

For:

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
np.sum(arr, axis=0)

works down the columns:

[5 7 9]
np.sum(arr, axis=1)

works across each row:

[6 15]
Remember
axis=0 → down columns
axis=1 → across rows
12. Boolean Masking
arr[arr > 20]

Multiple conditions:

arr[(arr > 20) & (arr < 50)]

Use:

& → AND
| → OR
~ → NOT
13. np.where()
np.where(condition, value_if_true, value_if_false)

Example:

np.where(arr > 25, 1, 0)
14. Sorting
np.sort(arr)

returns a sorted copy.

arr.sort()

sorts the array in place.

15. Combining Arrays
Concatenate
np.concatenate((a, b))
Vertical stacking
np.vstack((a, b))
Horizontal stacking
np.hstack((a, b))
Splitting
np.split(arr, 2)
16. Copy vs View
Copy
b = a.copy()

Creates independent data.

Changing b does not normally affect a.

View
b = a.view()

Shares the underlying data.

Changing b can affect a.

17. Linear Algebra
Matrix multiplication
A @ B
Transpose
A.T
Dot product
np.dot(a, b)
Determinant
np.linalg.det(A)
Inverse
np.linalg.inv(A)
18. Random Numbers
np.random.randint(1, 10, 5)
np.random.rand(2, 3)
np.random.randn(2, 3)
np.random.choice(arr, 2)

For reproducible results:

np.random.seed(42)

replace=False prevents selecting the same element more than once.

19. Normalization

Min-max normalization:

normalized = (arr - arr.min()) / (arr.max() - arr.min())

Scales values to approximately:

0 → 1
20. Standardization

Standardization transforms data based on its mean and standard deviation:

standardized = (arr - arr.mean()) / arr.std()

Typically:

mean ≈ 0
standard deviation ≈ 1
📊 Mini Project: Student Performance Analyzer
import numpy as np

marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [92, 88, 95],
    [60, 75, 68],
    [88, 91, 84]
])

student_avg = marks.mean(axis=1)
subject_avg = marks.mean(axis=0)

print("Shape:", marks.shape)
print("Number of students:", marks.shape[0])
print("Number of subjects:", marks.shape[1])

print("Student averages:", student_avg)
print("Subject averages:", subject_avg)

print("Maximum marks:", marks.max())
print("Minimum marks:", marks.min())

top_student = np.argmax(student_avg)

print("Top student index:", top_student)
print("Top student marks:", marks[top_student])
print("Top student average:", student_avg[top_student])

top_subject = np.argmax(subject_avg)

print("Top subject index:", top_subject)
print("Top subject marks:", marks[:, top_subject])
print("Top subject average:", subject_avg[top_subject])

passed = student_avg >= 70

print("Passed student indices:", np.where(passed)[0])
print("Number of passed students:", np.sum(passed))
🧠 Key NumPy Concepts to Remember
shape     → structure
ndim      → number of dimensions
size      → number of elements

axis=0    → down columns
axis=1    → across rows

copy()    → independent data
view()    → shared data

@         → matrix multiplication
.T        → transpose

masking   → filtering data
where()   → conditional selection

reshape() → change shape