from dataModel import ALLOWED_COURSES, MAX_STUDENTS


def add_student(students_list):
    """
    Adds a new student to the list after validating input.
    - Checks if the student limit has been reached.
    - Validates the course against ALLOWED_COURSES.
    - Ensures student ID is unique.
    """
    if len(students_list) >= MAX_STUDENTS:
        print(f"\nError: Cannot add more students. The limit of {MAX_STUDENTS} has been reached.")
        return

    print("\n--- Add New Student ---")
    student_id = input("Enter student ID: ").strip()

    # Check for duplicate ID
    for student in students_list:
        if student['id'] == student_id:
            print("\nError: A student with this ID already exists.")
            return

    name = input("Enter student name: ").strip()
    
    # Course input and validation loop
    while True:
        course = input(f"Enter course ({', '.join(ALLOWED_COURSES)}): ").strip().upper()
        if course in ALLOWED_COURSES:
            break
        else:
            print(f"Invalid course. Please choose from: {', '.join(ALLOWED_COURSES)}")

    # Marks input and validation
    while True:
        try:
            marks = int(input("Enter marks: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for marks.")

    if not student_id or not name:
        print("\nError: Student ID and Name are required.")
        return

    students_list.append({'id': student_id, 'name': name, 'course': course, 'marks': marks})
    print(f"\nSuccessfully added student: {name}")
