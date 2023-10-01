# class Point:
#     name = "point"
class B1: pass
class B2: pass


print(type(object))

Point = type("Point", (B1, B2), {"name": "point"})
p = Point()
print(p.name, Point.__mro__)
