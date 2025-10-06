def view_students(students_list):
    """
    Displays all student records in a tabular format.
    """
    print("\n--- All Student Records ---")
    if not students_list:
        print("No students found. The list is empty.")
    else:
        # Print table header
        print(f"{'ID':<10} {'Name':<20} {'Course':<10} {'Marks':<5}")
        print("-" * 47)
        # Print each student's details
        for student in students_list:
            print(f"{student['id']:<10} {student['name']:<20} {student['course']:<10} {student['marks']:<5}")
    print("---------------------------")
