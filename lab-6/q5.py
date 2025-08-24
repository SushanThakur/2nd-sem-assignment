class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.employee_id}, Salary: ₹{self.salary}")


# Example
emp1 = Employee("abc", 28, "E101", 50000)
emp1.display_employee()
