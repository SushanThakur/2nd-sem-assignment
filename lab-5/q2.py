class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


s1 = Student("Alice", 85)
s2 = Student("Bob", 90)
s3 = Student("Charlie", 78)

s1.show_details()
s2.show_details()
s3.show_details()
