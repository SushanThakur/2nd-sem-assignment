class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Contact:
    def __init__(self, person, address):
        self.person = person
        self.address = address

    def display_contact(self):
        print(f"Name: {self.person.name}, Age: {self.person.age}")
        print(f"Address: {self.address.street}, {self.address.city} - {self.address.zipcode}")


# Example
p1 = Person("Amit", 22)
a1 = Address("MG", "USA", "560001")
c1 = Contact(p1, a1)
c1.display_contact()
