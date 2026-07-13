from pathlib import Path

# Folder where this Python file is located
current_folder = Path(__file__).parent

# Create the path to students.txt
file_path = current_folder / "students.txt"

"""with open(file_path, "a") as file:
    students = ["Alice", "Bob", "Charlie"]
    for student in students:    
        file.write(student + "\n")"""

"""with open(file_path, "r") as file:
    index=0
    for line in file:
        index+=1
        print(f"{index}. {line.strip()}")
    if index==0:
        print("No students found in the file.")"""
"""student_name = input("Enter student name: ").strip().lower()

with open(file_path, "r") as file:
    for line in file:
        if student_name == line.strip().lower():
            print("Student Found")
            break
    else:
        print("Student Not Found")"""
"""
student_name = input("Enter student name: ").strip().lower()
student=[]
with open(file_path, "r") as file:
    for line in file:
        if student_name != line.strip().lower():
            student.append(line.strip())
with open(file_path, "w") as file:
    for name in student:
        file.write(name + "\n") 
with open(file_path, "r") as file:
    file_content = file.read()
    print("Updated file content:")
    print(file_content)       
"""
student_name = input("Enter student name: ").strip().lower()
new_student_name = input("Enter new student name: ").strip().lower()
student=[]
with open(file_path, "r") as file:
    for line in file:
            student.append(line.strip())
    if student_name in [name.lower() for name in student]:
          student[student.index(student_name)] = new_student_name
    else:
        print("Student Not Found")
with open(file_path, "w") as file:
    for name in student:
        file.write(name + "\n")
with open(file_path, "r") as file:
    file_content = file.read()
    print("Updated file content:")
    print(file_content)

   







