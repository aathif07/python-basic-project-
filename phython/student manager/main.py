# main.py

import student

while True:
    print("\n=== Student Record System ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        grade = input("Enter grade: ")
        student.add_student(name, roll, grade)
        print("Student added successfully!")

    elif choice == '2':
        student.view_students()

    elif choice == '3':
        roll = input("Enter roll number to search: ")
        student.search_student(roll)

    elif choice == '4':
        print("Thank you! Exiting.")
        break

    else:
        print("Invalid choice. Try again.")
     