class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"({self.x}, {self.y})")


# Example
v1 = Vector(2, 5)
v2 = Vector(4, 7)
v3 = v1 + v2
v3.display()
