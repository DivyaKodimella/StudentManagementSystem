def delete_student(students_list):
    """
    Deletes a student from the list by their ID.
    """
    if not students_list:
        print("\nNo students to delete. The list is empty.")
        return
        
    student_id = input("Enter the ID of the student to delete: ").strip()
    
    student_found = False
    for i, student in enumerate(students_list):
        if student['id'] == student_id:
            removed_student_name = students_list.pop(i)['name']
            student_found = True
            break
    
    if student_found:
        print(f"\nSuccessfully deleted student: {removed_student_name}")
    else:
        print("\nStudent with that ID not found.")
