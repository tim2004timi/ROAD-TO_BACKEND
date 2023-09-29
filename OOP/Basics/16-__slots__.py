class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 5)
p2 = Point2D(1, 5)

print(p1.__sizeof__(), "+", p1.__dict__.__sizeof__())
print(p2.__sizeof__())
