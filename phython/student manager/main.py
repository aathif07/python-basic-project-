# main.py
  
import tkinter as tk

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    grade = grade_entry.get()
    with open("students.txt", "a") as f:
        f.write(f"{name},{roll},{grade}\n")
    status_label.config(text="✅ Student Added!")

# GUI Window
root = tk.Tk()
root.title("Student Manager")
root.geometry("400x300")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll No").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Grade").pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()

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
     