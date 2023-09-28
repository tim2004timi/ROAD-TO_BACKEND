class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        print("__init__ in Geom")


class Line(Geom):
    def draw(self):
        print(f"Draw a line {[self.x1, self.y1, self.x2, self.y2]}")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self.fill = fill
        print("__init__", self.__class__)

    def draw(self):
        print(f"Draw a rectangle {[self.x1, self.y1, self.x2, self.y2]}, fill={self.fill}")


line = Line(1, 2, 3, 4)
rect = Rect(1, 1, 0, 0)
print(rect.name)
