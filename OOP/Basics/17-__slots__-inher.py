class Point2D:
    __slots__ = ("x", "y", "_r")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._r = (x ** 2 + y ** 2) ** 0.5

    @property
    def r(self):
        return self._r


class Point3D(Point2D):
    __slots__ = "z",

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        self._r = (x ** 2 + y ** 2 + z ** 2) ** 0.5


p = Point2D(3, 4)
print(p.r)

p3 = Point3D(1, 2, 2)
print(p3.r)
