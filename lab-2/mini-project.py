students = {}

while True:
    print("\n1. Add Student\n2. View All\n3. Display Topper\n4. Search by Roll\n5. Failed Students\n6. Update Marks\n7. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Name: ")
        roll = input("Roll: ")
        marks = [int(input(f"Marks in Subject {i+1}: ")) for i in range(3)]
        students[roll] = {"name": name, "marks": marks}

    elif choice == 2:
        for roll, data in students.items():
            print(roll, data["name"], data["marks"])

    elif choice == 3:
        topper = max(students.items(), key=lambda x: sum(x[1]["marks"]))
        print("Topper:", topper[1]["name"], "with marks:", topper[1]["marks"])

    elif choice == 4:
        roll = input("Enter roll: ")
        print(students.get(roll, "Student not found"))

    elif choice == 5:
        for data in students.values():
            if any(m < 40 for m in data["marks"]):
                print(data["name"], "has failed")

    elif choice == 6:
        roll = input("Enter roll to update: ")
        if roll in students:
            students[roll]["marks"] = [int(input(f"New Marks in Subject {i+1}: ")) for i in range(3)]
        else:
            print("Student not found")

    elif choice == 7:
        break
    else:
        print("Invalid choice")

