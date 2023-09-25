class Point:
    def __init__(self, x: int = 0, y: int = 0):  # инициализатор
        print("__init__", str(self))
        self.x = x
        self.y = y

    def __del__(self):  # финализатор
        print("__del__", str(self))

    def get_coords(self) -> tuple:
        return self.x, self.y


a = Point()
b = Point(3, 4)

print(a.get_coords(), a.__dict__)
print(b.get_coords(), b.__dict__)

