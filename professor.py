import csv


class Professor:
    def __init__(self, professor_id, name, email_address, rank, course_id):
        self.professor_id = professor_id
        self.name = name
        self.email_address = email_address
        self.rank = rank
        self.course_id = course_id

    def display(self):
        print(f"{self.professor_id} | {self.name} | {self.email_address} | {self.rank} | {self.course_id}")


def load_professors():
    professors = []
    with open("Professor.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            professors.append(Professor(
                row["professor_id"],
                row["name"],
                row["email_address"],
                row["rank"],
                row["course_id"]
            ))
    return professors


def save_professors(professors):
    with open("Professor.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["professor_id", "name", "email_address", "rank", "course_id"])
        for professor in professors:
            writer.writerow([
                professor.professor_id,
                professor.name,
                professor.email_address,
                professor.rank,
                professor.course_id
            ])


def professors_details():
    professors = load_professors()
    print("\nProfessor Details:")
    for professor in professors:
        professor.display()


def add_new_professor():
    professor_id = input("Enter professor id: ").strip()
    name = input("Enter professor name: ").strip()
    email_address = input("Enter professor email address: ").strip()
    rank = input("Enter professor rank: ").strip()
    course_id = input("Enter course id: ").strip()

    if not professor_id or not name or not email_address or not course_id:
        print("Professor_id, name, email_address and course_id cannot be empty.")
        return

    professors = load_professors()
    for professor in professors:
        if professor.professor_id == professor_id:
            print("Professor ID already exists.")
            return
        if professor.email_address == email_address:
            print("Professor email already exists.")
            return

    professors.append(Professor(professor_id, name, email_address, rank, course_id))
    save_professors(professors)
    print("Professor added successfully!")


def delete_professore():
    professor_id = input("Enter professor id to delete: ").strip()
    professors = load_professors()

    updated_professors = [professor for professor in professors if professor.professor_id != professor_id]

    if len(updated_professors) == len(professors):
        print("Professor not found.")
        return

    save_professors(updated_professors)
    print("Professor deleted successfully!")


def modify_professor_details():
    professor_id = input("Enter professor id to modify: ").strip()
    professors = load_professors()

    for professor_obj in professors:
        if professor_obj.professor_id == professor_id:
            professor_obj.name = input("Enter new professor name: ").strip()
            professor_obj.email_address = input("Enter new professor email address: ").strip()
            professor_obj.rank = input("Enter new rank: ").strip()
            professor_obj.course_id = input("Enter new course id: ").strip()

            if not professor_obj.name or not professor_obj.email_address or not professor_obj.course_id:
                print("Fields cannot be empty.")
                return

            save_professors(professors)
            print("Professor details updated successfully!")
            return

    print("Professor not found.")

def show_course_details_by_professor():
    professor_id = input("Enter professor id: ").strip()
    professors = load_professors()

    course_map = {}
    with open("Course.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            course_map[row["course_id"]] = row["course_name"]

    for professor in professors:
        if professor.professor_id == professor_id:
            print("\nProfessor Details:")
            professor.display()
            print("Course Name:", course_map.get(professor.course_id, "Unknown Course"))
            return

    print("Professor not found.")


def search_professor():
    professor_id = input("Enter professor id to search: ").strip()
    professors = load_professors()

    for professor in professors:
        if professor.professor_id == professor_id:
            print("Professor found:")
            professor.display()
            return

    print("Professor not found.")


def sort_professors():
    professors = load_professors()
    professors.sort(key=lambda professor: professor.name.lower())

    print("\nProfessors sorted by name:")
    for professor in professors:
        professor.display()