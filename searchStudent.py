def search_student(students_list):
    """
    Searches for a student by their ID or name (case-insensitive).
    """
    if not students_list:
        print("\nNo students to search. The list is empty.")
        return

    query = input("Enter student ID or Name to search: ").strip().lower()
    
    found_students = []
    for student in students_list:
        if query == student['id'].lower() or query in student['name'].lower():
            found_students.append(student)
            
    if not found_students:
        print("\nStudent not found.")
    else:
        print("\n--- Search Results ---")
        print(f"{'ID':<10} {'Name':<20} {'Course':<10} {'Marks':<5}")
        print("-" * 47)
        for student in found_students:
             print(f"{student['id']:<10} {student['name']:<20} {student['course']:<10} {student['marks']:<5}")
        print("----------------------")
