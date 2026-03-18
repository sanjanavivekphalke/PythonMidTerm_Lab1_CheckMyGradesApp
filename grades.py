import csv


class Grades:
    def __init__(self, student_id, first_name, last_name, email_address, course_id, grade, marks):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.course_id = course_id
        self.grade = grade
        self.marks = marks

    def display(self):
        print(f"{self.student_id} | {self.first_name} | {self.last_name} | {self.email_address} | {self.course_id} | {self.grade} | {self.marks}")


def load_grades():
    grades = []
    with open("Student.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(Grades(
                row["student_id"],
                row["first_name"],
                row["last_name"],
                row["email_address"],
                row["course_id"],
                row["grade"],
                row["marks"]
            ))
    return grades


def save_grades(grades):
    with open("Student.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["student_id", "first_name", "last_name", "email_address", "course_id", "grade", "marks"])
        for g in grades:
            writer.writerow([
                g.student_id,
                g.first_name,
                g.last_name,
                g.email_address,
                g.course_id,
                g.grade,
                g.marks
            ])


def display_grade_report():
    grades = load_grades()
    print("\nGrade Report:")
    for g in grades:
        g.display()


def add_grade():
    student_id = input("Enter student id: ").strip()
    grades = load_grades()

    for g in grades:
        if g.student_id == student_id:
            g.grade = input("Enter grade: ").strip()
            g.marks = input("Enter marks: ").strip()
            save_grades(grades)
            print("Grade added successfully!")
            return

    print("Student not found.")


def delete_grade():
    student_id = input("Enter student id to delete grade: ").strip()
    grades = load_grades()

    for g in grades:
        if g.student_id == student_id:
            g.grade = ""
            g.marks = ""
            save_grades(grades)
            print("Grade deleted successfully!")
            return

    print("Student not found.")


def modify_grade():
    student_id = input("Enter student id to modify grade: ").strip()
    grades = load_grades()

    for g in grades:
        if g.student_id == student_id:
            g.grade = input("Enter new grade: ").strip()
            g.marks = input("Enter new marks: ").strip()
            save_grades(grades)
            print("Grade modified successfully!")
            return

    print("Student not found.")