import csv


class Course:
    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description

    def display(self):
        print(f"{self.course_id} | {self.course_name} | {self.description}")


def load_courses():
    courses = []
    with open("Course.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            courses.append(Course(
                row["course_id"],
                row["course_name"],
                row["description"]
            ))
    return courses


def save_courses(courses):
    with open("Course.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["course_id", "course_name", "description"])
        for course in courses:
            writer.writerow([course.course_id, course.course_name, course.description])


def display_courses():
    courses = load_courses()
    print("\nCourses:")
    for course in courses:
        course.display()


def add_new_course():
    course_id = input("Enter course id: ").strip()
    course_name = input("Enter course name: ").strip()
    description = input("Enter description: ").strip()

    if not course_id or not course_name:
        print("Course_id and course_name cannot be empty.")
        return

    courses = load_courses()
    for course in courses:
        if course.course_id == course_id:
            print("Course already exists.")
            return

    courses.append(Course(course_id, course_name, description))
    save_courses(courses)
    print("Course added successfully!")


def delete_new_course():
    course_id = input("Enter course id to delete: ").strip()
    courses = load_courses()

    updated_courses = [course for course in courses if course.course_id != course_id]

    if len(updated_courses) == len(courses):
        print("Course not found.")
        return

    save_courses(updated_courses)
    print("Course deleted successfully!")


def search_course():
    course_id = input("Enter course id to search: ").strip()
    courses = load_courses()

    for course in courses:
        if course.course_id == course_id:
            print("Course found:")
            course.display()
            return

    print("Course not found.")


def sort_courses():
    courses = load_courses()
    courses.sort(key=lambda course: course.course_name.lower())

    print("\nCourses sorted by course name:")
    for course in courses:
        course.display()

def modify_course():
    course_id = input("Enter course id to modify: ").strip()
    courses = load_courses()

    for course_obj in courses:
        if course_obj.course_id == course_id:
            course_obj.course_name = input("Enter new course name: ").strip()
            course_obj.description = input("Enter new description: ").strip()

            if not course_obj.course_name:
                print("Course name cannot be empty.")
                return

            save_courses(courses)
            print("Course modified successfully!")
            return

    print("Course not found.")