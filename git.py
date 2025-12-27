# Student Registration Module

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students[roll] = {"Name": name, "Course": course}
    print("Student added successfully.")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        info = students[roll]
        print(f"Roll: {roll}, Name: {info['Name']}, Course: {info['Course']}")
    else:
        print("Student not found.")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter New Name: ")
        course = input("Enter New Course: ")
        students[roll] = {"Name": name, "Course": course}
        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

while True:
    print("\n--- Student Registration Menu ---")
    print("1. Add Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
