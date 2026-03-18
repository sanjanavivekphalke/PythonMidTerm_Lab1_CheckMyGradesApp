from student import (
    display_records,
    add_new_student,
    delete_new_student,
    update_student_record,
    check_my_grades,
    check_my_marks,
    search_student,
    sort_students_by_marks,
    sort_students_by_email,
    course_wise_statistics
)

from course import (
    display_courses,
    add_new_course,
    delete_new_course,
    search_course,
    sort_courses,
    modify_course
)

from professor import (
    professors_details,
    add_new_professor,
    delete_professore,
    modify_professor_details,
    show_course_details_by_professor,
    search_professor,
    sort_professors
)

from grades import (
    display_grade_report,
    add_grade,
    delete_grade,
    modify_grade
)

from login import (
    register_user,
    Login,
    Logout,
    Change_password
)


def main():
    while True:
        print("\n--- CheckMyGrade Application ---")
        print("1. Display Student Records")
        print("2. Add New Student")
        print("3. Delete Student")
        print("4. Update Student Record")
        print("5. Check My Grades")
        print("6. Check My Marks")
        print("7. Search Student")
        print("8. Sort Students by Marks Ascending")
        print("9. Sort Students by Marks Descending")
        print("10. Sort Students by Email")
        print("11. Course-wise Average and Median")
        print("12. Display Courses")
        print("13. Add New Course")
        print("14. Delete Course")
        print("15. Search Course")
        print("16. Sort Courses")
        print("17. Modify Course")
        print("18. Professor Details")
        print("19. Add New Professor")
        print("20. Delete Professor")
        print("21. Modify Professor Details")
        print("22. Show Course Details By Professor")
        print("23. Search Professor")
        print("24. Sort Professors")
        print("25. Display Grade Report")
        print("26. Add Grade")
        print("27. Delete Grade")
        print("28. Modify Grade")
        print("29. Register User")
        print("30. Login")
        print("31. Logout")
        print("32. Change Password")
        print("33. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_records()
        elif choice == "2":
            add_new_student()
        elif choice == "3":
            delete_new_student()
        elif choice == "4":
            update_student_record()
        elif choice == "5":
            check_my_grades()
        elif choice == "6":
            check_my_marks()
        elif choice == "7":
            search_student()
        elif choice == "8":
            sort_students_by_marks(True)
        elif choice == "9":
            sort_students_by_marks(False)
        elif choice == "10":
            sort_students_by_email(True)
        elif choice == "11":
            course_wise_statistics()
        elif choice == "12":
            display_courses()
        elif choice == "13":
            add_new_course()
        elif choice == "14":
            delete_new_course()
        elif choice == "15":
            search_course()
        elif choice == "16":
            sort_courses()
        elif choice == "17":
            modify_course()
        elif choice == "18":
            professors_details()
        elif choice == "19":
            add_new_professor()
        elif choice == "20":
            delete_professore()
        elif choice == "21":
            modify_professor_details()
        elif choice == "22":
            show_course_details_by_professor()
        elif choice == "23":
            search_professor()
        elif choice == "24":
            sort_professors()
        elif choice == "25":
            display_grade_report()
        elif choice == "26":
            add_grade()
        elif choice == "27":
            delete_grade()
        elif choice == "28":
            modify_grade()
        elif choice == "29":
            register_user()
        elif choice == "30":
            Login()
        elif choice == "31":
            Logout()
        elif choice == "32":
            Change_password()
        elif choice == "33":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Try again.")


main()