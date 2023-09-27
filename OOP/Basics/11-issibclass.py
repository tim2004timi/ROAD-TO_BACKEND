class Geom:
    pass


class Line(Geom):
    pass


g = Geom()
l = Line()
print(l.__class__)
print(issubclass(Line, Geom))  # True
print(isinstance(l, object))  # True
