class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print("norm2: ", self.norm2(self.x, self.y))

    @classmethod
    def validate(cls, arg):  # метод класса
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def get_coords(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):  # статический метод
        return x ** 2 + y ** 2


v = Vector(1, 200)
result = v.get_coords()
print(Vector.validate(5))
print(v.validate(10))
print(Vector.norm2(1, 2))
print(result)
