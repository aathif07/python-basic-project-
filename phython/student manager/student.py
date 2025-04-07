# student.py

def add_student(name, roll, grade):
    with open("students.txt", "a") as f:
        f.write(f"{name},{roll},{grade}\n")

def view_students():
    try:
        with open("students.txt", "r") as f:
            lines = f.readlines()
            print("\n--- Student Records ---")
            for line in lines:
                name, roll, grade = line.strip().split(",")
                print(f"Name: {name} | Roll No: {roll} | Grade: {grade}")
    except FileNotFoundError:
        print("No records found!")

def search_student(roll):
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, r, grade = line.strip().split(",")
                if r == roll:
                    print(f"Found: {name} | Roll No: {r} | Grade: {grade}")
                    found = True
                    break
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No data available.")
