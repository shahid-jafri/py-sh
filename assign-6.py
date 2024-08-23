def manage_student_database():
    students = []  # List to store student tuples
    student_id = 1  # Starting ID
    
   
    while True:
        name = input("Enter the student's name (or type 'stop' to finish): ").strip()
        
        if name.lower() == "stop":
            break
        
        # Check for duplicate names
        if any(student_name == name for _, student_name in students):
            print("Duplicate name found. The student was not added.")
        else:
            students.append((student_id, name))
            student_id += 1
    
    
    print("\nComplete list of students:")
    print(students)
    
   
    print("\nStudent Details:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
   
    total_students = len(students)
    print(f"\nTotal number of students: {total_students}")
    
   
    total_name_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_name_length}")
    
    
    if students:
        longest_name_student = max(students, key=lambda student: len(student[1]))
        shortest_name_student = min(students, key=lambda student: len(student[1]))
        
        print(f"Student with the longest name: ID: {longest_name_student[0]}, Name: {longest_name_student[1]}")
        print(f"Student with the shortest name: ID: {shortest_name_student[0]}, Name: {shortest_name_student[1]}")
    else:
        print("No students were added.")


manage_student_database()
