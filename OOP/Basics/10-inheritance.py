class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Draw the line")


class Rect(Geom):
    def draw(self):
        print("Draw the rectangle")


line = Line()
rect = Rect()
line.set_coords(1, 2, 3, 4)
rect.set_coords(1, 2, 1, 2)
line.draw()
rect.draw()
print(line.name)
