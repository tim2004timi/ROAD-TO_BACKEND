class Point:
    """Documentation"""
    color = "red"
    circle = 2


point1 = Point()
point2 = Point()

print(type(point1))  # <class '__main__.Point'>
print(type(point2) == Point)  # True

print(point1.color)  # red
Point.color = "green"
print(point1.color)  # green

point1.color = "black"
print(point1.color)  # black
print(point2.color)  # green
print(point1.__dict__)  # {'color': 'black'}

del point1.color
print(point1.color)  # green

print(Point.__doc__)  # Documentation
