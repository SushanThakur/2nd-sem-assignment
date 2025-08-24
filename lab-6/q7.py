class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# Example
b1 = Book("The White Tiger", "Aravind Adiga")
print(b1)
