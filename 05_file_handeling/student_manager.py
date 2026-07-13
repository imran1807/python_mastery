from pathlib import Path
current_folder = Path(__file__).parent
file_path = current_folder / "students.txt"
def add_student(student_name):
    with open(file_path, "a") as file:
        file.write(student_name + "\n")
def view_students():
    with open(file_path, "r") as file:
        index=0
        for line in file:
            index+=1
            print(f"{index}. {line.strip()}")
        if index==0:
            print("No students found in the file.")
def search_student(student_name):
    with open(file_path, "r") as file:
        for line in file:
            if student_name == line.strip().lower():
                print("Student Found")
                break
        else:
            print("Student Not Found")
def delete_student(student_name):
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
def update_student(student_name, new_student_name):
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
if __name__ == "__main__":
    while True:
        print("\nStudent Manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_name = input("Enter student name: ").strip()
            add_student(student_name)
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_name = input("Enter student name to search: ").strip().lower()
            search_student(student_name)
        elif choice == "4":
            student_name = input("Enter student name to delete: ").strip().lower()
            delete_student(student_name)
        elif choice == "5":
            student_name = input("Enter student name to update: ").strip().lower()
            new_student_name = input("Enter new student name: ").strip().lower()
            update_student(student_name, new_student_name)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
            
