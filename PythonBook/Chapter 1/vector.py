import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector ({self.x}, {self.y})"

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


v1 = Vector(3, 4)
v2 = Vector(2, 8)
print(abs(v1), abs(v2))
print(v1, v2)
print(abs(v1 + v2))
print(v1 * 2)
