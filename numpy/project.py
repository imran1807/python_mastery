import numpy as np

marks = np.array([
    [85, 90, 78],
    [70, 65, 80],
    [92, 88, 95],
    [60, 75, 68],
    [88, 91, 84]
])

print(f"Shape: {marks.shape}")
print(f"Number of students: {marks.shape[0]}")
print(f"Number of subjects: {marks.shape[1]}")

student_avg = marks.mean(axis=1)
subject_avg = marks.mean(axis=0)

print(f"Mean marks for each student: {student_avg}")
print(f"Mean marks for each subject: {subject_avg}")

print(f"Maximum marks for each student: {marks.max(axis=1)}")
print(f"Minimum marks for each subject: {marks.min(axis=0)}")

print(f"Overall mean: {marks.mean()}")

print(f"Students with average > 80:")
print(marks[student_avg > 80])

print(f"Students with average < 70:")
print(marks[student_avg < 70])
i= {np.argmax(student_avg)}
print(f"indices of the studeent with the highest average marks: {np.argmax(student_avg)}")
print(f"marks of the student with the highest average marks: {marks[np.argmax(student_avg)]}")
print(f"average marks of the student with the highest average marks: {marks[np.argmax(student_avg)].mean()}")
i = np.argmax(subject_avg)

print(f"Index of subject with highest average: {i}")
print(f"Marks in that subject: {marks[:, i]}")
print(f"Average marks: {marks[:, i].mean()}")
student_avg = marks.mean(axis=1)
print(f"indices of the students with average marks greater than 70: {np.where(student_avg > 70)}")
print(f"numbers of students with average marks greater than 70: {np.sum(student_avg > 70)}")