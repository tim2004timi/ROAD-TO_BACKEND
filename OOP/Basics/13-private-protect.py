class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    @staticmethod
    def _verify_coord(coord):
        return 0 < coord <= 100


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        if all(map(self._verify_coord, (x1, x2, y1, y2))):
            print("Good")
        else:
            print("Bad")
        super().__init__(x1, y1, x2, y2)
        self.fill = fill


rect = Rect(0, 1, 2, 2)
print(rect.__dict__)
print(rect.name)
