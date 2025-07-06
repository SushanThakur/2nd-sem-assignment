students = {
    "Ram": [70, 80, 90],
    "Shyam": [85, 75, 65],
    "Hari": [60, 55, 50]
}

# Average marks
for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(f"{name}: Average = {avg}")

# Topper
topper = max(students, key=lambda x: sum(students[x]))
print("Topper:", topper)

# Update marks
students["Ram"][0] = 95
print(students)

