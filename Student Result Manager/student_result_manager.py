student = {}

while True:
    print("\n-----------STUDENT MANAGER APP")
    print("1. Add student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == '1':
        name = input("Enter the name : ")
        mark = int(input("Enter marks : "))
        student[name] = mark
        # Rahul -> 50
        print(f"{name} Successfully Added")

    # View Student
    elif choice == '2':
        if not student:
            print("No Student found")
        else:
            for (name,marks) in student:
                print(name, ": " , marks)

    elif choice == '3':
        name = input("Enter student name")
        if name in student :
            marks = student[name]

            if marks >= 40 :
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student not found")

    # choice -> 4 exit
    elif choice == '4':
        print("Exit")
        break
    else:
        print("In-valid input")