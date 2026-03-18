import unittest
import csv
import os
import time
from unittest.mock import patch

import student
import course
import professor


class TestCheckMyGrade(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.files = ["Student.csv", "Course.csv", "Professor.csv"]

        cls.backups = {}
        for filename in cls.files:
            if os.path.exists(filename):
                with open(filename, "r", newline="") as f:
                    cls.backups[filename] = f.read()
            else:
                cls.backups[filename] = ""

    def setUp(self):
        self.create_test_courses()
        self.create_test_professors()
        self.create_test_students_1000()

    @classmethod
    def tearDownClass(cls):
        for filename, content in cls.backups.items():
            with open(filename, "w", newline="") as f:
                f.write(content)

    def create_test_students_1000(self):
        with open("Student.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["student_id", "first_name", "last_name", "email_address", "course_id", "grade", "marks"])

            for i in range(1000):
                writer.writerow([
                    f"S{i+1}",
                    f"First{i+1}",
                    f"Last{i+1}",
                    f"student{i+1}@sjsu.edu",
                    "DATA-200" if i % 3 == 0 else ("DATA-201" if i % 3 == 1 else "DATA-202"),
                    "A" if i % 4 == 0 else "B",
                    str(60 + (i % 41))
                ])

    def create_test_courses(self):
        with open("Course.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["course_id", "course_name", "description"])
            writer.writerow(["DATA-200", "Data Science", "Provides insight about DS and Python"])
            writer.writerow(["DATA-201", "Database Tech for DI", "Basics of Data Structures"])
            writer.writerow(["DATA-202", "Math for DI", "Basics of Mathematics"])

    def create_test_professors(self):
        with open("Professor.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["professor_id", "name", "email_address", "rank", "course_id"])
            writer.writerow(["P101", "Paramdeep Saini", "paramdeep.saini@sjsu.edu", "Associate Professor", "DATA-200"])
            writer.writerow(["P102", "Guannan Liu", "guannan.liu@sjsu.edu", "Assistant Professor", "DATA-201"])

    # ---------------- STUDENT TESTS ----------------

    @patch("builtins.input", side_effect=["S2001", "Test", "User", "testuser@sjsu.edu", "DATA-200", "A", "95"])
    def test_add_student(self, mock_input):
        before = len(student.load_students())
        student.add_new_student()
        after = len(student.load_students())
        self.assertEqual(after, before + 1)

    @patch("builtins.input", side_effect=["S1", "Updated", "Name", "updated1@sjsu.edu", "DATA-201", "A", "99"])
    def test_modify_student(self, mock_input):
        student.update_student_record()
        students = student.load_students()
        found = False
        for s in students:
            if s.student_id == "S1":
                found = True
                self.assertEqual(s.first_name, "Updated")
                self.assertEqual(s.email_address, "updated1@sjsu.edu")
                self.assertEqual(s.marks, "99")
        self.assertTrue(found)

    @patch("builtins.input", side_effect=["S2"])
    def test_delete_student(self, mock_input):
        before = len(student.load_students())
        student.delete_new_student()
        after = len(student.load_students())
        self.assertEqual(after, before - 1)

    @patch("builtins.input", side_effect=["S10"])
    def test_search_student_timing(self, mock_input):
        start = time.time()
        student.search_student()
        end = time.time()
        total = end - start
        print(f"\nTotal search time: {total:.6f} seconds")
        self.assertGreaterEqual(total, 0)

    def test_sort_students_by_marks_timing(self):
        start = time.time()
        student.sort_students_by_marks(True)
        end = time.time()
        total = end - start
        print(f"\nSort by marks ascending time: {total:.6f} seconds")
        self.assertGreaterEqual(total, 0)

    def test_sort_students_by_email_timing(self):
        start = time.time()
        student.sort_students_by_email(True)
        end = time.time()
        total = end - start
        print(f"\nSort by email ascending time: {total:.6f} seconds")
        self.assertGreaterEqual(total, 0)

    # ---------------- COURSE TESTS ----------------

    @patch("builtins.input", side_effect=["DATA-300", "AI Fundamentals", "Introduction to AI"])
    def test_add_course(self, mock_input):
        before = len(course.load_courses())
        course.add_new_course()
        after = len(course.load_courses())
        self.assertEqual(after, before + 1)

    def test_modify_course(self):
        # create target record first so test is independent
        courses = course.load_courses()
        courses.append(course.Course("DATA-300", "AI Fundamentals", "Introduction to AI"))
        course.save_courses(courses)

        with patch("builtins.input", side_effect=["DATA-300", "Advanced AI", "Updated AI course"]):
            course.modify_course()

        courses = course.load_courses()
        found = False
        for c in courses:
            if c.course_id == "DATA-300":
                found = True
                self.assertEqual(c.course_name, "Advanced AI")
                self.assertEqual(c.description, "Updated AI course")
        self.assertTrue(found)

    def test_delete_course(self):
        # create target record first
        courses = course.load_courses()
        courses.append(course.Course("DATA-300", "AI Fundamentals", "Introduction to AI"))
        course.save_courses(courses)

        with patch("builtins.input", side_effect=["DATA-300"]):
            before = len(course.load_courses())
            course.delete_new_course()
            after = len(course.load_courses())
            self.assertEqual(after, before - 1)

    # ---------------- PROFESSOR TESTS ----------------

    @patch("builtins.input", side_effect=["P200", "Test Professor", "testprof@sjsu.edu", "Professor", "DATA-200"])
    def test_add_professor(self, mock_input):
        before = len(professor.load_professors())
        professor.add_new_professor()
        after = len(professor.load_professors())
        self.assertEqual(after, before + 1)

    def test_modify_professor(self):
        # create target record first so test is independent
        professors = professor.load_professors()
        professors.append(professor.Professor("P200", "Test Professor", "testprof@sjsu.edu", "Professor", "DATA-200"))
        professor.save_professors(professors)

        with patch("builtins.input", side_effect=["P200", "Updated Professor", "updatedprof@sjsu.edu", "Senior Professor", "DATA-201"]):
            professor.modify_professor_details()

        professors = professor.load_professors()
        found = False
        for p in professors:
            if p.professor_id == "P200":
                found = True
                self.assertEqual(p.name, "Updated Professor")
                self.assertEqual(p.email_address, "updatedprof@sjsu.edu")
                self.assertEqual(p.rank, "Senior Professor")
                self.assertEqual(p.course_id, "DATA-201")
        self.assertTrue(found)

    def test_delete_professor(self):
        # create target record first
        professors = professor.load_professors()
        professors.append(professor.Professor("P200", "Test Professor", "testprof@sjsu.edu", "Professor", "DATA-200"))
        professor.save_professors(professors)

        with patch("builtins.input", side_effect=["P200"]):
            before = len(professor.load_professors())
            professor.delete_professore()
            after = len(professor.load_professors())
            self.assertEqual(after, before - 1)


if __name__ == "__main__":
    unittest.main()