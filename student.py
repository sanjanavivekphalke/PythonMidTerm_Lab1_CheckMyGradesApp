import csv
import time


class Student:
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


def load_students():
    students = []
    with open("Student.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(Student(
                row["student_id"],
                row["first_name"],
                row["last_name"],
                row["email_address"],
                row["course_id"],
                row["grade"],
                row["marks"]
            ))
    return students


def save_students(students):
    with open("Student.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["student_id", "first_name", "last_name", "email_address", "course_id", "grade", "marks"])
        for student in students:
            writer.writerow([
                student.student_id,
                student.first_name,
                student.last_name,
                student.email_address,
                student.course_id,
                student.grade,
                student.marks
            ])


def display_records():
    students = load_students()
    print("\nStudent Records:")
    for student in students:
        student.display()


def add_new_student():
    student_id = input("Enter student id: ").strip()
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    email_address = input("Enter email address: ").strip()
    course_id = input("Enter course id: ").strip()
    grade = input("Enter grade: ").strip()
    marks = input("Enter marks: ").strip()

    if not student_id or not first_name or not last_name or not email_address or not course_id:
        print("Student_id, first_name, last_name, email_address and course_id cannot be empty.")
        return

    students = load_students()
    for student in students:
        if student.student_id == student_id:
            print("Student ID already exists.")
            return
        if student.email_address == email_address:
            print("Email already exists.")
            return

    students.append(Student(student_id, first_name, last_name, email_address, course_id, grade, marks))
    save_students(students)
    print("Student added successfully!")


def delete_new_student():
    student_id = input("Enter student id to delete: ").strip()
    students = load_students()

    updated_students = [student for student in students if student.student_id != student_id]

    if len(updated_students) == len(students):
        print("Student not found.")
        return

    save_students(updated_students)
    print("Student deleted successfully!")


def update_student_record():
    student_id = input("Enter student id to update: ").strip()
    students = load_students()

    for student in students:
        if student.student_id == student_id:
            student.first_name = input("Enter new first name: ").strip()
            student.last_name = input("Enter new last name: ").strip()
            student.email_address = input("Enter new email address: ").strip()
            student.course_id = input("Enter new course id: ").strip()
            student.grade = input("Enter new grade: ").strip()
            student.marks = input("Enter new marks: ").strip()

            if not student.first_name or not student.last_name or not student.email_address or not student.course_id:
                print("Fields cannot be empty.")
                return

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def check_my_grades():
    student_id = input("Enter student id: ").strip()
    students = load_students()

    for student in students:
        if student.student_id == student_id:
            print(f"Grade for {student.first_name} {student.last_name}: {student.grade}")
            return

    print("Student not found.")


def check_my_marks():
    student_id = input("Enter student id: ").strip()
    students = load_students()

    for student in students:
        if student.student_id == student_id:
            print(f"Marks for {student.first_name} {student.last_name}: {student.marks}")
            return

    print("Student not found.")


def search_student():
    student_id = input("Enter student id to search: ").strip()
    students = load_students()

    start_time = time.time()

    for student in students:
        if student.student_id == student_id:
            end_time = time.time()
            print("Student found:")
            student.display()
            print(f"Search time: {end_time - start_time:.6f} seconds")
            return

    end_time = time.time()
    print("Student not found.")
    print(f"Search time: {end_time - start_time:.6f} seconds")


def sort_students_by_marks(ascending=True):
    students = load_students()
    students.sort(key=lambda student: int(student.marks), reverse=not ascending)

    print("\nStudents sorted by marks:")
    for student in students:
        student.display()


def sort_students_by_email(ascending=True):
    students = load_students()
    students.sort(key=lambda student: student.email_address.lower(), reverse=not ascending)

    print("\nStudents sorted by email:")
    for student in students:
        student.display()


def course_wise_statistics():
    students = load_students()

    course_dict = {}
    for student in students:
        course = student.course_id
        marks = int(student.marks)

        if course not in course_dict:
            course_dict[course] = []

        course_dict[course].append(marks)

    course_names = {}
    with open("Course.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            course_names[row["course_id"]] = row["course_name"]

    for course_id, marks_list in course_dict.items():
        marks_list.sort()
        n = len(marks_list)
        avg = sum(marks_list) / n

        if n % 2 == 1:
            median = marks_list[n // 2]
        else:
            median = (marks_list[n // 2 - 1] + marks_list[n // 2]) / 2

        print(f"\nCourse ID: {course_id}")
        print(f"Course Name: {course_names.get(course_id, 'Unknown Course')}")
        print(f"Marks: {marks_list}")
        print(f"Average: {avg:.2f}")
        print(f"Median: {median}")