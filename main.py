import os
from addStudent import add_student
from dataModel import students
from viewStudent import view_students
from searchStudent import search_student
from deleteStudent import delete_student
from updateStudent import update_student

def menu():
    """
    Displays the main menu.
    """
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("===================================")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")
            
        input("\nPress Enter to continue...")

