class Geom:
    def get_perimeter(self):
        raise NotImplementedError("Method of getting perimeter is not overridden")


class Rectangle(Geom):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return (self.a + self.b) * 2


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return self.a * 4


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_perimeter(self):
    #     return self.a + self.b + self.c


geom_list = []
geom_list.extend((Rectangle(4, 5), Square(10), Triangle(2, 4, 2)))

for geom in geom_list:
    print(geom.get_perimeter())
