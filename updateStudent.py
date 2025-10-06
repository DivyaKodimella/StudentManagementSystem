from dataModel import ALLOWED_COURSES


def update_student(students_list):
    """
    Updates an existing student's course or marks based on their ID.
    """
    if not students_list:
        print("\nNo students to update. The list is empty.")
        return

    student_id = input("Enter the ID of the student to update: ").strip()
    
    student_to_update = None
    for student in students_list:
        if student['id'] == student_id:
            student_to_update = student
            break
            
    if student_to_update is None:
        print("\nStudent with that ID not found.")
        return

    print(f"\nUpdating details for {student_to_update['name']} (ID: {student_to_update['id']})")
    
    while True:
        choice = input("What do you want to update? (course/marks): ").strip().lower()
        if choice in ['course', 'marks']:
            break
        print("Invalid option. Please enter 'course' or 'marks'.")

    if choice == 'course':
        while True:
            new_course = input(f"Enter new course ({', '.join(ALLOWED_COURSES)}): ").strip().upper()
            if new_course in ALLOWED_COURSES:
                student_to_update['course'] = new_course
                break
            else:
                print(f"Invalid course. Please choose from: {', '.join(ALLOWED_COURSES)}")
    elif choice == 'marks':
        while True:
            try:
                new_marks = int(input("Enter new marks: ").strip())
                student_to_update['marks'] = new_marks
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        
    print("\nStudent details updated successfully.")
